---
type: Playbook
title: Persistent Codex Goals
description: Use a runtime goal to track long work while keeping durable truth in repository files.
status: verified
scope: Codex CLI
confidence: high
timestamp: 2026-07-15T00:00:00+08:00
last_verified: 2026-07-15
review_after: 2026-10-15
tags: [codex, goals, workflow]
---

# Persistent Codex Goals

## Use a Goal

Set a goal when work spans multiple steps or automatic continuations. In the
Codex CLI, `/goal <objective>` sets the objective and `/goal` displays it.
Use `/goal edit`, `/goal pause`, `/goal resume`, and `/goal clear` to manage
the lifecycle.

Goal objectives are limited in length. Put detailed requirements, validation,
and stop boundaries in a versioned or file-backed specification, then point the
goal at that file.

## Keep Durable Truth Separate

A runtime goal tracks what the active task is pursuing. It does not replace
repository instructions, specifications, current-state files, tests, or result
artifacts. After a restart, reconstruct intent from those durable sources and
confirm that the resumed goal still matches them.

## Restart Prompt Shape

A useful restart prompt names the objective file, asks the session to read it,
and requires continuation only within its scope and stop conditions. Do not put
credentials, mutable runtime state, or the only copy of critical context in the
goal text.

## Citations

- [OpenAI Codex CLI slash commands](https://learn.chatgpt.com/docs/developer-commands.md?surface=cli)
