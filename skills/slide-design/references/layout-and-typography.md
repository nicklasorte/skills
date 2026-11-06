# Layout and typography

Every deck is built on the NTIA template (`DOC NTIA_Style Guide July 2026.pptx`).
The `ntia-talking-deck` skill owns the template mechanics: getting the binary,
the template map, the layouts, and the rules for keeping the master intact.
This file sets the layout and type rules that apply inside the template, and
the matching rules for report and doc figures.

## Slide canvas and grid

- Use the template's slide size and layouts. Never add a blank slide and
  redraw the master's look.
- Work inside each layout's content area, the region free of the logo,
  footer, and master graphics. The template map
  (`claude/ntia-template-map.md` in the project) records it.
- Lay out on a 12-column grid across the content area, with 16 pt gutters.
  Every element's left and right edges sit on a column edge.
- Until the template map exists, use a 12-column grid inside 0.5 in margins
  on the template's slide size, and keep clear of the logo and footer
  areas. Replace it with the mapped content area once the map exists.
- Use only these gaps for spacing, padding, and offsets: 8, 16, 24, 32, 48,
  and 64 pt.
- Keep the headline in the same position on every content slide. The
  evidence starts 32 or 48 pt below it.
- Leave at least a third of the content area empty. White space is what
  makes the focal element stand out.

## Common slide layouts

These match the composition presets in `ntia-talking-deck`. Each has one
focal point.

| Layout | Use for |
|---|---|
| **Statement** | The bottom line or the ask. Headline alone, larger, upper-left third |
| **Hero number** | One number that matters, with a label and a plain comparison |
| **Third and two-thirds** | A short statement or key figure in columns 1–4, evidence in columns 5–12. The default data slide |
| **Full-width evidence** | One chart, table, or map across columns 1–12 |
| **Cards** | Two to four options or comparisons on grey cards |
| **Flow** | Three to five icon steps, left to right |

Avoid four-quadrant layouts, slides with more than one chart (unless they're
small multiples of the same chart), and full-paragraph text slides. Don't use
the same layout on more than two consecutive slides.

## Reading order

People scan a slide in a Z pattern (top left, top right, bottom left, bottom
right) unless something draws their eye first. Put the headline at top left,
the focal visual in the middle, and the source line at bottom left. Set the
same order in the Selection Pane for screen readers.

## Type scale for slides

Use only these sizes. If a template placeholder sets a size, keep the
template's size for that role and use it consistently.

| Role | Size | Weight |
|---|---|---|
| Headline | 32 pt (up to 40 pt on a statement slide) | Bold |
| Body text | 20 pt | Regular |
| Labels: chart labels, card labels, icon captions, annotations | 16 pt | Regular, or bold for a card title |
| Hero number | 96–120 pt | Bold |
| Source line | 11 pt | Regular, dark blue (mid gray fails text contrast at this size) |

If text doesn't fit at these sizes, cut text or split the slide. Don't shrink
it. Read-ahead pages use smaller sizes; see `read-ahead.md`.

## Type sizes for report and doc figures

Size these at the final printed size, not the size in the plotting tool.

| Element | Size at final size |
|---|---|
| Figure title | 10–12 pt, bold |
| Axis labels, data labels, annotations | 8–10 pt |
| Caption (in the document, not the image) | Body text size |

A common error is making a figure in MATLAB at screen size and then scaling
it down to fit the column, which shrinks the fonts. Set the figure size to
the column width first. A single-column figure is about 6.5 in wide in a
standard report with 1-in margins.

## Fonts

- On slides, use the template's theme fonts. Don't set font faces on
  individual runs; set only size and weight.
- The July 2026 NTIA style guide specifies Times New Roman (regular, bold,
  and italic). The older brand book names Archerus Grotesque and Scala; the
  template's theme fonts take precedence over both.
- In report and doc figures made in MATLAB or matplotlib, use Times New Roman
  so figures match the NTIA report template. The helpers in `scripts/` and
  `assets/` do this by default.
- Use sentence case for titles and labels. Don't use all caps except for
  short labels of four words or fewer, and the required marking.
- Left-align text. Never center body text, labels, or numbers, except inside
  a card or a table cell. Never justify text.
- Keep line length under about 60 characters for any block of text.
- Use bold for emphasis, sparingly. Use italics only for titles of works.
  Don't underline anything except hyperlinks in notes.

## Text rules

- Write the headline as a full sentence with a verb. Keep it to 12 words or
  fewer and two lines in presented mode.
- Keep other text to 15 words or fewer per slide in presented mode. Chart
  titles, labels, annotations, the source line, and the marking don't count.
  Don't use bullet lists on main slides.
- Avoid acronyms on slides. Never put one in a title. If one is
  unavoidable, spell it out in the label. Standard unit abbreviations (km,
  MHz, GHz, dB) aren't acronyms and are allowed everywhere.
- Round numbers to the precision the decision needs, and use the same
  rounded form everywhere (see "Numbers" in SKILL.md).

## Alignment and grouping (Gestalt)

- **Proximity:** items placed close together read as a group. Use spacing
  before you add boxes or dividers.
- **Similarity:** items that look alike read as related. Same color means
  same thing.
- **Enclosure:** a light grey card or shaded area groups items strongly. Use
  it for a takeaway box or to mark a region on a chart.
- **Continuity and alignment:** elements on the same line read as a set. Line
  up edges and baselines.
- **Figure and ground:** the focal element needs strong contrast with the
  background. Everything else gets less contrast.

## Images and photos

- Use a photo only if it shows something real that supports the headline,
  such as the actual site or the actual equipment. NTIA photos show real
  people and real technology; no stock clichés.
- Use one photo per slide at most. Crop it to grid edges. Don't put a
  border, rounded corners, or a shadow on it.
- Don't search for or insert photos of real people.
