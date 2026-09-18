---
type: Playbook
title: GitLab Runner Connected Preparation
description: Use GitLab as an internal execution plane for connected preparation while keeping source authority, runner health, short-lived identity, and offline runtime boundaries explicit.
status: reviewed
scope: GitHub-primary repositories mirrored to GitLab for CI/CD and connected preparation
confidence: high
timestamp: 2026-09-18T13:52:00+08:00
last_verified: 2026-09-18
review_after: 2027-03-18
tags: [gitlab, github, runner, mirror, oidc, ci, preparation, security, offline]
---

# GitLab Runner Connected Preparation

Use GitLab Runner as a replaceable connected execution host, not as the source of application truth.

Canonical pattern:

    canonical source repository
      -> internal GitLab pull mirror
      -> current GitLab Runner
      -> connected preparation
      -> short-lived cloud identity when required
      -> bounded internal artifact publication
      -> offline/private runtime

## 1. Keep one source authority

When GitHub is canonical and GitLab exists for internal CI/CD, use GitHub -> GitLab Pull mirror -> GitLab CI/Runner.

Do not configure push or bidirectional mirroring unless the project explicitly requires a different authority model.

Mirror acceptance must be based on real refs and SHA equality, not a UI status alone:

    MIRROR_DIRECTION=Pull
    SOURCE_MAIN_SHA=<sha>
    TARGET_MAIN_SHA=<same sha>
    TARGET_MAIN_EXISTS=true
    RESULT=PASS

## 2. Prove a current Runner first

Historical Runner success is architectural evidence, not current capacity. Before CI work record Runner availability, status, executor, architecture, and tags.

A stale, paused, offline Runner, or one backed by deleted compute, is a platform-availability problem. If repository automation has no runner-administration authority, classify it as:

    RESULT=BLOCKED
    BLOCKER=RUNNER_ADMIN_ACTION_REQUIRED

Stop before application preparation.

## 3. Use the cheapest preflight first

Advance in this order:

1. current Runner;
2. architecture and executor;
3. outbound Internet to one approved public endpoint;
4. required local tools;
5. short-lived identity if cloud access is needed;
6. bounded storage/registry access;
7. application-specific preparation.

A generic health result is:

    RUNNER_AVAILABLE=PASS
    RUNNER_INTERNET=PASS
    REQUIRED_TOOLS=PASS
    RESULT=PASS

Stop at the first meaningful blocker.

## 4. Keep CI orchestration thin

CI configuration should call repository-owned scripts. Do not duplicate discovery, build, migration, validation, or release logic inside a large .gitlab-ci.yml.

Prefer: GitLab CI -> generic runner-health script -> project-owned preparation command -> compact evidence artifact.

## 5. Use a dedicated preparation image when needed

Hosted or autoscaled runners often begin with a minimal job image. If tools are missing, use a dedicated preparation image and record its immutable image digest plus tool versions.

Do not assume Docker-in-Docker is available. Unprivileged runners may reject privileged Docker builders. Use an approved rootless/unprivileged builder or a prebuilt preparation image.

Keep the preparation image separate from application/runtime images.

## 6. Prefer short-lived workload identity

When a Runner must access a cloud account, prefer CI-native OIDC/workload identity over static keys.

Use identity-first sequencing: Runner -> CI ID token -> cloud STS/workload identity -> temporary credentials -> identity readback only.

First prove:

    OIDC_TRUST=PASS
    CLOUD_IDENTITY=PASS
    RAW_TOKEN_RECORDED=NO
    TEMPORARY_CREDENTIALS_RECORDED=NO

Do not grant storage, registry, deployment, or administration rights as part of the identity proof.

## 7. Add data-plane access incrementally

After identity succeeds, add only the smallest required scope: one storage prefix, one registry namespace, read-only metadata, or one disposable smoke object/image.

Keep evidence truthful. If an out-of-scope deny test was not run, record NOT_RUN rather than inventing PASS.

## 8. Separate connected preparation from offline runtime

Connected preparation may fetch source, inspect dependencies, resolve plugins/images, and stage approved assets. Offline/private runtime must consume only staged internal artifacts.

Do not infer offline-runtime proof merely because connected preparation succeeded.

## 9. Mirror-compatible repository policy

Externally authored history may conflict with project push rules that assume every commit was authored, signed, or mapped to a local GitLab user.

For a pull-mirror repository, evaluate verified-user-only authorship, mandatory local-user mapping, and mandatory commit-signing rules for technical compatibility. Do not weaken group or instance policy globally. Apply only the smallest approved repository-level exception.

Keep secret-detection controls enabled unless an owning security policy says otherwise.

## 10. Common failure modes

- Wrong mirror direction: verify Pull for source -> GitLab use cases.
- Green mirror status but no refs: inspect branches/commits and compare SHAs.
- Runner stale/offline: classify as external platform/admin recovery.
- Tools absent: use a preparation image; keep CI YAML thin.
- Privileged Docker unavailable: use approved unprivileged/rootless build.
- OIDC failure: verify issuer, audience, subject/project/ref constraints, and trust before changing permissions.
- Architecture mismatch: record Runner architecture before selecting images or native binaries.

## 11. Minimal evidence packet

    SOURCE_AUTHORITY=
    MIRROR_DIRECTION=
    SOURCE_MAIN_SHA=
    TARGET_MAIN_SHA=
    MIRROR_RESULT=
    RUNNER_AVAILABLE=
    RUNNER_STATUS=
    RUNNER_EXECUTOR=
    RUNNER_ARCHITECTURE=
    RUNNER_TAGS=
    RUNNER_INTERNET=
    REQUIRED_TOOLS=
    WORKLOAD_IDENTITY=PASS|NOT_REQUIRED|BLOCKED
    DATA_PLANE_ACCESS=PASS|NOT_REQUIRED|NOT_RUN
    APPLICATION_PREPARATION=PASS|BLOCKED|NOT_RUN
    RESULT=PASS|BLOCKED|FAIL
    NEXT=<one action>

Keep evidence compact and non-secret.

## 12. Promotion boundary

Project repositories own scripts, CI files, permissions, runner tags, and runtime evidence. Agent OS owns reusable policy and sequence guidance. Local host/tool defaults belong in local/dotfiles guidance.

Do not turn Agent OS into a copy of one project implementation.

## Citations

- https://github.com/amitkarpe/nextflow-offline/issues/22
- https://github.com/amitkarpe/nextflow-offline/pull/23
- https://github.com/amitkarpe/nextflow-offline/pull/25
- https://github.com/amitkarpe/nextflow-offline/issues/26
- https://github.com/amitkarpe/nextflow-offline/pull/27
- https://github.com/amitkarpe/nextflow-offline/issues/28
- https://github.com/amitkarpe/nextflow-offline/pull/29
- https://github.com/amitkarpe/nextflow-offline/pull/39
- https://github.com/amitkarpe/cloudos-offline/pull/6
