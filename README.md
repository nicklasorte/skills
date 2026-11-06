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

## Install in GitHub Copilot (VS Code)

These are agent instruction skills, not VS Code extensions. Use a recent version of VS Code with GitHub Copilot Chat and agent skills support. Your organization's settings may restrict agent mode or custom skills.

### Option A: Install for one repository (recommended for teams)

1. Clone or download this repository: `git clone https://github.com/nicklasorte/skills.git`.
2. In the **project where you use Copilot**, create a `.github/skills/` directory.
3. Copy each desired **entire skill folder** from this repository's `skills/` directory into that project's `.github/skills/` directory. Keep `SKILL.md` at the root of each skill folder and include any `references/` files.
4. Open the project in VS Code and use GitHub Copilot Chat in **Agent** mode. Commit the copied skill folders to share them with collaborators on that project.

Example resulting project layout:

```text
your-project/
└── .github/
    └── skills/
        ├── ntia-review/
        │   └── SKILL.md
        ├── ntia-meeting/
        │   └── SKILL.md
        └── comment-resolution/
            ├── SKILL.md
            └── references/
                ├── example.md
                └── quality-checklist.md
```

### Option B: Install for your own Copilot sessions

Copy desired folders into the personal Copilot skills directory, `~/.copilot/skills/`, where supported by your VS Code/Copilot version. On Windows, `~` refers to your user home directory. A personal installation does not change a project repository.

For example, after cloning on macOS or Linux:

```bash
mkdir -p ~/.copilot/skills
cp -R skills/ntia-review ~/.copilot/skills/
cp -R skills/ntia-meeting ~/.copilot/skills/
```

On Windows PowerShell, from the cloned repository:

```powershell
New-Item -ItemType Directory -Force "$HOME/.copilot/skills" | Out-Null
Copy-Item -Recurse -Force "skills/ntia-review" "$HOME/.copilot/skills/"
Copy-Item -Recurse -Force "skills/ntia-meeting" "$HOME/.copilot/skills/"
```

### Verify the installation

1. Open the target project in VS Code and check **Chat: Open Customizations** in the Command Palette, if available in your version. Look for the installed skills.
2. Start a new Copilot Chat session in Agent mode.
3. Try: **“Use the ntia-review skill to review this sample report. Identify unsupported claims and return an issue register.”**
4. Check that Copilot follows the skill's workflow. If it does not, confirm the folder path, the `SKILL.md` YAML frontmatter, your Copilot version, and your organization's agent-skill settings.

Skill selection is model- and product-dependent. Installing a skill makes its instructions available in supported environments; it does not guarantee automatic invocation on every request. You can ask for a skill by name.

### Limitations and information handling

- The public skills are instruction-based. They do not include proprietary NTIA data, internal engines, or all original suite validation scripts.
- Some skills need source documents, spreadsheets, PDFs, or MATLAB outputs supplied during the task.
- Copilot cannot claim a validator ran unless it actually ran. Skill outputs do not constitute official agency clearance.
- Only use Copilot with agency data when permitted by your organization's AI and information-handling policies.
- See [GitHub's agent skills documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) for current product support and installation locations.

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
