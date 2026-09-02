# Temporary Evidence Inventory

Use `scripts/temp_evidence_inventory.py` for one explicitly selected
temporary evidence root. It is a read-only classifier. It does not delete,
move, rename, archive, migrate, or enforce retention.

## One dry run

```bash
python3 scripts/temp_evidence_inventory.py /path/to/evidence \
  --manifest /tmp/evidence-manifest.json \
  --summary /tmp/evidence-summary.md
```

The output paths must be outside the scanned root. The JSON manifest contains
relative paths, file metadata, a classification, a reason, and bounded goal
metadata when it is present. It never emits arbitrary file contents.

Classifications are:

- `KEEP`: active runs, explicit holds, canonical result and goal metadata,
  source pointers, or files explicitly referenced by `RESULT.md`.
- `ARCHIVE_CANDIDATE`: output under a superseded retry.
- `DELETE_CANDIDATE`: recreatable dependencies/caches, copied repositories,
  or unreferenced media/archive files. This is a suggestion only.
- `REVIEW`: unknown, incomplete, private, or symlink evidence.

Active and held evidence always wins over candidate classifications. Selected
proof referenced by `RESULT.md` is also protected, including archive/media
files. Symlinks are listed but never followed. Unknown evidence defaults to
`REVIEW`.

## Storage rule

Keep source code and dependencies in the owning repository. Keep only one
bounded goal/run result in the evidence area. Place real retries below that
goal as `attempt-01/`, `attempt-02/`, and keep one canonical `RESULT.md`.
A later cleanup or retention implementation requires a separate approved
milestone; this command is deliberately dry-run only.

## Validation

Run the focused tests from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_temp_evidence_inventory.py' -v
```
