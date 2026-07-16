---
type: Pattern
title: Controller-Worker Goal Execution Framework
description: Use Fast Goal by default and extend it only when risk requires a Deep Goal.
status: reviewed
scope: controller-worker execution
confidence: high
timestamp: 2026-07-16T00:00:00+08:00
review_after: 2027-01-16
tags: [controller, worker, goals, planning, gates]
---

# Controller-Worker Goal Execution Framework

## Vocabulary

| Term | Meaning |
| --- | --- |
| Workstream or Lane | An optional long-running area of responsibility. |
| Goal | The complete outcome delegated once. |
| Plan | The ordered method created or refined by the worker. |
| Phase | An optional major block used when a Deep Goal needs more structure. |
| Task | One bounded deliverable inside a phase. |
| Step | One action inside a task. |
| Command or Run | One deterministic execution of a script, job, or other repeatable operation. |
| Gate | An objective condition that determines whether execution may continue. |
| Milestone | Recorded progress; it is not automatically an approval stop. |
| Approval envelope | The scope, mutations, systems, and conditions authorized for the complete goal. |
| No-go gate | Written condition that requires the worker to stop. |
| Result | The concise terminal record of outcome, evidence, validation, and remaining risk. |

## Ownership

The controller owns the outcome, scope, approval envelope, safety constraints,
acceptance criteria, and final acceptance. The worker owns execution truth,
creates or refines the plan, performs the approved work, validates it, and
returns evidence.

Delegate one complete Goal rather than a stream of separate prompts. This gives
the worker enough context to sequence work while keeping authority bounded by
the original approval envelope.

## Choose the Mode

Use **Fast Goal** for most work. Use **Deep Goal** only when risk or complexity
needs more structure. The controller chooses the smallest mode that safely
defines the work.

When either mode is reasonable, offer:

```text
Mode: Fast (recommended) or Deep
```

If the risk clearly requires Deep Goal, select it directly and explain why in
one line. Do not ask a mode question when the answer is obvious.

## Fast Goal

Fast Goal is the default. Keep it short and simple. Do not force phases into
it.

```text
Create and execute one complete Fast Goal.

Outcome: <required final state>
Scope: <allowed files, systems, or resources>
Approved: <allowed actions and mutations>
Success: <observable proof of completion>
Stop: <hard blockers, safety guards, ambiguity, or authority changes>

Continue automatically inside this approval envelope.
Milestones are not approval stops.
Use: inspect -> act -> validate -> continue.
Return one concise final Result.
```

The worker creates or refines the Plan needed to reach the outcome. It may
diagnose and correct failed validation when the correction remains inside
Scope and Approved actions. It stops at a written Stop condition, unexpected
scope or risk, unavailable required authority, irrecoverable validation
failure, or final completion.

## Deep Goal

Deep Goal extends Fast Goal with only the fields needed for the risk:

- up to four Phases;
- deterministic Gates;
- evidence paths;
- rollback or cleanup;
- environment, account, or resource identity; and
- stronger no-go conditions.

Use Deep Goal for:

- production or destructive mutation;
- infrastructure, database, network, IAM, or state migration;
- multiple repositories or systems;
- recovery or partial-failure risk; or
- unattended long-running execution.

Do not copy a large template when only one or two extensions are needed. Both
modes authorize automatic continuation inside the written approval envelope,
and Milestones remain progress rather than approval stops.

## Planning Only

```text
Prepare one complete Fast Goal or Deep Goal for controller review. Choose the
smallest mode that safely defines the work. Do not execute or mutate anything
until the complete Goal is approved.
```
