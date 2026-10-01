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

Use this page as a **selector**, not as a replacement for the detailed Agent OS
playbooks.

Existing [Portfolio Economy Defaults](../../../AGENTS.md#portfolio-economy-defaults)
remain the starting point. Use a different runner or validation shape only when
project trust, connectivity, tooling, architecture, cost, or acceptance evidence
justifies the exception.

## 1. Reproducibility

**Use when:** another host, runner, or future agent must reproduce the working
path.

Keep build/start/health/check commands, compatible tool versions, lockfiles,
configuration shape, and cleanup/recovery instructions in versioned source.

A host inventory is discovery, not proof. When portability matters, add one
clean-consumer or fresh-install proof that does not depend on the original
developer cache.

## 2. Containers

**Use when:** containerization removes real dependency, runtime, or CI-tool drift.

Good fits include dependency-heavy local services, disposable integration
environments, preparation images, and portable build/test toolchains.

**Skip or limit when:** the behavior depends on the real host OS, kernel, mount
policy, systemd, SSM/host patching, privileged networking, or a restricted
environment.

Pin important inputs, keep secrets out of image layers, and prove the consumer
path rather than only proving that the image builds.

## 3. CI runner

Start with the existing Agent OS runner defaults, then select the execution
substrate by trust, connectivity, required tools/architecture, workload shape,
current availability, and measured or bounded cost.

Keep CI thin: workflows should call repository-owned commands.

For detailed AWS/GitHub control use
[GitHub OIDC and AWS-Owned Control](../integrations/github-oidc-aws-control.md).
For internal connected preparation use
[GitLab Runner Connected Preparation](../integrations/gitlab-runner-connected-preparation.md).

## 4. OIDC and secrets

Prefer short-lived workload identity where the platform supports it.

Keep repository/workflow permission, runner identity, cloud workload identity,
application secrets, and human authentication separate.

Version configuration **shape** in Git; supply secret values through the approved
runtime/CI/local secret mechanism. Authentication success is not mutation
authority.

Detailed trust and execution sequencing belongs in the linked OIDC/runner
playbooks, not here.

## 5. Validation layers

The Agent OS testing-economy rule still applies: **zero new tests by default is
not zero validation**.

Choose the smallest proof that reaches the real failure boundary:

- static/lint/schema checks for structure;
- focused tests for isolated logic, contracts, deny paths, or regressions;
- integration proof for component interaction;
- one end-to-end golden path when the user/runtime journey is the claim;
- provider/runtime readback when external state matters.

Do not optimize for test count.

## 6. Browser E2E

**Use when:** the accepted behavior is an interactive browser journey.

Prove real user action, backend/API or persisted state, rendered DOM, browser
errors, and cleanup. A screenshot alone is not enough.

Reuse
[Agent-Run Browser E2E and Screenshot Evidence](../tools/agent-run-browser-e2e-screenshot-evidence.md)
and
[Run Playwright Core with Windows Node and Chrome from WSL](../tools/agent-run-playwright-core-wsl.md).

**Skip when:** API/integration proof fully covers the acceptance claim.

## 7. CI proof versus runtime proof

Treat these as separate evidence layers:

```text
source revision
  -> CI/check result
  -> execution/deployment identity
  -> provider/runtime readback
  -> acceptance journey
  -> cleanup/retained-state result
```

A green CI run does not automatically prove deployment convergence, target
identity, service health, offline behavior, UI acceptance, or cleanup.

Persist durable execution IDs for long-running operations and reconcile the
original execution before retrying.

## 8. Cost and cleanup

For demos, labs, build systems, retained compute/storage, large artifacts, or
frequent CI, record:

- what was created;
- what remains;
- the TTL/lifecycle/cleanup path;
- cleanup evidence;
- measured usage/cost when it materially affects future platform selection.

Keep estimates separate from billing evidence. Do not invent a price comparison
from architecture alone.

## Selection rule

Ask only what changes the decision:

1. What drift or failure has actually occurred?
2. Would a container remove that drift or hide the real target?
3. Which existing runner already satisfies trust and connectivity?
4. Can short-lived identity replace a stored cloud key?
5. What is the smallest proof that reaches the acceptance boundary?
6. Is browser interaction part of that boundary?
7. What is CI evidence versus runtime/provider evidence?
8. What must be cleaned or cost-measured?

If the current repository already answers these safely, add no new framework.

## Promotion boundary

- Project repositories remain authoritative for implementation and runtime truth.
- Detailed procedures stay in their existing Agent OS playbooks.
- This page selects and links; it does not duplicate them.
- Do not propagate these patterns into `repo-starter` until repeated use proves
  which rules are truly universal.
- Host-specific facts stay in dotfiles/local guidance.

## Citations

- https://docs.docker.com/build/building/best-practices/
- https://docs.docker.com/build/building/secrets/
- https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html
- https://playwright.dev/docs/library
