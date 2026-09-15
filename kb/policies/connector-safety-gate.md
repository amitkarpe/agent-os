---
type: Policy
title: Connector Safety Gate
description: Fail closed when an already-authorized connector action is blocked by platform safety without widening scope or safeguards.
status: reviewed
scope: connector-mediated repository and external-service actions
confidence: high
timestamp: 2026-09-15T10:00:00+08:00
review_after: 2027-03-15
tags: [connectors, safety, github, handoff, authority]
---

# Connector Safety Gate

A connector or platform safety block is a distinct failure class. It is not by
itself proof of stale state, authentication failure, insufficient repository
permission, validation failure, missing user approval, or disallowed intent.

Connector access never creates authority. The active repository rules, approved
scope, target identity, and explicit safety boundaries remain controlling.

## Recovery Rule

For an already-authorized, bounded connector action:

1. Re-read the exact repository or service, branch/PR when applicable, target
   object, and current SHA/state immediately before retrying.
2. Keep the requested target, scope, permissions, and safeguards unchanged.
3. Retry the identical bounded connector action at most once.
4. If the same action is blocked again, stop connector retries and report
   `BLOCKED_CONNECTOR_SAFETY`.
5. Continue through the existing Issue/PR handoff to an already-authorized local
   or repository worker only when that route is within the same approved scope.

Do not widen permissions, weaken safeguards, change repository or branch, create
a replacement handoff, or switch model/thinking effort merely to get past the
block.

## Classify Other Failures Separately

Use their own recovery paths for stale SHA or conflict errors, authentication or
permission failures, validation/syntax failures, access blockers, and explicit
user-approval prompts. Do not relabel those failures as connector safety blocks.

## Handoff Boundary

A fallback execution path is not new authority. Reuse the owning Issue/PR and
preserve the original objective, no-go gates, target, and acceptance conditions.
If no already-authorized path exists, stop rather than invent one.

## Related

- [ChatGPT and Codex Collaboration Protocol](../playbooks/integrations/chatgpt-codex-collaboration-protocol.md)
- [Knowledge Lifecycle and Publication](knowledge-lifecycle-and-publication.md)

## Citations

- [repo-starter `CHATGPT.md` Connector Safety Gate](https://github.com/amitkarpe/repo-starter/blob/main/CHATGPT.md#connector-safety-gate)
