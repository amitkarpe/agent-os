---
type: Policy
title: Git Issue and PR Workflow
description: One bounded goal, one coherent change, proportional validation and verified repository closeout.
status: reviewed
scope: Reusable public-safe GitHub and GitLab repository workflow
confidence: high
timestamp: 2026-10-21T16:30:00+08:00
review_after: 2027-04-21
tags: [git, github, gitlab, issues, pull-requests, review, goals]
---

# Git Workflow

Use the owning repository's `AGENTS.md`, applicable `SPEC.md`, current
approved Issue/PR and branch rules first. This reusable guide does not grant
merge, publication, cloud, credential, or destructive permissions.

## One goal, coherent PR

1. Confirm the target repository, remote, base branch, HEAD, dirty state,
   existing worktrees and owning Issue/PR before writing.
2. Use the already-approved Issue for one bounded outcome. Work on a
   non-default branch unless the repository explicitly allows otherwise.
3. Deliver one cohesive, reviewable PR/MR for related implementation,
   validation and corrections. Draft means incomplete; do not force a Draft
   PR for ready work or a new PR for every small fix.
4. Verify the **entire current diff**, exact PR head, required checks,
   acceptance and scope. Obtain only the independent review that actual
   repository rules require. A subagent review from the same GitHub identity
   is not a separate-account approval.
5. Merge only with the applicable owner/Issue/Spec authority and platform
   protection gates. Continue the next already-approved milestone without
   asking for another routine `go`. A merge is not runtime deployment proof.
6. Confirm merged commit and Issue closure separately; a closed unmerged PR,
   push, green CI or queue receipt is not completion evidence.

Prefer about two to five tightly related slices per PR when useful. Split for
a materially different security/approval, architecture, external integration,
deployment, lifecycle or independent review boundary—not cosmetic task size.
Use the repository's naming conventions; otherwise a compact
`type/<issue>-topic` branch and `type(scope): summary` commit are sufficient.

Do not repurpose a completed Issue, edit unrelated dirty work, force-push over
another writer, delete an active worktree, or mirror between hosts/providers
without the exact repository's authority. Never assume that a GitLab project
is secondary to GitHub; source selection and controlled publication are
repository-specific.

## Minimal durable records

The Issue is the goal and the PR/MR is the delivery. Do not create duplicate
packet, outbox or status files for information already in those records.
Keep only the current state, blocker, material evidence and one next step.

A compact Issue snapshot may use:

```text
Status: doing | blocked | review | resolved
Objective: <one outcome>
Now: <current milestone / exact HEAD if relevant>
Next: <one authorized action>
Blocker: none | <one concrete dependency>
PR: #<number> | none
```

Keep short body sections only when they improve execution:

```text
Scope: in / out
Acceptance: observable, bounded checks
Evidence: relevant checks or verified provider results
```

The PR/MR description states **what changed, why, validation and risk**,
plus one supported resolver reference when appropriate (e.g.
`Resolves #123`). On closeout record the actual merged revision, relevant
validation, retained risk/cleanup, and a next action only if necessary.

## Tools are not policy

Agents already know basic `git`, `gh` and `glab` syntax. Discover installed
versions, authentication and command help when relevant; do not preload a
manual of generic commands. Never publish credentials or private host/cloud
payloads in Issue bodies or logs. GitHub and GitLab may have different author,
signing, merge, mirror and branch rules: verify the exact target.

For multi-agent Goal routing use the
[G and Coding-Agent Collaboration Protocol](kb/playbooks/integrations/chatgpt-codex-collaboration-protocol.md).
For validation depth use [Testing and Validation](TESTING.md).
Host-specific GitLab identity, aliases and source-of-truth registers belong
in local setup or the owning private repository, **not** this public guide.
