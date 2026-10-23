---
type: Policy
title: Knowledge and Evidence Lifecycle
description: Promote unique safe learning and retire temporary evidence with explicit ownership.
status: reviewed
confidence: high
scope: Reusable public-safe agent guidance
review_after: 2027-04-23
tags: [knowledge, evidence, privacy, lifecycle]
---

# Knowledge and Evidence Lifecycle

## Publish once, in the correct owner

Project repositories own current decisions, implementations, approvals and runtime evidence. Dotfiles and provider-native configuration own host facts, versions, secrets paths and operational setup. Agent OS owns only **sanitized, reusable guidance**.

Promote a non-obvious lesson only when it would help another task. Search this repository first and extend the canonical page rather than creating a second policy. Rewrite project learning, remove private identifiers, credentials, logs and local paths, distinguish dated claims from lasting principles, add primary citations and a review date, and review the **entire** PR branch for public publication safety. A human owner approves public promotion; implementation permission alone does not grant publication permission.

Lifecycle: `candidate` (outside public Git), `reviewed` (sanitized and useful), `verified` (current evidence), `deprecated` (historical, not active). Recheck old technical claims and links at `review_after`; preserve Git history and link the replacement where needed. Only universal defaults should also flow to repo-starter.

## Temporary evidence

One approved goal/run should own one canonical result, selected evidence and immutable source pointers. Retrying does not require copied repositories or a new evidence framework. Classify material before cleanup:

| Class | Disposition |
| --- | --- |
| KEEP | Active work, accepted proof, explicit compliance/audit hold |
| ARCHIVE_CANDIDATE | Useful inactive records with an approved destination |
| DELETE_CANDIDATE | Duplicated or reproducible artifacts with no retention hold |
| REVIEW | Unknown ownership, sensitivity, value or provenance |

Unknown is **not** permission to delete. First inventory read-only. Any later destructive action requires explicit authority, exact path and ownership verification, retention check, preservation of accepted commits/backups and a non-escaping symlink boundary. Stop on active, locked, dirty, untracked, private or uncertain material.

Record disposition **outside** a removed path as `deleted_after_acceptance`, `retained_with_reason` (owner/review date) or `blocked_cleanup`. Goal acceptance, time-to-live, a worker receipt or an old comment alone does not authorize cleanup.

## Maintenance

Use [README](README.md) as the single task index. Don't mirror generic policy into provider adapters; those should route to the one canonical page while retaining local exceptions. Preserve the unique knowledge before removing or rewriting its old path.

## Citations

- [Open Knowledge Format 0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [GitHub sensitive-data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
