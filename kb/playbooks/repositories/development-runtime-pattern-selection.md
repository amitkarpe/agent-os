---
type: Practice
title: Development and Runtime Pattern Selection
description: Choose reproducible development, CI, identity, testing, browser E2E, runtime evidence, cost, and cleanup patterns without forcing one stack onto every repository.
status: candidate
scope: repository development and runtime workflow selection
confidence: medium
timestamp: 2026-10-02T00:00:00+08:00
review_after: 2027-01-02
tags: [development, runtime, containers, ci, oidc, testing, playwright, reproducibility, cost, cleanup]
---

# Development and Runtime Pattern Selection

Use this page as a **selection guide**, not as a mandatory stack.

The recurring lesson is simple:

> Make the development and proof path reproducible enough for the task, then stop.

Different repositories need different execution substrates. A browser POC, an AMI
factory, an offline workflow, and a host-patching repository should not be forced
into the same container, runner, test, or deployment model.

## 1. Reproduce the working path from Git

A meaningful deliverable should keep enough versioned material to rebuild or
re-run the intended capability without depending on one developer host.

Prefer repository-owned:

- build/start/health/check commands;
- supported language/runtime/tool versions;
- lockfiles or equivalent dependency pins where supported;
- configuration **shape** and safe examples;
- container or preparation-image definitions when used;
- cleanup/recovery instructions;
- one clean-consumer or fresh-install proof when portability matters.

Do not commit credentials, browser state, databases, raw private evidence, or
machine-specific secrets merely to make the repository "complete."

A host inventory is useful discovery. It is not reproducibility proof.

## 2. Use containers when they remove real drift

Use a container, Compose service, or dedicated preparation image when it
materially reduces dependency, package, runtime, or CI-runner drift.

Good candidates include:

- dependency-heavy local services;
- repeatable build/test toolchains;
- disposable integration environments;
- CI preparation images with exact tools;
- portable/offline consumers where image identity matters.

Skip or limit containerization when the behavior being tested depends on the
real host OS, kernel, mount policy, systemd, SSM/host patching, privileged
networking, or a restricted office runtime that must not install another
container engine.

When containers are used:

- pin application dependencies;
- prefer immutable image digests for trusted/release paths;
- record architecture when it matters;
- keep secrets out of image layers and build arguments;
- prove the real consumer path, not only that the image builds.

Containers are an isolation tool, not proof that host assumptions disappeared.

## 3. Choose the runner by trust, connectivity, tools, and cost

Keep workflow definition separate from the execution substrate.

Possible substrates include:

- standard GitHub-hosted runners;
- an existing approved GitLab Runner;
- CodeBuild-hosted GitHub Actions runners;
- CodeBuild/CodePipeline or another AWS-owned execution service.

Choose based on:

1. network reachability;
2. organization/security policy;
3. required tools and architecture;
4. workload duration and artifact behavior;
5. current runner availability;
6. measured or bounded cost.

Keep CI orchestration thin. CI should call repository-owned commands instead of
reimplementing application logic inside a large workflow file.

For AWS control, reuse
[GitHub OIDC and AWS-Owned Control](../integrations/github-oidc-aws-control.md).
For internal connected preparation, reuse
[GitLab Runner Connected Preparation](../integrations/gitlab-runner-connected-preparation.md).

Do not infer that "public" always means GitHub-hosted or "private" always means
CodeBuild. Those are useful defaults only when the actual trust/connectivity
constraints agree.

## 4. Prefer short-lived identity; keep secrets separate

For supported CI-to-cloud access, prefer OIDC/workload identity with narrowly
bounded roles over copied long-lived cloud keys.

Keep these concerns separate:

- repository/workflow permission;
- runner identity;
- cloud workload identity;
- application/API secrets;
- human browser/session authentication.

Version configuration schemas and required variable names. Supply secret values
through the approved CI/runtime/local secret mechanism.

Do not:

- commit raw credentials or tokens;
- bake secrets into container layers;
- expose temporary credentials in evidence;
- treat successful authentication as authority for every mutation.

Identity proof should read back the actual target identity before privileged work.

## 5. Use testing economy, but cover the real failure boundary

The existing Agent OS testing-economy rule still applies: default to **zero new
tests** and add tests only when they cover a real uncovered regression,
contract, security boundary, failure mode, or high-signal isolated logic.

That does **not** mean zero validation.

Select the smallest sufficient proof layer:

- static/lint/schema checks for structure;
- focused unit tests for isolated risky logic;
- contract tests for interfaces and deny paths;
- integration tests for component interaction;
- one end-to-end golden path when the user/runtime journey is the claim;
- provider/runtime readback when external state matters.

Do not measure quality by test count. A small suite plus one strong integration
journey is often better than many low-signal tests.

## 6. Use Playwright when the browser journey is part of the claim

For meaningful interactive UI behavior, prefer the repository's browser
framework or Playwright to prove the actual journey.

The useful proof chain is:

```text
real user action
  -> expected API / persisted state
  -> rendered DOM
  -> browser/network error checks
  -> screenshot or review artifact
  -> exact cleanup
```

A screenshot alone proves rendering, not policy, backend execution, persistence,
or cleanup.

Reuse:

- [Agent-Run Browser E2E and Screenshot Evidence](../tools/agent-run-browser-e2e-screenshot-evidence.md)
- [Run Playwright Core with Windows Node and Chrome from WSL](../tools/agent-run-playwright-core-wsl.md)

Skip browser E2E when the change has no user-facing browser contract or when a
smaller API/integration proof fully covers the acceptance claim.

## 7. Keep CI proof and runtime proof separate

A green CI run proves only the checks configured for that exact revision.

It does not automatically prove:

- the intended cloud account/Region/resource was used;
- deployment converged;
- the service is healthy;
- an offline consumer has no undeclared dependency;
- the UI renders the accepted result;
- cleanup succeeded.

For stateful or external systems, keep separate evidence for:

```text
source revision
  -> CI/check result
  -> execution/deployment identity
  -> provider/runtime readback
  -> acceptance journey
  -> cleanup/retained-state result
```

Persist execution IDs or equivalent durable handles for long-running operations.
Resume by reading the original execution state instead of blindly starting a
replacement.

## 8. Treat cost and cleanup as engineering evidence

For demos, labs, build systems, retained EC2/storage, large artifacts, or
frequent CI:

- identify resources intended to remain after the run;
- define TTL/lifecycle/cleanup when practical;
- provide an exact bounded cleanup path for resources the repository owns;
- record duration/usage/cost evidence when it is material to future platform
  selection;
- distinguish measured billing evidence from estimates.

Do not invent a price comparison from architecture alone.

A useful closeout answers:

```text
What was created?
What is retained?
What was cleaned?
What still costs money?
What evidence proves cleanup?
```

## Selection checklist

Before adding infrastructure or tooling, ask:

1. What host/runtime drift has actually caused pain?
2. Does a container remove that drift, or hide the real target behavior?
3. What runner already satisfies trust and connectivity?
4. Can short-lived identity replace a stored cloud key?
5. What is the smallest validation that proves the changed behavior?
6. Is a real browser journey part of acceptance?
7. What evidence is CI-only versus provider/runtime truth?
8. What must be cleaned or cost-measured when the work ends?

If the current repository already answers these questions safely, do not add a
new framework.

## Promotion boundary

This is a candidate synthesis of recurring cross-project learning.

- Project repositories remain authoritative for their implementation and runtime.
- Existing Agent OS playbooks remain authoritative for their detailed procedures.
- This page should link and select; it should not duplicate them.
- Do **not** propagate this page into `repo-starter` until repeated use shows
  which, if any, rules are universal enough to become starter defaults.
- Host-specific adapters and machine facts belong in dotfiles/local guidance.

## Citations

- https://docs.docker.com/build/building/best-practices/
- https://docs.docker.com/build/building/secrets/
- https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html
- https://playwright.dev/docs/library
