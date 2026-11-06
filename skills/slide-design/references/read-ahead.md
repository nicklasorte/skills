# Read-ahead mode

Some decks are read, not presented: read-aheads sent to political appointees
before a meeting, leave-behinds, and decks circulated by email. Nobody is
there to explain them. Nancy Duarte calls these slidedocs: visual documents
that pair words and images so the reader can follow them alone. Edward Tufte
makes the same argument for serious talks: give people a handout dense enough
to study.

Use read-ahead mode when the user says the deck is a read-ahead, a leave-behind,
a pre-read, or will be sent without the user presenting it. Otherwise, use
presented mode (the default).

Read-ahead mode has its own type scale (below). Use only those sizes; the
presented-mode scale in `layout-and-typography.md` doesn't apply.

**Page count:** when the user names a number of pages, it includes every page.
The first page is the executive summary, which carries the title and the
ask; don't add a separate title slide unless the user asks for one.

## What changes

| Rule | Presented mode | Read-ahead mode |
|---|---|---|
| Headline | Sentence, 12 words or fewer | Sentence, up to about 20 words |
| Other text | 15 words or fewer, outside chart labels | About 75–120 words, in short blocks |
| Explanations | In speaker notes | On the page, next to the evidence |
| Annotations per chart | One to three | Up to five |
| Headline size | 32 pt | 28 pt |
| Body text size | 20 pt | 16 pt |
| Chart text size | 16 pt | 14 pt |
| Source line | 11 pt | 11 pt |
| Tables | Four rows × three columns or fewer | Up to about 12 × 6 |
| Sources and caveats | Source line only | Source line plus the caveats that matter |
| Backup | Separate section | Can be an appendix the reader flips to |

## What stays the same

- One point per page, stated in a sentence headline.
- Visual evidence first; text explains the visual, not the other way around.
- Gray plus light blue, decluttered charts, honest scales.
- Grid alignment and generous white space. Denser doesn't mean crowded.
- NTIA template and palette, native shapes, no animation, Section 508
  checks, and the DRAFT//PRE-DECISIONAL marking on every page.
- Horizontal logic: the titles alone still tell the story.

## Page patterns

- **Evidence + explanation:** the third-and-two-thirds preset, mirrored:
  evidence in columns 1–8, and in columns 9–12 a short block that says what
  the chart shows, why it matters, and what to decide. Use the same side for
  every page in the deck.
- **Numbered takeaways:** three short numbered blocks, each with a bold
  lead-in phrase and one or two sentences, beside one supporting visual.
- **Annotated chart:** a full-width chart with three to five callouts that
  walk the reader through it.
- **Decision page:** options in a simple table and one sentence per option
  on the trade-off. Highlight a recommended option only if the user gave one.
  If the user didn't, highlight nothing, state the decision needed, and put
  `[CONFIRM: recommendation]` in the notes.

## Writing on the page

- Lead each text block with its point in bold, then support it.
- Write short sentences in plain language. Apply Google developer
  documentation style.
- Spell out every acronym on first use; readers can't ask.
- Put the executive summary page first, with the ask.

## Notes and the numbers ledger

Nobody presents a read-ahead, so the speaker notes don't hold a script. Use
them for sources, caveats too detailed for the page, and, on the last page,
the numbers ledger. Also deliver the ledger to the user with the deck.

## Uncertainty without ranges

If the analysis gives a single value per option, say so once in a caveat
("The analysis gives one value per option, with no range.") and round to
the precision the model supports. Don't invent ranges.

## Hybrid decks

When a deck is both presented and sent afterward, build the presented
version, and put the read-ahead explanation in the speaker notes. Export to
PDF with notes ("Notes Pages") for the leave-behind. If the audience needs
real pages, build a separate read-ahead version instead of cramming the
presented slides.
