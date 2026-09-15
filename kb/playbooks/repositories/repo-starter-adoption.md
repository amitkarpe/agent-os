---
type: Practice
title: KISS Repository Starter Adoption
description: Create or retrofit an agent-managed repository with the smallest current repo-starter truth files.
status: reviewed
scope: repository foundation
confidence: high
timestamp: 2026-09-15T10:00:00+08:00
review_after: 2027-03-15
tags: [repositories, agents, context, kiss]
---

# KISS Repository Starter Adoption

Use the public [repo-starter](https://github.com/amitkarpe/repo-starter) GitHub
template for a new agent-managed repository. Treat it as a downstream baseline,
not a second global knowledge base. Agent OS owns reusable guidance; the active
repository owns its project truth and authority.

Current root responsibilities are:

1. `README.md`: human entrypoint and project purpose.
2. `AGENTS.md`: durable local rules and read order.
3. `CONTEXT.md`: current-only restart index, active truth, blocker, and next action.
4. `INIT.md`: first-time initialization interview/status only.
5. `CHATGPT.md`: ChatGPT/Codex/GitHub collaboration rules and repository-binding guard.
6. `ENV.md`: project runtime, cloud, tool, and external dependency facts.
7. `SPEC.md`: bounded execution/acceptance contract for implementation or mutation.
8. `ROADMAP.md`: only still-relevant future milestones.

Not every repository needs project-specific content in every file immediately,
but responsibilities should not be duplicated across competing files.

## New Repository

Create from the GitHub template, complete `INIT.md` once, replace only relevant
placeholders, and define one first useful outcome in `SPEC.md` when implementation
or mutation needs an execution contract. Do not import old chat logs, `.git` data,
dependencies, credentials, authentication state, copied repositories, or temporary
evidence.

## Existing Repository

Use a small `chore/repo-foundation` branch. Preserve the existing README and
product code. Add only missing responsibilities needed for safe agent work, then
record current truth and one next action. Do not rewrite history or add frameworks,
CI, tests, or a large documentation tree merely to adopt the template.

## File Rules

Keep root truth files short and role-specific:

- `CONTEXT.md` is current-only. Move completed history to Git history, closed
  Issues/PRs, or an existing history location.
- `AGENTS.md` changes only for durable repository-local operating rules.
- `INIT.md` is for initialization, not recurring planning.
- `CHATGPT.md` owns collaboration mechanics and connector/repository-binding
  behavior; reusable global rules should point back to Agent OS when practical.
- `ENV.md` records project dependency truth, not authority.
- `SPEC.md` is required when a change creates a trusted release, external
  contract, environment mutation, deployment, cleanup, or multi-step acceptance
  gate.
- `ROADMAP.md` contains only still-relevant future milestones.

The template gives structure, not authority. Current user instruction plus the
active repository's `AGENTS.md`, approved `SPEC.md`, owning Issue/PR, and project
context override generic Agent OS guidance.

For connector/platform safety blocks, follow the canonical
[Connector Safety Gate](../../policies/connector-safety-gate.md). Downstream
repositories may keep a short distilled rule, but Agent OS remains the canonical
policy home.

## Reusable Prompt

```text
Use https://github.com/amitkarpe/repo-starter and this Agent OS playbook:
https://github.com/amitkarpe/agent-os/blob/main/kb/playbooks/repositories/repo-starter-adoption.md

Prepare this existing repository for agent work. Preserve README.md and product
code. Add only the missing repo-starter responsibilities needed for safe work:
AGENTS.md, CONTEXT.md, INIT.md, CHATGPT.md, ENV.md, SPEC.md, and ROADMAP.md.
Keep CONTEXT.md current-only. Do not add scripts, tests, CI, dependencies,
temporary copies, or broad documentation merely for adoption. Stop on unknown
or uncommitted work and report the proposed diff before merge.
```
