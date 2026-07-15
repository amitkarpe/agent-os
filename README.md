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

Validate a checkout with:

```bash
scripts/validate.sh
```

Run the validator's focused pass/fail checks with:

```bash
scripts/validate.sh --self-test
```

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
