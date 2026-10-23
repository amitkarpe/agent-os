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

## Remaining specialist source (next content batch)

- [G/Codex collaboration](kb/playbooks/integrations/chatgpt-codex-collaboration-protocol.md)
- [Codex native transport](kb/playbooks/delegation/codex-native-controller-worker-protocol.md)
- [AWS durable OIDC control](kb/playbooks/integrations/github-oidc-aws-control.md)
- [GitLab runner preparation](kb/playbooks/integrations/gitlab-runner-connected-preparation.md)
- [ChatGPT Projects and files](kb/playbooks/integrations/chatgpt-project-context-and-files.md)
- [ChatGPT events/tasks](kb/playbooks/integrations/chatgpt-event-vs-scheduled-tasks.md)
- [Browser E2E/evidence](kb/playbooks/tools/agent-run-browser-e2e-screenshot-evidence.md)
- [Repository starter](kb/playbooks/repositories/repo-starter-adoption.md)
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
