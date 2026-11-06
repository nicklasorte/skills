# Coordinated skills — Copilot instructions

Use the skill-router workflow in `.github/skills/skill-router/SKILL.md` (or `skills/skill-router/SKILL.md` when working in this repository) when a request spans more than one specialist skill. For a single-purpose request, use the matching specialist directly.

## Operating rules
1. Read only the relevant skill instructions. Select **one primary owner** per request; add specialists only for distinct evidence or deliverables.
2. Route by user intent, not keywords alone. Preserve the requested scope; do not start a filing, meeting, or readiness assessment merely because a related skill exists.
3. Specialists produce **handoff recommendations and artifacts**, not executable calls. The Copilot agent decides whether to load the next skill. Do not claim a skill ran unless its workflow was actually performed.
4. Maintain source version, real source locators, assumptions, unresolved issues, and decision status across handoffs. Use `contracts/handoff.schema.json` for machine-readable handoffs when useful; prose handoffs are fine for small tasks.
5. Avoid cycles: one orchestrator owns routing; a specialist may recommend a next skill but cannot recursively dispatch. Track completed skills and do not repeat the same skill for unchanged inputs.
6. Apply the domain-specific style owner: Google Developer Writing Style for general prose, STE100 Writing for requested controlled language (STE wins on conflicts), and NTIA-specific brand/filing conventions for applicable products. Apply NTIA Quality Gate only when explicitly requested or required by an approved project workflow. A gate is advisory, never agency clearance.
7. Fail closed on unsupported conclusions, not on unrelated work. No invented agency positions, results, decisions, citations, or approvals.
8. Keep source data in authorized locations. Never upload nonpublic agency material to this public repository.

## Specialist ownership and composition
- **NTIA talking deck:** `ntia-talking-deck` owns the PowerPoint; `made-to-stick-briefing` supports message; `slide-design` supports visuals; Google style supports wording. Preserve template and approval gates.
- **Visuals:** `slide-design` owns standalone charts, tables, maps, figures, and slide layout. Use `matlab-builtin-first` only if MATLAB code is produced or changed.
- **MATLAB:** `matlab-builtin-first` owns code; `matlab2paper` owns evidence traceability from code and outputs to report text.
- **Training:** `oxford-tutorial-lessons` owns the weekly lesson/mentor format. Keep mentor-only reference solutions out of learner materials.
- **Controlled language:** `ste100-writing` owns explicit ASD-STE100 writing/audits; it overrides general writing style on conflicting rules.
- **Regulatory and review:** preserve existing NTIA Policy, Filing, Review, Meeting, Comment Resolution, and Quality Gate routing.
- Follow the full routing matrix in `skills/skill-router/SKILL.md`; don't infer permission to generate additional artifacts or run tools from a skill's optional dependencies.

## Installation
Copy this file to the **root of the coworker's working project** as `AGENTS.md` if the Copilot environment supports it. Also copy the required skill folders into that project's `.github/skills/`. Instructions in this repository do not automatically govern unrelated projects.
