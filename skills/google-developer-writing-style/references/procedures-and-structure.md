# Procedures and document structure

Paraphrased from the Google developer documentation style guide (CC BY 4.0): Procedures, Lists, Headings and titles, Notices, Cross-references.

## Contents
- Procedures
- Lists
- Headings and titles
- Notices
- Cross-references and links
- Tables

## Procedures

A procedure is a numbered sequence of steps for one task.

**Introducing the procedure**
- Usually introduce it with a sentence that adds context beyond the heading. If the heading already says everything, skip the intro rather than repeat it.
- The intro must be a complete sentence or an imperative, never a fragment the steps complete.
  - Good: "To customize the buttons, follow these steps:" / "To customize the buttons, do the following:" / "Customize the buttons:"
  - Bad: "To customize the buttons:"
- End with a colon if the steps follow immediately; a period if a note or paragraph comes between.

**Step content**
- Each step starts with an imperative verb and is a complete sentence.
- One action per step. Sequential menu clicks can share a step with `>`: "Click **File > New > Document**."
- Put the location before the action, and the goal before the action: "In the console, go to the **Monitoring** page." / "To start a new document, click **File > New**." *(Skill addition: when a step has both, location → goal → action usually reads best.)*
- If the goal phrasing ("To sort the data…") could make a required step look optional, use the colon form: "Sort the data by date: click **Sort**."
- State the result after the action, in the same paragraph: "Click **Run**. The query results appear." Fold the result into the next step when that's cleaner ("In the **New file** dialog that appears, click **Next**").
- Justifications come after the action: "Store the key in a secure location. You need it later."
- Optional steps start with "Optional:" — not "(Optional)".
- If the reader must press Enter, include it in the step.
- Don't use directional words (*above*, *below*, *left*, *right-hand*). Use *preceding*/*following*, or name the element.
- Don't introduce commands with "Run the following command:". Say what the command does: "Create the bucket:".
- Don't include keyboard shortcuts in steps ("Copy the command, and then paste it," not "Press Ctrl+C, and then press Ctrl+V"). Don't use *please*.
- Don't use UI labels as verbs: "To save the settings, click **Save**," not "**Save** the settings."

**Complex steps** — use this order inside one step:
1. The action.
2. The command (code block).
3. Placeholder explanations ("Replace `NAME` with…").
4. Further explanation of the command, if needed.
5. Example output ("The output is similar to the following:").
6. In a separate paragraph, what the result means.

**Sub-steps**: lowercase letters (a, b, c), then lowercase Roman numerals. A step with sub-steps ends with a colon or period like an intro sentence.

**Single-step procedures**: write as one sentence in a bulleted item, not "follow this step: 1."

**Other rules**
- Give one way to do a task — the shortest, most accessible (keyboard-only works) path. Put alternatives in separate sections or tabs if they must exist.
- Don't repeat a procedure; link to it.
- Put prerequisites before the steps so the reader can prepare.
- Restate the context ("In the console…") at the start of each procedure under a new heading.

## Lists

**Choosing a type**
- Numbered: sequence matters (steps, phases, ranked priorities).
- Bulleted: no sequence. Make clear whether every item is required.
- Description list: term + explanation pairs. In Markdown use bulleted run-in headings: `- **Term**: description`.
- Don't make a one-item list.
- Use a table instead when items share several attributes you'd compare across.

**Intro sentences**: complete sentence; "the following" is fine as a noun ("Use the button for any of the following purposes:").

**Capitalization and punctuation**
- Capitalize each item's first word (unless case is meaningful, like code).
- Period at the end of items that are sentences or contain a verb.
- No end punctuation for: single words, verbless phrases, items entirely in code font, items that are only a link or title.
- If that produces a mixed list, rewrite for parallelism or punctuate every item.

**Run-in headings**
- Capitalize the heading; end it with a colon or period, consistently within the list.
- After a colon: lowercase start; period only if the description has a verb or is a full thought.
- After a period: capital start; end with a period.
- Don't use a dash between term and description.

**In-sentence lists**: serial comma. Don't end with *etc.* or *and so on*; instead signal non-exhaustiveness up front ("such as," "including").

## Headings and titles

- Sentence case.
- Title reflects the document's main purpose. Task pages: bare-verb titles ("Create an instance"). Concept pages: noun phrases ("Instance lifecycle").
- Mixed documents can mix heading types per section.
- Avoid *-ing* as the first word ("Transfer data," not "Transferring data"). Gerund nouns like *Billing* or *Pricing* are fine; *-ing* later in the heading is fine.
- Optional sections: prefix "Optional: Customize your alias".
- One H1 per page; unique headings; don't repeat the page title as a section heading.
- No numbers for sequence, no links, minimal punctuation. Avoid code in headings; if unavoidable, add a noun ("The `init` method").
- Abbreviations in headings only if more common than the long form; define in the first paragraph after.
- Don't skip levels (H2 → H4). Don't leave a heading with nothing under it before the next subheading — add an intro sentence.
- To refer to a group of subsections, write "the following sections," not "this section" or "these sections."

## Notices

Readers often skip notices. Write the content as ordinary text first; promote it to a notice only if it truly sits outside the flow.

| Type | Use for |
|---|---|
| **Note** | Relevant but not necessary info. The reader succeeds even if they skip it. |
| **Caution** | Proceed carefully; a risky but not destructive choice. |
| **Warning** | Don't do this, or this is irreversible: data loss, money loss, security exposure. |
| **Success** | Only in interactive content, to confirm success. |

Don't use a note for: prerequisites, a required step, expected results, cross-references, or text that just continues the paragraph. Avoid back-to-back or nested notices — reorganize instead.

## Cross-references and links

- Prefer giving brief context on the page over sending the reader away (define a term, explain briefly, give a couple of steps).
- One link per destination per page unless the page is long or the link serves different sections.
- Link text: the destination's exact title, or a short descriptive phrase with key words first. It must make sense out of context.
- Never: "click here," "this document," "this page," "this blog post," or a raw URL as link text (legal docs excepted).
- Standard form: "For more information, see [Title]." or "For more information about *topic*, see [Title]." Use *about*, not *on*. Use *see*.
- Include abbreviations inside the link text: "[Google Kubernetes Engine (GKE)]".
- Say when a link downloads a file (and its type), opens email, or jumps within the page ("see the *X* section of this document").
- Don't force new tabs; if unavoidable, say "(opens in a new tab)".
- Put trailing punctuation outside the link. No quotation marks around link text.
- Unlinked references: quotation marks for sections or short works; italics for full-length works.

## Tables

- Use for data with multiple attributes per item; use lists for simple sets or sequences. A one-column table should be a list.
- Introduce each table with a sentence ("The following table lists…"). Don't put a table in the middle of a sentence or in the middle of a numbered procedure.
- Sentence-case column headers with no end punctuation.
- Don't merge cells. Sort rows in a logical or alphabetical order.
- Don't use tables to lay out code snippets.
- If a document has several tables, caption them "**Table 1.** Description" and refer to them in lowercase ("see table 2").
- *(Skill addition)* Keep cells short where you can; long cells are harder to scan.
- It's OK to abbreviate months and days in tables (Sep 3, 2018) if you do it consistently.
- Rates may use a slash in tight table cells (requests/day) even though prose uses *per*.
