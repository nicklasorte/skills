---
name: "slide-design"
description: Visual design and data visualization rules for every slide, deck, read-ahead, chart, map, table, dashboard, and figure the user makes, presented or read, in decks, reports, memos, or docs. Always uses the NTIA template and brand and marks everything DRAFT//PRE-DECISIONAL. Covers ghost decks, layout, NTIA color, number consistency, a chart-type catalog, annotation, uncertainty, maps, tables, decluttering, honest scales, Section 508, and turning technical results (dB, CDFs, coverage maps, Monte Carlo output) into visuals non-technical leaders get at a glance. Use it whenever you build or revise slides, a deck, a read-ahead, a chart, plot, figure, map, table, tracker, or diagram, or when the user asks to make a visual clearer or better, even if the user doesn't mention design. Load it with dataviz for any chart; where they conflict, this skill wins. Works alongside ntia-talking-deck (template mechanics), made-to-stick-briefing (message), and matlab-builtin-first (plot code).
---

# Slide design

This skill is the design layer for anything visual: slides, decks, and the
figures that go into reports, memos, and docs. It decides how a visual looks
and how it shows data. Other skills keep their own jobs:

| Concern | Owner |
|---|---|
| NTIA template mechanics (getting the binary, the template map, keeping the master intact) and NTIA writing conventions | `ntia-talking-deck` |
| The message, story, and memorability | `made-to-stick-briefing` |
| Personal stories in a talk | `storyworthy-talks` |
| MATLAB plotting code | `matlab-builtin-first` |
| File mechanics for .pptx and .docx | `pptx` and `docx` |
| General chart mechanics (form heuristics, palette validation, mark specs) | `dataviz` |
| Everything about how it looks and how data is shown | This skill |

## NTIA template and brand

Everything the user makes uses the NTIA template and the NTIA brand, with no
exceptions: leadership briefings, conference talks, read-aheads, report
figures, and one-off charts.

- **Decks** are built on `DOC NTIA_Style Guide July 2026.pptx`, following
  "NTIA template" in `ntia-talking-deck` (get the binary, use the template
  map, keep the master, layouts, theme, logo, and footer intact). Never build
  a deck off-template. If the template binary isn't available, ask the user to
  attach it and stop until the user does. This rule outranks the build-without-
  waiting rule for one- or two-slide requests: any slide needs the template.
  A standalone figure (an image for a report or an email) doesn't.
- **Colors** come from the NTIA palette in `references/color.md`: mid gray
  for context, light blue for the one highlight, purple only for a second
  highlight or an alert, and dark blue for text.
- **Fonts** are the template's theme fonts on slides, and Times New Roman in
  report and doc figures (the July 2026 NTIA style guide).
- **Source lines** are 11 pt dark blue, regular. Mid gray fails the 4.5:1
  text contrast rule at that size, so this skill overrides the mid-gray
  source line in `ntia-talking-deck`.
- **Light blue text** follows the brand file: 24 pt or larger, or bold.
  Annotations and labels in light blue at 16 pt must be bold.
- **Units aren't acronyms.** Standard unit abbreviations (km, MHz, GHz, dB)
  are allowed in titles and on slides. The no-acronyms rule applies to
  organizations, programs, and technical terms such as I/N.
- **Brand values** (palette, logo, voice, writing conventions) are defined in
  `ntia-talking-deck`'s `references/brand-and-design.md`. If this skill and
  that file disagree on a brand value, that file wins. On everything else
  (chart choice, annotation, uncertainty, maps, tables, read-ahead mode),
  this skill governs.

## Marking

- Mark every deck, read-ahead, report, memo, and doc **DRAFT//PRE-DECISIONAL**,
  exactly in that form, in all caps.
- **Slides:** on every slide, including the title slide and backup slides, in
  the template's footer area. If the footer has no free placeholder, add a
  small text box (11 pt, dark blue, bold) at the bottom of the content area
  that doesn't cover master elements.
- **Reports, memos, and docs:** in the header and the footer of every page.
- **Standalone figures** sent on their own (for example, a PNG in an email):
  add the marking in small type at the top of the image.
- Keep the marking even when the user calls a product final. Remove it only if
  the user explicitly says to remove the marking from that product.
- Don't add CUI or classification markings.
- This rule supersedes the "PRE-DECISIONAL" footer rule in
  `ntia-talking-deck`, including its rule to drop the marking when a deck is
  final.
- On slides, the marking and the source line share the bottom row: source
  line at the left of the content area, marking at the right.

## Working with dataviz

When you make a chart, load both this skill and `dataviz`. Use `dataviz` for
its methods, such as validating a palette or speccing marks. Where the two
conflict, this skill takes precedence for the user's work. For example, this
skill's gray-plus-one-accent approach, NTIA palette, native PowerPoint
charts, audience defaults, and Section 508 rules win over `dataviz`
defaults.

## Defaults

Apply these unless the user says otherwise:

- **Audience:** non-technical decision makers, such as political appointees
  and senior leadership. They're smart and busy, and they aren't engineers.
  They need the "so what," not the method.
- **Mode:** presented, with low text density. The slide supports the
  speaker; it doesn't replace the speaker. Put detail in speaker notes or
  backup slides.
- **Read-ahead mode:** when the user says the deck is a read-ahead, pre-read, or
  leave-behind, or will be sent without the user presenting, follow
  `references/read-ahead.md`. Pages carry more explanation but keep the same
  visual rules. If the mode is unclear, ask.
- **Accessibility:** every deck and report meets Section 508. See
  `references/accessibility-508.md`.
- **Icons and diagrams:** native PowerPoint shapes only. Don't use pictures,
  SVGs, or icon sets. See `references/native-shapes.md`.
- **Animation:** none. Don't add slide transitions or build animations.
- **Technical audiences** (for example, a MILCOM or IEEE talk): still use the
  NTIA template and the same visual rules, but you can show more of the
  method, use technical units, and allow one denser chart per slide.

## Workflow

Follow these steps in order. Most bad slides come from skipping step 1.

1. **Write the headline first.** For every slide or figure, write the one
   sentence you want the audience to remember. This becomes the slide title
   or figure title. If you can't write it, the slide doesn't have a point
   yet, so don't design it. For a deck of three or more slides, write the
   ghost deck (all headlines in order, with the evidence for each), check it
   with the horizontal logic test, and get the user's approval before building.
   For one or two slides, or a single figure, state the headline in your
   reply and build without waiting. See `references/storyline.md`.
2. **Pick the visual that proves the headline.** Ask what the audience must
   see to believe the sentence. Use the decision table in this file, then
   `references/chart-types.md` for detail. Sometimes the answer is one big
   number, a simple diagram, or nothing but the headline.
3. **Translate technical content.** If the data is technical (dB, CDFs,
   I/N, probabilities, distances), read `references/technical-to-plain.md`
   and convert it to terms the audience already uses. If the result has
   spread, read `references/uncertainty.md`.
4. **Lay it out.** Use the grid, type sizes, and white-space rules in
   `references/layout-and-typography.md`. Use the gray-plus-one-accent color
   approach in `references/color.md`.
5. **Build, then declutter and annotate.** Build charts as native, editable
   charts when the tool supports it. Strip them using
   `references/decluttering.md`, then add one to three annotations that
   prove the headline (`references/annotation.md`). For helper code, see
   `scripts/`.
6. **Check honesty.** Run the scale and baseline checks in
   `references/honesty.md`.
7. **Make it accessible.** Add alt text, set the reading order, and run the
   checks in `references/accessibility-508.md`.
8. **Review.** Run `references/checklist.md` on every slide or figure before
   you hand anything over. Render the slides to images and look at them. Fix
   what you find, then check again.

## Core visual rules

1. **One idea per slide.** If a slide makes two points, split it.
2. **Titles are sentences that state the takeaway.** Write "Coordination
   zones cut auction revenue by more than a third," not "Revenue impact."
   Check that the wording matches the number: "about a third" for 37.7% would
   understate it.
3. **Pass the three-second glance test.** Someone glancing at the slide for
   three seconds should know what it's about and where to look first.
4. **Keep text short.** In presented mode, a slide holds a headline of 12
   words or fewer and at most 15 words of other text. Chart titles, axis and
   data labels, annotations, the source line, and the marking don't count
   toward the 15.
   Zero other words is often better. Don't use bullet lists on main slides.
   Read-ahead mode allows more; see `references/read-ahead.md`.
5. **Use white space on purpose.** Empty space is what makes the important
   element stand out. Don't fill it.
6. **Align everything to a grid.** Every element's edge lines up with
   something else. Misaligned elements look careless even when the viewer
   can't say why.
7. **Group by proximity.** Put related things close together and unrelated
   things far apart. Distance carries meaning, so use it before you add boxes
   or lines.
8. **Repeat consistently.** The same kind of thing looks the same on every
   slide: same position for titles, same color for the same series, and same
   label style.
9. **Create one focal point.** Use size, color, or position to make one
   element dominant. If everything is emphasized, nothing is.
10. **Nothing is decorative.** Every element earns its place by helping the
    headline. Remove clip art, stock photos that only set a mood, gradients,
    shadows, 3D effects, and accent lines under titles. Keep the template's
    logo and footer exactly as the master places them.

## Core data visualization rules

1. **The chart title is the takeaway.** Use the headline sentence, not a
   description of the axes.
2. **Choose encodings by accuracy.** People compare positions on a common
   scale most accurately, then lengths, then angles, then areas, then color
   intensity (Cleveland and McGill). Prefer bars, dots, and lines over pies,
   bubbles, and color shading when the comparison matters.
3. **Gray everything, then color one thing.** Draw context in mid gray
   (`#8A8D91`) and the series or bar that carries the message in NTIA light
   blue (`#5674C4`). Mid gray and light blue are close in lightness, so
   always label the highlighted mark directly ("Recommended," "20 km
   zone"). The direct label, not the color difference alone, carries the
   distinction. This is a deliberate exception to `dataviz` palette
   validation.
4. **Label directly.** Put series names at the end of lines and values on or
   next to bars. Remove the legend whenever you can.
5. **Maximize the data-ink ratio.** Remove borders, background fills, heavy
   gridlines, tick marks, and redundant axis labels (Tufte). Keep only what
   helps someone read the data.
6. **Annotate the point.** Add a short text callout on the chart at the place
   the audience should look, such as "Interference threshold" or "Auction
   closes."
7. **Be honest about scale.** Bar charts start at zero. Don't use dual y-axes.
   Label any log scale clearly. See `references/honesty.md`.
8. **Show fewer data.** Show the comparison that proves the headline. Move
   the full dataset to an appendix or backup slide.
9. **Make it readable from the back of the room.** Chart text on slides is
   16 pt. Chart text in documents is at least 8 pt at final size.
10. **Make it work in grayscale and for colorblind viewers.** Never let
    color be the only cue. Use the NTIA palette and scales in
    `references/color.md`.

## Numbers

The same number must look the same everywhere it appears: on the slide, in
the speaker notes, in the read-ahead, and in the report.

- **Keep a numbers ledger.** When a deck, read-ahead, or report uses more
  than a few key figures, list each one once, with its exact value, its
  source, and the single rounded form you'll use: for example, "Revenue at
  risk: $4.213B (model run 2026-10-21) → about $4 billion." Use that
  value and rounding everywhere. Put the ledger in the speaker notes of the
  first backup slide; if there's no backup, in the notes of the last slide;
  in a report, in the methods appendix. Also give it to the user with the
  deliverable.
- **Same value, not same glyph.** NTIA style spells out zero through nine in
  running text and headlines ("four in 1,000"), while chart labels use
  numerals ("4"). That's consistent. Changing the value or the rounding
  isn't.
- **Pick one denominator for rates.** Use "per 100" or percentages for
  rates of 1% and up, and "per 1,000" when any rate in the comparison is
  below 1%. Use the same denominator for every option in a comparison and
  across the deck.
- **Derive from exact values.** Compute percentages, differences, ratios,
  and icon counts from the exact values in the ledger, then round once.
  Round icon counts to whole icons and say so ("each figure = 1 million
  people, rounded"). Round percentages to whole numbers unless a decimal
  changes the decision.
- **Label decimals consistently.** Within one chart, use the same number of
  decimals on every label, with enough decimals that no nonzero value shows
  as zero (show "$0.02B," not "$0.0B").
- **Round to the decision's precision,** and to the model's uncertainty (see
  `references/uncertainty.md`).
- **Make totals add up.** If parts are rounded, check that they still sum
  to the rounded total, or footnote the difference.
- **Use one unit per quantity** across a product: don't switch between "MHz"
  and "megahertz," "km" and "miles," or "$4B" and "$4 billion." Follow the
  NTIA number conventions in `ntia-talking-deck` (for example, spell out
  zero through nine except with units, and write amounts of spectrum as
  "100 megahertz").
- **Recheck derived numbers** (percentages, ratios, icon counts) by running
  the arithmetic, not by eye.

## Quick chart chooser

Start from the message, not the data. For the full catalog of chart types,
including when not to use each one, see `references/chart-types.md`.

| If the message is... | Start with... |
|---|---|
| One number matters | Big number with a one-line context |
| A is bigger than B (few items) | Bar chart, sorted |
| Each item against its own benchmark | Bar chart with reference marker |
| Ranking of many items | Sorted horizontal bar or dot plot |
| Above or below a target or limit | Diverging bar |
| Change over time | Line chart |
| Gap between two series over time | Surplus/deficit filled line |
| Before versus after for several items | Slope chart or dumbbell chart |
| Parts of a whole (two to four parts) | Single stacked bar or waffle chart |
| Parts of a whole (many parts) | Sorted bar chart (not a pie or donut) |
| A subset inside its total | Nested shading |
| How a total builds up or breaks down | Waterfall chart |
| Spread or distribution | Histogram, strip plot, or beeswarm |
| Monte Carlo or forecast spread, for leadership | Quantile dotplot or range bar |
| Probability of exceeding a level | CDF or exceedance curve, annotated |
| Concentration ("a few account for most") | Cumulative curve or sorted bar |
| Relationship between two measures | Scatter plot |
| Where something happens | Map (choropleth, points, or zones); see `references/maps.md` |
| How big something is | Scale comparison against a familiar area |
| Frequencies and who uses them | Band plan (horizontal bars on a frequency axis) |
| When something is in use | Time-of-day heatmap |
| How things move between states | Paneled alluvial or Sankey |
| Process, sequence, or flow | Flow diagram |
| Schedule, milestones, or durations | Timeline, Gantt chart, or duration timeline |
| Many small comparisons of the same kind | Small multiples |
| Status against targets, at a glance | Dashboard; see `references/dashboards.md` |
| Exact values people will look up | Table; see `references/tables.md` |

## Figures in reports and docs

The same rules apply, with these changes:

- **Report figures:** the image holds only the chart and its annotations.
  The takeaway title, the caption, and the source line go in the document as
  text (for example, a Word caption), so they stay editable and searchable.
  The image carries no marking; the document's header and footer do.
- **Standalone figures** (an image sent by email or pasted elsewhere): the
  image holds the takeaway title, the chart, the source line, and
  DRAFT//PRE-DECISIONAL at the top.
- The figure title still states the takeaway. Put method details in the
  caption, which can be one to three sentences.
- Add a source line under each figure, for example "Source: NTIA analysis of
  ... (2026)."
- Size the figure to the text column, and set fonts so they're 8–10 pt at
  final printed size.
- Export EMF for Word when the tool can (MATLAB `exportgraphics` can).
  From Python, export SVG for Word 365 and PDF for LaTeX or PDF reports, plus
  a 300 dpi PNG as a fallback. Don't crop to the content (`bbox_inches="tight"`)
  when the figure must be exactly the column width; use constrained layout
  instead.
- Use the NTIA palette and Times New Roman, so figures match the NTIA report
  template.
- Add alt text that states the takeaway and the chart type.
- Number figures and refer to each one in the body text before it appears.
- Mark the document DRAFT//PRE-DECISIONAL in the header and footer.

## Reference files

Read only the files you need for the task:

| File | Read when |
|---|---|
| `references/storyline.md` | Planning a deck: ghost deck, horizontal logic, structure, backup slides |
| `references/read-ahead.md` | The deck will be read without the user presenting it |
| `references/chart-types.md` | Choosing a chart type, or the user asks what charts to use |
| `references/layout-and-typography.md` | Laying out a slide or figure, and setting sizes and fonts |
| `references/color.md` | Choosing any color or palette |
| `references/decluttering.md` | Cleaning up a default PowerPoint, Excel, MATLAB, or matplotlib chart |
| `references/annotation.md` | Adding labels, callouts, reference lines, or highlights |
| `references/honesty.md` | Setting axes, scales, or baselines |
| `references/uncertainty.md` | Showing ranges, Monte Carlo spread, forecasts, or error bars |
| `references/technical-to-plain.md` | The content is technical and the audience isn't |
| `references/maps.md` | Making any map |
| `references/tables.md` | Making any table |
| `references/dashboards.md` | Building a status slide, tracker, or dashboard |
| `references/native-shapes.md` | Drawing icons, callouts, or diagrams in PowerPoint |
| `references/accessibility-508.md` | Finishing any deck or report (always) |
| `references/checklist.md` | Reviewing any finished slide or figure (always) |

## Helper code

- `scripts/pptx_chart_style.py`: `style_chart()` declutters a python-pptx
  chart and applies the NTIA gray-plus-light-blue approach. `set_alt_text()`
  adds Section 508 alt text to any shape, chart, or group. `strip_effects()`
  removes theme-inherited shadows from native shapes.
- `scripts/briefing_style.m`: applies the same look to a MATLAB axes for
  report figures and backup slides.
- `assets/briefing.mplstyle`: a matplotlib style file with the same look.

Prefer native PowerPoint charts on slides, because they stay editable. Use
MATLAB or matplotlib images for charts PowerPoint can't draw, such as maps,
contour plots, and CDFs with many points.
