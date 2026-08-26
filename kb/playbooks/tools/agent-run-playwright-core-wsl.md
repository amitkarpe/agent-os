---
type: Playbook
title: Run Playwright Core Through Windows Chrome from WSL
description: Use an existing Windows Chrome and Node.js installation to run deterministic local browser evidence from a WSL-owned repository.
status: candidate
scope: local web application browser evidence in WSL with Windows Chrome
confidence: high
timestamp: 2026-08-27T00:00:00+08:00
review_after: 2026-11-27
tags: [browser, e2e, playwright, playwright-core, wsl, screenshots]
---

# Run Playwright Core Through Windows Chrome from WSL

This playbook records the small POC pattern used when the application lives in
WSL, Chrome and Node.js live on Windows, and the repository must capture
repeatable browser evidence. Use it with [Agent-Run Browser E2E and Screenshot
Evidence](agent-run-browser-e2e-screenshot-evidence.md); that playbook remains
the source for test layers, stop conditions, and evidence rules.

## Why this route

`playwright-core` supplies the automation API without downloading or managing
its own browser. The runner attaches to the already-installed Windows Chrome
over the local Chrome DevTools Protocol (CDP). This keeps a small POC fast and
avoids a second browser installation.

Install it in the owning JavaScript project, then audit the dependency:

```bash
npm install --save-dev playwright-core
npm audit --audit-level=high
```

Do not put credentials, cloud identifiers, raw logs, or private screenshots in
the knowledge base or public evidence.

## Boundary contract

The repo-owned Bash runner must:

1. Start the local application on loopback and poll a health endpoint.
2. Refuse a busy port instead of killing an unknown process.
3. Create a unique Windows temporary Chrome profile.
4. Launch Chrome with `--headless=new`, CDP on the loopback host, and
   `--remote-debugging-port=0`.
5. Read the selected port from `DevToolsActivePort` in that profile.
6. Convert WSL paths with `wslpath -w` before passing them to Windows Node.
7. Run the repo-owned `.mjs` script with Windows Node and an explicit
   `PLAYWRIGHT_CORE` module path.
8. Capture machine-checkable JSON and screenshots in a run-specific directory.
9. Stop only the Chrome process whose command line contains this exact profile,
   stop the app process created by the run, remove that profile, and verify the
   app port and CDP endpoint are gone.

The runner must not use `pkill`, `taskkill /IM chrome.exe`, a shared browser
profile, a public bind address, or a cloud mutation.

## Minimal launcher pattern

Use placeholders owned by the runner rather than hard-coded user directories:

```bash
chrome_wsl=${CHROME_WSL:?set the Windows Chrome executable}
windows_node=${WINDOWS_NODE:?set the Windows Node executable}
profile_wsl=$(mktemp -d "$windows_temp_wsl/seccop-e2e.XXXXXX")
profile_windows=$(wslpath -w "$profile_wsl")

"$chrome_wsl" \
  --headless=new \
  --disable-background-networking \
  --remote-debugging-address=localhost \
  --remote-debugging-port=0 \
  "--user-data-dir=$profile_windows" \
  about:blank &
chrome_launcher_pid=$!

debug_port=$(sed -n '1p' "$profile_wsl/DevToolsActivePort" | tr -d '\r')
cdp_url="http://localhost:$debug_port"
runner_windows=$(wslpath -w "$repo_dir/scripts/browser-e2e.mjs")
core_windows=$(wslpath -w "$playwright_core")

APP_URL="$app_url" CDP_URL="$cdp_url" PLAYWRIGHT_CORE="$core_windows" \
  "$windows_node" "$runner_windows"
```

The real runner must use bounded polling for `DevToolsActivePort`; the snippet
shows the boundary, not an excuse to wait forever.

## Minimal attachment pattern

The Windows Node script imports the explicit module path and attaches to the
existing browser:

```javascript
import { pathToFileURL } from 'node:url';

const modulePath = process.env.PLAYWRIGHT_CORE;
const { chromium } = await import(pathToFileURL(modulePath).href);
const browser = await chromium.connectOverCDP(process.env.CDP_URL);
const context = browser.contexts()[0] ?? await browser.newContext();
const page = context.pages()[0] ?? await context.newPage();
await page.setViewportSize({ width: 1920, height: 1080 });
```

Drive the real UI, assert the API result, and then take the screenshot. A
screenshot alone is not proof of policy, tool execution, or cleanup.

## Evidence checks used for a local POC

- Health JSON confirms the expected local/synthetic mode.
- The positive path asserts the expected ready state and visible finding cards.
- The approval path asserts `mutation_performed === false` for a mock action.
- The negative path asserts a stable block reason and
  `executed_calls.length === 0`.
- Every request is recorded; external request count must remain zero.
- Browser console and page errors must remain zero.
- Screenshots are written both to the restricted run directory and to the
  operator's review mirror only when that mirror is explicitly requested.

## Failure handling

Stop and retain the run evidence if the port is busy, Chrome does not expose a
CDP endpoint, the module cannot be imported, an assertion fails, an external
request appears, or cleanup cannot be proven. Do not retry by killing unrelated
processes or by widening network access. Fix the runner or application and
start a new unique run.

## References

- [Agent-Run Browser E2E and Screenshot Evidence](agent-run-browser-e2e-screenshot-evidence.md)
- [Playwright library documentation](https://playwright.dev/docs/library)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

## Citations

- Playwright library documentation: https://playwright.dev/docs/library
- Chrome DevTools Protocol: https://chromedevtools.github.io/devtools-protocol/
