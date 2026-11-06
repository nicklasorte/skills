---
name: matlab2paper
description: Turn MATLAB spectrum studies into reproducible technical papers. Use for matlab2paper tasks with source-grounded review and drafting.
---
# MATLAB2Paper

## Scope and intake
Identify MATLAB release, code revision, input data provenance, analysis question, scenario definitions, and intended audience. Never assume code or output has been executed.

## Method
Trace each reported result to code, configuration, units, criteria, assumptions, propagation model, antenna models, simulation count, random seed, uncertainty, and output artifact. Validate plots and tables against actual output; check reproducibility and numerical consistency. Flag missing dependencies and unsupported interpretations.

## Deliverables
Produce a paper outline or manuscript with methods, assumptions, results, limitations, reproducibility appendix, and traceability table. Do not fabricate runs, figures, or statistics.

## Quality and safety gates
- Cite exact accessible source versions and locations for material claims; distinguish facts, assumptions, proposals, and unknowns.
- No internal documents, agency-specific positions, source code, or restricted data are bundled in this public skill.
- Missing evidence blocks only unsupported conclusions; continue independent draft work with explicit gaps.
- Use NTIA-Review for cross-document review and NTIA Quality Gate for an explicit advisory readiness assessment when those skills are available.
- Human review and applicable institutional clearance remain required; this skill does not authorize publication or filing.

## Coordinated skill handoffs
Primary for MATLAB-to-manuscript traceability. Recommend ntia-review for independent cross-document review; never invent execution results.

For multi-skill requests, follow the central `skill-router` workflow and repository `AGENTS.md` instructions. The primary skill retains task ownership. Handoffs may use `contracts/handoff.schema.json` and findings may use `contracts/issue.schema.json`; these are optional portable formats, not official agency records. Include real source locations, version, unresolved issues, and already completed skills. A handoff is a recommendation to the host agent, not an executable skill call. Avoid circular calls and duplicate work.
