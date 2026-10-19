---
type: Practice
title: Download Cloudflare Demo Access Playbook
description: Reusable Cloudflare Workers demo publication, custom domains, public access, email allowlists, and GitHub configuration.
status: reviewed
scope: synthetic Cloudflare Workers demos
confidence: high
timestamp: 2026-10-19T00:00:00+08:00
review_after: 2027-04-19
tags: [cloudflare, workers, access, github-actions, dns, deployment]
---

# Download Cloudflare Demo Access Playbook

**Purpose:** publish reviewed, synthetic-only demos using a dedicated Cloudflare Worker and branded custom domain. This is reusable guidance, not account authorization. The owning repository Issue/SPEC and live provider evidence decide what is permitted.

## Access options

| Mode | Visitor experience | Setup | Consideration |
|---|---|---|---|
| PUBLIC | Open URL, no login | Dedicated Worker and custom domain, no Access challenge | Suitable for strictly synthetic demos; content can be copied by anyone |
| EMAIL_ALLOWLIST | Allowed email receives one-time PIN | Cloudflare Access self-hosted app, explicit Allow emails and OTP method | Individual identity control; 5–10 reviewers is practical |
| SHARED_SECRET_GATE | Shared long passphrase | Custom server-side Worker secret plus validated session, expiration and rate limiting | Shareable credential, no individual audit; NOT Cloudflare Access OTP |

**Do not put passwords in HTML, browser JS, URLs, Git history, GitHub Variables, or screenshots.** For a public synthetic showcase, prefer PUBLIC rather than inventing a new password gate.

## PUBLIC Worker runbook

1. Reconcile current repository Issue, exact approved Git commit, static asset allowlist and package hash. Review for secrets, real account IDs, customer information, private incident data, outbound network calls and third-party scripts.
2. Read current Cloudflare account, Workers, existing domains, DNS, Access applications and routes before touching anything. Select a **distinct** Worker and unused hostname.
3. Deploy only the reviewed source package. Capture Worker name, provider version/deployment identity, Git SHA, package hash and rollback identity. Repository merge alone is not deployment.
4. Bind the approved subdomain via **Worker custom domain** in the correct zone. Avoid overlapping an existing Worker, DNS record or route. Keep preview endpoints disabled unless requested.
5. PUBLIC means no login challenge at **all reachable hostnames**, including an active workers.dev URL. Do not alter unrelated Access applications or broad Zero Trust settings.
6. Test from an unauthenticated browser session: correct HTTPS URL, no email OTP, correct version, working MOCK journey and exported evidence with REAL_WRITES=0.
7. Retain a short sanitized release receipt. A successful domain API response does not by itself prove TLS, DNS propagation or anonymous-browser acceptance.

## Restrict access later: 5–10 reviewer emails

In Cloudflare Zero Trust → Access → Applications, configure a self-hosted application for the exact hostname (and alternative Worker URLs where necessary). Configure One-time PIN or another approved identity provider. Add a policy with **explicit email addresses**. Do NOT create an Allow rule for Everyone or all OTP users. Test an allowed and a disallowed identity; verify there is no workers.dev bypass. Keep private reviewer email lists outside the public KB.

## Optional shared passphrase

A shared password requires a custom **server-side** gate with a Worker secret, constant-time verification, rate limiting, HTTPS-only HttpOnly session cookie, expiration and revocation. A shared string is easier to redistribute than an identity-based credential; avoid this implementation for ordinary public synthetic demos.

## GitHub Actions configuration (names only)

| Optional key | Store in | Meaning |
|---|---|---|
| CLOUDFLARE_ACCOUNT_ID | GitHub Actions Variable | Non-secret, intended account reference |
| CLOUDFLARE_ZONE_ID | GitHub Actions Variable | Target DNS zone when a custom hostname is used |
| CLOUDFLARE_WORKER_NAME | GitHub Actions Variable | Distinct per-project Worker name |
| CLOUDFLARE_CUSTOM_DOMAIN | GitHub Actions Variable | Explicit approved hostname |
| CLOUDFLARE_API_TOKEN | GitHub Actions encrypted Secret, only if genuinely needed | Least-privilege credential for target Worker deployment |

**Only placeholders/key names belong in Agent OS.** Do not push local environment files or copy existing keys into a public GitHub repository. Prefer a supported connected identity or managed/short-lived credential. If CI truly requires a token, configure only the minimal scoped secret in the relevant **application repository**, never the public KB repository, through an approved secret-write workflow. GitHub Variables are not secrets; encrypted GitHub Actions Secrets are write-only to agents without permission. Do not assume any of the five example names are already configured.

## Acceptance

- [ ] Exact account, Worker and hostname approved; no existing Worker overwritten
- [ ] Assets reviewed as public-safe and synthetic-only
- [ ] Git source SHA, package checksum, deployment/version receipt and rollback recorded
- [ ] Worker domain resolves to the intended service
- [ ] All endpoints honor the selected access mode
- [ ] PUBLIC: truly anonymous browser works without an OTP
- [ ] EMAIL_ALLOWLIST: approved email succeeds and disallowed email is blocked
- [ ] Visible MOCK/SYNTHETIC label and no claims of real provider writes
- [ ] No secrets copied to GitHub or logs; cost assumptions are labeled accurately

## Reuse

This Markdown is the canonical general reference. Link it from project-specific Issues and AGENTS files instead of copying it. Consider a small Skill only when multiple agents need repeatable readback/deploy/rollback tool orchestration; any Skill should reference this playbook, not duplicate it.

## Citations

- [Workers custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/)
- [Workers Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/)
- [Cloudflare Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)
- [GitHub Actions secrets and variables](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
