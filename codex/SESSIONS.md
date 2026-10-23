---
type: Policy
title: Codex Sessions and Native Goals
description: Reuse exact sessions and native Goals while keeping persistence distinct from completion.
status: reviewed
confidence: high
scope: Reusable public-safe agent guidance
review_after: 2027-04-23
tags: [codex, session, goal, identity]
---

# Codex Sessions and Native Goals

## Identity before resume

Use stable session names for humans; use **provider-issued unique IDs** for deterministic resume. Before reconstruction verify the current provider, version, worktree, ID uniqueness, current process attachment, queue and Goal state. Generate a read-only recovery plan first. Do not attach two writers, bulk-resume or create a replacement for an active session. If identity or state cannot be proven, stop and write a safe handoff.

## One approved Goal

The owning Issue and repository define what is authorized; a plan describes how.
One owner-approved Goal can cover multiple authorized Phase 2 milestones without repetitive GO requests. For substantial work, verify the **existing exact native thread** is idle, its queue has no conflicting work and it has no unfinished Goal. Use actual supported native Goal SET/GET controls, set the bounded objective once, then read it back.

An interactive `/goal` command is not automatically a supported `codex exec` flag, nor does a generic MCP `message_send` with `/goal` text register a native Goal. A live adapter must actually expose the native lifecycle. Keep file-backed scope, stop gates, tests and evidence in the owning Issue/PR; runtime Goal text is not their only copy.

Native continuation can occur at safe idle boundaries within budget. It may stop on interrupts, pending owner input, stalled process, budget or restart. Persisted Goal state is **not** always-on execution, and a queue receipt does not prove completion. Correlate actual turns, completed status, changed HEAD and final native Goal readback before acceptance.

Office [Issue #62 native pilot](https://github.com/amitkarpe/agents/issues/62#issuecomment-6345654567) proved one read-only Goal SET/GET and one automatic continuation only; longer milestone work, restart persistence, Home and Factory/Home MCP control exposure were **not** proved.

## Related

- [One approved goal](../GOALS.md)
- [Native controller/worker protocol](DELEGATION.md)
- [Context](../CONTEXT.md)

## Citations

- [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)
- [Codex developer commands](https://learn.chatgpt.com/docs/developer-commands)
