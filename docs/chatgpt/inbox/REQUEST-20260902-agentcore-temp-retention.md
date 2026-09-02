---
type: ChatGPT review request
title: AgentCore temporary evidence retention and layout
status: request-only
date: 2026-09-02
safety: public-safe summary; no implementation or deletion authorized
---

# Request: improve temporary evidence retention

Please review this request using the public protocol:

<https://gist.github.com/amitkarpe/c8d29ad89cafe3ba178fcae29de3c238>

## Context

The local AgentCore temporary area is used for Codex/AI experiments,
read-only AWS checks, and POC evidence. A snapshot on 2026-09-02 contains:

- 15,694 directories
- 101,025 files
- approximately 2.85 GiB
- 63 top-level project/run directories
- 66 `node_modules` trees
- 3 nested `.git` directories
- 86 large media/archive files

The largest groups are repeated Issue/POC folders containing copied project
trees, dependencies, nested Git data, media, and retry outputs. The directory
is evidence storage, not a source repository.

## Rules already in force

The local Codex rules require:

- KISS: one problem, one happy path, one command, one proof, one result.
- One bounded goal per worker lane with a durable `RESULT.md`.
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
Preserve audit evidence until an owner approves its retention decision.

## Requested response

Create one new standalone GitHub Issue containing:

- a recommended KISS directory layout;
- a keep/archive/delete classification;
- practical retention defaults;
- a retry and result-file rule;
- a no-copy dependency/media policy;
- a dry-run cleanup acceptance checklist;
- risks and rejected alternatives; and
- one bounded implementation Issue plus one Draft PR plan.

Do not implement the recommendation. Treat the measurements above as a
sanitized local snapshot, not as permission to clean anything.
