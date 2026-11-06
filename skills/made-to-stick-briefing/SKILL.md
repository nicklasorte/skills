---
name: "made-to-stick-briefing"
description: "Turns technical analysis into briefings non-experts understand, remember, and act on, using the Heath brothers' Made to Stick principles (SUCCESs). Use this whenever the user says \"run [topic] through Made to Stick,\" \"make this stick,\" \"make this less technical,\" \"Dan Heath would…,\" or asks to rework slides or talking points for executives, leadership, decision-makers, or any non-technical audience. Also use it for critiques of an existing deck's clarity or memorability, for turning big numbers into relatable comparisons, or for planning a story-driven briefing, even if the book isn't named. To build the NTIA-template PowerPoint itself, use ntia-talking-deck. For shaping a personal story, use storyworthy-talks."
---

# Made to Stick Briefing

Turns a technical topic (analysis results, studies, models, algorithms, policy findings) into a briefing that a non-expert can repeat accurately the next day.

The reason this needs a structured process: analysts suffer from the Curse of Knowledge. They can't un-know the background that makes their own explanation feel clear. The process forces the message through checks an expert would otherwise skip, while guarding the one thing stickiness must never cost, which is accuracy.

## Files

- `references/framework.md`: the five working tools (canvas, diagnostic grid, pattern decision guide, slide checklist, outsider test). Read it on every run.
- `references/playbook.md`: the full book catalog: every example with page reference, lesson, and how to borrow it, plus guardrails (Section 12). Read the relevant sections when choosing patterns or citing the book.
- `assets/sticky-brief-canvas.md`: blank canvas to fill in and hand back.

## Workflow

Follow these steps in order. Work from the user's source material (project files, papers, slides). The user's documents are the authority on facts; the book is the authority on technique.

### 1. Intake
Read the source material. Identify the audience, the decision wanted, and the core finding in the analyst's own words. If the audience isn't stated, ask. Audience changes everything.

### 2. Fill the Sticky Brief canvas
Use `references/framework.md` Section 1. Fill every box from the source. Where the source can't support a box, write **GAP** and list it as an open question. Never invent stakes, examples, or numbers to fill a box. The book's Halloween-candy and Kidney Heist examples are the warning: false ideas stick too.

### 3. Diagnose
If there's an existing draft (deck, memo, talking points), run it through the diagnostic grid (framework Section 2) and score it with the rubric (playbook Section 9). Name the broken stages, with evidence. If there's no draft, diagnose the analyst's likely default framing instead.

### 4. Choose patterns
For each broken stage, pick 1–2 moves from the pattern decision guide (framework Section 3). Tie each to its book source (playbook Section 4). Prefer patterns that use real, named elements from the source.

### 5. Propose a sequence
Lay out the briefing using the sequence template (playbook Section 10). Tag every slide with its principle and pattern. Put method detail, equations, and full tables in backup.

### 6. Accuracy check
Before presenting the plan:
- Trace every factual claim to the source.
- Recompute every derived number (ratios, time conversions, counts) and show the arithmetic.
- Mark anything illustrative (invented examples, sample values, schematic curves) as "Illustration."
- State pending items (placeholder thresholds, unverified data) on the relevant slide.
- Respect sensitivities, such as site-coordinate precision for wider audiences.

If a sticky framing conflicts with the analysis, the analysis wins. Find a different true framing. A true surprise is usually available, and it is often more surprising than the planned framing.

### 7. Confirmation gate
Present the plan using the output format below and **stop**. Build slides only after the user approves. The user wants to steer framing before effort goes into production.

### 8. Build and triage (after approval)
When building, run every slide through the slide checklist (framework Section 4). Move 0–1 scorers to backup. Recommend the outsider test (framework Section 5) before the briefing goes to its real audience.

## Output format for a plan

```
## Core
[One sentence]

## Audience diagnosis
[Grid: stage, OK/WEAK/BROKEN, evidence]  — before score: S_ U_ C_ C_ E_ S_

## Canvas
[Filled canvas; GAPs listed]

## Proposed sequence
| # | Slide | Principle | Pattern | Source / illustration |

## Accuracy check
[Claims traced; arithmetic shown; illustrations and pending items listed]

## Projected score
S_ U_ C_ C_ E_ S_

## Open questions
[GAPs and choices that need the user]
```

## Project-specific rules

If the project has standing rules or constraints (in project files, prior decisions, or the user's instructions), apply them during the accuracy check. When a rule changes what can be shown, follow the rule rather than the pattern.

## Coordinated skill handoffs

Primary owner for briefing message and memorability, including critique without slide production. For an NTIA PowerPoint deliverable, ntia-talking-deck owns the file and slide-design owns visuals. Preserve this skill's approval gate and factual accuracy checks.

For a multi-skill request, follow the repository `skill-router` and `AGENTS.md` when available. Keep one primary owner, preserve source evidence and outstanding decisions, and avoid duplicate work. A handoff is an instruction for the host agent to consider another skill, not a direct executable call. Do not bypass this skill's own required approval, template, data-handling, or verification gates.
