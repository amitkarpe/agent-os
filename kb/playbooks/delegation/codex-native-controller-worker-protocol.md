---
type: Playbook
title: Codex Native Controller-Worker Protocol
description: Use durable goals and results with native Codex queue transport and the Agent Command Center as an observability surface.
status: reviewed
scope: Codex CLI controller-worker sessions
confidence: medium
timestamp: 2026-08-31T00:00:00+08:00
last_verified: 2026-08-31
review_after: 2026-10-31
tags: [codex, controller, worker, queue, agents, delegation, completion]
---

# Codex Native Controller-Worker Protocol

## Decision

Use native `codex queue` as the normal transport between persistent Codex
controller and worker sessions. Use the Agent Command Center for human
visibility and lifecycle operations. Keep a supervisor or screen-key delivery
system only as a fallback when native queue delivery is genuinely unavailable.

Do not build normal automation around custom composer keys such as `F12`.
Interactive keys can change by version or local configuration, while native
queue delivery addresses the Codex session directly.

This protocol is based on repeated local controller-to-worker,
worker-to-worker, and worker-to-controller use. The exact non-interactive
`codex queue` command and Agent Command Center behavior are CLI-version
sensitive. Check the installed version and command help before adopting the
examples unchanged.

## Three separate responsibilities

| Layer | Purpose | It does not prove |
| --- | --- | --- |
| Durable goal and result | Scope, authority, evidence, and terminal truth | Message delivery |
| `codex queue` | Native message transport to a Codex session | Execution, success, or approval |
| Agent Command Center | Search, open, start, rename, stop, and observe managed tasks | Message acceptance, authority, or completion |

Keep these layers separate. A healthy worker display does not prove that a
goal completed. A queue receipt does not prove that a worker executed the
goal. A result file does not prove that its final state was accepted.

## Persistent workers and subagents are different

A persistent worker is an independent Codex session with its own thread,
workspace, context, and lifecycle. It can be named, resumed, observed in the
Agent Command Center, and addressed through native queue transport.

A subagent is a bounded child created by a parent agent for one part of the
current task. It normally reports back to that parent and is not a replacement
for a durable role-owned worker session.

Use persistent workers for long-lived ownership, operational lanes, and work
that needs durable goals and results. Use subagents for small independent
research, inventories, validation, or reviews whose findings return to the
parent task.

## Identity

Record these fields separately:

- stable Codex thread UUID;
- unique human-readable session name;
- intended repository or working directory;
- optional terminal or tmux location; and
- assigned worker role.

Use the UUID for deterministic automation. A unique name is acceptable for
convenient manual use after uniqueness is verified. A tmux pane name, process
title, or visible label is not session identity.

Do not hard-code session UUIDs in project policy or general-purpose scripts.
Resolve them from the owning environment's registry at delivery time.

## Controller to worker

Before sending a message:

1. Confirm the installed CLI exposes `codex queue` and review its current
   command help.
2. Write the complete durable goal.
3. Record the requested outcome, scope, approved mutations, success evidence,
   and stop conditions.
4. Confirm the worker identity, role, and intended workspace.
5. Keep the queue message short and point to the durable goal.
6. State provenance with `FROM`, `Requested by`, and `Delegated by`.

Example:

```bash
MSG='FROM controller: Execute the approved goal at <goal-path>. Return one terminal result at the goal-defined path. Queue admission is not execution or completion.'
codex queue --thread <worker-uuid> --message "${MSG}"
```

Quote `"${MSG}"`. An unquoted or empty shell variable can turn a correct
delivery into a missing-argument failure.

When the command returns a valid queue receipt, delivery is finished. Do not:

- paste the same message into tmux;
- press `Enter`, `Tab`, or `F12` as a second delivery method;
- inspect the worker composer to see whether the text appeared;
- resend because the worker still looks `Ready`; or
- treat the receipt as completion.

Native queue may wake or immediately advance an idle worker. Therefore, verify
the message and authority before sending it, especially for transaction-capable
or production workers.

## Worker to controller

The worker completes the durable artifact before notifying the controller:

1. Finish the approved work or reach a truthful terminal stop.
2. Write and validate one durable terminal result.
3. Reconcile current state when the task changed external or persistent state.
4. Send one short native queue message containing the result path.
5. Stop; do not repeatedly notify, poll, or paste the full result.

Example:

```bash
MSG='FROM worker: Terminal result ready for controller review: <result-path>. Queue admission is not acceptance or completion.'
codex queue --thread <controller-uuid> --message "${MSG}"
```

Routine messages do not need a visible SHA-256 value. Keep hashes as quiet
integrity and deduplication evidence, and show one only for a real stale-file,
supersession, external-transfer, or authority-binding dispute.

## Controller acceptance

The controller accepts a result only after checking the evidence required by
the goal. For stateful or risky work, acceptance normally requires both:

- the durable result; and
- fresh current-state verification.

Use truthful terminal states such as `SUCCESS`, `HEALTHY/ARMED/NO_ACTION`,
`PARTIAL`, `BLOCKED`, `FAILED`, or `UNKNOWN_PENDING`. A chat message, queue
receipt, task status, transaction hash, or pane state alone is not terminal
proof.

## Agent Command Center

The Agent Command Center is the preferred human dashboard for persistent Codex
sessions. It is useful for:

- finding sessions across repositories;
- seeing broad `Working`, `Ready`, or needs-input state;
- opening the correct thread;
- starting, renaming, or stopping a managed task; and
- reducing dependence on terminal-pane numbering.

It is intentionally not the transport or authority layer. Do not scrape its
screen as a completion API, and do not infer that `Ready` means a queued goal
was ignored or that `Working` means the correct goal was accepted.

## Steering, queuing, and native delivery

Codex also supports interactive steering and queuing while a run is active.
Interactive `Enter` can steer the current turn and `Tab` can queue a follow-up
for the next turn in supported CLI versions. That composer behavior is useful
for a human operator, but it is separate from UUID-addressed `codex queue`
transport between persistent sessions.

For controller-worker automation, prefer native queue transport. Do not depend
on a custom function key. Treat interactive key behavior as local and
version-sensitive.

## Fallback only

Keep an existing supervisor, durable notification queue, or terminal delivery
adapter only for recovery when native queue:

- returns a clear failure;
- returns an uncertain result with no usable receipt; or
- is unavailable for the target session type.

One explicit recovery attempt is enough. Do not invoke the fallback after a
valid native queue receipt. Do not restore `F12` as the normal submit key.

A fallback transports a pointer; it does not become the source of truth. The
durable goal/result remains authoritative.

## Authority and safety

Transport never creates authority. Repository instructions, approved goals,
specifications, machine policy, permissions, hard guards, journals, receipts,
and reconciliation remain authoritative.

Do not place secrets, credentials, tokens, private keys, raw environment
values, or signer material in queue messages, names, dashboards, goals, or
results.

For corrections, send one clear superseding goal or result identity. Do not
assume a later message silently cancels already accepted work. Preserve
ambiguous or possibly executed state until it is reconciled.

## Minimum adoption checklist

- [ ] Persistent sessions have unique recorded UUIDs and names.
- [ ] The installed CLI exposes `codex queue`, and its current help was
      reviewed.
- [ ] Each worker has one intended role and workspace.
- [ ] Goals and results are durable files.
- [ ] Queue messages contain provenance and one exact artifact path.
- [ ] A valid receipt ends delivery; no tmux or key fallback follows it.
- [ ] The Agent Command Center is used for visibility, not proof.
- [ ] Completion requires controller acceptance, not a receipt or status dot.
- [ ] Supervisor/SS-style delivery is fallback only.
- [ ] No workflow depends on `F12`.
- [ ] Project authority and safety rules override this portable playbook.

## Citations

- [OpenAI Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
- [OpenAI prompting: steering and queuing](https://learn.chatgpt.com/docs/prompting#steering-and-queuing)
- [Controller-Worker Goal Execution Framework](controller-worker-goal-execution-framework.md)
- [Completion Notification without Polling](completion-notification-without-polling.md)
- [Named Agent Session Reuse](../codex/named-session-reuse.md)
