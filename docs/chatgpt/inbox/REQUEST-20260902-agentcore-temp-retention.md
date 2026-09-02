---
type: ChatGPT review request
title: Cross-repository temporary evidence retention and layout
status: accepted-implementation-lane
date: 2026-09-02
safety: public-safe summary; no implementation or deletion authorized
---

# Request: improve cross-repository temporary evidence retention

Please review this request using the public protocol:

<https://gist.github.com/amitkarpe/c8d29ad89cafe3ba178fcae29de3c238>

## Context

The shared temporary area is used across repositories for Codex/AI experiments,
read-only checks, long-running operations, and POC evidence. A snapshot on
2026-09-02 contains:

- 24,472 directories
- 154,341 files
- approximately 6.5 GiB
- 68 `node_modules` trees
- 15 nested `.git` directories

The largest groups are repeated Issue/POC folders containing copied project
trees, dependencies, nested Git data, media, and retry outputs. The directory
is evidence storage, not a source repository.

## Rules already in force

The local Codex rules require:

- KISS: one problem, one happy path, one command, one proof, one result.
- One bounded goal/run per worker lane with a durable `RESULT.md`.
- Evidence under a temporary area; source code remains in its owning repository.
- Separate worktrees for genuinely parallel missions.
- Preserve current success proof, active-debug evidence, and audit evidence.
- Keep raw logs out of controller chat.
- Do not add unnecessary tests, dependencies, runners, or duplicate paths.
- Use automatic compaction; do not solve context pressure by replacing workers.
- Destructive cleanup requires a separate approved goal.

## Problem to review

Every issue, PR, agent attempt, and retry currently tends to receive a new
directory. That protects evidence from being overwritten, but it also permits
full repository copies, dependency trees, and large files to accumulate. The
result is slower search, more filesystem work, and a higher risk of reading
irrelevant or private material.

## Accepted implementation lane

ChatGPT's bounded recommendation is now recorded as:

- Issue #4: <https://github.com/amitkarpe/agent-os/issues/4>
- Draft PR #5: <https://github.com/amitkarpe/agent-os/pull/5>

Codex is the sole implementation owner for PR #5. PR #5 is the only
implementation lane for this problem. Do not create another PR, branch,
worker implementation, cleanup tool, or alternate architecture. The lane is
read-only dry-run classification only; destructive cleanup remains out of
scope and requires a separate approved goal.

## Questions

1. Should the storage unit be one folder per bounded goal/run, rather than one
   folder per Issue, PR, agent message, or retry?
2. Which artifacts must remain after completion: `RESULT.md`, selected logs,
   screenshots, source pointers, or only a compact evidence summary?
3. What retention periods should apply to active, successful, blocked, failed,
   and superseded runs?
4. Should retries use `attempt-01/`, `attempt-02/` under one goal folder?
5. How should copied repositories, `node_modules`, nested `.git`, media, and
   generated caches be prevented from entering evidence storage?
6. What deterministic dry-run cleanup and approval gate would be safest?
7. Is a small index/current pointer preferable to scanning all historical runs?
8. What privacy controls should apply before any evidence is shared externally?

## Constraints

Give a recommendation only. Do not delete, move, archive, or rewrite local
files. Do not change Codex configuration, repository rules, AWS resources, or
cloud credentials. Do not infer that a file is safe from its name alone.
Preserve audit evidence until an owner approves its retention decision. The
accepted implementation must remain repository-generic; it must not encode
AgentCore-only assumptions.

## Requested response

For any further ChatGPT review, use the existing Issue #4 and Draft PR #5;
do not create a duplicate Issue or PR. Review the actual PR diff and comment
only on whether it satisfies the existing acceptance contract:

- a recommended KISS directory layout;
- a keep/archive/delete classification;
- practical retention defaults;
- a retry and result-file rule;
- a no-copy dependency/media policy;
- a dry-run cleanup acceptance checklist;
- risks and rejected alternatives; and
- deterministic dry-run behavior with zero filesystem mutation.

Do not perform cleanup or configuration changes. Treat the measurements above
as a sanitized local snapshot, and treat PR #5 as the only implementation
authority for this milestone.
