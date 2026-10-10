# Humanly

[![skills.sh](https://skills.sh/b/giorgiberia/humanly)](https://skills.sh/giorgiberia/humanly)

**Built for agents. Made for humans.**

Humanly is a lightweight, self-assessed standard and coding-agent skill for apps that use AI agents without leaving people behind.


## Install Humanly

Give your AI coding agent the ability to build software
that remains accessible, transparent, and human-controlled.

```bash
npx skills add giorgiberia/humanly
```

### For OpenAI Codex

Install globally across your projects:

```bash
npx skills add giorgiberia/humanly -g -a codex
```

### What Humanly checks

- H0 — Agent Only
- H1 — Human Access
- H2 — Human Control
- H3 — Human Ownership

### Example

Ask your coding agent:

"Use Humanly to review this project for H2 compliance."

## Humanly levels

| Level | Name | What it means |
| --- | --- | --- |
| **H0** | Agent Only | Human path not demonstrated. |
| **H1** | Human Access | Core tasks work without an agent, through usable and accessible controls. |
| **H2** | Human Control | H1 + transparent agent actions, consequential approvals, and feasible intervention. |
| **H3** | Human Ownership | H2 + action history, portable export, and clear deletion processes. |

Levels build on one another. They are **self-assessed**; this is not a certification program.

## Add Humanly to a project

1. Copy [`assets/HUMANLY-template.md`](assets/HUMANLY-template.md) to your project's root as `HUMANLY.md`.
2. Test the relevant workflows; choose an honest H0-H3 level or leave `unassessed`.
3. Optionally add [`assets/AGENTS-snippet.md`](assets/AGENTS-snippet.md) to the project's `AGENTS.md`.
4. Check the declaration text with `python scripts/check_declaration.py /path/to/project` (not a runtime accessibility audit).

The full draft requirements are in [`references/standard-v0.3-draft.md`](references/standard-v0.3-draft.md).

## Principles

- Human access without requiring AI for core tasks.
- Visible, understandable automation and appropriate human oversight.
- Respectful cancellation, recovery, and honest handling of irreversible effects.
- User access to history, portable data, and deletion controls at H3.
- Straightforward adoption and verification, without heavy infrastructure.

**Status:** v0.3 draft; Apache 2.0 license. No owned domain or external certification is asserted here.
