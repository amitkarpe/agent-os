# Agent OS

Agent OS is a public knowledge bundle of concise operating principles,
policies, playbooks, practices, patterns, and dated observations for agentic
work.

The repository uses Markdown as its canonical format. Content under [`kb/`](kb/)
targets [Open Knowledge Format 0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

## Use

Start with the [knowledge index](kb/index.md). Treat policies and principles as
stable guidance, playbooks as repeatable procedures, and observations as dated
evidence that may need retesting.

Agents should use the [task-scoped usage guide](kb/playbooks/knowledge/using-agent-os-task-scoped.md)
to load only the concepts relevant to the current task.

## Universal Onboarding Prompt

```text
Learn from Agent OS before continuing.

Agent OS source: <AGENT_OS_ROOT, configured workspace, or public Agent OS URL>
Active project: <active-project-root or repository context>
Task: <task>

Learn: Locate the configured clone through AGENT_OS_ROOT or workspace discovery.
If it is unavailable, use the public Agent OS knowledge base. Read Agent OS
AGENTS.md, README.md, and kb/index.md first.

Apply: Choose the matching task route and load only one to three relevant
concepts. Briefly state what applies, what does not apply, and any conflict. The active
project's instructions, SPEC, approvals, and safety policy remain authoritative.
Apply the useful guidance to planning and execution.

Contribute: At closeout, name the Agent OS concepts used and suggest reusable
learning as a sanitized candidate. Do not publish private runtime truth or
modify Agent OS unless explicitly asked.
```

Validate a checkout with:

```bash
scripts/validate.sh
```

Run the validator's focused pass/fail checks with:

```bash
scripts/validate.sh --self-test
```

GitHub Actions validates pushes and pull requests. After the workflow is pushed,
the repository owner must select **GitHub Actions** as the Pages source if it is
not already enabled.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
