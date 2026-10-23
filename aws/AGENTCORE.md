---
type: Policy
title: Bounded AWS Agent Experiment
description: Select managed or code-owned model loops and verify a bounded tool boundary.
status: candidate
confidence: high
scope: Reusable public-safe agent guidance
review_after: 2027-04-23
tags: [aws, agentcore, harness, strands, proof]
---

# Bounded AWS Agent Experiment

Use an agent only if the goal genuinely requires model-directed tool choice. A deterministic script or direct API call is simpler for fixed steps. Reading this guide grants no AWS identity, IAM, paid inference, deployment, mutation or production authority.

## Choose the owner of orchestration

| Requirement | Smallest starting point |
| --- | --- |
| Known deterministic steps | Existing script/workflow; no agent framework |
| Model + instructions + allowlisted tools suffice | Consider managed AgentCore Harness |
| Custom orchestration, middleware or code ownership | Code-owned loop such as Strands; Runtime is optional hosting |

Harness runs a configuration-defined managed loop; AgentCore Runtime hosts application-owned code. Do not export/create a codebase just because a service allows it. Check current official AWS availability, versions, pricing and Regions rather than treating dated guides as evergreen.

## Prove one interaction

1. Define one question, expected result and observable evidence.
2. Use synthetic input and one deterministic no-op/read-only tool. Validate accepted arguments and authorization **outside the model**, denying other requests.
3. Prove this boundary locally with the smallest existing check; do not create a test framework. SDK execution may still call a paid remote provider.
4. For **approved** inference, bound tool allowlist, number of calls, loop duration and spending. Keep request/trace identity, validated arguments, tool output and final response. Reconcile an uncertain result before repeating it.
5. For deployments, mutations or long-running AWS operations, apply the separate [durable AWS control](../kb/playbooks/integrations/github-oidc-aws-control.md) gates and verify actual target state. Those OIDC/durable-execution controls are **not mandatory for a short authorized read-only invocation**.
6. Distinguish local simulation, configured resources, model-call result and actual live deployment proof.

Gateway, Browser, Memory and other components are optional, not a starter checklist. Detailed vendor research and local provider configuration remain in their existing legitimate dotfiles/project owners; this selection guide is not an API reference or deployment mandate.

## Related

- [Shared Core](../CORE.md)
- [Proportional testing](../TESTING.md)
- [Evidence lifecycle](../KNOWLEDGE.md)

## Citations

- [AgentCore Harness vs Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-vs-runtime.html)
- [AgentCore overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [Strands agent loop](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/agent-loop/)
- [Dated specialist source notes](https://github.com/amitkarpe/dotfiles/tree/815f31b7995dcfe023f10c041cc5416b412b4ed5/config/.config/agent/aws-agent)
