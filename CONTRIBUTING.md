# Contributing

## Promotion Flow

1. Capture a candidate outside the public Git repository.
2. Confirm that the idea is reusable and that publication is permitted.
3. Rewrite it as a concise concept with OKF frontmatter.
4. Remove private identifiers, paths, authentication details, and unsupported
   claims.
5. Add official or primary citations for technical claims.
6. Link the concept from `kb/index.md`.
7. Run `scripts/validate.sh --self-test` and `scripts/validate.sh`.
8. Review the complete diff as permanently public material before promotion.

## Metadata

Every concept Markdown file under `kb/`, except reserved `index.md` files,
requires YAML frontmatter with a non-empty `type`. Prefer only metadata that
helps readers assess scope, lifecycle, confidence, and freshness.

Lifecycle status values are `candidate`, `reviewed`, `verified`, and
`deprecated`.

## Scope

Executable workflows belong in their owning automation repositories. This
repository records knowledge about those workflows, not host operations,
credentials, runtime state, or evidence bundles.
