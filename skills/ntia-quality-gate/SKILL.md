---
name: ntia-quality-gate
description: Assess an NTIA artifact against explicit evidence, technical, policy, attribution, and presentation checks, returning a fail-closed advisory readiness record. Use for an explicit quality gate or readiness assessment, not routine editing or official clearance.
---

# NTIA Quality Gate

Assess whether the exact artifact meets the stated review criteria. Run independently from supplied text, attachments, or local files. No repository, other skill, or remote validator is required. Own the evidence checklist and advisory result; institutional decisions and any external-system promotion remain outside this advisory result.

## Fix the target and criteria

Use the baseline check matrix described below. Identify the artifact version or exact file hash, scope, applicable authorities, and required checks before assessing it. Do not let the artifact's author remove a failing check from the required set.

The bundled baseline profile requires `source_coverage`, `claim_support`, `technical_consistency`, `policy_precision`, `attribution`, and `presentation`. These are local working checks, not NTIA requirements. An approved project profile may add checks; removing baseline checks requires a separately governed profile revision and is unsupported by the bundled validator.

## Assess evidence

For each required check, record `pass`, `fail`, `unknown`, or `not_applicable`, its rationale, and evidence references. A pass requires evidence of an actual check. Confidence scores, polished prose, schema validity, and a prior assistant assertion do not establish substantive correctness.

Use specialists for relevant substance. If policy conformance is requested, establish the applicable NTIA Policy source and version; a missing required policy source yields unknown. If no institutional policy conclusion is asserted, `policy_precision` can pass only after checking that the artifact makes no unsupported policy, authority, or concurrence claims. Apply the same scope reasoning to technical claims and attribution.

A check is not applicable only with a specific rationale showing why it is outside the fixed scope. Unknown is not not-applicable. Preserve failed and unknown observations and unresolved material issues; do not rewrite evidence to obtain a pass.

## Compute the advisory result

Return `blocked` when a required check fails or is unknown, required evidence is unavailable, source references are invalid, the target changed, or a critical/high issue remains unresolved. Return `ready_for_human_review` only when all required checks pass or have supported not-applicable rationales, the target identity is fixed, and no material blocker remains. This result is never institutional clearance, certification, or permission to publish.

When code execution is available, validate source links and target hashes with an authorized project validator. Otherwise use manual validation and disclose the limitation. Hashes must be computed, never invented.

## Deliver

Lead with the advisory result, affected artifact, and blockers. Provide the check matrix, exact evidence pointers, unresolved issues, and the smallest supported corrections. Supply a structured JSON gate record when machine-readable evidence is requested. A recheck must bind to the revised artifact and retain previous check results as history outside the current record. Never edit the reviewed target in place during a gate-only request.


## Public distribution note
This public edition is a standalone instructional workflow. It does not bundle the original installed suite's machine-readable schemas, validation scripts, internal integrations, or any agency materials. Do not claim automated validation or official clearance.
