#!/usr/bin/env python3
"""Deterministic, read-only inventory for temporary evidence trees."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
import tempfile
from pathlib import Path

CLASSIFICATIONS = ("KEEP", "ARCHIVE_CANDIDATE", "DELETE_CANDIDATE", "REVIEW")
KEEP_NAMES = {"RESULT.md", "GOAL.md", "goal.md", "SPEC.md", "HANDOFF.md", ".done"}
HOLD_NAMES = {"HOLD", ".hold", "KEEP", "AUDIT_HOLD", "LEGAL_HOLD", "RETENTION_HOLD"}
ACTIVE_NAMES = {"ACTIVE", ".active", "RUNNING", "RUN_STATE.env", "PROGRESS.env"}
CACHE_NAMES = {
    ".git", "node_modules", "__pycache__", ".terraform", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".cache", "package-cache", "pip-cache",
    "terraform.d", "plugins",
}
CACHE_NAMES_LOWER = {name.lower() for name in CACHE_NAMES}
MEDIA_SUFFIXES = {
    ".mp4", ".mov", ".avi", ".mkv", ".gif", ".webm", ".zip", ".tar", ".gz",
    ".tgz", ".7z", ".iso",
}
ATTEMPT_RE = re.compile(r"^attempt-(\d+)$", re.IGNORECASE)
GOAL_ID_RE = re.compile(r"(?im)^\s*(?:goal[_ -]?id|run[_ -]?id)\s*[:=]\s*([A-Za-z0-9][A-Za-z0-9._:/-]{0,120})")
STATUS_RE = re.compile(r"(?im)^\s*status\s*[:=]\s*([A-Za-z][A-Za-z0-9_-]{0,40})")
RETENTION_RE = re.compile(r"(?im)^\s*retention[_ -]?until\s*[:=]\s*(\d{4}-\d{2}-\d{2})")
TEXT_LIMIT = 32768


def read_metadata(directory: Path) -> dict[str, str]:
    """Read only small, well-known metadata files; never emit their contents."""
    result = {"goal_id": "", "goal_status": "", "retention_until": "", "result_state": "absent"}
    files = [directory / name for name in ("RESULT.md", "GOAL.md", "goal.md", "SPEC.md")]
    for path in files:
        if path.is_symlink() or not path.is_file():
            continue
        if path.name == "RESULT.md":
            result["result_state"] = "present"
        try:
            text = path.read_text(encoding="utf-8", errors="replace")[:TEXT_LIMIT]
        except OSError:
            continue
        if not result["goal_id"]:
            match = GOAL_ID_RE.search(text)
            if match:
                result["goal_id"] = match.group(1)
        if not result["goal_status"]:
            match = STATUS_RE.search(text)
            if match:
                result["goal_status"] = match.group(1).lower()
        if not result["retention_until"]:
            match = RETENTION_RE.search(text)
            if match:
                result["retention_until"] = match.group(1)
    return result


def walk(root: Path) -> tuple[list[Path], dict[Path, dict[str, str]], dict[Path, set[str]]]:
    entries: list[Path] = []
    metadata: dict[Path, dict[str, str]] = {root: read_metadata(root)}
    names_by_dir: dict[Path, set[str]] = {}
    pending = [root]
    while pending:
        current = pending.pop()
        try:
            children = sorted(os.scandir(current), key=lambda item: item.name)
        except OSError as exc:
            raise RuntimeError(f"cannot read {current}: {exc}") from exc
        names_by_dir[current] = {entry.name for entry in children}
        for entry in children:
            path = Path(entry.path)
            entries.append(path)
            if entry.is_dir(follow_symlinks=False):
                metadata[path] = read_metadata(path)
                pending.append(path)
    return sorted(entries, key=lambda path: path.relative_to(root).as_posix()), metadata, names_by_dir


def ancestors(path: Path, root: Path) -> list[Path]:
    current = path if path.is_dir() else path.parent
    result: list[Path] = []
    while current != root:
        result.append(current)
        current = current.parent
    result.append(root)
    return result


def has_result(path: Path) -> bool:
    result = path / "RESULT.md"
    return not result.is_symlink() and result.is_file()


def superseded_attempts(directories: list[Path], metadata: dict[Path, dict[str, str]]) -> set[Path]:
    grouped: dict[Path, list[Path]] = {}
    for directory in directories:
        if ATTEMPT_RE.match(directory.name):
            grouped.setdefault(directory.parent, []).append(directory)
    result: set[Path] = set()
    successful = {"success", "succeeded", "pass", "passed", "complete", "completed"}
    for siblings in grouped.values():
        if any(has_result(item) and metadata.get(item, {}).get("goal_status") in successful for item in siblings):
            result.update(item for item in siblings if not (has_result(item) and metadata.get(item, {}).get("goal_status") in successful))
    return result


def context(path: Path, root: Path, metadata: dict[Path, dict[str, str]], names_by_dir: dict[Path, set[str]], superseded_set: set[Path]) -> tuple[dict[str, str], bool, bool, bool]:
    dirs = ancestors(path, root)
    info = {"goal_id": "", "goal_status": "", "retention_until": "", "result_state": "absent"}
    active = False
    held = False
    is_superseded = False
    for directory in dirs:
        direct = metadata.get(directory, {})
        for key in ("goal_id", "goal_status", "retention_until"):
            if not info[key] and direct.get(key):
                info[key] = direct[key]
        if direct.get("result_state") == "present":
            info["result_state"] = "present"
        names = names_by_dir.get(directory, set())
        active = active or bool(names & ACTIVE_NAMES)
        held = held or bool(names & HOLD_NAMES)
        is_superseded = is_superseded or directory in superseded_set
    return info, active, held, is_superseded


def classify(path: Path, root: Path, metadata: dict[Path, dict[str, str]], names_by_dir: dict[Path, set[str]], superseded_attempts_set: set[Path]) -> tuple[str, str, dict[str, str]]:
    info, active, held, superseded = context(path, root, metadata, names_by_dir, superseded_attempts_set)
    name = path.name
    if path.is_symlink():
        return "REVIEW", "symlink_not_followed", info
    if held:
        return "KEEP", "explicit_hold", info
    if active:
        return "KEEP", "active_run", info
    if name in KEEP_NAMES:
        return "KEEP", "canonical_or_goal_metadata", info
    if superseded:
        return "ARCHIVE_CANDIDATE", "superseded_retry_output", info
    if path.is_dir() and ".git" in names_by_dir.get(path, set()):
        return "DELETE_CANDIDATE", "copied_repository_worktree", info
    if name.lower() in CACHE_NAMES_LOWER:
        return "DELETE_CANDIDATE", "recreatable_dependency_or_cache", info
    if path.is_file() and path.suffix.lower() in MEDIA_SUFFIXES:
        return "DELETE_CANDIDATE", "unreferenced_media_or_archive", info
    return "REVIEW", "unknown_or_requires_owner_review", info


def entry_record(path: Path, root: Path, metadata: dict[Path, dict[str, str]], names_by_dir: dict[Path, set[str]], superseded: set[Path]) -> dict[str, object]:
    try:
        st = path.lstat()
    except OSError as exc:
        raise RuntimeError(f"cannot stat {path}: {exc}") from exc
    classification, reason, info = classify(path, root, metadata, names_by_dir, superseded)
    kind = "symlink" if stat.S_ISLNK(st.st_mode) else "directory" if stat.S_ISDIR(st.st_mode) else "file"
    return {
        "path": path.relative_to(root).as_posix(),
        "kind": kind,
        "size_bytes": st.st_size if kind == "file" else 0,
        "mtime_epoch": st.st_mtime_ns,
        "classification": classification,
        "reason": reason,
        "goal_id": info["goal_id"],
        "goal_status": info["goal_status"],
        "result_state": info["result_state"],
        "retention_until": info["retention_until"],
        "hold": reason == "explicit_hold",
    }


def build_report(root: Path) -> tuple[dict[str, object], str]:
    if not root.is_dir():
        raise ValueError(f"evidence root is not a directory: {root}")
    entries, metadata, names_by_dir = walk(root)
    superseded = superseded_attempts(list(metadata), metadata)
    records = [entry_record(path, root, metadata, names_by_dir, superseded) for path in entries]
    counts = {name: {"entries": 0, "bytes": 0} for name in CLASSIFICATIONS}
    for record in records:
        bucket = counts[record["classification"]]
        bucket["entries"] += 1
        bucket["bytes"] += record["size_bytes"]
    manifest = {
        "schema": "temp-evidence-inventory/v1",
        "dry_run": True,
        "follows_symlinks": False,
        "entry_count": len(records),
        "summary": counts,
        "entries": records,
    }
    lines = [
        "# Temporary evidence inventory (dry run)",
        "",
        "This report classifies one configured root. It performs no delete, move, rename, archive, or retention enforcement.",
        "",
        f"Entries: {len(records)}",
        "",
        "| Classification | Entries | Bytes |",
        "| --- | ---: | ---: |",
    ]
    for name in CLASSIFICATIONS:
        lines.append(f"| {name} | {counts[name]['entries']} | {counts[name]['bytes']} |")
    lines.extend([
        "",
        "Safety: symlinks are not followed; active and held evidence is retained; unknown evidence defaults to REVIEW.",
        "The manifest contains relative paths and metadata only; arbitrary file contents are never emitted.",
        "",
    ])
    return manifest, "\n".join(lines)


def outside_root(output: Path, root: Path) -> bool:
    try:
        return os.path.commonpath((os.path.realpath(output.parent), os.path.realpath(root))) != os.path.realpath(root)
    except ValueError:
        return True


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError(f"output must not be a symlink: {path}")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="one explicitly configured evidence root")
    parser.add_argument("--manifest", type=Path, required=True, help="JSON output path outside root")
    parser.add_argument("--summary", type=Path, required=True, help="Markdown output path outside root")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not outside_root(args.manifest, root) or not outside_root(args.summary, root):
        parser.error("manifest and summary outputs must be outside the scanned root")
    if args.manifest.resolve() == args.summary.resolve():
        parser.error("manifest and summary must be different files")
    try:
        manifest, summary = build_report(root)
        write_text(args.manifest, json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        write_text(args.summary, summary)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"PASS: entries={manifest['entry_count']} manifest={args.manifest} summary={args.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
