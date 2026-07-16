---
type: Pattern
title: Controller-Worker Goal Execution Framework
description: Delegate one complete outcome under explicit approval, gates, evidence, and stop conditions.
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
| Phase | One major block of the plan; use no more than four by default. |
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

Delegate one complete Goal rather than a stream of separate phase prompts.
This gives the worker enough context to sequence work while keeping authority
bounded by the original approval envelope.

## Execution Contract

1. State the complete Goal, approval envelope, acceptance criteria, and no-go
   gates before execution starts.
2. The worker creates or refines one Plan with no more than four Phases by
   default. Each Phase contains bounded Tasks and deterministic Gates.
3. When a Gate passes, the worker continues automatically to the next Task or
   Phase inside the approval envelope. Record Milestones without treating them
   as new approval stops.
4. The worker stops only for a written no-go condition, unexpected scope or
   risk, unavailable required authority, irrecoverable validation failure, or
   final completion.
5. On completion, the worker returns one concise Result with acceptance
   evidence, changed state, validation, remaining risk, and the next safe
   action.

Failed Gates are not always irrecoverable. The worker may diagnose and correct
them when the correction remains inside the approval envelope and safety rules.
Any expansion of scope or authority returns to the controller.

## Generic Execution Prompt

```text
Execute this complete Goal continuously.

Outcome: <complete outcome>
Scope: <owned systems and files>
Approval envelope: <approved actions and mutations>
Acceptance: <observable success criteria>
No-go gates: <conditions that require a stop>

Create or refine one Plan with no more than four Phases by default. Put bounded
Tasks and deterministic Gates inside each Phase. Continue automatically when a
Gate passes and work remains inside the approval envelope. Stop only at a
written no-go gate, unexpected scope or risk, unavailable required authority,
irrecoverable validation failure, or final completion. Return one concise
Result with evidence and remaining risk.
```

## Planning-Only Prompt

```text
Prepare one Plan for this complete Goal with no more than four Phases by
default. Define Tasks, deterministic Gates, the approval envelope, acceptance
criteria, no-go gates, evidence, and remaining risks. Do not execute or mutate
anything until the complete Goal is approved.
```
