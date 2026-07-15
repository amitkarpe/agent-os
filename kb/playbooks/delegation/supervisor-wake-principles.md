---
type: Pattern
title: Supervisor Wake Principles
description: Wake a controller only for new actionable evidence under explicit fail-closed gates.
status: reviewed
scope: unattended controller notification
confidence: high
timestamp: 2026-07-15T00:00:00+08:00
review_after: 2027-01-15
tags: [supervisor, notification, safety]
---

# Supervisor Wake Principles

## State Is Truth

Use deterministic state files, terminal result markers, and explicit policy as
the supervisor's inputs. A user interface snapshot may help delivery but should
not be the sole record of work or authority.

## Wake Gate

Wake only when all required conditions hold:

- unattended delivery is explicitly armed;
- the exact recipient is present, idle, stable, and safe to receive input;
- an approved goal exists;
- new evidence requires a decision or continuation; and
- the same evidence has not already been delivered.

No active goal or no new actionable evidence means no action.

## Suppression

Record delivered evidence and suppress duplicates. When the same hard blocker
repeats, stop waking until new input or state changes. Fail closed on uncertain
recipient identity, nonempty input, active work, missing approval, or unstable
state.

## Delivery Is Not Authority

Send one short file-backed pointer and perform at most one bounded acceptance
check. The supervisor may observe and notify; it must not expand scope, approve
work, or perform the controller's state-changing decisions.

## Validation

Test arming, wrong-recipient, active-state, nonempty-input, deduplication,
no-action, blocker suppression, and approved-goal cases. Start new deployments
in observe-only mode and prove that they leave an active controller untouched.
