---
name: comment-resolution
description: Resolve NTIA working-paper agency comments from an Excel matrix against a line-numbered report PDF, preserving source comments and producing evidence-grounded, report-ready resolutions.
---
# Comment Resolution

## Trigger
Use when asked to adjudicate, resolve, consolidate, or package agency comments on an NTIA working paper. This is the comment-resolution workflow within NTIA-Review, not a replacement for broader technical review or NTIA Quality Gate.

## Inputs
- Original Excel Comment Resolution Matrix (CRM), with original sheet names, formatting, and comments intact.
- Corresponding report PDF, preferably with visible printed line numbers; identify the exact report revision.
- Optional technical evidence, agency positions, rules, and prior dispositions.
- Optional user request for **report-integration mode**: a new, implementation-ready Excel CRM containing exact report text, rather than adjudication in the source CRM.

## Procedure
1. Inspect the workbook before editing. Identify columns by exact headers, not fixed indices. Preserve all input columns, original comments, suggested text, notes, sheets, and formatting.
2. Verify the report revision. For each row, anchor Section, Page, and *printed* Line to the report. Distinguish PDF viewer page from printed page. Do not invent an anchor. Capture sufficient paragraph context.
3. Separate agency concern (Agency Notes) from candidate wording (Agency Suggested Text Change). Suggested text is not automatically accepted. Consider WG Chain Comments when present.
4. Cluster duplicate or related comments; adjudicate consistently, without silently deleting rows. Identify factual disputes, methodological conflicts, and dependencies on pending analysis.
5. Populate existing NTIA Comments with a concise, evidence-based rationale; populate Comment Disposition with Accept, Partial Accept, Reject, or Pending as supported by the workbook's permitted values and project rules. Do not override an established decision without evidence.
6. Populate Resolution with exact report-ready replacement or insertion text for accepted edits, with a clear location and edit operation (replace/insert/delete) in an existing designated field or separate companion log. Do not put internal instructions or unsupported claims into paste-ready text. For Reject, leave Resolution blank unless the matrix's established contract expressly requires a rejection statement. For Pending, do not fabricate final language; document the open question in NTIA Comments.
7. Cross-check numerical values, frequency bands, assumptions, protection criteria, citations, and terminology against supplied sources. Escalate conflicts and unresolved technical issues.
8. Save a new XLSX preserving the source workbook structure. Do not add columns to a contract-clean source matrix **in ordinary adjudication mode**. In explicitly requested report-integration mode, create the new multitab implementation workbook and keep source matrix unchanged. Put optional provenance, clusters, edit operations, and validation details in a separate companion file or existing authorized metadata fields.
9. Validate all populated Resolution cells for paste-readiness, revision alignment, conflicts, missing anchors, and correct dispositions. Report accepted/rejected/pending counts and unresolved blockers.


## Report-integration mode (opt-in)
Use this mode when the user requests a **new comment resolution matrix containing all language needed to update a named report revision**. It complements the contract-preserving mode above. The user's project-specific filtering and workbook format control; never force the original 13/14-column schema on a new integration workbook.

1. **Freeze inputs and scope.** Identify the dated original matrix, baseline report revision, and available working papers. Keep source files unchanged. Record the source filename/version and original row number and comment ID for traceability.
2. **Filter first.** Exclude comments with disposition `Reject`/`Rejected` or status `Closed`/`Complete`/`Resolved` from **further analysis and drafting**, even if their historical disposition says `Accepted`. Do not reopen them. Count excluded rows on the dashboard. Comments that are open, partially resolved, pending, or have blank/unclear status remain in the actionable population; a blank is **not proof of acceptance**. Preserve the original status and attribution. Do not equate a populated `Resolution` with formal closure.
3. **Anchor the actionable rows.** Map them to the specified report revision using heading, printed page, line when reliable, and an exact text excerpt. Viewer-page numbers, appendix-relative page numbers, and malformed spreadsheet cell errors (`#VALUE!`) are not valid anchors. Report a missing anchor rather than inventing one.
4. **Consolidate repeated edits.** Cluster same-issue and multi-location comments under a stable change ID. One report change may resolve many comment IDs; one comment can require multiple report changes. Draft each unique replacement passage once and link all related comments. Capture executive-summary/main-body/conclusion dependencies.
5. **Produce real paste-ready text.** A report text field contains the **complete** proposed insertion, replacement, caption, table note, or footnote—not a paraphrase of the complaint, an instruction to fix it, or a truncated suggested phrase. For formatting-only changes, record the exact editorial operation with `No narrative text change`; do not manufacture prose. Use the agency's suggested wording as a candidate, not an automatically approved decision.
6. **Trace and verify.** Identify the supporting source and location for material claims, preserving measurement vs. modeling vs. assumptions, scope, units, percentiles, band boundaries, and agency positions. Mark unsupported technical claims, unavailable attachments, disputed regulatory choices, or missing calculation inputs `Needs verification`/`Blocked`, with the smallest required follow-up. Do not fabricate coordinates, source tables, approvals, or completed validation.
7. **Deliver one XLSX with four working tabs** unless user specifies otherwise: `Actionable Comments` (all original actionable fields + report change ID and status), `Report Text Changes` (one row per report edit, precise location, operation, original passage where verified, **complete report-ready text**, related IDs, evidence, readiness), `Unresolved Issues` (only unresolved actionable blockers/decisions), and `Dashboard` (source/actionable/excluded counts, draft/readiness coverage). Explicitly document exclusions; avoid redundant fifth source-data tab unless requested.
8. **Quality-check** every actionable row for a change ID, justified `no change`, or unresolved issue; verify every unique change's full text/anchor/source and that no excluded IDs leak into working tabs. Report coverage and blockers without claiming agency clearance or final concurrence.

**Example trigger:** “Using CRM Rev 9 and report Rev 8, exclude closed and rejected comments and produce Rev 10 as a four-tab workbook containing all report-ready text and a separate unresolved-issues register.”

## Output contract
The original matrix is authoritative. Common canonical 13-column layout: Comment Number; Reviewer Initials; Agency; Report Version; Section; Page; Line; Comment Type: Editorial/Grammar, Clarification, Technical; Agency Notes; Agency Suggested Text Change; NTIA Comments; Comment Disposition; Resolution. Some versions have WG Chain Comments or expanded metadata. **Never force a schema conversion or reorder existing columns**; use actual workbook headers and document mapping. Output an updated XLSX plus a short adjudication summary and, where needed, a separate report-edit log. In report-integration mode, place the edit log **inside** the new XLSX as a dedicated tab.

## Gates
- Fail closed if report revision cannot be established, or if a proposed technical change lacks support.
- No invented evidence, citations, page/line anchors, or agency decisions.
- Do not label a technical comment resolved if the analysis or agency decision is outstanding.
- Preserve source artifacts; write to a new file.
- Apply NTIA Quality Gate when available, without duplicating its checks.

## Integration
Module-first: keep schemas and validation logic in the existing spectrum-systems monorepo; reuse the comment-resolution-engine interfaces rather than create a parallel canonical contract. This portable skill contains operational instructions, not a copy of proprietary report data or a standalone engine.

See `references/quality-checklist.md` and `references/example.md`.

## Coordinated skill handoffs
Primary for an agency comment matrix. Hand off cross-document technical findings to ntia-review; do not replace or duplicate the matrix. Use the quality gate only for an explicitly requested readiness assessment.

For multi-skill requests, follow the central `skill-router` workflow and repository `AGENTS.md` instructions. The primary skill retains task ownership. Handoffs may use `contracts/handoff.schema.json` and findings may use `contracts/issue.schema.json`; these are optional portable formats, not official agency records. Include real source locations, version, unresolved issues, and already completed skills. A handoff is a recommendation to the host agent, not an executable skill call. Avoid circular calls and duplicate work.
