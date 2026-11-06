---
name: "google-dev-docs-style"
description: "Write, edit, or review technical writing to match the Google developer documentation style guide (developers.google.com/style). Use whenever the user asks to apply Google style, \"Google dev docs style,\" or to clean up, tighten, copyedit, or style-check technical docs, READMEs, how-tos, procedures, API docs, runbooks, briefing papers, or tech memos — even if Google isn't named but they want consistent, clear technical prose with standard formatting. Applies alongside other writing skills; where ntia-fcc-filing-voice or ntia-talking-deck sets a conflicting convention, that skill governs."
---

# Google developer documentation style

Apply the Google developer documentation style guide to technical writing. The guide's goal is documentation that a hurried, possibly non-native reader can scan, trust, and act on. Every rule below serves one of three aims: **clarity** (the reader understands on first pass), **consistency** (the same thing is always written the same way), and **durability** (the text stays true after it ships).

Source: Google developer documentation style guide, https://developers.google.com/style, licensed CC BY 4.0. Rules here are paraphrased and condensed. Items marked *(skill addition)* are this skill's own guidance in the guide's spirit, not Google rules — don't cite Google for them.

The guide itself says to break a rule when doing so serves the reader better. Treat these as strong defaults, not law.

## Pick the mode

Figure out which job the user wants, then follow that section:

- **Write** — draft new content in Google style.
- **Edit** — rewrite the user's text in place so it conforms.
- **Review** — leave the text alone and report issues.

If it's unclear whether the user wants edits or a review, default to **Edit** and include a short change summary.

## Core rules (apply every time)

These are the guide's highlights plus the highest-frequency rules. Apply them without opening a reference file.

**Voice and tone**
1. Be conversational and direct — like a knowledgeable colleague — without slang, jokes, exclamation points, or pop-culture references.
2. Address the reader as *you*. Avoid *let's*, and *the user* when you mean the reader.
3. Use active voice. Make the actor explicit.
4. Use present tense. Avoid *will* and *would* for things that happen as a result of an action ("The command returns…", not "The command will return…").
5. In instructions, cut *please*, *simply*, *just*, *easy*, *quickly*, *carefully*, and *properly*. (*Please* is fine only when asking permission or forgiveness: "If the issue persists, please contact support.")
6. Don't make excessive claims: avoid *best*, *fastest*, *always*, *never*, *guarantee*, *ensure* unless literally true and sourced. Prefer "helps protect" over "protects."
7. Keep text timeless: cut *currently*, *now*, *new*, *latest*, *existing*, *soon*, *as of this writing*, *eventually*, *at present*. Don't pre-announce future features. When editing, don't silently delete roadmap facts; see "When style conflicts with the domain."

**Sentence construction**
8. Put the condition, goal, or location before the instruction: "To delete the file, click **Delete**." / "For more information, see [X]." / "In the console, go to…"
9. Prefer short sentences (aim for fewer than 26 words) and plain words. Write for a global audience: no idioms, metaphors, or culturally specific references.
10. Define unfamiliar abbreviations on first use: *spelled-out term* (*ABBR*). Don't use *e.g.* or *i.e.* — write *for example* or *that is*. Avoid *etc.*; introduce the list with *such as* or *including* instead.
11. Don't use abbreviations, code terms, or UI labels as verbs ("Use SSH to log in", not "ssh into"; "Send a `POST` request", not "`POST` the data").
12. Use *that* for restrictive clauses (no comma) and *which* for nonrestrictive ones (with a comma). Keep the optional *that* ("the file that you created"). Follow *this* or *these* with a noun ("Set this value", not "Set this").
13. Commas: after an introductory phrase; before *and*/*but*/*or* joining two independent clauses; before nonrestrictive *which*; not before *because*. Always use the serial (Oxford) comma.

**Formatting**
14. Use sentence case for titles and headings. Start task headings with a bare verb ("Configure the receiver"), conceptual headings with a noun phrase ("Receiver configuration"). Avoid *-ing* openers. Don't number headings to show sequence, and don't put links or end punctuation in them. Don't skip heading levels or leave a heading with no text under it.
15. Numbered lists for sequences; bulleted lists for everything else; description lists (`**Term**: description`) for term–explanation pairs. In most cases, introduce a list with a complete sentence, never a fragment the items complete ("To configure the receiver, do the following:", not "To configure the receiver:"). A list can follow its heading directly if the heading gives all the context.
16. Keep list items parallel. Capitalize the first word. End with a period if the item is a sentence or has a verb; omit end punctuation for single words, verbless fragments, items entirely in code, or items that are just a link.
17. Put code-related text in `code font`: filenames, paths, commands, functions, variables, parameters, values to type. Put UI element names in **bold**. Don't put product names or browser URLs in code font.
18. Use bold *only* for UI elements, run-in headings, and notice labels. For emphasis, use italics — never bold or underline. Don't use all caps for emphasis.
19. Use straight quotation marks and apostrophes (`"` `'`), never curly ones.
20. Use descriptive link text — the destination's title or a phrase describing it — never "click here," "this page," or a bare URL.
21. Use notices sparingly: **Note** (useful, not critical), **Caution** (proceed carefully), **Warning** (don't do this / irreversible / security or data loss). Don't stack notices, and never put prerequisites, required steps, or cross-references in a note.

**Numbers, units, dates** (most common errors)
22. Spell out zero through nine; use numerals for 10 and up. Always use numerals for measurements, technical quantities, versions, percentages, money, and any number in a sentence that also has one ≥10. Don't start a sentence with a numeral.
23. Commas in numbers with four or more digits (1,532 not 1532). Leading zero on decimals (0.3). Percent with no space (40%).
24. Space between a number and its unit symbol (64 GB, 50 MHz). Ranges: when the unit is a symbol or abbreviation, repeat it and use *to* ("-40 °C to 85 °C," "10 GB to 20 GB"). When the unit is a spelled-out noun, use a hyphen with no spaces ("5-10 minutes," "8-20 files"). Plain number ranges also take a hyphen (2012-2016). Never use an en dash for ranges.
25. Dates: "January 19, 2017"; numeric only as ISO `YYYY-MM-DD`. Times: 12-hour clock, "3 PM", "3:45 PM". Don't refer to seasons; use months or quarters.
26. Spell out ordinals (*first*, not *1st*). Avoid *10x*; write "10 times."

## When to read the reference files

Open a reference file only when the text exercises that area in depth:

| File | Read when the text has… |
|---|---|
| `references/procedures-and-structure.md` | Numbered steps, how-tos, tutorials, sub-steps, optional steps, notices, tables, page organization |
| `references/language-details.md` | Questions on abbreviations, capitalization, punctuation (colons, dashes, hyphens, parentheses, quotes), pronouns, possessives, inclusive language, jargon |
| `references/numbers-units-dates.md` | Heavy numeric content, measurements, currency, rates, data units (MB vs MiB), time zones, fractions |
| `references/code-and-ui.md` | Code in prose, command-line syntax, placeholders, code samples, UI element names, keyboard keys, HTTP status codes |
| `references/word-list.md` | Word-choice questions; also skim before a final review pass |

If a question isn't covered here, check the live guide at https://developers.google.com/style (use web fetch) rather than guessing.

## How to work in each mode

### Write
1. Settle the document type first (task/how-to, concept, reference, tutorial). It decides the title form and structure.
2. Write only what the user asked for. Don't invent requirements, checklists, or troubleshooting sections the user didn't supply; offer them in one line instead.
3. Draft to the core rules. Lead with what the reader can do or needs to know; put prerequisites before steps.
4. Run a final pass against the word list and the core rules.

### Edit
1. Preserve meaning, technical accuracy, every fact the user supplied, and any domain conventions (see "When style conflicts with the domain"). Style never overrides correctness.
2. Fix structure first (headings, lists, step order), then sentences, then mechanics (numbers, punctuation, code font).
3. Return the edited text, then a short change summary grouped by rule category — not a line-by-line diff unless asked. Flag anything you changed that could alter meaning.

### Review
Report issues without rewriting the whole document. Use this format:

```
## Style review: <document name>

**Summary**: <1-2 sentences: overall state and the 2-3 most important fixes>

### Issues
| # | Location | Issue | Rule | Suggested fix |
|---|----------|-------|------|---------------|
| 1 | Para 2, sentence 1 | Passive voice hides actor | Active voice | "The system rejects the request" |

### Patterns
<Recurring problems worth fixing globally, e.g., "Headings use -ing forms throughout (8 instances).">

### Domain conventions kept
<Departures from Google style you deliberately did not flag, and why.>
```

Order issues by impact on the reader (clarity and correctness first, mechanics last). Group repeated instances of the same issue rather than listing each one.

Cap the issues table at 15 rows. A long table buries the fixes that matter. If you find more than 15 issues, keep the 15 with the most reader impact in the table, and fold the rest into "Patterns" as one line per category ("Number formatting: 4 more instances, such as `76,000,000` → *76 million*"). Say in the summary how many lower-priority items are under "Patterns." If the user asks for every issue, drop the cap.

## When style conflicts with the domain *(skill addition)*

The guide is written for software documentation, and it explicitly allows breaking a rule when that serves the reader. When the user's field or document type has established conventions, keep them and note the departure rather than "correcting" them:

- **Designations**: regulatory or standards names (band names such as "7125-7400 MHz," rule parts, document numbers like "ITU-R P.452") keep their official form even if it breaks number formatting.
- **Units**: units required by a governing standard (dBm, dBW/MHz, EIRP, I/N) stay as the standard writes them; still put a space between number and unit.
- **Quoted text**: legal or regulatory text is never restyled.
- **Formal memos and correspondence**: keep the document type's conventions — header blocks (TO/FROM/DATE/RE), third-person address of the recipient ("We recommend that the Assistant Secretary…"), and organizational *we*. Don't convert these to second person. Still apply the rest of the guide (active voice, plain words, numbers, dates).
- **Roadmap and known-issue information**: when editing, timeless style changes *where* forward-looking facts live, not *whether* they survive. Move them out of feature descriptions into a dated or clearly labeled section ("Planned changes," "Known issues"), or attach a version or date. Never delete a fact the user supplied; if you rewrite it, say so in the change summary.
- **House style**: if the user's organization has its own style guide, it wins on any conflict; Google style fills the gaps.

When you keep a domain convention, say so once in the change summary or the review's "Domain conventions kept" section so the user knows it was deliberate.
