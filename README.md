# Skills

Portable, independent AI-agent skills for spectrum engineering, regulatory writing, review, and meeting workflows.

## Catalog

| Skill | Use |
| --- | --- |
| [Comment Resolution](skills/comment-resolution/SKILL.md) | Agency comment adjudication and report-ready changes |
| [NTIA Policy](skills/ntia-policy/SKILL.md) | Policy and regulatory research and drafting |
| [NTIA-Review](skills/ntia-review/SKILL.md) | Evidence-traceable technical and policy reviews |
| [NTIA-Meeting](skills/ntia-meeting/SKILL.md) | Minutes, decisions, actions, and handoffs |
| [NTIA Quality Gate](skills/ntia-quality-gate/SKILL.md) | Advisory readiness checks |
| [NTIA-Filing](skills/ntia-filing/SKILL.md) | FCC filing preparation and validation |
| [MATLAB2Paper](skills/matlab2paper/SKILL.md) | Reproducible analysis-to-paper traceability |

## Structure

Each skill lives at `skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter. Optional `references/`, `scripts/`, and `assets/` belong within the corresponding skill directory. Keep each skill independent and avoid duplicating project-owned code.

## Installation and use

Copy the desired skill directory into the skills location supported by your AI agent, or supply its `SKILL.md` as instructions. A GitHub URL does not automatically install skills in every ChatGPT environment.

Provide the source documents, exact versions, and task-specific evidence when using these workflows. Outputs are drafts or advisory assessments, not institutional decisions.

## Publication status

- NTIA-Review, NTIA-Meeting, and NTIA Quality Gate are **public standalone adaptations** of existing installed workflows. They do not contain the original installed suite's schemas, scripts, or integration files.
- NTIA Policy, NTIA-Filing, and MATLAB2Paper are **initial public skill definitions** and should be extended and tested against approved examples before production use.
- Comment Resolution is a portable instruction workflow, not an executable workbook engine.

## Contributing

Add `skills/<kebab-case-name>/SKILL.md`, keep its dependencies documented, and update this catalog. Check instructions, links, and sample artifacts. Do not commit credentials, private documents, agency-sensitive material, or controlled technical data.

## Disclaimer

This is a personal collection of workflows, not an official NTIA publication or statement of agency policy. Follow applicable information-handling, review, and clearance requirements before distributing material.
