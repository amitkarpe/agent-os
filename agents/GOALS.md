---
type: Policy
title: Goal Execution and Delegation
description: Continue one approved agent goal with bounded delegation, evidence, and stop gates.
status: reviewed
scope: Reusable public-safe agent goal execution and delegation
confidence: high
timestamp: 2026-10-21T18:00:00+08:00
review_after: 2027-04-21
tags: [goals, delegation, evidence, agents, context]
---

# Goals and Delegation

The owning project, Issue/PR, specification and approval define authority.
This guide helps an agent execute that work; it does not grant permission for
cloud, production, credentials, publication or destructive actions.

## One approved goal

Use one complete goal for one bounded outcome. It should name the repository,
scope, allowed writes, success evidence and stop conditions. Continue obvious
steps inside that boundary without asking for a new approval at every
milestone. A milestone, plan, push or queue receipt is progress, not proof of
completion.

Start with the smallest current truth: owning Issue/PR, latest handoff,
current HEAD and dirty state. Reload broader context only when the repository,
authority, governing file or safety boundary is unclear or changed. Preserve
unrelated work and stop on conflicting ownership or target identity.

## Tight execution loop

For each meaningful wave:

1. ingest current goal and repository truth;
2. choose the next bounded action;
3. implement or execute inside the approved scope;
4. run the narrowest meaningful validation and inspect its output;
5. record durable evidence when the work is long-lived or stateful; and
6. reassess whether the goal is complete or another approved wave remains.

Do not create a watcher, daemon, framework or duplicate runner merely to keep a
goal moving. A long command may be bounded and interruptible, but a process
status or agent display is not completion evidence.

## Delegation

Delegate only an independently answerable question that saves meaningful
coordination or review effort. Give every helper one objective, one owner for
each mutable file set, allowed sources and writes, required evidence, and stop
conditions. Keep one writer per mutable surface; make independent reviewers
read-only. The controller accepts evidence; a worker's report or transport
receipt is not acceptance.

Use the existing provider-native transport and adapter. Transport creates no
authority and does not prove execution. For persistent Codex sessions, use the
[native controller-worker protocol](../kb/playbooks/delegation/codex-native-controller-worker-protocol.md).
Keep provider setup, host paths, versions and authentication in the provider's
local adapter, not in this public guide.

## Stop gates and closeout

Stop and report a blocker when the next action would widen scope, change
authority, touch production or destructive state without approval, expose a
secret/private fact, encounter uncertain identity or ownership, or require a
non-obvious recovery decision. Do not silently create a second worker or
replay an uncertain mutation.

Finish the approved work, validate the actual result, and write the durable
Issue/PR or result record before sending one completion notification. Reconcile
the final repository or external state when the goal changed it. Cleanup is a
separate authorized action: age, TTL, a marker or a queue notice does not grant
deletion authority.

For deeper sequencing, gates and evidence use the
[Controller-Worker Goal Execution Framework](../kb/playbooks/delegation/controller-worker-goal-execution-framework.md),
[Effective Subagent Delegation](../kb/playbooks/delegation/effective-subagent-delegation.md),
and [Context Loading Policy](../kb/policies/context-loading-policy.md).
