# Humanly declaration

> Template: replace placeholders, test the evidence, and remove this note before publishing.

```yaml
humanly:
  version: "0.3-draft"
  level: "unassessed" # Set H0, H1, H2, or H3 only after review
  scope: "[Product and features covered]"
  reviewed: "[YYYY-MM-DD]"
```

**Standard:** Humanly v0.3 draft  
**Human interface:** [Link to the UI or instructions]  
**Issues/contact:** [Link or email]

## H1 — Human Access

- **Core tasks without an AI agent:** [Describe tested workflow]
- **How to find the manual path:** [Link or directions]
- **Accessible interaction:** [Keyboard use, labels, focus, errors, assistive technology and known gaps]

## H2 — Human Control

- **Agent action status:** [Where users see actions and outcomes]
- **Approvals:** [Which consequential actions need informed approval or scoped preauthorization]
- **Intervention:** [How to stop/pause/revoke future work]
- **Completed effects:** [What cannot be undone and how it is explained]

## H3 — Human Ownership

- **Action history:** [Location and what is recorded]
- **Data export:** [UI, format, and scope]
- **Data deletion:** [Process, timing, and retention limitations]

## Known limitations

[Explain gaps, exclusions, and N/A findings. Never hide uncertain requirements.]

## Verification

Only check items you have **actually verified** for the declared scope and level.

- [ ] Core tasks work with AI unavailable. (H1)
- [ ] Manual controls are usable with keyboard, labels, and understandable errors. (H1)
- [ ] Agent actions, states, and outcomes are visible. (H2)
- [ ] Consequential actions require informed approval or an explicit scoped policy. (H2)
- [ ] Users can intervene in pending/future work or limits are explained. (H2)
- [ ] Important completed and failed actions can be reviewed later. (H3)
- [ ] User data can be exported in a usable format. (H3)
- [ ] Data deletion or request process can be found and used. (H3)

**Assessed by:** [Team or maintainer]  
**Evidence / tests:** [URLs or steps]

---

H1 requires both H1 checks; H2 requires H1 and H2 checks; H3 requires all applicable checks. H0 means H1 has not been demonstrated. This is a self-assessment, not independent certification.
