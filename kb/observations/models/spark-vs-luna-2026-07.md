---
type: Experiment
title: Spark versus Luna Evaluation, July 2026
description: A single read-only sample comparing a latency-focused profile with a low-cost repeatable-work profile.
status: reviewed
scope: one bounded read-only corpus evaluation
confidence: low
timestamp: 2026-07-14T00:00:00+08:00
last_verified: 2026-07-14
review_after: 2026-08-14
tags: [models, evaluation, delegation]
---

# Spark versus Luna Evaluation, July 2026

## Question

For one fixed, read-only corpus task, did a latency-focused Spark profile at
high reasoning effort outperform a low-effort Luna profile enough to justify
using it by default?

## Result

Both runs scored 40 of 40 deterministic answer atoms and passed the required
schema. The Spark run completed in 24.89 seconds and the Luna run in 56.12
seconds, making Spark 2.25 times faster in this sample.

The faster run used 15,277 output tokens, including 13,729 reasoning tokens,
and made 13 successful shell calls. The lower-cost run used 2,585 output
tokens, including 664 reasoning tokens, and made 3 successful shell calls.

## Interpretation

This sample supports Luna low as the economical default for clear, repeatable,
batchable read-only work. Spark high effort may be useful when one tiny lookup
blocks an interactive workflow and latency matters more than usage. The sample
does not show an accuracy advantage for Spark and does not isolate the value of
high reasoning effort because no lower-effort Spark control was run.

Do not generalize this result to writing, architecture, policy, security, or
other risk-bearing work.

## Limitations and Retest

This was one task with one run per profile. Two fixture cardinality defects and
a nested instruction-scope difference reduced comparability. Retest with at
least three frozen prompts, corrected fixtures, and a lower-effort Spark
control when the CLI, model, or profile changes or before granting write scope.

## Citations

- [OpenAI Codex model guidance](https://learn.chatgpt.com/docs/models)
- [OpenAI Codex speed guidance](https://learn.chatgpt.com/docs/agent-configuration/speed)
- [OpenAI Codex subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [GPT-5.3-Codex-Spark announcement](https://openai.com/index/introducing-gpt-5-3-codex-spark/)
