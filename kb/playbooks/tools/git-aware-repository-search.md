---
type: Playbook
title: Git-Aware Repository Search
description: Separate tracked inventory, working-tree discovery, content search, and source verification.
status: reviewed
scope: Git repositories
confidence: high
timestamp: 2026-07-28T00:00:00+08:00
review_after: 2026-10-28
tags: [git, search, discovery, tools]
---

# Git-Aware Repository Search

Use this hierarchy from the repository root:

1. Run `git ls-files` for the authoritative tracked-file inventory.
2. Run `git status --short` when modified or untracked work matters.
3. Use `fd` for ignore-aware working-tree filename discovery.
4. Use `rg` for ignore-aware content search.
5. Read the selected source directly before deciding or editing.

## Match the Tool to the Question

| Question | Command |
| --- | --- |
| Which files does Git track under `src/`? | `git ls-files src/` |
| What tracked or untracked work is present? | `git status --short` |
| Which Python filenames are discoverable under `src/`? | `fd -g '*.py' src/` |
| Where does the literal name occur? | `rg -nF 'ConfigValue' src/` |

`git ls-files` and `fd` answer different questions. `fd` may find useful
untracked files, while its defaults omit hidden and ignored paths. It does not
prove that Git owns a file.

Use `fd`, rather than `find`, as the default agent filename-discovery tool
inside a repository. Use broader or unrestricted search flags only when
ignored or hidden paths are deliberately in scope.

## Source Is the Authority

Search output narrows the candidates; it does not establish current behavior.
Open the selected file, read enough surrounding code to understand it, and
check related changes before making a decision or edit.

A generated `INDEX.md` may be an optional hint when the agent knows the intent
but not the filename or symbol. It never replaces tracked-file inventory,
direct source reading, or validation against the current source.

## Citations

- [Git `ls-files` documentation](https://git-scm.com/docs/git-ls-files)
- [Git `status` documentation](https://git-scm.com/docs/git-status)
- [`fd` project documentation](https://github.com/sharkdp/fd)
- [`ripgrep` project documentation](https://github.com/BurntSushi/ripgrep)

