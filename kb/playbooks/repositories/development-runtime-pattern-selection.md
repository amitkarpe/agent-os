---
type: Practice
title: Development and Runtime Pattern Selection
description: Select reproducibility, containers, CI runners, identity, validation, browser E2E, runtime evidence, cost, and cleanup without forcing one stack onto every repository.
status: candidate
scope: repository development and runtime workflow selection
confidence: medium
timestamp: 2026-10-02T00:00:00+08:00
review_after: 2027-01-02
tags: [development, runtime, containers, ci, oidc, testing, playwright, reproducibility, cost, cleanup]
---

# Development and Runtime Pattern Selection

Use this page as a **selector**, not a detailed implementation guide.

The existing [Portfolio Economy Defaults](../../../AGENTS.md#portfolio-economy-defaults)
remain the starting point. Deviate only when project trust, connectivity, tooling,
architecture, cost, or acceptance evidence justifies it.

## 1. Reproducibility

**Use when:** another host, runner, or future agent must reproduce the working path.

Keep repo-owned build/start/health/check commands, compatible tool versions,
lockfiles, configuration shape, and cleanup/recovery instructions. When
portability matters, prove one fresh or clean-consumer path without the original
developer cache.

A host inventory is discovery, not reproducibility proof.

## 2. Containers

**Use when:** a container, Compose service, or preparation image removes real
dependency/runtime/CI-tool drift.

**Skip or limit when:** the behavior depends on the real host OS, kernel, mounts,
systemd, SSM/host patching, privileged networking, or a restricted environment.

Pin important inputs, keep secrets out of image layers, and prove the consumer
path rather than only the image build.

## 3. CI runner

Start from the Agent OS runner defaults. Choose another substrate only when trust,
network access, required tools/architecture, workload shape, availability, or
measured/bounded cost requires it.

Keep CI thin and call repository-owned commands.

Detailed guidance:
- [GitHub OIDC and AWS-Owned Control](../integrations/github-oidc-aws-control.md)
- [GitLab Runner Connected Preparation](../integrations/gitlab-runner-connected-preparation.md)

## 4. OIDC and secrets

Prefer short-lived workload identity where supported.

Keep workflow permission, runner identity, cloud identity, application secrets,
and human authentication separate. Version configuration **shape** in Git; supply
secret values through approved runtime/CI/local secret mechanisms.

Authentication success is not mutation authority. Detailed trust sequencing stays
in the linked OIDC/runner playbooks.

## 5. Validation layers

**Zero new tests by default is not zero validation.**

Choose the smallest proof that reaches the real failure boundary:
- static/lint/schema checks for structure;
- focused tests for logic, contracts, deny paths, or regressions;
- integration proof for component interaction;
- one end-to-end golden path when the user/runtime journey is the claim;
- provider/runtime readback when external state matters.

Do not optimize for test count.

## 6. Browser E2E

**Use when:** the accepted behavior is an interactive browser journey.

Prove user action + API/persisted state + rendered DOM + browser errors + cleanup.
A screenshot alone is not enough.

Reuse:
- [Agent-Run Browser E2E and Screenshot Evidence](../tools/agent-run-browser-e2e-screenshot-evidence.md)
- [Run Playwright Core with Windows Node and Chrome from WSL](../tools/agent-run-playwright-core-wsl.md)

**Skip when:** API/integration proof fully covers the acceptance claim.

## 7. CI proof versus runtime proof

Treat these separately:

```text
source revision
  -> CI/check result
  -> execution/deployment identity
  -> provider/runtime readback
  -> acceptance journey
  -> cleanup/retained-state result
```

A green CI run does not automatically prove deployment, target identity, service
health, offline behavior, UI acceptance, or cleanup. Persist durable execution
IDs for long work and reconcile the original execution before retrying.

## 8. Cost and cleanup

For demos, labs, build systems, retained compute/storage, large artifacts, or
frequent CI, record:
- what was created and retained;
- TTL/lifecycle/cleanup path;
- cleanup evidence;
- measured usage/cost when it affects future platform selection.

Keep estimates separate from billing evidence.

## Decision check

Before adding tooling, ask:
1. What drift or failure has actually occurred?
2. Would a container remove that drift or hide the real target?
3. Which existing runner already satisfies trust and connectivity?
4. Can short-lived identity replace a stored cloud key?
5. What is the smallest proof that reaches acceptance?
6. Is browser interaction part of acceptance?
7. What is CI evidence versus runtime/provider evidence?
8. What must be cleaned or cost-measured?

If the repository already answers these safely, add no new framework.

## Promotion boundary

- Project repos own implementation and runtime truth.
- Detailed procedures stay in existing Agent OS playbooks.
- This page selects and links; it does not duplicate.
- Do not propagate to `repo-starter` until repeated use proves a rule universal.
- Host-specific facts stay in dotfiles/local guidance.

## Citations

- https://docs.docker.com/build/building/best-practices/
- https://docs.docker.com/build/building/secrets/
- https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html
- https://playwright.dev/docs/library
