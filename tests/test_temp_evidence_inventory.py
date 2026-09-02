#!/usr/bin/env python3
"""Focused tests for the read-only temporary evidence inventory."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "temp_evidence_inventory.py"


class InventoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "evidence"
        self.root.mkdir()
        (self.root / "active").mkdir()
        (self.root / "active" / "ACTIVE").write_text("", encoding="utf-8")
        (self.root / "active" / "log.txt").write_text("active", encoding="utf-8")
        (self.root / "held").mkdir()
        (self.root / "held" / "HOLD").write_text("", encoding="utf-8")
        (self.root / "held" / "audit.txt").write_text("held", encoding="utf-8")
        goal = self.root / "goal"
        (goal / "attempt-01").mkdir(parents=True)
        (goal / "attempt-01" / "failed.log").write_text("failed", encoding="utf-8")
        (goal / "attempt-02").mkdir()
        (goal / "attempt-02" / "RESULT.md").write_text(
            "goal_id: demo-1\nstatus: success\n", encoding="utf-8"
        )
        (self.root / "copied" / ".git").mkdir(parents=True)
        (self.root / "copied" / ".git" / "config").write_text("git", encoding="utf-8")
        (self.root / "node_modules" / "pkg").mkdir(parents=True)
        (self.root / "node_modules" / "pkg" / "index.js").write_text("js", encoding="utf-8")
        (self.root / "capture.zip").write_bytes(b"zip")
        (self.root / "unknown.txt").write_text("review", encoding="utf-8")
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (outside / "secret.txt").write_text("outside", encoding="utf-8")
        os.symlink(outside, self.root / "outside-link", target_is_directory=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_inventory(self, output_dir: Path) -> dict:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root),
             "--manifest", str(output_dir / "manifest.json"),
             "--summary", str(output_dir / "summary.md")],
            check=True, capture_output=True, text=True,
        )
        self.assertIn("PASS: entries=", result.stdout)
        return json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))

    def test_classifies_safety_and_retries_without_following_symlink(self) -> None:
        before = sorted(path.relative_to(self.root).as_posix() for path in self.root.rglob("*"))
        with tempfile.TemporaryDirectory() as output:
            manifest = self.run_inventory(Path(output))
        records = {item["path"]: item for item in manifest["entries"]}
        self.assertEqual(records["active/log.txt"]["classification"], "KEEP")
        self.assertEqual(records["held/audit.txt"]["classification"], "KEEP")
        self.assertEqual(records["goal/attempt-01/failed.log"]["classification"], "ARCHIVE_CANDIDATE")
        self.assertEqual(records["copied"]["reason"], "copied_repository_worktree")
        self.assertEqual(records["node_modules"]["classification"], "DELETE_CANDIDATE")
        self.assertEqual(records["capture.zip"]["classification"], "DELETE_CANDIDATE")
        self.assertEqual(records["outside-link"]["reason"], "symlink_not_followed")
        self.assertEqual(records["unknown.txt"]["classification"], "REVIEW")
        after = sorted(path.relative_to(self.root).as_posix() for path in self.root.rglob("*"))
        self.assertEqual(before, after)

    def test_unchanged_fixture_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            one = self.run_inventory(Path(first))
            two = self.run_inventory(Path(second))
        self.assertEqual(one, two)

    def test_rejects_output_inside_scanned_root(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root),
             "--manifest", str(self.root / "manifest.json"),
             "--summary", str(self.root / "summary.md")],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("outside the scanned root", result.stderr)


if __name__ == "__main__":
    unittest.main()
