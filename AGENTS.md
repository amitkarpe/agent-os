# Agent OS Repository Guidance

## Purpose

This repository publishes portable operating knowledge for people and software
agents. Markdown is canonical, and the `kb/` tree follows Open Knowledge Format
(OKF) 0.1.

## Contribution Rules

- Keep content general, reusable, and safe for a public repository.
- Never add credentials, authentication state, private infrastructure details,
  customer information, raw logs, chat transcripts, or local machine paths.
- Rewrite source learning; do not copy private or third-party documents.
- Put external source URLs in a `## Citations` section.
- Use relative Markdown links for repository content.
- Use only `candidate`, `reviewed`, `verified`, or `deprecated` for lifecycle
  status.
- Run `scripts/validate.sh` before committing.

## Context Loading

Use the owning Issue/PR plus its latest relevant authorized delta and current
HEAD for normal continuation. Treat broad repository read orders as
bootstrap/recovery guidance, not a per-handoff checklist.

Reload wider context only when the session lacks usable repository context, a
governing file materially changed, identity/objective is ambiguous, current
context is stale/incomplete/contradictory/unsafe, or a new authority/safety
domain requires it. Canonical detail lives in the indexed **Context Loading
Economy** playbook; do not duplicate that policy across repositories.

## Ownership

Agent OS is the canonical home for sanitized, reusable, cross-project operating
knowledge: principles, policies, repeatable playbooks, dated observations, and
the lifecycle used to promote or retire that knowledge.

Ownership roles:

- **Amit** is the policy owner and final decision-maker for durable global
  standards and public promotion.
- **G / ChatGPT** is the curator/controller: identify reusable candidates, check
  for an existing canonical concept, propose sanitized promotion, and check
  cross-repository consistency.
- **X / Codex or repository workers** may implement and validate approved
  changes; implementation authority does not imply policy or publication
  authority.

G is also the portfolio controller for `agent-os`, `repo-starter`, and
`dotfiles`. This role belongs to G, not to one chat session: reconstruct it from
GitHub truth. Periodically triage open work, deduplicate or close stale work,
identify reusable learning, canonicalize it in Agent OS, and propagate only
universal repository defaults to `repo-starter` or local/runtime guidance to
`dotfiles`. Amit remains the final human authority; X implements or validates
when delegated.

Repository responsibilities stay separate:

- `agent-os` owns reusable public knowledge and the promotion model.
- `repo-starter` is a downstream distribution baseline for the smallest
  mandatory defaults new or retrofitted repositories should start with. It
  should distill or reference Agent OS guidance rather than become a second
  knowledge base.
- `dotfiles/agent/.agent` owns local/runtime/tool adapters, host-specific facts,
  provider preferences, and machine-wide operating defaults. It may reference
  Agent OS but should not duplicate reusable public policies.
- Project repositories remain authoritative for their own `AGENTS.md`, `SPEC`,
  current context, approvals, implementation, evidence, and runtime truth. They
  are the primary source of new learning candidates.
- `work` and other active repositories may prove or refine a practice, but once
  generalized they are not the final global source of truth.

Candidate material remains outside this public Git repository until it has been
sanitized, reviewed, and deliberately promoted. Keep one canonical home for a
reusable concept; extend or cross-link it instead of copying competing policy.

Use this promotion direction:

`project learning -> reusable candidate -> sanitize/deduplicate -> Agent OS -> repo-starter only when it is a universal repository default`

Critical safety rules may justify proactive retrofit. Normal improvements should
usually propagate to existing repositories when those repositories are next
touched.

KISS: **Learn locally. Generalize once. Store canonically. Distribute minimally.**

## Portfolio Economy Defaults

- Testing: default to **zero new tests**. Use the smallest existing validation that can prove the change. Add or modify tests only for a real uncovered regression, contract, security boundary, failure mode, or high-signal isolated logic. Once required checks pass and the changed behavior is proven, **stop**.
- Runners: public repositories may use standard GitHub-hosted runners such as `ubuntu-latest`. Private repositories should avoid GitHub-hosted runners by default and reuse an existing approved CodeBuild/CodePipeline or CodeBuild-hosted Actions runner; do not create new CI infrastructure merely to replace a free public runner.
