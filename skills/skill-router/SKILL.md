---
name: skill-router
description: Coordinate multiple installed NTIA and spectrum skills using one primary task owner, conditional handoffs, shared evidence, and no duplicate work. Use for cross-skill workflows, not isolated tasks.
---
# Skill Router

## Intake
Identify the user's decision or deliverable, available sources, authorized actions, and constraints. Select exactly one primary skill; include only specialists whose unique capabilities are needed. Never widen the task without permission.

## Routing table
| Intent | Primary | Conditional specialist |
| --- | --- | --- |
| Policy position, rule analysis | ntia-policy | ntia-filing when an FCC filing is requested; ntia-review for substantive cross-document review |
| FCC filing | ntia-filing | ntia-policy for legal/policy questions; ntia-review for requested review |
| Technical or multi-document review | ntia-review | comment-resolution for agency matrix; matlab2paper for analysis-to-report traceability |
| Meeting package | ntia-meeting | ntia-review for a distinct unresolved review task |
| Agency comment matrix | comment-resolution | ntia-review for cross-cutting technical findings |
| MATLAB analysis to paper | matlab2paper | ntia-review for requested independent review |
| Editing/style | google-developer-writing-style | domain specialist only if substantive verification is requested |
| Explicit readiness assessment | ntia-quality-gate | relevant domain specialist for evidence gathering |

## Expanded routing: communication, code, and learning

| Intent | Primary owner | Conditional supporting skills |
| --- | --- | --- |
| Build NTIA PowerPoint talking deck | ntia-talking-deck | made-to-stick-briefing for message, slide-design for visuals, google-developer-writing-style for prose, and authorized PPTX tooling for file production |
| Critique or plan a memorable briefing without building slides | made-to-stick-briefing | slide-design only when evaluating actual visuals |
| Design/revise chart, figure, map, table, diagram, or slide visuals | slide-design | matlab-builtin-first only when producing MATLAB plotting code; ntia-talking-deck when building an NTIA deck |
| Produce or modify MATLAB code | matlab-builtin-first | matlab2paper only for requested code-to-report traceability |
| Convert MATLAB results into a technical paper | matlab2paper | matlab-builtin-first only if code must be written, changed, or run |
| Design weekly technical lessons, learner assignments, or mentor guides | oxford-tutorial-lessons | matlab-builtin-first only when producing or testing MATLAB code; google-developer-writing-style for prose |
| Write or audit ASD-STE100 controlled language | ste100-writing | google-developer-writing-style for nonconflicting formatting only |
| General technical writing or copyediting | google-developer-writing-style | ste100-writing only when controlled language is explicitly requested or necessary for the specified procedure |

## Ownership and precedence

- **Deliverable owner wins:** ntia-talking-deck owns the deck file and template mechanics; made-to-stick-briefing owns briefing message and accuracy of memorable framing; slide-design owns chart and visual presentation; matlab-builtin-first owns MATLAB code choices; matlab2paper owns code-to-paper traceability; oxford-tutorial-lessons owns the training format; ste100-writing owns controlled-language constraints.
- **Specific rules override general style:** STE100 governs requested controlled-language text over Google style. NTIA template/brand and filing conventions override generic visual or writing preferences where they apply. Substantive technical and legal accuracy outrank all style rules.
- **Don't widen a request:** a deck critique is not permission to build a PPTX; a figure request is not a deck request; code review is not automatically a paper rewrite; training design is not authorization to run MATLAB.
- **Preserve specialist gates:** do not bypass a skill's required template, source clearance, confirmation, dependency, or verification step. If a required asset or approved environment is missing, report the blocker; do not invent a substitute.
- **No implicit compliance certification:** applying STE-inspired rules is not proof of ASD-STE100 compliance; quality-gate readiness is not official NTIA clearance. Never claim MATLAB was run without execution evidence.
- **No circular chains:** specialist suggestions return to the primary owner for reconciliation. A specialist may not independently trigger another specialist and then route back to itself.

## Execution protocol
1. Write a brief plan: primary owner, optional specialists, artifacts, and stop condition.
2. Execute the primary workflow against actual accessible sources.
3. Create a handoff only for a **specific remaining task**. Include exact source/version, source locators, accepted findings, unknowns, requested output, and prior completed skills.
4. Check the handoff for duplicate work, circular routing, unsupported assumptions, and unnecessary external actions.
5. Invoke the next specialist **only when supported by the host agent** and needed for the user's request. Otherwise provide the handoff as a recommendation; never pretend a call occurred.
6. Reconcile outputs under the primary owner. Keep one issue register and preserve conflicting findings rather than silently overriding.
7. Apply editorial polish after technical substance. A quality gate is a distinct, advisory assessment, not an automatic approval.
8. Stop when requested outputs are complete, evidence is insufficient for further conclusions, or a human decision is required.

## Shared contract
Use `contracts/handoff.schema.json` for reusable JSON handoffs. This is a portable exchange format, not a replacement for project-owned records or an official NTIA form. A lightweight equivalent is acceptable for a short task.

## Boundaries
No direct skill-to-skill execution, background work, publishing, filing, email, or repository mutation is authorized by this skill alone. Follow applicable security and institutional clearance rules.
