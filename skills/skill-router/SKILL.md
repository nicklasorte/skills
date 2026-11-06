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
