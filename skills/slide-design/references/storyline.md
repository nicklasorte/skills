# Storyline and deck structure

Design starts before the first slide. A deck with beautiful slides and no
spine still fails. Use this file to plan the order of slides, check the
story, and decide what goes to backup. For message craft (simplicity,
concreteness, stories), use `made-to-stick-briefing`. This file covers the
structure that the design depends on.

## Sentence headlines (assertion-evidence)

Every content slide has a sentence headline that states its point, and
visual evidence that supports it: a chart, diagram, map, or image, not a
bullet list. Michael Alley's studies at Penn State found that audiences who
saw assertion-evidence slides understood and remembered the content
significantly better than audiences who saw topic titles with bullets, even
when the spoken content was identical. Presenters who built assertion-evidence
slides also understood their own material better.

Use this research when someone asks for topic titles like "Background" or
"Results."

## Ghost deck first

Before you build any slide, write the ghost deck: a list of slide headlines
in order, one sentence each, with a note on the evidence each slide will
show.

```
1. [Exec summary] Three decisions are needed by March.
2. Coordination zones cover 8% of the band's population. — zone map + big number
3. Smaller zones protect the radars in 98 of 100 cases. — exceedance curve, annotated
4. Smaller zones recover about $2 billion. — waterfall
5. We recommend option B. — options table, B highlighted
```

For decks of three or more slides, show the ghost deck to Nick for approval
before you build the slides. Fixing order and headlines at this stage is
cheap; fixing them after design isn't. When `ntia-talking-deck` is also in
use, its outline table and confirmation gate serve as the ghost deck; don't
ask twice. For one or two slides, state the headline and build.

## Horizontal logic test

Read only the slide titles, in order. They should tell the whole story on
their own. To test a built deck, extract the titles (for example, with
python-pptx) and read them as a list.

- Every title is a sentence that states a takeaway, not a topic label.
- Each title follows from the one before it.
- No title repeats another's point.
- If there's an executive summary, its bullets match the later slide titles,
  in the same order.

## Vertical logic test

On each slide, everything below the title supports that title, and nothing
else. If an element supports a different point, move it to the slide that
makes that point, or cut it.

## Choose a structure

| Situation | Structure |
|---|---|
| Decision briefing for leadership | **BLUF.** Bottom line and the ask first, then the evidence, then options, then next steps. If Nick hasn't given a recommendation, present the options neutrally and mark `[CONFIRM: recommendation]` |
| Update or status | **Situation, complication, resolution.** What's true, what changed, what we're doing |
| Persuasive talk or keynote | **Sparkline** (Nancy Duarte). Alternate "what is" with "what could be" three to five times, then end with the call to action |
| Technical results | **Question, method in one slide, results, implications.** Put the method detail in backup |

For leadership, default to BLUF. Busy decision makers may leave after slide
three, so the ask must come first.

### Sparkline details

- **Beginning:** show you understand the audience's current situation.
- **Middle:** alternate the problem today with the better future, building
  from easier points to the most consequential.
- **One STAR moment** ("something they'll always remember"): a surprising
  number, a vivid comparison, a physical prop, or one powerful visual, placed
  near the climax. Design this slide differently from the rest so it stands
  out: a full-slide big number or a single striking image.
- **End:** describe the better future concretely, and state the call to
  action.

## Backup and appendix slides

Move these to backup:

- Method details, equations, model parameters, and assumptions tables.
- Full datasets and tables larger than four rows × three columns.
- Scenarios other than the baseline, the recommendation, and one
  alternative.
- Charts for technical questions you expect but won't raise.

Rules:

- Put a divider slide titled "Backup" before them, using the template's
  section layout, and label backup slides "Backup" in the footer.
- Give backup slides sentence headlines too.
- On the main slide, you can point to backup in the source line, for example
  "Method: see backup slide B3."
- Number backup slides (B1, B2, …) so you can jump to them in Q&A.

## Speaker notes

Put what you'll say, and the detail you cut from the slide, in the speaker
notes. In presented mode, the notes carry the words; the slide carries the
evidence.
