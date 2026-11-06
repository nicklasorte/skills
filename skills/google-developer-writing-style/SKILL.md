---
name: google-developer-writing-style
description: Apply Google Developer Documentation Style Guide-inspired conventions to technical documentation, policy drafts, reports, instructions, and reviews. Use for clear, audience-first editing without changing technical or regulatory meaning.
---
# Google Developer Writing Style

This is an independent, unofficial operational adaptation of general principles associated with the public Google Developer Documentation Style Guide. It is not Google-authored or endorsed.

## When to use
Use when writing or editing technical documents, procedures, reports, explanatory material, or regulatory text for clarity and consistency. For NTIA policy, technical studies, and filings, use this skill for presentation **after** substantive accuracy is established.

## Writing rules
1. **Audience first.** State what readers need to know or do; identify prerequisites and assumptions.
2. **Lead with the point.** Put the outcome, recommendation, or required action first. Use descriptive headings in sentence case.
3. **Use active voice.** Identify the actor when known. Prefer "The team reviews the model" over "The model is reviewed" unless the actor is irrelevant or unknown.
4. **Use direct second person for instructions.** Prefer "Select Save" over "The user should select Save." Do not use second person when a formal agency position or objective technical description requires another construction.
5. **Use plain language.** Choose precise, familiar terms; define acronyms at first use where appropriate. Avoid jargon, unnecessary adverbs, filler, and inflated claims.
6. **Keep sentences and paragraphs focused.** Use short, parallel steps and lists when they aid scanning. Keep necessary qualifications close to the claims they limit.
7. **Be consistent.** Use American English, serial commas, consistent capitalization, terms, units, and formatting. Use descriptive link text.
8. **Make instructions executable.** Give ordered steps, expected outcomes, and relevant conditions; do not assume an interface or capability you have not verified.
9. **Preserve meaning.** Never silently change frequency ranges, numerical values, units, thresholds, citations, equations, regulatory terms, technical assumptions, or uncertainty.
10. **Respect authority and status.** Preserve distinctions among "must," "shall," "should," "may," and "will"; proposed versus adopted requirements; and agency positions versus third-party claims.

## Editing workflow
1. Determine audience, purpose, requested degree of editing, and any controlling template or style requirement.
2. Identify substantive ambiguities and unsupported statements separately from copyediting.
3. Rewrite for clarity, structure, active voice, and consistency without altering the source's meaning.
4. Check every changed technical and regulatory claim against supplied evidence. Flag unsupported changes rather than inventing support.
5. Return the revised text or requested artifact. For substantial revisions, summarize consequential edits and open questions.

## Priority and exceptions
- Binding law, official filing conventions, agency-approved language, exact quotations, technical notation, and the user's explicit requirements take precedence over stylistic preferences.
- Never remove necessary caveats to make a sentence shorter.
- Do not present this skill as an official Google or NTIA policy.
- For source-specific guidance, consult the current public [Google Developer Documentation Style Guide](https://developers.google.com/style) rather than assuming this summary reproduces every rule.

## Coordinated skill handoffs
Primary for editorial-only tasks. For domain-specific substance, defer to the appropriate specialist. Never change technical or regulatory meaning during style editing.

For multi-skill requests, follow the central `skill-router` workflow and repository `AGENTS.md` instructions. The primary skill retains task ownership. Handoffs may use `contracts/handoff.schema.json` and findings may use `contracts/issue.schema.json`; these are optional portable formats, not official agency records. Include real source locations, version, unresolved issues, and already completed skills. A handoff is a recommendation to the host agent, not an executable skill call. Avoid circular calls and duplicate work.
