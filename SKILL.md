---
name: humanly
description: Apply the Humanly H0-H3 standard to agent-enabled apps so people can use core features without AI, understand agent activity, approve consequential actions, intervene in automation, and control their data. Use when creating, reviewing, or updating HUMANLY.md; auditing human accessibility, action transparency, cancellation, approval, history, export, or deletion; reviewing AI features that affect human access or control; or adding Humanly guidance to AGENTS.md.
---

# Humanly

Build for agents. Keep humans capable, informed, and in control. Treat H0-H3 as a **proposed, self-assessed** standard, not a certification. Consult [Humanly v0.3 draft](references/standard-v0.3-draft.md) for complete requirements.

## Inspect first

1. Read `HUMANLY.md` at the repository root, if present. Read existing `AGENTS.md` and inspect only relevant product flows and code.
2. Identify standard `version`, declared `level`, affected feature/scope, and test evidence. Apply the project's declared version and flag unsupported or unverified claims.
3. If the user requests a new declaration, start from [HUMANLY template](assets/HUMANLY-template.md) with `level: "unassessed"` until checks pass. Don't overwrite existing declarations.
4. For unrelated code work, do not initiate a broad standards audit.

## Check the applicable level

Humanly levels are cumulative. Record **Pass / Fail / Unknown / N/A** for each applicable requirement, with reproducible evidence. Unknown never means Pass. Explain N/A.

| Level | Required evidence |
| --- | --- |
| H0: Agent Only | H1 not demonstrated; no verified complete human workflow. Descriptive, not an endorsement. |
| H1: Human Access | Core tasks usable without an agent, discoverable manual route, understandable errors, accessible controls (keyboard, labels, focus, assistive technology as relevant). |
| H2: Human Control | H1 plus visible agent actions/status/results; informed approvals for consequential actions or explicitly scoped prior authorization; feasible intervention; honest handling of failures and irreversible effects. |
| H3: Human Ownership | H2 plus durable understandable important-action history; portable user-data export; discoverable deletion process and stated retention limitations. |

Core tasks depend on the product and audience; optional AI-only enhancements need not have manual equivalents. Don't require pointless approvals for harmless actions, or claim reversibility where none exists.

## Make targeted changes

- Prefer familiar screens, plain language, and existing controls over a separate AI dashboard.
- Protect manual functionality during agent-first development. Don't make agent availability a prerequisite for core work.
- Display pending/running/completed/failed/stopped states and what actually changed; never mark queued work as completed.
- Preview recipients, charges, access changes, or records affected before consequential operations.
- Support cancellation of future or pending work where feasible; disclose effects already completed. Offer undo only when real undo exists.
- Preserve authorization and privacy; avoid exposing other people's data in history or export.
- Fix failed controls narrowly, then test affected flows.

## Verify, document, and report

1. Exercise core workflows without AI. For relevant interfaces, test keyboard interaction, clear errors, and recovery. For H2/H3 test action status, approvals, interruption, history, export, and deletion.
2. Run project tests when possible. Optionally run `python scripts/check_declaration.py <repo-root>` for **text-only** checks, not compliance certification.
3. Update `HUMANLY.md` only with demonstrated evidence, real scope/date, known gaps, and honest level. Do not silently upgrade or downgrade an existing claim.
4. Report scope, claimed level, checks (pass/fail/unknown), changed files, tests, and remaining gaps concisely. If only scaffolding was requested, report `unassessed` and next steps.

## Agent integrations

For broader agent reminders, append or adapt the [AGENTS.md snippet](assets/AGENTS-snippet.md) without overwriting existing instructions. Agents should read `HUMANLY.md` before relevant changes; `AGENTS.md` improves discoverability but is not a guarantee of enforcement. The standard and this skill work without external connectors.
