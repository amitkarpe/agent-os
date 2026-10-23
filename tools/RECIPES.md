---
type: Policy
title: Tracked Repository Search and Tool Recipes
description: Choose tracked source searches and focused CLI helpers, with direct evidence verification.
status: reviewed
confidence: high
scope: Reusable public-safe agent guidance
review_after: 2027-04-23
tags: [tools, search, git, source]
---

# Tracked Repository Search and Tool Recipes

Search output narrows candidates; it does not prove tracked ownership or current
behavior. Start at a verified repository root and open the exact source before
editing. The default tracked inventory is `git ls-files`, not `fd` or `rg`.

| Question | Preferred command |
| --- | --- |
| Tracked filenames | `git ls-files src/` |
| Dirty or untracked work | `git status --short` |
| Tracked exact literal | `git grep -n -F 'ConfigValue' -- src/` |
| Discover filename in working tree | `fd -g '*.py' src/` |
| Broad content discovery | `rg -nF 'ConfigValue' src/` |

`fd` and `rg` may intentionally omit ignored/hidden files and include
untracked work; they are useful discovery tools but not Git ownership evidence.
Use unrestricted searches only when the task explicitly requires them.
Inspect the source, scope and changed diff before a bulk replacement.

## CLI recipe reference

The following concrete command recipes are preserved from the existing
specialist reference, with tracked-search priority established above.


Confirm command and file scope before trusting its output.

## `rg`: Search File Contents

Find a literal value with line numbers:

```bash
rg -nF 'ConfigValue' src/
```

Failure mode: regex metacharacters change a search when `-F` is omitted.
Unrestricted flags also include ignored or hidden data that is normally noise.

## `fd`: Discover Filenames

List Python files under a source directory:

```bash
fd -g '*.py' src/
```

Failure mode: `fd` is ignore-aware working-tree discovery, not proof that Git
tracks a result. Use `git ls-files` for tracked inventory.

## `ast-grep`: Inspect Code Structure

Find JavaScript logging calls without rewriting them:

```bash
ast-grep -p 'console.log($$$)' src/
```

Failure mode: the pattern must be valid syntax for the target language. Keep
inspection read-only by omitting rewrite or fix options.

## `sd`: Replace Known Literal Text

Verify the scope, replace the literal, then inspect the diff:

```bash
rg -nF 'OldValue' src/config.py
sd -F 'OldValue' 'NewValue' src/config.py
git diff -- src/config.py
```

Failure mode: without literal mode, punctuation may act as regular-expression
syntax. `sd` replaces every matching occurrence in the named scope.

## `jq` or `jaq`: Validate JSON Shape

Require `items` to be an array:

```bash
jq -e '.items | type == "array"' data.json >/dev/null
```

Failure mode: printing a missing field can yield `null` without proving the
required shape. Use an assertion and check its exit status. A compatible
`jaq` installation can run the same basic filter.

## `hyperfine`: Compare Commands

Measure repeated runs with warmup:

```bash
hyperfine --warmup 3 "rg -nF 'ConfigValue' src/" \
  "git grep -nF 'ConfigValue' -- src/"
```

Failure mode: timing commands with different file sets or outputs does not
support a fair performance claim. Prove equivalent scope first.

## `tokei`: Estimate Repository Size

Summarize languages and code size under a source directory:

```bash
tokei src/
```

Failure mode: line count is a scope hint, not a measure of complexity, risk, or
required effort.

## QMD: Search an Existing Index

Use QMD only after proving that the required collection is fresh and contains
at least one document:

```bash
qmd status
qmd search "configuration loading" -c docs
```

Failure mode: a configured, empty, or stale collection can omit current
evidence. Fall back to the Git-aware search hierarchy when freshness or
nonzero content is not proven, and always read the selected source directly.

## Citations

- [`ripgrep` project documentation](https://github.com/BurntSushi/ripgrep)
- [`fd` project documentation](https://github.com/sharkdp/fd)
- [`ast-grep` pattern syntax](https://ast-grep.github.io/guide/pattern-syntax.html)
- [`sd` project documentation](https://github.com/chmln/sd)
- [`jq` manual](https://jqlang.org/manual/)
- [`jaq` project documentation](https://github.com/01mf02/jaq)
- [`hyperfine` project documentation](https://github.com/sharkdp/hyperfine)
- [`tokei` project documentation](https://github.com/XAMPPRocky/tokei)
- [QMD project documentation](https://github.com/tobi/qmd)


