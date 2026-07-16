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

## Learn

1. Locate a local clone through configured workspace context or an already
   configured `AGENT_OS_ROOT`. If neither is available, use the public Agent OS
   URL and start at [`kb/index.md`](../../index.md).
2. Read the Agent OS [`AGENTS.md`](../../../AGENTS.md),
   [`README.md`](../../../README.md), and [`kb/index.md`](../../index.md).
3. Treat the repository as reusable guidance and inspiration. Do not preload
   the whole knowledge base.

## Apply

1. Select the matching route in **Start by task** and load only one to three
   relevant concepts.
2. Briefly state what applies, what does not apply, and any conflict with the
   active project.
3. Treat the active project's instructions, `SPEC`, approvals, and safety
   policy as authoritative over generic Agent OS guidance.
4. Apply only the useful guidance to planning and execution. Report conflicts
   instead of silently overriding local policy.

For controller-worker delegation, include the
[Controller-Worker Goal Execution Framework](../delegation/controller-worker-goal-execution-framework.md)
in the task-scoped set.

## Contribute

1. At closeout, name the Agent OS concepts used.
2. Suggest reusable learning as a sanitized candidate for curator review under
   the [Knowledge Lifecycle and Publication](../../policies/knowledge-lifecycle-and-publication.md)
   policy.
3. Do not publish private runtime truth or modify Agent OS unless explicitly
   asked.

Use the concise [universal onboarding prompt](../../../README.md#universal-onboarding-prompt)
when a reusable instruction is needed.
