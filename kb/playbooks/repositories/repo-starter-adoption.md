---
type: Practice
title: KISS Repository Starter Adoption
description: Create or retrofit an agent-managed repository with five small root files.
status: reviewed
scope: repository foundation
confidence: high
timestamp: 2026-09-03T01:00:00+08:00
review_after: 2027-03-03
tags: [repositories, agents, context, kiss]
---

# KISS Repository Starter Adoption

Use the public [repo-starter](https://github.com/amitkarpe/repo-starter) GitHub
template for a new agent-managed repository. It contains five small root files:

1. `README.md`: human entrypoint and project purpose.
2. `AGENTS.md`: local rules and read order.
3. `CONTEXT.md`: current truth and next action.
4. `SPEC.md`: a bounded acceptance contract.
5. `ROADMAP.md`: the next few milestones.

## New Repository

Create from the GitHub template, replace placeholders, and define one first
outcome in `SPEC.md`. Do not import old chat logs, `.git` data, dependencies,
credentials, or temporary evidence.

## Existing Repository

Use a small `chore/repo-foundation` branch. Preserve the existing README and
product code. Add only the missing root files, then record current truth and
one next action. Do not rewrite history or add frameworks, CI, tests, or a
large documentation tree merely to adopt this template.

## File Rules

Keep `AGENTS.md`, `CONTEXT.md`, `SPEC.md`, and `ROADMAP.md` short. `CONTEXT.md`
changes with active work; `AGENTS.md` changes only for durable local rules.
`SPEC.md` is required when a change creates a trusted release, external
contract, environment mutation, or multi-step acceptance gate. `ROADMAP.md`
contains only still-relevant milestones.

The template gives structure, not authority. The active repository's rules,
approved SPEC, and safety boundaries always win over generic Agent OS guidance.

## Reusable Prompt

```text
Use https://github.com/amitkarpe/repo-starter and this Agent OS playbook:
https://github.com/amitkarpe/agent-os/blob/main/kb/playbooks/repositories/repo-starter-adoption.md

Prepare this existing repository for agent work. Create only missing KISS root
files: AGENTS.md, CONTEXT.md, SPEC.md, and ROADMAP.md. Preserve README.md and
all product code. Use a small foundation branch. Do not add scripts, tests, CI,
dependencies, temporary copies, or broad documentation. Stop on unknown or
uncommitted work and report the proposed diff before merge.
```
