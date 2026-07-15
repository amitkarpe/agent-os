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

1. Rewrite the learning for general reuse rather than copying its source.
2. Remove credentials, private identifiers, local paths, raw evidence, customer
   details, and current authentication state.
3. Distinguish stable guidance from dated observation.
4. Cite official or primary public sources for technical claims.
5. Validate metadata, links, and secret patterns deterministically.
6. Review the complete local branch as material that may remain public
   permanently.
7. Promote only after an explicit human public-safety decision.

## Format

Markdown is canonical. The knowledge bundle uses OKF 0.1: concept documents
contain YAML frontmatter with a non-empty `type`, while the root index declares
the OKF version using the specification's root-index exception.

## Retirement

Do not silently erase superseded learning. Mark it `deprecated`, explain the
replacement or reason, and remove it only when repository policy permits.

## Citations

- [Open Knowledge Format 0.1 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [GitHub guidance for removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
