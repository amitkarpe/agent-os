# Agent OS

Public-safe reusable knowledge for people and agents. **One authoritative
topic per rule, loaded when needed.** The active project owns its permissions,
implementation, approved Goal and runtime evidence. Dotfiles/native provider
homes own actual host configuration and private data.

## Find a topic

| Task | Canonical file |
| --- | --- |
| Authority, separation, evidence | [CORE.md](CORE.md) |
| One goal, milestones and delegation | [GOALS.md](GOALS.md) |
| Cold/warm context and handoff | [CONTEXT.md](CONTEXT.md) |
| Public knowledge and evidence cleanup | [KNOWLEDGE.md](KNOWLEDGE.md) |
| Connector safety/recovery | [SAFETY.md](SAFETY.md) |
| Git and PR convention | [GIT.md](GIT.md) |
| Test/validation economy | [TESTING.md](TESTING.md) |
| Tool choice | [TOOLS.md](TOOLS.md) |
| Tracked repository search and recipes | [tools/RECIPES.md](tools/RECIPES.md) |
| Terraform state and drift | [TERRAFORM.md](TERRAFORM.md) |
| Codex sessions and native Goals | [codex/SESSIONS.md](codex/SESSIONS.md) |
| AWS AgentCore selection and proof | [aws/AGENTCORE.md](aws/AGENTCORE.md) |
| Repository foundation and runtime | [REPOSITORIES.md](REPOSITORIES.md) |
| Browser E2E and screenshots | [tools/BROWSER.md](tools/BROWSER.md) |
| Windows/WSL Playwright route | [tools/PLAYWRIGHT.md](tools/PLAYWRIGHT.md) |
| X/Grok research validation | [tools/RESEARCH.md](tools/RESEARCH.md) |
| Repository-first Codex worker attachment | [codex/CONTROL.md](codex/CONTROL.md) |

## Additional specialist topics — new canonical paths

Distinct technical documents below remain available **temporarily** while G
rewrites and merges their unique content in the next batches. This is an
exhaustive navigation map of remaining active KB guidance, not a recommendation
to preserve the hierarchy.

**Goals, delegation and Codex**

- [Agent operating principles](CORE.md)
- [Controller-worker goal framework](GOALS.md)
- [Native Codex controller/worker protocol](codex/DELEGATION.md)
- [Effective subagent delegation](GOALS.md)
- [Repository-first local agent control](codex/CONTROL.md)
- [Completion notifications](GOALS.md)
- [Supervisor wake boundaries](GOALS.md)
- [Curated Codex skills](codex/SKILLS.md)

**ChatGPT and external provider interactions**

- [G/Codex collaboration](chatgpt/COLLABORATION.md)
- [ChatGPT Projects and file surfaces](chatgpt/PROJECTS.md)
- [Event-triggered vs scheduled tasks](chatgpt/AUTOMATIONS.md)
- [Grok route selection](tools/RESEARCH.md)
- [Validate X/Grok research](tools/RESEARCH.md)
- [Dated model comparison - historical](kb/observations/models/spark-vs-luna-2026-07.md)

**Infrastructure, integrations and repositories**

- [AWS GitHub/OIDC durable control](aws/OIDC.md)
- [GitLab runner preparation](GITLAB.md)
- [Cloudflare Worker demo deployment](CLOUDFLARE.md)
- [Repo-starter adoption](REPOSITORIES.md)
- [Development/runtime pattern selection](REPOSITORIES.md)

**Browser and visual evidence**

- [Browser E2E and screenshot evidence](tools/BROWSER.md)
- [Playwright Core on WSL](tools/PLAYWRIGHT.md)
- [Transitional KB index](kb/index.md)

The `kb/` hierarchy and `agents/*.md` pointers are **temporary**. Their
retirement and Office/Home installed-host acceptance belong to
[Issue #62](https://github.com/amitkarpe/agents/issues/62). The canonical
checkout is `~/.agents/`; retired `~/.agent/` is **not** an accepted endpoint.

## Task-scoped onboarding

```text
Agent OS: <verified clone or official public repository>
Project: <active repo>; task: <objective>
Read the active project's AGENTS/spec/approved Goal and current state.
Select one to three relevant canonical topics from Agent OS README.
Never treat public guidance as authorization or automatically loaded context.
At closeout, suggest only a sanitized non-duplicative reusable lesson.
```

Validate the repository with `scripts/validate.sh` and its focused
`--self-test` mode. GitHub Actions is the merge proof, not native-provider
auto-loading proof.

## License

[Apache-2.0](LICENSE).
