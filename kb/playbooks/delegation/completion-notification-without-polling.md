---
type: Practice
title: Completion Notification without Polling
description: Preserve a durable terminal result before sending one bounded completion notice.
status: reviewed
scope: asynchronous worker completion
confidence: high
timestamp: 2026-07-15T00:00:00+08:00
review_after: 2027-01-15
tags: [notification, delegation, evidence]
---

# Completion Notification without Polling

## Contract

The durable result is the source of truth. A notification is only a pointer to
that result and must not carry the only copy of the outcome.

On completion:

1. Write and validate the terminal result artifact.
2. Verify once that the intended recipient is available and safe to notify.
3. Send one short, unambiguous result pointer.
4. Check acceptance once when the transport requires it.
5. Do not poll, repeatedly wake, or paste the full result.

## Failure Behavior

Notification failure must not erase or invalidate a valid result. Record the
notification as deferred and leave the durable artifact available for later
consumption. Do not restart or recreate the recipient merely to deliver a
completion notice.

Make delivery idempotent with a result identity or deduplication record. A
retry may resend the same pointer only when policy allows it and the system can
prove that the prior attempt was not accepted.

## Authority Boundary

Delivery proves neither review nor approval. The recipient still decides
whether to accept, reject, or re-scope the result.

## Citations

- [OpenAI Codex prompting: steering and queuing](https://developers.openai.com/codex/prompting/#steering-and-queuing)
