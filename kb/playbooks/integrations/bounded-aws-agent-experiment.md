---
type: Playbook
title: Choose and Bound an AWS Agent Experiment
description: Choose managed configuration or a code-owned loop and prove one safe tool interaction before expanding an AWS agent experiment.
status: candidate
scope: Task-scoped agent experiments; source guidance, not deployment or runtime acceptance
confidence: medium
last_verified: 2026-10-23
review_after: 2027-01-23
tags: [aws, agentcore, strands, experiments, tools, evidence]
---

# Choose and Bound an AWS Agent Experiment

Use this when the learning goal requires a model-directed tool loop. A script
or ordinary API call is sufficient when the work is deterministic. The owning
project and [Shared Agent Core](../../../CORE.md) retain authority; reading this
guide grants no installation, inference, deployment or spending permission.

## Choose who owns the loop

| Requirement | Smallest starting point |
| --- | --- |
| Fixed inputs and deterministic steps | Existing script or workflow; no agent framework |
| Model, instructions and allowed tools can express the experiment | Consider AgentCore Harness, which manages the loop from configuration |
| Custom orchestration, middleware or code ownership is required | A code-owned loop, such as Strands; AgentCore Runtime is an optional hosting target |

Harness manages orchestration; Runtime hosts code whose orchestration remains
application-owned. Do not create or export a codebase merely because that route
exists. Check current official capabilities before choosing; this guide does
not freeze service status, SDK versions, models, Regions, pricing or defaults.

## Prove one bounded interaction

1. Name the question the experiment must answer and the observable expected
   result. Follow [Testing and Validation](../../../TESTING.md); this recipe is
   not a requirement to add a test suite or framework.
2. Start with one deterministic no-op or read-only tool and synthetic input.
   Define accepted arguments and denial behavior. Validate authorization and
   arguments before execution, outside the probabilistic model decision. Do not
   add broad shell, filesystem or remote-tool access without a concrete need.
3. Prove the tool boundary locally with the smallest existing check. Keep this
   distinct from model invocation: a locally running SDK may still contact a
   remote provider and incur cost.
4. For an authorized model or cloud invocation, bound the tool allowlist,
   invocations, loop/time limits and cost in the owning goal. Use the existing
   [AWS control gates](github-oidc-aws-control.md) for exact target identity,
   durable execution state, uncertain-retry handling and live readback.
5. Inspect the actual tool request, validated arguments, result and final
   response or trace. A prepared configuration or local check is not deployed
   runtime proof. Record what ran and what remains unproved before changing one
   relevant variable or adding another capability.

Memory, Gateway, Browser, Code Interpreter and other services are optional
requirements, not a starter checklist. Add only what the experiment needs.
Keep retention and cleanup disposition in the owning goal using the existing
[evidence lifecycle](../knowledge/temporary-agent-evidence-lifecycle.md).

## Ownership

This playbook owns the reusable selection and evidence workflow. Installation,
CLI availability, provider routing, account configuration and detailed vendor
research remain with their setup/project owners. Preserve useful specialist
references until their replacement coverage is checked; this short workflow
does not replace a service catalog, API reference or operational runbook.

## Citations

- [AWS: AgentCore Harness versus Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html)
- [AWS: AgentCore overview and optional services](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [Strands: Agent loop](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/agent-loop/)
- [Dated public source notes preserved during migration](https://github.com/amitkarpe/dotfiles/tree/815f31b7995dcfe023f10c041cc5416b412b4ed5/config/.config/agent/aws-agent) — provenance, not current vendor authority.
