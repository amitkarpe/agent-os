---
type: Policy
title: Knowledge Lifecycle and Publication
description: A public-safety workflow for capturing, reviewing, promoting, and retiring knowledge.
status: verified
scope: public knowledge repositories
confidence: high
timestamp: 2026-07-15T00:00:00+08:00
last_verified: 2026-07-15
review_after: 2027-01-15
tags: [knowledge, publication, okf]
---

# Knowledge Lifecycle and Publication

## Lifecycle

Use four lifecycle states:

- `candidate`: captured outside the public repository and not approved for publication.
- `reviewed`: sanitized and checked for usefulness and support.
- `verified`: technical claims have current primary evidence or repeatable validation.
- `deprecated`: retained for history but no longer recommended.

## Promotion Gate

One curator owns promotion. Before moving a candidate into Git:

1. Search the index and existing concepts. Extend or cross-link the one
   canonical home instead of publishing duplicate policy.
2. Rewrite the learning for general reuse rather than copying its source.
3. Remove credentials, private identifiers, local paths, raw evidence, customer
   details, and current authentication state.
4. Distinguish reusable guidance from dated observations.
5. Record scope, confidence, lifecycle status, and a review date.
6. Cite official or primary public sources for externally verifiable technical
   claims.
7. Link the concept from the index using a relative repository link.
8. Validate metadata, links, and secret patterns deterministically.
9. Review the complete local branch as material that may remain public
   permanently.
10. Promote only after an explicit human public-safety decision.

Reject raw chats, unsupported universal claims, duplicated policy, credentials,
private infrastructure, and host-specific runtime truth.

## Reusable-Learning Closeout

After meaningful project work, surface a reusable-learning candidate only when a
non-obvious lesson is likely to help other repositories or future work.

Keep closeout small:

1. State the lesson in sanitized, general terms.
2. Classify it as `policy`, `playbook`, or dated `observation`.
3. Check whether Agent OS already has the canonical concept; extend or cross-link
   it instead of creating a competing home.
4. Leave project-specific details in the owning project.
5. Promote into Agent OS only through the normal public-safety gate.

Do not create a candidate merely to document routine work, obvious facts, or
one-off project state. Normal reusable guidance belongs in Agent OS; only a
universal repository default should also be distilled into `repo-starter`.
Machine-, host-, or tool-specific operating facts belong in the relevant local
runtime configuration instead.

## Use and Maintenance

Project instructions, specifications, approvals, and safety rules override
general Agent OS guidance. Select only the one to three concepts needed for
the current task, then read their canonical source directly.

Review each concept by its `review_after` date. Recheck evidence, citations,
scope, confidence, links, and whether another concept has become canonical.
Keep dated observations separate from reusable guidance.

## Format

Markdown is canonical. The knowledge bundle uses OKF 0.1: concept documents
contain YAML frontmatter with a non-empty `type`, while the root index declares
the OKF version using the specification's root-index exception.

## Retirement

Do not silently erase superseded learning. Mark it `deprecated`, link its
replacement or explain the reason, and remove it only when repository policy
permits.

## Citations

- [Open Knowledge Format 0.1 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [GitHub guidance for removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
