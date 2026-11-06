---
name: "ntia-fcc-filing-voice"
description: "Rewrites, expands, reorganizes, reviews, or assembles NTIA filings to the FCC on spectrum matters under spectrum-related CFR parts: comments, reply comments, comments on waiver petitions, petitions for reconsideration or stay, letters to the Chairman or Commissioners, ex parte notices, and proposed rule text. Use when Nick asks to draft or fix a filing, put text in NTIA's voice, respond to an FCC NPRM or waiver request, or write to the Commission. Do not use for internal policy briefs, decision memos, or regulation summaries; use ntia-policy-research for those."
---

# NTIA FCC filing voice

Turn Nick's paragraphs, loose notes, and drafts into text that reads like the National Telecommunications and Information Administration (NTIA) filing before the Federal Communications Commission (FCC) on spectrum matters: precise, lawyerly, calibrated, and cooperative. NTIA speaks on behalf of the Executive Branch, so every sentence carries institutional weight and may later be tested in court. Accuracy, restraint, and a preserved record matter more than polish.

This skill's conventions override the google-dev-docs-style skill for filing text. Google style still governs plain word choice, active voice, cutting filler, and defining abbreviations.

## Contents

1. Scope and modes
2. Workflow and output
3. Voice
4. Paragraph architecture and reorganizing
5. Argument patterns
6. Administrative-law toolkit
7. Waivers (in `references/filing-types.md`)
8. Reconsideration, clarification, and stay (in `references/filing-types.md`)
9. Letters (in `references/filing-types.md`)
10. Proposed rule text and conditions (in `references/filing-types.md`)
11. Citations (in `references/citations-and-procedure.md`)
12. Full filings and procedure (in `references/citations-and-procedure.md`)
13. Record-preservation pass
14. Plain-language pass
15. Review mode checklist
16. Guardrails
17. Exemplar bank (in `references/examples.md`)
18. Worked example (in `references/examples.md`)

Sections 1 through 6 and 13 through 16 apply to every run. Read a reference file when the filing type, mode, or step needs it: `filing-types.md` for waivers, reconsideration, stays, letters, and rule text; `citations-and-procedure.md` for footnotes and Assemble mode; `examples.md` to calibrate voice before a first draft.

## 1. Scope and modes

### Spectrum-only scope

Use this skill only for filings on spectrum matters governed by spectrum-related CFR parts. Before starting, confirm the subject falls in the list below.

**In scope (Title 47):**
- Part 1, only as it governs spectrum proceedings: practice and procedure, wireless licensing (subpart F), competitive bidding (subpart Q), and spectrum leasing
- Part 2: frequency allocations and radio treaty matters, including the Table of Frequency Allocations (§ 2.106), equipment authorization, and definitions such as harmful interference (§ 2.1)
- Part 5: experimental radio service
- Parts 15 and 18: radio frequency devices and industrial, scientific, and medical equipment
- Spectrum service rules: Parts 22, 24, 25, 27, 30, 74, 80, 87, 90, 95, 96, 97, and 101, and the spectrum and technical provisions of Part 73
- Part 300: the NTIA Manual, incorporated by reference
- Part 301: relocation of, and spectrum sharing by, federal government stations

**Also in scope when they bear on a spectrum proceeding:** the Communications Act and NTIA Organization Act provisions on spectrum management (for example, 47 U.S.C. §§ 303, 305, 309(j), 902, 923, 928), spectrum-specific public laws, ITU Radio Regulations, and administrative-law authority.

**Out of scope:** non-spectrum CFR parts and programs, such as 47 CFR Part 302 (Connecting Minority Communities Pilot Program), Part 54 (universal service), broadband grant programs, and Part 1 rules applied to non-spectrum proceedings. When a request falls outside scope, say so in one sentence and don't apply this skill's voice, ladder, or templates. If the ntia-policy-research skill is available and fits (rule summaries, memos, or retrospective reviews of NTIA parts such as Part 302), point Nick to it; otherwise help with the request as ordinary writing if he wants.

**Mixed requests:** When a filing touches both, apply the skill only to the spectrum portions and flag the rest.

### Filing types

- Comments and reply comments on a Notice of Inquiry (NOI), Notice of Proposed Rulemaking (NPRM), or Further Notice (FNPRM)
- Comments on petitions for waiver and petitions for rulemaking
- Petitions for reconsideration or clarification, petitions for stay, oppositions, and replies
- Letters to the Chairman, Commissioners, and bureau or office chiefs, including staff-level letters from the Office of Spectrum Management (OSM)
- Ex parte notices and letters transmitting technical materials or agency letters
- Proposed rule text and license conditions for an appendix or attachment

**Unit of work:** anything from one paragraph to a full filing.

### Modes

Pick the mode from the request. If it's unclear, use Rewrite.

- **Rewrite:** Return the text in NTIA voice with the same facts and the same position strength.
- **Expand:** Turn loose notes or bullets into complete paragraphs. Add only framing, transitions, and citations; never add technical facts.
- **Reorganize:** Reorder sentences, paragraphs, or sections into the architecture in section 4.
- **Assemble:** Build a full filing with caption, opening, sections, conclusion, signature block, and the procedural items in section 12.
- **Draft rule text:** Write proposed rule language or license conditions per section 10.
- **Review:** Critique a draft against section 15 without rewriting it.

## 2. Workflow and output

1. Confirm the subject is in scope (section 1).
2. Identify the filing type, proceeding, docket, CFR parts involved, and the Commission document, petition, or order being answered. If missing, use placeholders; don't stop to ask.
3. List every fact, number, descriptor, and position in the input. This list is the ceiling: the output may not exceed it.
4. Set the position strength on the ladder in section 3. Match the input; never escalate.
5. Order the content using section 4.
6. Draft. Apply voice, terms of art, and mechanics.
7. Draft footnotes with full citations in the format in `references/citations-and-procedure.md`, verifying each one with web tools when available (FCC EDOCS, ECFS, eCFR, govinfo.gov, ntia.gov, court opinions).
8. Run the record-preservation pass (section 13) and the plain-language pass (section 14).
9. Run the fact-ceiling check: compare every technical claim, number, system name, and descriptive modifier in the draft (for example, *high-power*, *mission-critical*, *safety-of-life*, *nationwide*) against the list from step 3. Remove anything not in the input, or replace it with `[CONFIRM: <item>]`. Framing, transitions, and the ladder phrasing don't count as facts.
10. Check acronyms: each one is spelled out at its first appearance in the body, including inside proper names such as "National Aeronautics and Space Administration (NASA) Deep Space Network."
11. Write flags.

**Output format (Rewrite, Expand, Reorganize, Assemble, Draft rule text):**

```
<clean text with footnote markers as [1], [2]>

Footnotes
[1] <full citation>

Flags
- <only real issues>
```

Keep flags to five or fewer for paragraph-level work and ten or fewer for full filings. Flag unverified citations, [CONFIRM] items, positions that need interagency clearance, possible sensitive content, preservation gaps, and any out-of-scope material. Omit the section if there are none. Don't add a change log unless Nick asks.

**Output format (Review):** see section 15.

## 3. Voice

### Institutional identity

- Refer to the filer as "NTIA." Use "we" only to avoid naming NTIA three times in one paragraph.
- Refer to the FCC as "the Commission." Use "FCC" in citations or when distinguishing it from another agency in the same sentence.
- NTIA speaks "on behalf of the Executive Branch." When a filing rests on specific agencies' equities, name them: "on behalf of the Executive Branch, particularly the Department of Defense (DoD) and the Department of Transportation (DOT)."
- Name agencies in full with the acronym on first use: DoD, Federal Aviation Administration (FAA), National Aeronautics and Space Administration (NASA), National Science Foundation (NSF), National Oceanic and Atmospheric Administration (NOAA), Department of Homeland Security (DHS), DOT.
- Describe the government side as federal incumbents, federal users, federal operations, federal systems, or federal missions.

### Position ladder

Use the lowest rung that carries the input's position.

| Rung | Use when | Phrasing |
|---|---|---|
| Endorse | NTIA agrees with the proposal | "NTIA supports," "NTIA commends the Commission for," "NTIA appreciates" |
| Encourage | A soft push tied to a federal interest | "NTIA encourages the Commission to" |
| Recommend | A specific technical or procedural fix | "NTIA recommends that the Commission adopt" |
| Urge | A serious federal equity or a guiding principle is at stake | "NTIA urges the Commission to," "As a foundational matter, NTIA urges" |
| Condition | Acceptable only with protections | "NTIA does not object to ..., provided that," "any grant should be conditioned on" |
| Sequence | The Commission should act in a set order | "As a threshold matter, the Commission should first resolve" |
| Oppose | NTIA can't support the action | "NTIA cannot support," "NTIA, on behalf of the Executive Branch, is unable to recommend approval of" |
| Seek relief | After an adverse order | "NTIA respectfully petitions the Commission to reconsider or, in the alternative, to clarify" |

Use "As a threshold matter" only when one decision must come before another. For a principle that should govern the whole analysis, such as accounting for aggregate interference, use "As a foundational matter."

Reserve *must* for requirements in a statute, treaty, or existing rule, and cite the source. In proposed rule text, *must* states the requirement (section 10).

### Calibration

- State technical findings at the confidence the input supports: "NTIA believes," "NTIA's preliminary analysis indicates," "could cause harmful interference," "can likely coexist," "may be necessary."
- Label analysis status honestly: preliminary, example, first step in an iterative process.
- Close substantive points cooperatively when it fits: "NTIA looks forward to working with the Commission," "NTIA is prepared to facilitate coordination among federal and non-federal stakeholders."
- When opposing, stay measured. Argue from the record and the law; don't characterize opponents' motives.
- Avoid *clearly*, *obviously*, *simply*, rhetorical questions, exclamation points, and casual words (*jam*, *kill*, *huge*, *bad idea*).

### Administration-neutral language

- Don't name the President, the administration, or administration-branded initiatives, slogans, or priorities unless Nick supplies them and asks.
- Frame benefits in durable terms: consumers, innovation, economic growth, national security, public safety, scientific research.
- Statutes and public laws are fine; they're law, not politics.

### Terms of art

Use these exactly; don't substitute synonyms:

- *harmful interference* (defined in 47 CFR § 2.1)
- *coordination zone*, *protection criteria*, *aggregate interference*, *interference-to-noise ratio (I/N)*
- *primary*, *secondary*, *co-primary* allocation; *on a non-interference basis*; *claim protection from*
- *in-band*, *adjacent band*, *out-of-band emissions*
- *federal* and *non-federal*
- *incumbent*, *repurpose*, *relocate*, *share*
- *Table of Frequency Allocations*, *NTIA Manual* (the Redbook), *Interdepartment Radio Advisory Committee (IRAC)*, *Government Master File (GMF)*

### Mechanics

NTIA conventions override Google style on these points:

- **Frequency ranges:** hyphen, no spaces, unit once: "3.98-4.2 GHz," "7125-7400 MHz." Band nicknames as "the 12.7 GHz band."
- **Amounts of spectrum:** spell out the unit: "100 megahertz," "a 20-megahertz guard band."
- **Power and criteria:** keep the user's values and units, with a space before the unit: "75 dBm/100 MHz EIRP," "-10 dB I/N."
- **Numbers:** numerals for every technical quantity; spell out one through nine otherwise.
- **Defined terms:** introduce short forms in parentheses on first use, then use them consistently: "Notice of Proposed Rulemaking (NPRM)." An acronym used inside a proper name still needs its first-use definition.
- **Capitalization:** lowercase *federal* except in titles, proper names, and quoted rules. Capitalize *Executive Branch* and *the Commission*.
- **Dates:** "January 20, 2026."
- **Sentences:** usually 30 words or fewer; serial comma; active voice unless the actor is sensitive or irrelevant.
- **Paragraphs:** four to eight sentences, one main point each.

## 4. Paragraph architecture and reorganizing

Build each substantive paragraph in this order. Skip a step only if the input has nothing for it.

1. **Anchor:** Tie the paragraph to what the Commission proposed, asked, or decided, with a pin cite.
2. **Position:** State NTIA's position at the right ladder rung.
3. **Federal equity:** Name the agency, system type, allocation status, and general location. Unclassified information only.
4. **Basis:** Give the technical analysis, protection criterion, record evidence, legal standard, or precedent. Move background and precedent detail into footnotes.
5. **Request:** Say exactly what the Commission should do: rule text, condition, process, or timing.
6. **Bridge (optional):** Add a cooperative close or a transition to the next point.

### Reorganize rules

- One request per paragraph. Split paragraphs that make two.
- Lead with the position, not the background.
- Merge fragments that support the same point.
- Default section order: follow the order of the Commission's document, so staff can map each comment to a question. Within a band discussion, cover in-band issues before adjacent-band issues. In a petition for reconsideration, lead with the strongest ground for relief.
- Organize letters band by band or issue by issue, with short headings, when they cover more than one band or issue.
- For three or more paragraphs, suggest section headings in NTIA form: roman numerals with all-caps or title-case headings ("II. COORDINATION WITH FEDERAL OPERATIONS"), lettered subsections, and run-in headings for parallel items.

## 5. Argument patterns

- **Threshold, then alternative:** "As a threshold matter, the Commission should first resolve [issue] before acting on [request]. If the Commission nevertheless proceeds, it should [protective step]."
- **Support with conditions:** "NTIA supports [action], provided that [condition]." List three or more conditions as a numbered list.
- **Two-sided protection:** Protect federal operations while warning against coordination so restrictive that it impedes new technologies. This shows balance and strengthens credibility.
- **Preserve the allocation:** Urge the Commission to reject requests to change the nature of an existing federal or co-primary allocation, and offer a process that accommodates the federal need.
- **Precedent analogy:** "NTIA recommends a coordination process similar to the one the Commission adopted for the [band]," with the order cited.
- **Process proposal:** NTIA-defined and published coordination zones, a pre-coordination portal, or an incumbent informing capability, each described as something NTIA can develop with the affected agency.
- **Iterative analysis:** Present studies as a starting point that further data (deployment information, propagation and clutter models) will refine.
- **Record engagement:** "NTIA agrees with [Party] that ..." or "Contrary to [Party]'s assertion that ..., the record shows ...," citing each commenter.
- **Executive Branch weight:** When the Commission discounts federal concerns, argue that the order gave insufficient weight to the technical showings of the agencies responsible for the affected systems, and cite those showings.
- **Limits on relief:** "without prejudice to the outcome of [proceeding]," "should not serve as precedent."

## 6. Administrative-law toolkit

Use these hooks when the input supports them. Verify every citation before finalizing.

- **Reasoned decision-making:** An agency must examine the relevant data and articulate a satisfactory explanation, including a rational connection between the facts found and the choice made. *Motor Vehicle Mfrs. Ass'n v. State Farm Mut. Auto. Ins. Co.*, 463 U.S. 29, 43 (1983). Use it to ask the Commission to address federal technical showings expressly.
- **Significant comments:** An agency must respond to significant comments that, if true, would require a change in the proposed rule. *See Home Box Office, Inc. v. FCC*, 567 F.2d 9, 35-36 (D.C. Cir. 1977). Use it to make sure NTIA's points are framed as significant, specific, and outcome-changing.
- **Logical outgrowth:** A final rule must be a logical outgrowth of the proposal. *See Long Island Care at Home, Ltd. v. Coke*, 551 U.S. 158, 174 (2007). Use it to ask the Commission to seek further comment before adopting rules the NPRM didn't propose.
- **Stay factors:** The Commission applies the four-factor test: likelihood of success on the merits, irreparable harm absent a stay, harm to other parties, and the public interest. *See Virginia Petroleum Jobbers Ass'n v. FPC*, 259 F.2d 921, 925 (D.C. Cir. 1958); *Washington Metro. Area Transit Comm'n v. Holiday Tours, Inc.*, 559 F.2d 841, 843 (D.C. Cir. 1977).
- **Issue exhaustion:** Courts won't review questions on which the Commission has been afforded no opportunity to pass. 47 U.S.C. § 405(a). See section 13.

Keep these arguments administration-neutral and measured. NTIA asks the Commission to complete the record; it doesn't accuse the Commission of bad faith.

## 7. Waivers

See `references/filing-types.md`.

## 8. Reconsideration, clarification, and stay

See `references/filing-types.md`.

## 9. Letters

See `references/filing-types.md`.

## 10. Proposed rule text and conditions

See `references/filing-types.md`.

## 11. Citations

See `references/citations-and-procedure.md`.

## 12. Full filings and procedure

See `references/citations-and-procedure.md`.

## 13. Record-preservation pass

Courts generally won't review questions on which the Commission has been afforded no opportunity to pass. 47 U.S.C. § 405(a). The D.C. Circuit construes this strictly, and an issue that first becomes relevant when the order issues still requires a petition for reconsideration before judicial review. *See Qwest Corp. v. FCC*, 482 F.3d 471, 474-75 (D.C. Cir. 2007) (verify). After drafting, check each argument:

- Is it stated as an argument, not just mentioned? Name the legal or technical point, the evidence, and the requested outcome.
- Is it specific enough that the Commission could rule on it? Generic concern about "interference" isn't enough; name the system, criterion, and analysis.
- Is each alternative argument stated, so a fallback position survives if the primary one fails?
- Is every technical showing the argument depends on in the record (filed, attached, or cited)?

Flag every argument that fails a check, and suggest the sentence that would fix it.

## 14. Plain-language pass

Apply the Federal Plain Language Guidelines without stripping technical terms or nuance:

- Replace hidden verbs and nominalizations: "make a determination" becomes "determine"; "provide protection to" becomes "protect."
- Cut meaningless formal language. Allow *hereby*, *herein*, and *above-captioned* only in the opening and closing formulas, where NTIA conventionally uses them.
- Prefer short words when they're as precise as long ones: *use*, not *utilize*; *before*, not *prior to*; *about*, not *with respect to*.
- Keep terms of art (section 3) even when a plainer word exists.

## 15. Review mode checklist

Report issues without rewriting the draft. Use this format:

```
Review: <document>

Summary: <1-2 sentences: overall state and the 2-3 most important fixes>

| # | Location | Issue | Category | Suggested fix |
|---|---|---|---|---|

Preservation gaps: <arguments that fail section 13>
Citations to verify: <list>
```

Check, in priority order:

1. Subject is in spectrum scope (section 1).
2. Facts, numbers, descriptors, and positions match the source and aren't inflated.
3. Record preservation (section 13).
4. Legal standard stated and applied (waiver, reconsideration, stay, admin-law hooks).
5. Position ladder used consistently and at the right rung, including threshold versus foundational framing.
6. Paragraph architecture: anchor, position, equity, basis, request.
7. Citations complete, verified, in the right form, and to spectrum-related CFR parts.
8. Terms of art, mechanics (including first-use acronyms), and plain language.
9. Procedure: table of contents, summary, page limits, deadlines, dockets.
10. Administration-neutral language and sensitive content.

Cap the table at 15 rows; fold lower-priority items into one line per category.

## 16. Guardrails

- **Spectrum only.** Apply this skill only within the scope in section 1.
- **No invented content.** Keep every number, system name, finding, and descriptive modifier as Nick wrote it. Use `[CONFIRM: <item>]` for anything missing.
- **No position inflation.** Don't state an Executive Branch, DoD, or other agency position more strongly than the input does. Flag any sentence that attributes a position to another agency so Nick can confirm it was coordinated through the IRAC or other clearance process.
- **Unclassified only.** Never include classified or controlled information. Flag specific system parameters, site locations, or operating schedules unless Nick marks them as public. Describe federal assignment data as unclassified.
- **Quotations.** Quote Commission text, rules, and court opinions briefly and exactly. Don't restyle quoted legal text.
- **Not legal advice.** Flag legal-standard and deadline questions for NTIA's Office of the Chief Counsel when the stakes warrant it.

## 17. Exemplar bank

See `references/examples.md`.

## 18. Worked example

See `references/examples.md`.
