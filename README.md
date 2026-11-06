# Skills

Reusable AI-agent skills maintained as independent, portable directories.

## Skill catalog

| Skill | Purpose |
| --- | --- |
| [Comment Resolution](skills/comment-resolution/SKILL.md) | Resolve agency comments against a report, prepare dispositions and report-ready edits, and validate a comment resolution matrix. |

## Repository layout

Each skill lives in `skills/<skill-name>/` and has a `SKILL.md` with YAML frontmatter (`name` and `description`). Optional supporting content belongs in `references/`, `scripts/`, or `assets/` inside that skill's directory.

```text
skills/
├── README.md
└── skills/
    └── comment-resolution/
        ├── SKILL.md
        └── references/
            ├── example.md
            └── quality-checklist.md
```

## Use a skill

Copy the desired `skills/<skill-name>/` directory into the skills directory supported by your AI agent, or provide its `SKILL.md` as instructions. Installation and automatic discovery depend on the host product; a GitHub URL alone does not install a skill in every ChatGPT client.

For the Comment Resolution skill, provide the original Excel comment resolution matrix and the matching report PDF. The skill describes a workflow, not an executable workbook engine.

## Contributing a new skill

1. Add `skills/<kebab-case-name>/SKILL.md` with `name` and `description` frontmatter.
2. Put optional examples and checklists in `references/`; executable helpers in `scripts/`; static resources in `assets/`.
3. Update the catalog above.
4. Validate paths, links, instructions, and sample inputs. Never commit agency-sensitive documents, credentials, or private data.

Keep each skill self-contained. Shared business logic and schemas should remain in their owning project rather than be duplicated here.

## Disclaimer

These are operational instructions, not official NTIA policy or approved agency determinations. Technical and regulatory decisions require verification against authoritative sources and applicable approval processes.
