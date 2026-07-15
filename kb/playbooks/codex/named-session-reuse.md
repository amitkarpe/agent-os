---
type: Playbook
title: Named Agent Session Reuse
description: Recover known sessions conservatively using names for people and unique identifiers for automation.
status: reviewed
scope: command-line agent sessions
confidence: medium
timestamp: 2026-07-15T00:00:00+08:00
review_after: 2026-10-15
tags: [sessions, recovery, identity]
---

# Named Agent Session Reuse

## Identity Rule

Use a stable display name so people can recognize a session. Record the
provider-issued unique session identifier separately and use that identifier
for deterministic resume. A name is an alias, not proof of identity.

## Before Reconstruction

1. Record the name and unique identifier from the live session's own status
   output before shutdown or handoff.
2. Verify that every resumable identifier is unique in the registry.
3. Confirm independently that no live process is already attached to the
   target session.
4. Require a known provider and the intended version-controlled workspace.
5. Stop on missing evidence, collision, active state, or stale and unsafe
   context.

## Read-Only Plan First

Generate and review a reconstruction plan before executing it. The planner
should validate registry structure, identity uniqueness, workspace existence,
provider evidence, and active-session guards without starting a process or
sending a prompt.

## Execution Gate

Resume only after the target is confirmed inactive and the identifier,
provider, workspace, and continuation safety are proven. Never bulk-resume or
attach two processes to one session identifier. When context is incomplete or
unsafe, create a fresh session and use a written handoff.

## Citations

- [OpenAI Codex CLI command reference](https://learn.chatgpt.com/docs/developer-commands.md?surface=cli)
- [Anthropic Claude Code common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
