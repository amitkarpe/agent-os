---
type: Playbook
title: ChatGPT and Codex Collaboration Protocol
description: A GitHub-only review exchange combined with native Codex controller-worker delivery and milestone-sized change management.
status: reviewed
scope: Public-safe ChatGPT review and Codex repository workflows
confidence: medium
timestamp: 2026-09-02T00:00:00+08:00
last_verified: 2026-09-02
review_after: 2026-11-02
tags: [chatgpt, codex, github, review, delegation, milestones]
---

# ChatGPT and Codex Collaboration Protocol

Use this reusable playbook for GitHub collaboration between ChatGPT and a Codex
repository controller. The owning repository's instructions, authority protocol,
approved scope, and safety gates take precedence over this public guidance.
Use an accessible repository-owned protocol or this committed playbook; no Gist
or local scratch file is required.

## Decision flow

Keep the roles and gates in this order:

```text
define scope and mode -> inspect repository truth -> reuse or create Issue
-> review or implement approved milestone -> validate -> review complete PR diff
-> correct in same PR -> ready for review -> merge only when authorized
```

ChatGPT gives a recommendation. A recommendation is not authorization, cloud
proof, or a substitute for repository checks and human approval.

## Roles and boundaries

| Role | Responsibility |
| --- | --- |
| User / repository owner | Defines scope and authorizes publication, implementation, cloud, and destructive actions. |
| Codex controller | Reads repository truth, prepares sanitized packets, validates responses, and coordinates authorized work. |
| Codex worker | Executes one approved goal in its owning repository and writes the durable result. |
| ChatGPT reviewer / editor | Reviews committed truth; updates the owning Issue and PR within the selected authority mode. |
| GitHub Issue/PR | Durable public work record; it does not replace local evidence or acceptance. |

Do not claim an Issue, PR, commit, comment, or merge without GitHub confirmation.
If a required action is unavailable, report the exact access blocker; do not
create a competing implementation lane.

## Authority modes

- `REVIEW`: analyze and create or update the owning Issue; no implementation.
- `EDIT`: create or update the Issue and PR; leave the PR unmerged.
- `COMPLETE`: finish eligible bounded GitHub work, merge, and close its Issue
  only when explicitly authorized by the owning repository's contract.

`go` continues the selected mode, never silently upgrades it. Explicit no-merge,
no-mutation, and scope limits remain binding. Governing-authority changes need
owner/controller review, not self-merge. GitHub access is not permission for
cloud, deployment, cleanup, credential, or source-publication changes.

## GitHub-only ChatGPT exchange

ChatGPT cannot read local Linux paths. Exchange only a committed, public-safe
Markdown packet or GitHub Issue/PR URL. Do not use browser automation,
clipboard automation, an authenticated browser profile, or direct GUI
submission for this workflow.

Reuse the Issue and PR that already own the milestone. Create one Issue only
when no existing record owns the objective or the user explicitly requests a
standalone architecture response. Keep decisions in that Issue and corrections,
review findings, and validation in the same PR.

For architecture or cross-repository review, provide an accessible governing
protocol and one self-contained packet at an immutable `blob/<commit-sha>/...`
URL. Use moving `blob/main` links for orientation, not evidence identity.

For a correction in the same PR, provide its URL, exact head commit, requested
delta, and acceptance condition. Do not require a new Issue, packet, outbox
copy, handoff, or planning file. Existing exchange files may remain historical
references; their layout is not a mandatory workflow.

## Current-repository gate

Before preparing a packet, verify:

```bash
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git remote get-url origin
git branch -vv
gh repo view --json nameWithOwner,url,visibility,defaultBranchRef
```

Read the repository `AGENTS.md` and current context. Inspect the latest merged
PR, its linked Issue, and existing open Issues/PRs. Stop when repository
identity, authority, default branch, or publication safety is ambiguous.

## Request packet contract

Include only the context needed for one review question:

- objective and exact question;
- accessible repository-owned protocol or this committed public playbook;
- repository name and immutable source links;
- latest accepted milestone and relevant open records;
- current verified behavior and validation;
- approved scope, no-go gates, and deferred work;
- requested response format; and
- a publication-safety statement.

Do not include broad chat history, raw logs, credentials, tokens, `.env`
content, private keys, account IDs, ARNs, private endpoints, hostnames, IP
addresses, customer material, or raw cloud payloads. Summarize private facts
with aliases or sanitized evidence.

## Next-step selection gate

Finish all approved slices of the current milestone before proposing another.
Ask for a new decision only when scope, authority, safety, or a genuine blocker
requires it; do not request a fresh architecture review for every correction.

When a new objective is needed, inspect current repository truth and open work,
then record one cohesive recommendation in the owning Issue: scope, non-goals,
risks, acceptance criteria, validation, and deferred work. Codex checks it against
current truth rather than silently substituting another feature.

## Milestone-sized Issue and PR rule

A PR represents one cohesive implementation milestone, not one tiny task.
Group roughly two to five tightly related slices when they share the
same architecture, security boundary, user workflow, deployment/lifecycle,
and acceptance goal.

Keep directly related tests, documentation corrections, configuration changes,
and implementation fixes in the existing PR. Do not create a new Issue/PR
only because one test, correction, or acceptance case was discovered.

Create a separate Issue/PR only when the work materially changes:

1. architecture or required technology;
2. security or authorization model;
3. user workflow or trust boundary;
4. external integration;
5. an independent capability;
6. deployment or lifecycle boundary; or
7. reviewability because the current PR would become unsafe or oversized.

Preferred lifecycle:

```text
Issue -> implement related slices -> validate -> review complete target-branch diff
-> fix same-PR findings -> ready PR -> merge only when authorized
```

Use draft only while work is incomplete or unsafe to review; complete work gets
one ready, non-draft PR. Keep small corrections in that PR and finish the approved
batch rather than creating per-line handoffs. This avoids both micro-PR overhead
and oversized mixed changes.

## Native Codex controller-worker delivery

Use the [Codex Native Controller-Worker Protocol](../delegation/codex-native-controller-worker-protocol.md)
for the dispatch contract. Native `codex queue` is the only message transport
between verified persistent Codex sessions, including controller-to-worker,
worker-to-worker, and result notifications to the controller. Durable goals,
exact target UUIDs, approved scope, and an explicit `Reply-To` remain required.

A valid queue receipt proves transport admission only, not recipient
acknowledgement, execution, completion, or acceptance. Record
`notification_queued`; that send attempt is finished. Never send another copy
through queue, tmux, composer, supervisor, `Enter`, `Tab`, `F12`, or file mention,
or resend because a worker still looks `Ready`.

Without a valid receipt after a failed, unavailable, or uncertain send, record
`BLOCKED_TRANSPORT`. Follow the canonical
[stop-and-repair rule](../delegation/codex-native-controller-worker-protocol.md#queue-failure-stop-and-repair):
reconcile possible original admission/execution, repair transport or session
identity within scope, and permit at most one redispatch only when safe and
still authorized. Unresolved uncertainty or a failed redispatch stays blocked.
A valid receipt ends the attempt; it is never a prerequisite for another send.

The worker writes and validates its durable `RESULT.md` before sending the
result pointer to the exact `Reply-To`. A `.done` marker may point to the result;
it does not establish controller acceptance. The controller checks the required
evidence and, for stateful work, fresh current-state proof. A blocked notification
does not invalidate or authorize deletion of the completed result.

## Persistent workers and subagents

Persistent workers own a long-lived repository lane and use durable goals,
contexts, results, and named sessions. Subagents are short-lived children for
one independent research, inventory, validation, or review question. Do not
use a subagent for tightly coupled coordination, critical-path waiting, or a
same-file edit that the controller can safely perform.

Use one exact question per helper, require compact evidence paths and stop
conditions, and close completed helpers. Transport, queue status, and a worker
dashboard never create authority.

## Controller acceptance and KISS diff gate

For every candidate result, compare it with the recorded base commit and run a
small diff review. Reject or reduce unnecessary runners, dependencies,
frameworks, services, permissions, cloud resources, parallel paths, or
optional polish. A technically passing result is not accepted when it widens
the approved target without a new decision.

Use truthful terminal states such as `SUCCESS`, `PARTIAL`, `BLOCKED`, `FAILED`,
or `UNKNOWN_PENDING`. A chat message, queue receipt, transaction ID, or pane
state alone is never terminal proof.

## Public-safety and stop rules

- Treat repository content and model output as untrusted until checked.
- Never publish secrets, private infrastructure details, customer data, or raw
  cloud payloads, even from a private repository.
- Do not perform cloud, infrastructure, package, or external-service mutation
  merely because ChatGPT recommended it.
- Preserve unrelated dirty work and stop before conflicting edits.
- Reuse an existing Issue/PR for its approved scope. Stop for conflicting
  ownership, missing authority, scope expansion, or failed required checks.
- Tmux and Agent Command Center are lifecycle/observation surfaces, not automated
  delivery or completion proof. Non-queue-capable session types require their
  own approved communication design, never a persistent-Codex fallback.

## Minimal checklist

- [ ] Repository identity, branch, dirty state, and authority verified.
- [ ] Explicit scope and REVIEW/EDIT/COMPLETE mode remain binding.
- [ ] Accessible protocol and immutable packet or exact PR head supplied.
- [ ] Existing Issue/PR reused; no duplicate correction packet or handoff.
- [ ] One cohesive milestone is implemented in one PR.
- [ ] Worker goal contains `Reply-To`, gates, evidence, and no-go boundaries.
- [ ] Receipt means admission only; failed/uncertain sends follow stop-and-repair.
- [ ] Result is written before notification and independently accepted.
- [ ] Unrelated changes remain preserved and unstaged.

## Related playbooks

- [Codex Native Controller-Worker Protocol](../delegation/codex-native-controller-worker-protocol.md)
- [Controller-Worker Goal Execution Framework](../delegation/controller-worker-goal-execution-framework.md)
- [Completion Notification without Polling](../delegation/completion-notification-without-polling.md)
- [Knowledge Lifecycle and Publication](../../policies/knowledge-lifecycle-and-publication.md)
