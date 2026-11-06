# Coordinated skills — Copilot instructions

Use the skill-router workflow in `.github/skills/skill-router/SKILL.md` (or `skills/skill-router/SKILL.md` when working in this repository) when a request spans more than one specialist skill. For a single-purpose request, use the matching specialist directly.

## Operating rules
1. Read only the relevant skill instructions. Select **one primary owner** per request; add specialists only for distinct evidence or deliverables.
2. Route by user intent, not keywords alone. Preserve the requested scope; do not start a filing, meeting, or readiness assessment merely because a related skill exists.
3. Specialists produce **handoff recommendations and artifacts**, not executable calls. The Copilot agent decides whether to load the next skill. Do not claim a skill ran unless its workflow was actually performed.
4. Maintain source version, real source locators, assumptions, unresolved issues, and decision status across handoffs. Use `contracts/handoff.schema.json` for machine-readable handoffs when useful; prose handoffs are fine for small tasks.
5. Avoid cycles: one orchestrator owns routing; a specialist may recommend a next skill but cannot recursively dispatch. Track completed skills and do not repeat the same skill for unchanged inputs.
6. Use Google Developer Writing Style only after substantive drafting/review; apply NTIA Quality Gate only when explicitly requested or required by an approved project workflow. A gate is advisory, never agency clearance.
7. Fail closed on unsupported conclusions, not on unrelated work. No invented agency positions, results, decisions, citations, or approvals.
8. Keep source data in authorized locations. Never upload nonpublic agency material to this public repository.

## Installation
Copy this file to the **root of the coworker's working project** as `AGENTS.md` if the Copilot environment supports it. Also copy the required skill folders into that project's `.github/skills/`. Instructions in this repository do not automatically govern unrelated projects.
