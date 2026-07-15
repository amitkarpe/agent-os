---
type: Practice
title: Effective Subagent Delegation
description: Delegate bounded work when parallelism or independent review outweighs coordination cost.
status: reviewed
scope: multi-agent task execution
confidence: high
timestamp: 2026-07-15T00:00:00+08:00
review_after: 2027-01-15
tags: [delegation, subagents, evidence]
---

# Effective Subagent Delegation

## Balanced Delegation

Delegate when a question is independently answerable, read-heavy, repetitive,
parallelizable, or benefits from independent review. Keep tiny, tightly coupled
actions with the controller when setup and review would cost more than the work.

## Launch Checklist

Before launch, define:

1. one exact question or bounded objective;
2. allowed sources and mutation boundaries;
3. one owner for every mutable surface;
4. the required result artifact and evidence;
5. blocker and stop conditions; and
6. who accepts or rejects the result.

Parallel workers may explore or review the same problem, but only one should
write a given file set. Make independent reviewers read-only.

## Completion

Treat workers as asynchronous. Require one terminal result or clear blocker,
continue non-overlapping work, and consume the result when notified. Do not
launch monitoring-only workers or create sleep and polling loops.

A submitted task or completion notice is not acceptance. The controller must
review evidence, resolve uncertainty, and record durable learning in the owning
project.

## Anti-Patterns

- Choosing the most expensive profile before understanding the task.
- Assuming a profile name proves the active model or effort.
- Giving two workers overlapping write ownership.
- Asking a worker to monitor another worker indefinitely.
- Letting a read-only worker make policy or state-changing decisions.
- Reconstructing a missing result from memory without labeling the gap.

## Citations

- [OpenAI Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md)
- [OpenAI Codex prompting](https://developers.openai.com/codex/prompting/#steering-and-queuing)
- [OpenAI Agents SDK handoffs](https://openai.github.io/openai-agents-python/handoffs/)
