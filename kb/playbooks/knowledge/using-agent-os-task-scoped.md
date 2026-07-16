---
type: Practice
title: Using Agent OS with Task-Scoped Context
description: Load the smallest relevant Agent OS guidance without overriding the active project's authority.
status: reviewed
scope: task-scoped knowledge use
confidence: high
timestamp: 2026-07-16T00:00:00+08:00
review_after: 2027-01-16
tags: [knowledge, context, agents, portability]
---

# Using Agent OS with Task-Scoped Context

Agent OS is reusable guidance, not automatic authority. Use it to improve a
task without flooding context or replacing the active project's rules.

## Minimal Context Flow

1. Locate a local clone through configured workspace context or an already
   configured `AGENT_OS_ROOT`. If neither is available, use the public Agent OS
   URL and start at [`kb/index.md`](../../index.md).
2. Read the Agent OS [`AGENTS.md`](../../../AGENTS.md) and
   [`kb/index.md`](../../index.md) first.
3. Select the route in **Start by task** that matches the current work.
4. Load only one to three relevant concepts. Do not preload the whole
   repository.
5. Treat the active project's instructions, `SPEC`, approvals, and
   safety policy as authoritative over generic Agent OS guidance.
6. Report conflicts instead of silently overriding local policy.
7. At closeout, state which Agent OS concepts were used.
8. Submit reusable learning as a sanitized candidate for curator review. Do
   not publish private runtime truth directly.

For controller-worker delegation, include the
[Controller-Worker Goal Execution Framework](../delegation/controller-worker-goal-execution-framework.md)
in the task-scoped set.

## Generic Copy-Ready Prompt

```text
Use Agent OS guidance for this task.

Agent OS source: <AGENT_OS_ROOT or public Agent OS URL>
Active project: <active-project-root or repository context>
Task: <task>

Read the active project's instructions and SPEC first. Then read Agent OS AGENTS.md and
kb/index.md, choose the matching task route, and load only one to three relevant
concepts. Active project specifications, approvals, and safety policy override
generic guidance. Report any conflict. If this task delegates controller-worker
execution, include:
<agent-os-root>/kb/playbooks/delegation/controller-worker-goal-execution-framework.md

At closeout, name the Agent OS concepts used. Submit reusable learning only as
a sanitized candidate; do not add private runtime truth directly.
```
