---
type: Practice
title: Repository Foundation and Runtime Choices
status: reviewed
scope: Public-safe reusable specialist guidance
confidence: high
review_after: 2027-04-23
tags: [repositories, ci, runtime, identity]
---

# Repository Foundation and Runtime Choices

Use [repo-starter](https://github.com/amitkarpe/repo-starter) as an optional
baseline for a new repository or a minimal retrofit. It distributes small
downstream entrypoints, not a replacement for the owning project's authority
or this Agent OS knowledge.

## One responsibility per project file

| File | Responsibility |
| --- | --- |
| `README.md` | Human project purpose and entrypoint |
| `AGENTS.md` | Durable local agent rules and read order |
| `CONTEXT.md` | Current-only restart state, blocker and next action |
| `INIT.md` | First-time setup checklist/interview, not recurring planning |
| `CHATGPT.md` | Repository-specific G/Codex binding and collaboration |
| `ENV.md` | Runtime/cloud/tool dependency facts, not blanket authority |
| `SPEC.md` | Scoped implementation, external contract and acceptance gate |
| `ROADMAP.md` | Still-relevant future milestones |

Not every repository needs substantial content in every file. Keep project
runtime truth in its owning files and Git Issues/PRs; do not copy global policies
or credentials into a new starter.

For a **new repository**, initialize from the template, complete INIT once,
replace real placeholders and define one first useful Goal/SPEC. For an
**existing repository**, preserve README and product code, use a small bounded
chore branch, add only missing responsibilities, and never invent extra CI,
tests, code, documents or history rewrite to adopt a template. Stop when
unrelated dirty/untracked work or identity is uncertain.

## Choose the smallest runtime and validation path

| Question | Default |
| --- | --- |
| Can another host reproduce this? | Pin repo-owned start/check commands, dependencies and lockfiles; validate a fresh consumer when necessary |
| Does containerization remove actual drift? | Use only when it helps; avoid obscuring host kernel, systemd, mounts, private networking or SSM behavior |
| Which CI runner? | Reuse the simplest trust- and network-compatible approved runner; call repository-owned commands |
| How authenticate automation? | Prefer narrowly scoped short-lived workload identity, never committed secrets |
| What proof reaches the risk? | Smallest existing static/logic/integration/E2E/provider readback required for the claim |
| Does a browser journey matter? | Use [Browser Evidence](tools/BROWSER.md) only for UI acceptance |
| Are resources or costs retained? | Record owner, TTL, cleanup and measured usage where material |

The smallest passing CI check may establish source health but does **not**
establish deployment, AWS target identity, external resource health, user
journey, offline behavior or cost/cleanup. Track exact provider execution IDs
and read back actual live state before declaring acceptance.

Detailed target-control procedures are in [AWS OIDC](aws/OIDC.md),
[GitLab Runner](GITLAB.md), [Testing](TESTING.md) and
[Playwright on WSL](tools/PLAYWRIGHT.md). Each is triggered only when needed.
A GitHub runner that works for a public repository is not automatically
permitted for restricted workloads.

## Citations

- [repo-starter source](https://github.com/amitkarpe/repo-starter)
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
- [Docker build secrets](https://docs.docker.com/build/building/secrets/)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [AWS CodeBuild runner](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html)
- [Playwright library](https://playwright.dev/docs/library)
