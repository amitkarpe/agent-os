---
type: ChatGPT review request
title: Native queue-only delivery for persistent Codex workers
status: review-requested
date: 2026-09-06
safety: public-safe summary; no infrastructure or worker mutation authorized
---

# Request: review native queue-only worker delivery

Please review this request using the public protocol:

<https://gist.github.com/amitkarpe/c8d29ad89cafe3ba178fcae29de3c238>

## Objective

Decide whether persistent controller-to-worker communication should use native
`codex queue` as its only normal message transport, while terminal-based tools
remain limited to session lifecycle and observation.

## Verified observations

- A durable goal path can remain visible in an interactive Codex composer as
  unsent input. Visibility is not proof of dispatch.
- A later human Enter action can submit that visible input. This makes a
  terminal paste unsuitable as deterministic controller transport.
- Native queue addresses a verified worker thread directly, but its receipt
  proves only transport admission, not execution, delivery acknowledgement, or
  successful work.
- Durable goals, `RESULT.md`, and `.done` markers provide scope and terminal
  truth; controller evidence review provides acceptance.
- The existing native controller-worker playbook already prohibits sending a
  second copy through tmux after a valid queue receipt. Some local playbooks
  still carried older composer-paste and Enter retry guidance.

## Proposed KISS rule

1. Write one complete durable goal.
2. Resolve the exact persistent worker UUID.
3. Send one short native queue message with the goal path and exact Reply-To.
4. Record a receipt as `notification_queued` only.
5. Review the durable result and marker before controller acceptance.

Tmux and the Agent Command Center may start, resume, locate, or observe a
worker session, but must not deliver goals through composer text, file mentions,
paste, Enter, F12, or similar key automation. If queue transport is unavailable
or has no valid receipt, the controller stops and repairs that transport rather
than silently using a composer fallback.

## Exact question

Is this queue-only rule the right KISS default for persistent Codex workers?
Identify one small documentation milestone, if any, that would make the rule
clearer and safer without creating a new transport framework, supervisor,
dashboard dependency, or automated recovery system.

## Constraints and non-goals

- Recommendation only. Do not implement anything.
- Do not propose browser automation, clipboard automation, or GUI automation.
- Do not propose a new queue service, retry framework, monitoring system, or
  fallback transport.
- Do not change cloud resources, credentials, worker models, or repository
  execution goals.
- Keep the recommendation public-safe and under one cohesive documentation
  milestone.

## Requested response

Create one standalone GitHub Issue in `amitkarpe/agent-os` containing:

- recommendation and one bounded Issue scope;
- one implementation PR plan;
- acceptance criteria and validation;
- risks and rejected alternatives; and
- explicitly deferred work.

Do not create a PR or implementation code. Codex will compare any response
with current repository truth before acting.
