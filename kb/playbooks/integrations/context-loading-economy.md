---
type: Playbook
title: Context Loading Economy for Agent Handoffs
description: Keep PR/comment handoffs fast by treating repository context files as bootstrap and recovery inputs instead of mandatory rereads for every task.
status: reviewed
scope: GitHub-centered ChatGPT, Codex, and repository-worker handoffs
confidence: high
timestamp: 2026-09-17T01:55:00+08:00
last_verified: 2026-09-17
review_after: 2027-03-17
tags: [chatgpt, codex, github, context, handoff, delegation, efficiency]
---

# Context Loading Economy for Agent Handoffs

Use the smallest durable pointer that is sufficient to continue safely.

**PR is the execution packet. The latest relevant comment is the delta. Context
files are bootstrap/recovery inputs, not boilerplate for every handoff.**

This guidance does not weaken repository instructions, authority, safety gates,
or stale-state checks. It only avoids repeatedly reloading context that the
worker already has and can safely reuse.

## Normal continuation

When repository identity and objective are already known:

- **New PR/task:** give the worker the PR number or URL.
- **Existing PR with a new instruction:** give the PR plus the exact relevant
  comment/handoff URL when useful.
- **Known objective:** a short continuation such as `go`, `g`, `.`, `Y`, or
  equivalent means fetch current PR HEAD/latest durable handoff and continue.
- Do not restate task details that are already durable in the owning Issue/PR
  merely to move them between ChatGPT, Codex, or another worker.

Example:

```text
Work on PR #27.
```

Existing PR with a new delta:

```text
Continue PR #27 from:
https://github.com/OWNER/REPO/pull/27#issuecomment-...
```

The receiving worker fetches current PR state, latest relevant comments, and
current HEAD before acting.

## Full context reload triggers

Explicitly reload `AGENTS.md`, `CONTEXT.md`, `CHATGPT.md`, `SPEC.md`, or
equivalent governing files only when at least one of these is true:

1. the worker/session lacks usable repository context;
2. a governing instruction/context file materially changed;
3. repository or objective identity is ambiguous;
4. current context is stale, incomplete, contradictory, or unsafe to reuse;
5. the task enters a new authority, security, production, deployment, or other
   trust domain that requires an additional governing contract.

A new PR number, milestone boundary, or routine continuation alone is **not** a
context-reload trigger.

## Bootstrap / recovery order

Repositories may define a read order for cold start or recovery. Label it
explicitly as **Bootstrap / Recovery Order** rather than a generic **Read
Order** when there is a risk that agents will treat it as a per-task checklist.

Typical recovery order:

1. repository instructions such as `AGENTS.md`;
2. current-only state such as `CONTEXT.md`;
3. authority contract such as `SPEC.md` when relevant;
4. owning Issue/PR and latest relevant handoff/comment;
5. current branch/HEAD/runtime truth as needed.

This is a recovery sequence, not a required preamble for every delegation.

## Handoff economy

Prefer:

```text
PR -> latest relevant comment -> current HEAD -> execute
```

Avoid:

```text
re-read every context file -> repeat the PR body -> repeat acceptance -> execute
```

unless a reload trigger above applies.

The durable GitHub record should contain objective, scope, acceptance, and
important no-go gates. A handoff normally points to that record rather than
copying it.

## Project and local context

Project instructions, repository instructions, local agent cores, and reusable
playbooks serve different scopes. Do not preload every layer on every task.
Load the narrowest context needed for the current objective and add broader
layers only when the task requires them.

For ChatGPT Projects, keep one canonical instruction source and remove stale or
unrelated duplicate source files through the product surface that owns them.
Repository-specific state still belongs in repository truth.

## Safety invariants

Context economy never authorizes skipping a required safety or authority check.
Always stop or reload when:

- repository identity is uncertain;
- the latest PR/comment conflicts with cached context;
- a production/security/credential/destructive boundary is entered;
- current HEAD differs from a recorded handoff and the difference matters;
- required evidence or authorization cannot be reconstructed safely.

## Adoption pattern

Use this promotion path:

```text
project learning -> sanitize/deduplicate -> Agent OS canonical guidance
-> repo-starter only if universally useful -> project repos when next touched
```

Project repositories should keep only the smallest local form. Avoid copying
this entire playbook into every `AGENTS.md` or `CHATGPT.md`.

## Related playbooks

- [ChatGPT and Codex Collaboration Protocol](chatgpt-codex-collaboration-protocol.md)
- [ChatGPT Project Context and File Surfaces](chatgpt-project-context-and-files.md)
- [Knowledge Lifecycle and Publication](../../policies/knowledge-lifecycle-and-publication.md)
