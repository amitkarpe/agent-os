---
type: Playbook
title: Temporary Agent Evidence Lifecycle
description: Keep temporary agent evidence bounded, traceable, minimal, and safe to clean up.
status: reviewed
scope: temporary agent work evidence
confidence: high
timestamp: 2026-09-15T13:40:00+08:00
review_after: 2027-03-15
tags: [evidence, cleanup, agents, retention, kiss]
---

# Temporary Agent Evidence Lifecycle

Temporary evidence supports a bounded goal; it is not a source repository or a
second project history.

## KISS Model

Use one goal/run as the unit of temporary work:

```text
goal/
  GOAL.md
  RESULT.md
  attempts/
  evidence/selected/
  pointers/
```

- Keep one canonical `RESULT.md` per goal.
- Put retries under the same goal unless the objective materially changes.
- Prefer immutable source pointers over copied repositories or dependencies.
- Keep only the smallest evidence needed to prove the result or diagnose an
  unresolved blocker.

## Retention Classes

Classify temporary material before cleanup:

- `KEEP`: active work, canonical result/goal metadata, selected proof, explicit
  audit/compliance hold.
- `ARCHIVE_CANDIDATE`: useful inactive evidence worth retaining elsewhere.
- `DELETE_CANDIDATE`: reproducible caches, superseded attempts, duplicated logs,
  copied dependencies or repositories not needed as proof.
- `REVIEW`: unknown ownership, provenance, privacy, or audit value.

Unknown material is never a delete candidate by default.

## Cleanup Safety

The first cleanup step is always read-only classification. Produce a deterministic
manifest and summary before any delete, move, or archive action.

A destructive cleanup is a separate authority decision. It must not follow
implicitly from age, filename, tool output, or a previous recommendation.

## Privacy

Do not copy credentials, authentication state, private infrastructure, customer
data, or raw sensitive payloads into temporary evidence reports. Prefer metadata,
sanitized summaries, and source pointers.

## Ownership Boundary

Agent OS owns this reusable lifecycle guidance. The repository or runtime that
stores temporary evidence owns its implementation, path conventions, retention
configuration, and destructive cleanup authority.

## Source

Generalized from [Issue #3](https://github.com/amitkarpe/agent-os/issues/3).
