---
type: Playbook
title: Context Loading Economy for Agent Handoffs
description: Reuse valid context without losing authority, enduring intent or execution-host knowledge.
status: reviewed
scope: GitHub-centered ChatGPT, Codex, and repository-worker handoffs
confidence: high
timestamp: 2026-09-17T01:55:00+08:00
last_verified: 2026-09-17
review_after: 2027-03-17
tags: [chatgpt, codex, github, context, handoff, delegation, efficiency]
---

# Context Loading Economy for Agent Handoffs

Use the smallest durable pointer sufficient to continue safely. The owning
Issue/PR records current work; the latest relevant authorized comment is the
delta. **Optional rereading is not optional authority.** Task history does not
replace enduring requirements, host constraints or observed runtime evidence.

## Normal continuation

When repository identity, objective and governing context remain usable:

```text
owning Issue/PR -> relevant authorized delta -> current HEAD/diff
-> changed governing context and required runtime evidence -> continue
```

Give the existing pointer and exact comment URL only when useful. Do not copy
the full plan, completed history or file-reading checklist. `go` stays within
the selected scope and mode; a newer or agent-authored comment is not approval
merely because it is the latest comment.

## Full context reload triggers

Reload affected context when the session lacks it, a governing file materially
changes, repo/goal/host identity is ambiguous, evidence contradicts cached
state, or a new authority/security/production/destructive boundary is entered.
A PR number or milestone change alone does not require a full reload.

Use existing fingerprints/references when available, not a new caching system.
If freshness cannot be established, reload the relevant contract before action.

## Bootstrap / recovery order

Follow repository-specific cold-start requirements. Generally establish:

1. repository/worktree identity, HEAD and local `AGENTS.md`;
2. owning Issue/PR and relevant authorized decision/handoff;
3. applicable operating contract, desired-state configuration and host/project
   environment context;
4. unique restart state and live facts required for the action.

A locally required `SPEC.md` cannot be skipped because a generic starter makes
that filename optional. Missing authority blocks the controlled action.

## Handoff economy

The existing record must preserve outcome, allowed scope, acceptance, stop
gates and relevant research/evidence. Same-PR corrections need head, delta and
proof, not another packet. The [collaboration playbook](chatgpt-codex-collaboration-protocol.md)
owns transport and human-copy handoff rules.

## Project and local context

The [core-file model](chatgpt-codex-collaboration-protocol.md#core-files-and-durable-truth)
separates reusable Agent OS policy, repository contracts/configuration,
GitHub current-work records and host-specific knowledge.

Preserve the existing dotfiles/local host profiles and active-host selection.
Project `ENV.md`, when needed, records workload dependencies and approved
execution targets, not another copy of the entire machine inventory. Resolve
the execution host, not just the browser host. If that host forbids a required
tool installation, select an authorized compatible target or report the
blocker. Remote compute does not authorize moving corporate data elsewhere.

Credentials/authentication state stay out of these documents. Private facts
stay in appropriately private/local sources, never public Agent OS. Manage
ChatGPT Project source membership through its owning product surface and
preserve unique information before removing duplicates.

## Safety invariants

Stop or reload on uncertain identity, conflicting evidence/authority, material
HEAD changes or entry into a new trust boundary. Preserve explicit no-go gates
and enforced controls. A worker observation, recommendation or receipt is not
approval. Reconstruct missing authority; never guess.

## Adoption pattern

Before removal or renaming, map unique content to its surviving home and audit
scripts, prompts, links and runtime consumers. `CONTEXT.md` and `CHATGPT.md`
remain where they contain unique recovery state or adapter rules.

Prove normal warm continuation and an authority/host-sensitive case on one
non-critical pilot; a paper policy review is not a live pilot result. Keep
rollback, then simplify downstream repositories gradually when next touched.
Do not mass-delete files or disturb live delivery for smaller file counts.

```text
project learning -> sanitize/deduplicate -> Agent OS
-> starter where universal -> existing repos when next touched
```

## Related playbooks

- [ChatGPT and Codex Collaboration Protocol](chatgpt-codex-collaboration-protocol.md)
- [ChatGPT Project Context and File Surfaces](chatgpt-project-context-and-files.md)
- [Knowledge Lifecycle and Publication](../../policies/knowledge-lifecycle-and-publication.md)
