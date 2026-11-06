---
name: "ntia-talking-deck"
description: "Turns Nick's document, notes, or thoughts into a short NTIA-template PowerPoint (.pptx) talking deck for non-technical audiences, with native charts, minimal text, and the NTIA brand and style guide applied. Use when Nick asks for a deck, slides, a briefing deck, or talking slides for NTIA leadership or political appointees, or asks to turn a memo or analysis into slides. Do not use to critique a deck's message without building one (use made-to-stick-briefing) or for decks outside NTIA."
---

# NTIA talking deck

Turns a document, analysis, notes, or a rough set of thoughts into a .pptx talking deck built on the NTIA template. The audience is usually non-technical, such as political appointees. The presenter talks; the slides show one point and its evidence.

Every deck keeps the NTIA template: its slide master, layouts, theme fonts, theme colors, logo, and footer. There is no off-template deck. Decks have no animation and no slide transitions.

This skill combines five things:

- **Assertion-evidence slide design**: a sentence headline that states the takeaway, supported by visual evidence instead of bullets. Controlled studies show better comprehension, fewer misconceptions, and stronger delayed recall than default topic-and-bullets slides.
- **The `made-to-stick-briefing` skill**: decides *what* each slide says.
- **The `google-developer-writing-style` skill**: decides *how* each headline and note is worded.
- **The NTIA template and brand and style guide**: decide colors, fonts, logo use, and NTIA writing conventions. See "NTIA template" here and "NTIA brand and style rules" in `references/brand-and-design.md`.
- **The modern look**: decides composition, type scale, icons, and chart style, drawn from great design outside slides. See "Modern look" in `references/brand-and-design.md`.

## Files and dependencies

Read these before the steps that use them:

| When | Read |
|---|---|
| Step 1 | `made-to-stick-briefing` SKILL.md and its `references/framework.md` |
| Step 5 | `pptx` SKILL.md (build mechanics, validation, and QA) |
| Step 5 | `claude/ntia-template-map.md` in the project and `references/brand-and-design.md` in this skill |
| Step 6 | `google-developer-writing-style` SKILL.md core rules |

Source files in the project:

- `DOC NTIA_Style Guide July 2026.pptx`: **the NTIA template.** Its master and layouts are the template for every deck. Its content is also the current NTIA style guide (font, logo misuse, terminology, and writing guidance).
- `NTIA Brand Style Guide.pdf`: the brand book (color values, logo colors, voice keywords, and photo guidance).

The user asked for .pptx output on the NTIA template, so use the `pptx` skill even if the session offers a Slides artifact type.

## NTIA template

### Get the template file

The deck must be built from the binary .pptx, not its extracted text. Look in this order:

1. A .pptx or .potx attached to the current message whose name contains "NTIA", such as `DOC NTIA_Style Guide July 2026.pptx`.
2. A copy already saved in the working directory from earlier in this session.
3. The project file `DOC NTIA_Style Guide July 2026.pptx`, through `Projects` `project_read`. If the read returns only text, the binary isn't available from the project.

If you can't get the binary, tell Nick in one sentence and ask him to attach `DOC NTIA_Style Guide July 2026.pptx` to a message. Stop at the confirmation gate until he does. Never build the deck off-template.

### Map the template (first run only)

When you first get the binary, inventory it and save the map so later runs skip this work:

1. Run `thumbnail.py` from the `pptx` skill on the file, and list every layout and placeholder with `python-pptx` (layout name, placeholder idx, type, position, and size).
2. Record the theme fonts, theme colors, logo placement, and footer fields. Compare them with "NTIA brand and style rules" and note any difference in the map.
3. Record each layout's content area (the bounding box free of logo, footer, and master graphics) and compute the 12-column grid for it (see "Grid and spacing").
4. Assign each composition preset in "Modern look" to a layout. Use the layouts behind the style guide's own slides: its title slide for the title, its section slides (such as "Visual Identity") for section breaks, and a title-only layout for most content slides.
5. Save the result to the project as `claude/ntia-template-map.md`.

On later runs, read `claude/ntia-template-map.md` instead of re-inventorying. If the template file changed, map it again.

### Keep the template intact

- Build from a copy of the template file. Delete all of its existing slides (the style guide content), and keep the master, layouts, theme, and media.
- Add every slide from a mapped layout. Never add a blank slide and redraw the master's look.
- Fill placeholders by assigning `run.text`, not `text_frame.text`, so template formatting survives.
- Don't edit the master, layouts, theme fonts, or theme colors. Don't move, resize, or recolor the logo or footer.
- Place charts, tables, icons, and shapes inside the layout's content area so they don't cover master elements.
- Use theme colors (`MSO_THEME_COLOR`) for fills and text where the theme defines them. Use the hex values in "Colors" only when the theme has no matching slot.

## Brand rules and modern look

`references/brand-and-design.md` holds two sections. Read the whole file before step 5 and again during step 6:

- **NTIA brand and style rules:** colors, fonts, logo, photos, voice, and NTIA writing conventions.
- **Modern look:** design principles, grid and spacing, type scale, composition presets, icons, Isotype counts, charts, tables, photos, and the "Never" list.

## Workflow

Follow these steps in order. Nick's source material is the authority on facts.

### 1. Intake

Read the source. Identify:

- **Audience**: default to non-technical decision-makers.
- **Purpose**: decide or inform. A decision deck must end with an explicit ask.
- **Talk length**: if not given, assume 10-15 minutes.
- **Sensitivity**: run the clearance check below before anything else.
- **Template**: confirm you have the template binary (see "Get the template file"). If not, ask for it now so it arrives by the build step.

#### Clearance check

Confirm both points before you read the source in depth:

1. **Clearance.** The source is public (Federal Register, CFR, FCC EDOCS or ECFS, ntia.gov, or the NTIA Manual), or Nick has said it's cleared for this environment.
2. **No sensitive content.** The source has no classification markings, no controlled unclassified information (CUI) markings, and no nonpublic federal system parameters, site locations, or operating schedules.

If either point fails, stop. Tell Nick which point failed and what you saw. Don't summarize, quote, or chart the material. For coordination zones and federal sites, show only the precision that public sources already show.

#### Inputs from other skills

The source can be output from `ntia-policy`, such as a decision memo, information memo, summary, or review table. Keep its facts, citations, `[CITE]` and `[CONFIRM]` placeholders, and "as of" date. Map a decision memo to the decision-deck spine in step 2.

Fill the Made to Stick Sticky Brief canvas. Mark anything the source can't support as **GAP**. Never invent numbers, stakes, or examples.

### 2. Outline

Write one row per slide:

| # | Slide type | Preset | Assertion headline | Evidence (and icons) | SUCCESs principle and pattern | Source |
|---|---|---|---|---|---|---|

Use this default spine, and adjust it to the content:

1. Title
2. Bottom line: the one-sentence takeaway and, for a decision deck, the ask
3. Context: why this matters now, in plain terms
4. Two to four evidence slides, one assertion each
5. Recommendation or implication
6. The ask: what, who, and by when
7. Appendix: method, full tables, and technical detail for Q&A only

For a decision deck, follow the same order as the `ntia-policy` decision memo:

1. Title
2. Decision requested and bottom line
3. Background, in plain terms
4. Federal equities: affected agencies, systems, or bands, from public sources only
5. Options: two to four mutually exclusive options, including "no action" or "retain the current rule" when it's viable
6. Recommendation, only if Nick supplied one or asked for one; otherwise `[CONFIRM: recommendation]`
7. The ask: what, who, and by when
8. Appendix: supporting tables, such as a per-area results table, and method

Size the main deck at about one slide per 2 minutes of talk time. Default cap: 8 main slides.

### 3. Accuracy check

Run the Made to Stick accuracy check before showing the outline:

- Trace every claim to the source.
- Recompute every derived number, including Isotype counts, and show the arithmetic.
- Label invented examples, sample values, and schematic curves as "Illustration."
- If a sticky framing conflicts with the analysis, the analysis wins.
- Never invent a citation, docket number, dollar figure, or date. Put `[CITE: <what's needed>]` or `[CONFIRM: <what's needed>]` in the speaker notes and list each one as an open question.
- Flag every statement of another agency's position, such as DoD, FAA, or NOAA. State it only if Nick supplied it and it was coordinated.

#### Policy neutrality

- Separate technical findings from policy judgment. Present options and tradeoffs; label which calls belong to the principal.
- Stay administration-neutral. Don't name the President, the administration, or administration-branded initiatives or slogans unless Nick supplies them and asks. Frame benefits in durable terms: consumers, innovation, economic growth, national security, public safety, and scientific research.

### 4. Confirmation gate

Present the canvas summary, the outline table, the accuracy check, and the open questions (GAPs). **Stop and wait for Nick's approval.** Don't build slides until he approves or revises the outline and the template binary is in hand.

### 5. Build

Build the deck with the `python-pptx` mechanics in the `pptx` skill, on a copy of the template, following "Keep the template intact" and "Modern look" in `references/brand-and-design.md`.

1. Compute the grid for each layout from the template map, and write small helpers for column positions, the spacing scale, the type scale, and each icon you need.
2. Build each slide from its preset.
3. Use native components only:
   - Charts: native PowerPoint charts with embedded, editable data (`chart_data` in `python-pptx`), styled per "Charts."
   - Tables: native tables, styled per "Tables."
   - Icons, diagrams, and flows: grouped native shapes and connectors.
   - Pictures only for photos and maps. Never place an image of text, a chart, a table, or an icon.
4. Put the script for each slide in its speaker notes, not on the slide.

### 6. Style pass

Apply the `google-developer-writing-style` core rules to every headline and note:

- Sentence case, active voice, present tense, and no end punctuation on headlines.
- Spell out abbreviations on first use in the deck and again in the notes.
- Number rules: numerals for measurements, "40%," "50 MHz," and commas in numbers of four or more digits.

Then apply "NTIA writing conventions" above.

NTIA conventions override Google style on these points, matching `ntia-filing`:

- **Frequency ranges**: hyphen, no spaces, unit once: "7125-7400 MHz," "3.98-4.2 GHz."
- **Amounts of spectrum**: spell out the unit: "100 megahertz."
- **Capitalization**: lowercase *federal* except in names and titles. Capitalize *Executive Branch* and *the Commission*.
- **Terms of art**: use them exactly, without synonyms: *harmful interference*, *coordination zone*, *protection criteria*, *federal* and *non-federal*, *primary* and *secondary* allocation. On a slide for a non-technical audience, pair a term of art with a plain gloss rather than replacing it.

Domain conventions kept: band designations, CFR citations, and standard units stay in their official form. Concrete analogies that Made to Stick calls for are allowed for this U.S. audience, as a deliberate departure from Google's no-metaphor rule. Keep them accurate.

### 7. QA and triage

1. Run the `pptx` skill's content, file, and visual QA. Pass `--original` with the template file to `validate.py`.
2. **Template check**: render thumbnails and confirm every slide shows the NTIA master, logo, and footer, that no slide uses a blank layout, and that the master, layouts, and theme are unchanged.
3. **Consistency check** (scripted with `python-pptx`): list every font size, fill color, and text color used, and every shape's left edge and gap. Flag any size outside the type scale, any color outside "Colors" and the mid gray, any left edge off a column edge, any gap off the spacing scale, any picture used as an icon, and any `p:transition` or `p:timing` element.
4. **Taste checks**, slide by slide on the rendered thumbnails:
   - **Squint test**: blur your attention; exactly one hero shows first.
   - **Rams test**: name any element whose removal leaves the point intact, and remove it.
   - **Space test**: at least a third of the content area is empty.
   - **Specificity test**: the slide couldn't be dropped into another agency's deck unchanged; its headline, number, and evidence are specific to this analysis.
   - **Data-ink test**: no chart ink (borders, fills, gridlines, legends) that doesn't encode data.
5. Check every slide against the text limits below and colors against the contrast limits.
6. Score each slide with the Made to Stick slide checklist. Move slides that score 0-1 to the appendix, or cut them.
7. Fix, re-render the changed slides, and stop.

### 8. Deliver

Send the .pptx with `SendUserFile`. In the reply, give one line on the deck, list any GAPs or "Illustration" labels still in it, and suggest the Made to Stick outsider test before the real briefing.

## Slide types

| Type | Preset | Evidence | Notes |
|---|---|---|---|
| Title | Template title layout | Title, subtitle, presenter, date | No acronyms in the title |
| Bottom line | Statement | The takeaway sentence, plus the ask for decision decks | No other content |
| Big number | Hero number | One number with a label and a plain comparison | Optional Isotype block on the right |
| Chart | Third and two-thirds, or full-width evidence | One native chart styled per "Charts" | The headline states the finding |
| Comparison | Cards (two) | Option A and option B, or before and after | Three or fewer short lines per card |
| Options | Cards (two to four) | Option cards with the same short labels, such as benefit, cost, and who must act | Mutually exclusive options; include "no action" when viable |
| Process | Flow | Three to five icon steps | Two to four words per label |
| Table | Full-width evidence | Native table, four or fewer rows and three or fewer columns | Larger tables go to the appendix |
| Map or photo | Third and two-thirds, or full-width evidence | One image with a headline | Respect location-precision limits for the audience |
| Section break | Template section layout | Section name | Use only in decks longer than eight slides |
| Ask | Statement | What, who, and by when | Last main slide of a decision deck |
| Appendix | Any preset, denser | Any of the above | Label "Backup" in the footer |

## Text limits

These limits define a talking deck. If content doesn't fit, cut words or split the slide; don't shrink the font.

- **Headline**: one full-sentence assertion, 12 words or fewer, two lines at most.
- **Body text**: 15 words or fewer per slide outside the headline and chart labels.
- **No bullet lists** on main slides.
- **Sizes**: only the sizes in "Type scale" in `references/brand-and-design.md`.
- **One idea per slide.** If a slide needs "and" in its headline, consider splitting it.
- **Acronyms**: avoid on slides. If one is unavoidable, spell it out in the label; never put one in a title.

## Speaker notes

Each main slide gets notes of about 60-120 words, in this order:

1. **Say**: the point in spoken language, starting with the headline's claim.
2. **Evidence**: what to point at on the slide.
3. **Transition**: one sentence leading to the next slide.
4. **Likely question**: one question this audience may ask, with a short answer.

## Markings and accessibility

- Every evidence slide gets a source line.
- Internal decks carry "PRE-DECISIONAL" in the footer of every slide, and the title slide notes say "Prepared with AI assistance." Remove the marking only when Nick says the deck is final or public.
- Alt text on every chart, picture, icon group, and diagram; 4.5:1 minimum text contrast; 3:1 for large text, icons, and chart elements.

## Revisions

When Nick asks for changes after delivery, edit only the affected slides, keep the rest unchanged, and re-run QA on the changed slides. Don't regenerate the whole deck unless he asks.
