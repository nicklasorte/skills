# Skills

Portable, independent AI-agent skills for spectrum engineering, regulatory writing, review, and meeting workflows.

## Catalog

| Skill | Use |
| --- | --- |
| [Comment Resolution](skills/comment-resolution/SKILL.md) | Agency comment adjudication and report-ready changes |
| [NTIA Policy](skills/ntia-policy/SKILL.md) | Policy briefs, decision memos, regulation summaries, and rule reviews |
| [NTIA-Review](skills/ntia-review/SKILL.md) | Evidence-traceable technical and policy reviews |
| [NTIA-Meeting](skills/ntia-meeting/SKILL.md) | Minutes, decisions, actions, and handoffs |
| [NTIA Quality Gate](skills/ntia-quality-gate/SKILL.md) | Advisory readiness checks |
| [NTIA-Filing](skills/ntia-filing/SKILL.md) | FCC filing drafting, review, and validation in NTIA's voice |
| [MATLAB2Paper](skills/matlab2paper/SKILL.md) | Reproducible analysis-to-paper traceability |
| [Google Developer Writing Style](skills/google-developer-writing-style/SKILL.md) | Google developer documentation style for technical and regulatory writing |
| [Skill Router](skills/skill-router/SKILL.md) | Coordinate conditional handoffs across specialist skills |
| [NTIA Talking Deck](skills/ntia-talking-deck/SKILL.md) | Short talking decks for non-technical audiences |
| [Slide Design](skills/slide-design/SKILL.md) | Slide, chart, map, and table design rules for briefings |
| [Made to Stick Briefing](skills/made-to-stick-briefing/SKILL.md) | Turn technical analysis into briefings non-experts remember |
| [MATLAB Built-in First](skills/matlab-builtin-first/SKILL.md) | Prefer verified built-in MATLAB functions over custom code |
| [Oxford Tutorial Lessons](skills/oxford-tutorial-lessons/SKILL.md) | Weekly question, short paper, and Socratic review format |
| [STE100 Writing](skills/ste100-writing/SKILL.md) | Write and audit ASD-STE100 Simplified Technical English |

The catalog contains **15 skills**: 14 specialists and one router. Install only the specialists relevant to your work.

## Structure

Each skill lives at `skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter. Optional `references/`, `scripts/`, and `assets/` belong within the corresponding skill directory. Keep each skill independent and avoid duplicating project-owned code.

## Coordinated multi-skill workflows

This repository supports **one primary task owner with conditional specialist handoffs**. See [Skill Router](skills/skill-router/SKILL.md) and [AGENTS.md](AGENTS.md). Portable data formats are in [handoff.schema.json](contracts/handoff.schema.json) and [issue.schema.json](contracts/issue.schema.json).

A skill's handoff instruction is **not an executable call**. The Copilot agent must choose and run the relevant specialist in a supported environment. Do not assume a quality gate, filing, or external action ran automatically.

### Routing and skill composition

| User request | Primary skill | Supporting skills only when needed |
| --- | --- | --- |
| NTIA policy analysis or memo | NTIA Policy | NTIA-Review; NTIA-Filing for a requested filing |
| FCC filing | NTIA-Filing | NTIA Policy; NTIA-Review |
| Multi-document technical review | NTIA-Review | Comment Resolution; MATLAB2Paper |
| Meeting minutes and handoff | NTIA-Meeting | NTIA-Review for a separate review task |
| Agency comment matrix | Comment Resolution | NTIA-Review for cross-cutting findings |
| MATLAB code or plot implementation | MATLAB Built-in First | MATLAB2Paper for requested report traceability |
| MATLAB results into a technical paper | MATLAB2Paper | MATLAB Built-in First for code changes or execution |
| NTIA PowerPoint talking deck | NTIA Talking Deck | Made to Stick Briefing, Slide Design, Google Developer Writing Style |
| Briefing story or deck-message critique | Made to Stick Briefing | Slide Design for existing visuals |
| Figure, chart, table, map, or layout | Slide Design | MATLAB Built-in First for MATLAB plotting code |
| Weekly technical lesson or mentor guide | Oxford Tutorial Lessons | MATLAB Built-in First for code; Google Developer Writing Style for prose |
| Explicit ASD-STE100 writing or audit | STE100 Writing | Google Developer Writing Style for nonconflicting formatting |
| General technical editing | Google Developer Writing Style | Domain owner for requested substantive checks |
| Explicit readiness assessment | NTIA Quality Gate | Relevant specialist for evidence only |

**Ownership:** the skill producing the requested artifact owns the workflow. Specialist contributions return to that owner; specialists do not recursively dispatch each other. Preserve source versions, decision status, and unresolved issues across handoffs.

**Precedence:** technical and regulatory accuracy, source-handling rules, and explicit user scope outrank style. STE100 governs requested controlled language over general Google style. NTIA Talking Deck governs NTIA deck template mechanics, Made to Stick governs message, and Slide Design governs visuals. Preserve the talking-deck template and approval gates. Do not claim MATLAB execution or official standards compliance without evidence.

**Host limitations:** some specialists reference optional assets or tools (such as the NTIA PowerPoint template, MATLAB toolboxes, or approved source files). Installing their `SKILL.md` does not install those dependencies. Follow the individual skill's prerequisites and stop conditions.

### Install coordination in a coworker's project

1. Install desired specialist folders under the **target project's** `.github/skills/` as described below.
2. Also copy `skills/skill-router/` into that project's `.github/skills/`.
3. Copy this repository's root `AGENTS.md` to the **root of the target project**. If that project already has an `AGENTS.md`, merge the routing instructions rather than overwrite existing rules.
4. The JSON contracts are optional for ordinary conversational tasks. Copy `contracts/` into the project only when structured handoff files are needed, and adjust contract paths if the project uses a different layout.
5. For deck, chart, MATLAB, or tutorial workflows, copy the complete skill directories including their `references/` and `assets/` files; supply any separately required template binary or approved runtime in the target environment.
6. Open Copilot Chat in Agent mode and try: **“Use the skill-router to review this technical report, use MATLAB2Paper only if code-to-report traceability is needed, and return one consolidated issue register.”**

Project instructions must be discoverable by the coworker's Copilot environment. Simply cloning this skills repository does not install its instructions into another project. Confirm actual skill loading and results; behavior varies by product/version.

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

### Multi-skill smoke tests

After installation, try these with fictional or approved public inputs:

- **NTIA deck:** “Plan a 5-slide NTIA talking deck from this public memo; use Made to Stick for message and Slide Design for visuals.” Expect the required template and confirmation checks before a PPTX is built.
- **MATLAB report:** “Trace this sample MATLAB function and its supplied outputs into a methods section.” Expect MATLAB2Paper ownership; use MATLAB Built-in First only if code must change.
- **Technical training:** “Draft a week-one Oxford tutorial question and learner/mentor package.” Expect learner and mentor material to remain separate.
- **Controlled language:** “Audit this procedure against STE100.” Expect STE100 to govern wording, without claiming official certification.
- **Review:** “Review this sample technical memo and return one issue register.” Expect NTIA-Review, not an automatic filing or quality gate.

## Publication status

- NTIA-Review, NTIA-Meeting, and NTIA Quality Gate are **public standalone adaptations** of existing installed workflows. They do not contain the original installed suite's schemas, scripts, or integration files.
- NTIA Policy, NTIA-Filing, and MATLAB2Paper are **initial public skill definitions** and should be extended and tested against approved examples before production use.
- Comment Resolution is a portable instruction workflow, not an executable workbook engine.

## Contributing

Add `skills/<kebab-case-name>/SKILL.md`, keep its dependencies documented, and update this catalog. Check instructions, links, and sample artifacts. Do not commit credentials, private documents, agency-sensitive material, or controlled technical data.

## Disclaimer

This is a personal collection of workflows, not an official NTIA publication or statement of agency policy. Follow applicable information-handling, review, and clearance requirements before distributing material.
