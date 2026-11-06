---
name: ntia-meeting
description: Coordinate an NTIA meeting package across source-grounded minutes, decisions, actions, unresolved issues, and study handoffs. Use for a reusable meeting-to-study package or reconciliation across meetings; ordinary minutes use spectrum-meeting-records.
---

# NTIA-Meeting

Turn meeting evidence into a coherent record and a proposed handoff to review or study work. Run independently from supplied text, attachments, or local files. No repository, pipeline, Saturn integration, or other skill is required. Use `spectrum-meeting-records` as an optional specialist when available.

## Establish the evidence

Identify the meeting, date and time zone when known, source versions, transcript coverage, speaker identification, slides, notes, and approved corrections. Follow the source-grounded meeting workflow below. Unknown dates, speakers, owners, and deadlines remain unknown.

Inspect an existing Saturn or spectrum-systems extraction artifact only if its schema, provenance, source coverage, and evaluation status are available. Do not assume a processor is installed or that a generated artifact is authoritative. Keep the source reference when converting a pipeline record. A blocked pipeline output may inform diagnosis but cannot be presented as a promoted record.

If extraction tools are absent, create source-grounded draft minutes directly using the existing meeting skill or its available source material. State the manual path. Missing transcript sections limit coverage; they do not establish that no decision or action occurred.

## Assemble the package

1. Produce source-grounded minutes using the bundled workflow, optionally reusing `spectrum-meeting-records` where available.
2. Normalize consequential items into distinct decisions, actions, and open issues. Retain stable source IDs and cross-meeting links; do not merge repeated wording when scope or status differs.
3. Reconcile the new record with prior approved records. A later statement supersedes an earlier decision only when the record establishes that relationship. Preserve the earlier evidence and the supersession basis.
4. Produce a proposed study or review handoff only for relevant unresolved questions. Label a proposed task separately from a commitment recorded in the meeting.

A decision requires explicit resolution with its conditions. A suggestion remains a proposal; silence does not establish consensus. An action is assigned only if the evidence establishes the assignment. Use `owner: null` and `due_date: null` for unstated fields. Use `status: proposed` for an unaccepted request. Preserve dissent, tentative status, scope limits, technical values, and the distinction between attendance and invitation.

Use a structured meeting record for reusable handoffs. Actions and decisions require exact source references even when their owner or date is unknown. Preserve source speaker labels instead of inferring an agency affiliation.

## Deliver and verify

Return the minutes and requested action/decision/issue records, source coverage, material discrepancies, and proposed handoff. If requested, draft a follow-up using confirmed commitments and labeled clarification requests. Sending a message requires the user's authorization to send.

Check each decision and action against its source, test owner and deadline attribution, and confirm dissent and conditions remain attached. Use the available Google writing skill for presentation. Apply `ntia-quality-gate` when a readiness assessment is requested. Draft records remain drafts until the applicable human or runtime process establishes approval; this skill cannot manufacture that approval.


## Public distribution note
This public edition is a standalone instructional workflow. It does not bundle the original installed suite's machine-readable schemas, validation scripts, internal integrations, or any agency materials. Do not claim automated validation or official clearance.
