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

Use this playbook when ChatGPT is the external reviewer and Codex is the
repository controller. It combines the public ChatGPT exchange protocol with
the native Codex queue protocol and the milestone sizing rule from `/tmp/pp1`.
The current repository instructions always define the actual scope.

Public protocol source: <https://gist.github.com/amitkarpe/c8d29ad89cafe3ba178fcae29de3c238>

## Decision flow

Keep the roles and gates in this order:

```text
define scope -> inspect repository truth -> implement one milestone
-> validate -> review the actual diff -> merge or accept
-> package immutable truth -> ask ChatGPT for exactly one next milestone
-> record the response -> decide and implement -> repeat
```

ChatGPT gives a recommendation. A recommendation is not authorization, cloud
proof, or a substitute for repository checks and human approval.

## Roles and boundaries

| Role | Responsibility |
| --- | --- |
| Amit | Defines scope and authorizes publication, implementation, cloud, and destructive actions. |
| Codex controller | Reads repository truth, prepares sanitized packets, validates responses, and coordinates authorized work. |
| Codex worker | Executes one approved goal in its owning repository and writes the durable result. |
| ChatGPT reviewer | Reviews committed public-safe truth and proposes one bounded next milestone. |
| GitHub Issue/PR | Durable public work record; it does not replace local evidence or acceptance. |

Do not claim that ChatGPT created an Issue, PR, commit, or comment unless the
GitHub audit record confirms it. If ChatGPT cannot create the response Issue,
Amit creates one from the exact response before Codex continues.

## GitHub-only ChatGPT exchange

ChatGPT cannot read local Linux paths. Exchange only a committed, public-safe
Markdown packet or GitHub Issue/PR URL. Do not use browser automation,
clipboard automation, an authenticated browser profile, or direct GUI
submission for this workflow.

Every completed ChatGPT review must be recorded in **one new standalone GitHub
Issue** in the owning repository. An existing Issue or PR comment is not the
final response record. Give ChatGPT both:

1. the public protocol Gist URL above; and
2. an immutable `blob/<commit-sha>/...` URL for the repository packet.

Use a moving `blob/main` URL only for orientation, never as the evidence
identity.

Suggested exchange layout:

```text
docs/chatgpt/inbox/REQUEST-YYYYMMDD-HHMM-topic.md
docs/chatgpt/outbox/REVIEW-YYYYMMDD-HHMM-topic.md
docs/chatgpt/README.md
```

`inbox/` is the sanitized request, `outbox/` is an accepted response copy,
and the repository README may add local rules.

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
- public protocol URL;
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

After a milestone is implemented, validated, and merged or accepted, ask
ChatGPT to select exactly one bounded next objective. Use wording equivalent
to:

> Review the current repository truth and existing open Issues. Choose exactly
> one small, bounded objective. Return one Issue and one implementation PR
> plan. Do not implement anything.

The response Issue should contain a recommendation, rejected alternatives,
one Issue scope, one PR scope, non-goals, risks, acceptance criteria,
validation/evidence, and deferred work. Codex compares it with current truth
and does not silently substitute another feature.

## Milestone-sized Issue and PR rule

A Draft PR represents one cohesive implementation milestone, not one tiny
task. Group roughly two to five tightly related slices when they share the
same architecture, security boundary, user workflow, deployment/lifecycle,
and acceptance goal.

Keep directly related tests, documentation corrections, configuration changes,
and implementation fixes in the existing PR. Do not create a new Issue/PR
only because one test, correction, or acceptance case was discovered.

Create a new Issue plus Draft PR only when the work materially changes:

1. architecture or required technology;
2. security or authorization model;
3. user workflow or trust boundary;
4. external integration;
5. an independent capability;
6. deployment or lifecycle boundary; or
7. reviewability because the current PR would become unsafe or oversized.

Preferred lifecycle:

```text
Issue -> milestone Draft PR -> implement related slices -> validate
-> review the actual diff -> fix same-PR findings -> pass -> merge
```

This avoids both micro-PR coordination overhead and oversized mixed changes.

## Native Codex controller-worker delivery

Use durable goal/result files for authority and evidence. Use `codex queue`
only for transport. Use the Agent Command Center for visibility and lifecycle,
not as proof of execution or completion.

Before sending a worker message:

1. confirm the installed CLI exposes `codex queue` and review current help;
2. write the complete goal with allowed mutations, gates, and result path;
3. verify worker UUID, role, repository, and workspace;
4. put the controller UUID in the goal and message as `Reply-To`; and
5. send one short, quoted message containing provenance and the goal path.

Example:

```bash
MSG='FROM controller. Reply-To: <controller-uuid>. Execute <goal-path>. Write the terminal result there, then notify Reply-To. Queue admission is not execution or completion.'
codex queue --thread <worker-uuid> --message "${MSG}"
```

A valid queue receipt proves delivery only. Do not paste the same message into
tmux, press a second function key, inspect the composer, or resend because a
worker still looks `Ready`. The sender is not an implicit return route.

The worker must finish the approved goal, write and validate one durable
`RESULT.md`, reconcile changed state, and send one short message to the exact
`Reply-To`. A `.done` marker may point to the result. The controller accepts
only after checking the required evidence and, for stateful work, fresh
current-state proof.

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
- Stop when an existing Issue/PR already owns the request, no standalone
  response Issue exists, the response expands scope, or required checks fail.
- Keep fallback supervisor or tmux delivery only for a clear native-queue
  failure. One recovery attempt is enough; F12 is not normal transport.

## Minimal checklist

- [ ] Repository identity, branch, dirty state, and authority verified.
- [ ] One sanitized packet asks one bounded question.
- [ ] Immutable packet URL and public protocol URL supplied.
- [ ] ChatGPT response recorded in a new standalone Issue.
- [ ] Existing Issues/PRs checked before new records are proposed.
- [ ] One cohesive milestone is implemented in one PR.
- [ ] Worker goal contains `Reply-To`, gates, evidence, and no-go boundaries.
- [ ] Result is written before notification and independently accepted.
- [ ] Unrelated changes remain preserved and unstaged.

## Related playbooks

- [Codex Native Controller-Worker Protocol](../delegation/codex-native-controller-worker-protocol.md)
- [Controller-Worker Goal Execution Framework](../delegation/controller-worker-goal-execution-framework.md)
- [Completion Notification without Polling](../delegation/completion-notification-without-polling.md)
- [Knowledge Lifecycle and Publication](../../policies/knowledge-lifecycle-and-publication.md)
