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

## Ownership

One curator owns promotion into this repository. Candidate material remains
outside Git until it has been sanitized, reviewed, and deliberately promoted.
