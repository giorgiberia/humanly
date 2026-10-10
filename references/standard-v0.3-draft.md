# Humanly

**A small, practical standard for software that works with AI agents without leaving people behind.**

**Status:** Proposed v0.3 (draft; not independently certified)  
**Brand:** Humanly  
**Principle:** Build for agents. Keep humans capable, informed, and in control.

AI agents can make software faster and easier to use. They should not become the only way to use it. A Humanly product keeps a usable path for people, shows what automation is doing, and gives people appropriate control over the outcome.

## Start here

1. **Build the human path.** A person should be able to complete the product's core tasks without asking an AI agent to do them.
2. **Choose an honest level.** Use the H0-H3 checklist below. Each level includes the requirements of the levels below it.
3. **Publish a `HUMANLY.md` file.** Put it in the repository root, describe what works, and link to real controls or documentation.
4. **Test it yourself.** Complete the checks without an AI agent before claiming a level.

You do **not** need a new framework, certification service, separate app, or special AI integration to adopt this standard.

## Humanly levels

| Level | Name | Minimum requirements |
| --- | --- | --- |
| **H0** | Agent Only | No complete human-operated path is provided, or H1 has not been demonstrated. |
| **H1** | Human Access | People can complete core tasks without an agent, using a usable and accessible interface. |
| **H2** | Human Control | H1, plus visible automation, meaningful approval for consequential actions, and the ability to intervene where technically possible. |
| **H3** | Human Ownership | H2, plus a useful action history, portable data export, and a clear, usable deletion process. |

**Levels are cumulative.** Claim the highest level for which *every* applicable requirement passes. H0 is a descriptive starting point, not a quality endorsement.

## Requirements

### H1 - Access without an agent

A product claiming H1 **must**:

- Provide a documented, working way to complete each **core task** manually. Core tasks are the essential user-facing activities the product promises; optional AI-specific features do not need a manual equivalent.
- Let users view the required information, submit actions, understand outcomes, and recover from ordinary errors without depending on an agent.
- Make the human path discoverable. Do not hide it behind an AI chat interface or require an AI account to reach it.
- Use an interface appropriate for its intended audience. A command-line interface may suit a developer tool; a consumer app normally needs an understandable graphical interface.
- Support basic accessibility: keyboard use, meaningful labels, visible focus, readable contrast, clear errors, and assistive technology where applicable. **WCAG 2.2 AA** is a recommended target for web interfaces, not an automatic claim of certification.

**Example:** Someone can create, edit, and download a report from the product UI even when AI features are turned off.

### H2 - See and control automation

A product claiming H2 **must** also:

- Clearly distinguish actions taken by a person from actions taken by an agent.
- Show the agent's current state (such as **waiting, running, completed, failed, stopped**) and the concrete action or result in plain language.
- Request explicit confirmation **before consequential actions**, such as sending external messages, spending money, deleting data, or changing permissions, unless the user has knowingly configured a specific, limited approval policy.
- Let users stop or pause pending work and change or revoke future agent permissions where technically possible. Explain when an action already completed cannot be undone.
- Make failures visible and offer a manual path to continue or recover.

**Example:** Before an agent emails a customer, the user can inspect the recipient and message, approve sending, or cancel it.

### H3 - History and data ownership

A product claiming H3 **must** also:

- Provide a durable, understandable history of important agent actions, including what happened, when, whether it succeeded, and what was changed. Protect secrets and other users' private data.
- Let users export their own relevant data in a documented, widely usable format, such as CSV or JSON.
- Offer a discoverable way to delete user-controlled data or request its deletion. Explain the scope, timing, and legally required retention exceptions.
- Let users find their history, export, and deletion controls without asking an agent.

**Example:** A user can review recent automated edits, download their project data, and initiate account-data deletion from settings.

## Instructions for developers and coding agents

When designing or modifying a Humanly product:

1. **Identify the human workflow first.** For each new core feature, write down how a person will use it without AI.
2. **Reuse existing UI where possible.** Do not create duplicate screens solely to meet this standard.
3. **Keep controls obvious.** Use clear labels such as *Review*, *Approve*, *Cancel*, *Undo* (only if truly possible), and *Export*.
4. **Make agent work understandable.** Show intent, current status, outcomes, and errors. Avoid opaque messages like "The agent handled it."
5. **Protect consequential actions.** Preview recipients, affected records, charges, and permission changes before user confirmation.
6. **Preserve escape routes.** Never remove manual workflows or quietly expand an agent's authority as part of an unrelated feature.
7. **Test accessibility and recovery.** Include keyboard, screen-reader, failure, and agent-unavailable cases in normal QA.
8. **Update `HUMANLY.md` with the change.** If a feature weakens the declared level, lower the claim until it is fixed.

### Keep it simple

- Prefer a normal button and clear status text over a complicated agent-control dashboard.
- Add confirmation only where the consequences justify it; avoid interrupting harmless, reversible actions.
- A **Cancel** button must cancel pending work, not falsely suggest an already completed action has been reversed.
- If a requirement does not apply, say **N/A** and explain why. Do not silently skip it.
- Provide direct links to controls or docs as evidence; screenshots and long compliance reports are optional.

## Five-minute self-check

Use this before publishing or changing your declared Humanly level:

- [ ] **Manual task:** Complete a representative core task with AI disabled or unavailable. (H1)
- [ ] **Accessible task:** Do the same with keyboard-only controls; verify labels, focus, and error messages. (H1)
- [ ] **Visible action:** Trigger an agent task and verify that the action and state are understandable. (H2)
- [ ] **High-impact review:** Check that a consequential action needs informed approval or a clearly configured policy. (H2)
- [ ] **Intervention:** Stop pending agent work; verify that completed effects are described honestly. (H2)
- [ ] **History:** Find an important completed or failed agent action later. (H3)
- [ ] **Export:** Export usable user data without agent assistance. (H3)
- [ ] **Deletion:** Find and use, or initiate, the documented data-deletion process. (H3)

This is a **quick smoke test**, not proof of full accessibility, security, or legal compliance. Products should also run normal quality, privacy, and accessibility reviews.

## Declare support with `HUMANLY.md`

Place a file named `HUMANLY.md` in the repository root. Use the [included template](../assets/HUMANLY-template.md), which combines a short machine-readable declaration with simple human-readable evidence.

The declaration should say:

- **Version and level:** which draft or released standard it follows, and the level claimed.
- **Scope:** which app, platform, or feature set was assessed.
- **Evidence:** where to find manual access, agent controls, history, export, and deletion.
- **Exceptions:** any missing features, technical limits, or retention restrictions.
- **Last reviewed:** when someone last checked the claim.

A level is **self-assessed**, not awarded by this repository. Never present an untested declaration as independently certified. A product may describe separate levels for distinct products or surfaces, but it must clearly identify each scope and must not imply the highest claim covers everything.

## Terms

- **Agent:** Software acting on a user's behalf with some autonomy, including an AI assistant that can use tools or change state.
- **Core task:** An essential activity normally available to the product's intended users.
- **Consequential action:** An action with meaningful external, financial, privacy, security, or irreversible effects.
- **Manual path:** A human-usable workflow that does not depend on invoking an agent. Ordinary software services and automation are allowed.
- **Portable export:** Data in a documented format that is useful outside the product, not just a screenshot or a proprietary backup.

## Non-goals

This standard does not replace privacy law, accessibility standards, application security, or domain-specific safety rules. It does not require all agent actions to be reversible, or require a human to approve every harmless step. It is intended to make human access and control easy to discover, implement, and verify.

## Versioning and license

This document is a **proposal**, not an independently established or certified external standard. Humanly levels are self-assessed and must be supported by evidence for the declared scope. Changes that alter level requirements should receive a new standard version.

Licensed under Apache License 2.0 (see the repository `LICENSE`).
