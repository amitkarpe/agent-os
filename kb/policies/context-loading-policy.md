---
type: Policy
title: Context Loading Policy
description: Load context on change, not on every turn - event-driven cold-start and warm-continuation reads with explicit reload triggers.
status: reviewed
scope: agent cold-start, warm continuation, and handoffs across repositories
confidence: high
timestamp: 2026-09-18T10:00:00+08:00
review_after: 2027-03-18
tags: [context, handoff, delegation, efficiency, kiss, bootstrap]
---

# Context Loading Policy

KISS: **load on change, not on every turn.** Context loading is event-driven,
not per-turn or per-handoff. Do not re-read `AGENTS.md`, `CONTEXT.md`,
`SPEC.md`, `ROADMAP.md`, or broad repository history on every mission, turn, or
session merely because a new one started. Read wider context only when a
concrete event or trigger requires it.

## Cold start

On a genuine cold start, read ONLY:

1. the repository rules needed to operate safely (the repository's `AGENTS.md`),
   once;
2. the owning Issue/PR;
3. the current branch/HEAD.

Read `CONTEXT.md`, `SPEC.md`, `ROADMAP.md`, or broader history only when:

- the owning Issue/PR explicitly references them;
- their fingerprint changed;
- the task requires that exact content; or
- recovering from stale or missing state.

## Warm continuation

On warm continuation, reuse already-loaded context and fingerprints. Read only:

- the latest relevant owning Issue/PR comment or handoff;
- the current HEAD/status/diff needed for the task; and
- the exact files needed for the next action.

Do NOT reload all bootstrap or context files merely because a new agent turn,
session, or handoff started.

## Reload triggers

A broad reload is allowed only on:

- repository switch;
- explicit context mismatch;
- material rules or spec change;
- recovery after uncertain or stale state; or
- explicit user request.

A new PR number, milestone, turn, or session alone is not a reload trigger.

## Child repositories link, do not duplicate

Agent OS is the canonical home for this rule. Child and downstream repositories
should LINK to this policy rather than copy it, mirroring how repositories point
to the [Connector Safety Gate](connector-safety-gate.md). A downstream repository
may keep a short distilled pointer to this policy, but Agent OS remains the
canonical home for the cold-start and warm-continuation rule.

## Safety invariants

Loading less context never lowers safety or authority requirements.

- Connector, worker, or comment observations are not approval; the latest
  comment is not authority merely because it is latest.
- Stop or reload on uncertain identity, conflicting evidence or authority,
  material HEAD changes, or entry into a new trust, authority, or security
  boundary.
- Never guess missing authority - reconstruct it from repository truth before
  acting.

These invariants stay consistent with the repository `AGENTS.md` and the
[Context Loading Economy for Agent Handoffs](../playbooks/integrations/context-loading-economy.md)
playbook; nothing here overrides an explicit no-go gate or enforced control.

## Related

- [Context Loading Economy for Agent Handoffs](../playbooks/integrations/context-loading-economy.md) - the handoff-focused procedure and adoption detail; this policy is the canonical event-driven cold-start and warm-continuation rule.
- [Knowledge Lifecycle and Publication](knowledge-lifecycle-and-publication.md)
- [Connector Safety Gate](connector-safety-gate.md)
