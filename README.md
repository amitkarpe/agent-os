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

## Remaining specialist sources — indexed until retirement

Distinct technical documents below remain available **temporarily** while G
rewrites and merges their unique content in the next batches. This is an
exhaustive navigation map of remaining active KB guidance, not a recommendation
to preserve the hierarchy.

**Goals, delegation and Codex**

- [Agent operating principles](kb/principles/amit-agent-operating-principles.md)
- [Controller-worker goal framework](kb/playbooks/delegation/controller-worker-goal-execution-framework.md)
- [Native Codex controller/worker protocol](kb/playbooks/delegation/codex-native-controller-worker-protocol.md)
- [Effective subagent delegation](kb/playbooks/delegation/effective-subagent-delegation.md)
- [Repository-first local agent control](kb/playbooks/delegation/repository-first-local-agent-control.md)
- [Completion notifications](kb/playbooks/delegation/completion-notification-without-polling.md)
- [Supervisor wake boundaries](kb/playbooks/delegation/supervisor-wake-principles.md)
- [Curated Codex skills](kb/playbooks/codex/curated-skill-exposure.md)

**ChatGPT and external provider interactions**

- [G/Codex collaboration](kb/playbooks/integrations/chatgpt-codex-collaboration-protocol.md)
- [ChatGPT Projects and file surfaces](kb/playbooks/integrations/chatgpt-project-context-and-files.md)
- [Event-triggered vs scheduled tasks](kb/playbooks/integrations/chatgpt-event-vs-scheduled-tasks.md)
- [Grok route selection](kb/playbooks/providers/hermes-grok-route-selection.md)
- [Validate X/Grok research](kb/playbooks/integrations/x-grok-research-validation.md)
- [Dated model comparison - historical](kb/observations/models/spark-vs-luna-2026-07.md)

**Infrastructure, integrations and repositories**

- [AWS GitHub/OIDC durable control](kb/playbooks/integrations/github-oidc-aws-control.md)
- [GitLab runner preparation](kb/playbooks/integrations/gitlab-runner-connected-preparation.md)
- [Cloudflare Worker demo deployment](kb/playbooks/integrations/cloudflare-worker-demo-deployment.md)
- [Repo-starter adoption](kb/playbooks/repositories/repo-starter-adoption.md)
- [Development/runtime pattern selection](kb/playbooks/repositories/development-runtime-pattern-selection.md)

**Browser and visual evidence**

- [Browser E2E and screenshot evidence](kb/playbooks/tools/agent-run-browser-e2e-screenshot-evidence.md)
- [Playwright Core on WSL](kb/playbooks/tools/agent-run-playwright-core-wsl.md)
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
