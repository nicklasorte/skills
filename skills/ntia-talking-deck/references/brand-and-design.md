# NTIA brand rules and modern look

Part of the ntia-talking-deck skill. Read this whole file before step 5 (Build) and again during step 6 (Style pass). Section names match the references in SKILL.md.

## NTIA brand and style rules

The template's theme and master take precedence. Use these rules to check the template and to word every slide and note.

### Colors

| Name | RGB | Hex | Use |
|---|---|---|---|
| Dark blue | 22, 51, 83 | #163353 | Text, headlines, icons, dark backgrounds |
| Light blue | 86, 116, 196 | #5674C4 | The one highlight per slide: chart series, icon, shape, or large text |
| Logo light blue | 97, 126, 204 | #617ECC | Logo on dark backgrounds only; don't use elsewhere |
| Grey | 232, 233, 234 | #E8E9EA | Card and panel fills only |
| Purple | 110, 79, 146 | #6E4F92 | Second highlight, only when a slide must compare two highlighted items |
| Yellow | 217, 207, 160 | #D9CFA0 | Fill only, behind dark blue text |

The brand book labels the palette primary, secondary, and accent and shows 70%, 20%, and 10% weights, but the extracted text doesn't tie each weight to a color. Treat dark blue and light blue as the core pair and the rest as supporting. Use `[CONFIRM: palette roles]` only if a slide depends on it.

Contrast limits (Section 508, 4.5:1 for text, 3:1 for large text and graphics):

- Light blue on white is about 4.5:1. Use it for text only at 24 pt or larger or in bold; use it freely for chart fills, icons, and shapes.
- Grey and yellow on white fall below 3:1. Never use either for text, lines, icons, or chart series on white.
- For context chart series and secondary text, use a neutral mid gray of at least 3:1 on white, such as #8A8D91. This gray isn't a brand color; use it only for context.

### Fonts

- Use the template's theme fonts. Don't set font faces on individual runs; set only size and weight.
- The July 2026 style guide specifies Times New Roman (regular, bold, and italic). The older brand book specifies Archerus Grotesque and Scala. If the theme fonts differ from Times New Roman, note it in the template map and keep the theme fonts.

### Logo

- Use only the logo already in the template's master. Never draw, retype, or import a logo.
- Never recolor, ghost, crop, rotate, or set the wordmark in another typeface.
- Use the white logo on dark backgrounds and the main logo on white. Never put the white logo on a light background or the main logo on a dark one.

### Photos

Photos show real people and real technology at NTIA touchpoints: bright and realistic. No stock clichés.

### Voice

The brand voice is a sage: evidence-based, objective, analytical, and plain. Good tone words: *analysis*, *data*, *evidence*, *guidance*, *research*, *counsel*, *convene*. Use them as a tone check, not as slogans.

The brand book's secondary "ruler" archetype says NTIA speaks for the administration. The policy-neutrality rule in step 3 still wins: stay administration-neutral unless Nick supplies the framing and asks.

### NTIA writing conventions

Apply these in step 6, along with Google style:

- **Federal, state, local**: lowercase when generic; capitalize only in a specific name or title or a direct statutory quote.
- **internet**: always lowercase.
- **Acronyms**: spell out on first use. Never put an acronym in a title; a section heading can use one already spelled out. On talking-deck slides, keep the stricter rule: avoid acronyms on slides.
- **Numbers**: spell out zero through nine, except with units of measurement ("5 MHz"), at the start of a sentence (always spelled out), and in titles (usually spelled out). Money: "$9.27," and "$9" when there are no cents.
- **Dates**: "March 1," never "March 1st." Use "the 1st of March" only when the ordinal comes before the month. Numeric dates use two digits each: "03/01."
- **Seasons**: lowercase.
- **Time**: "3 p.m. ET." Always give the time zone, and don't specify standard or daylight time. Use "5 PM ET" only in What/Where/When event listings.
- **URLs**: on slides, a short in-text URL is fine because viewers can't click, such as "NTIA.gov." Don't include sentence-ending punctuation in the URL.
- **Link text**: in notes or handouts, link a few descriptive words, never "click here" or "read more," never more than a sentence, and keep each link's text unique.

## Modern look

The modern feel comes from composition, scale, white space, and discipline, inside the template. It never comes from decoration, effects, or motion.

### Principles and their sources

| Principle | Source | What it means on a slide |
|---|---|---|
| Less, but better | Dieter Rams (Braun) | Every element must carry the point. If removing it leaves the point intact, remove it. |
| Emptiness is the frame | Kenya Hara (Muji) | Leave at least a third of the content area empty. White space is designed, not leftover. |
| One hero per slide | Apple keynotes | Each slide has one thing the eye lands on first: a number, a highlighted series, or a sentence. |
| Grid, flush left, asymmetry | Josef Müller-Brockmann (Swiss style) | Align everything to a 12-column grid. Text is flush left, ragged right. Prefer off-center compositions. |
| Few sizes, strict system | Massimo Vignelli (NPS Unigrid) | Three working type sizes, one hero size, one source size. Nothing else. |
| Consistency is the brand | NASA Graphics Standards Manual (1975); U.S. Web Design System | Same positions, sizes, and spacing on every slide of the same type. |
| Geometric pictograms | Otl Aicher (Munich 1972); AIGA and DOT symbol signs (1974); Susan Kare | Icons from a few simple shapes, one style, readable at small size, meaning without words. |
| Count with pictures | Otto Neurath (Isotype) | Show quantity as repeated identical icons, one icon per stated unit. |
| Gray first, then color | Cole Nussbaumer Knaflic (*Storytelling with Data*) | Make everything gray, then color only what makes the point. |
| Editorial charts | Financial Times visual journalism | The headline states the finding, labels sit on the data, one annotation, and a one-line source. |

Borrow principles only. Never reproduce another organization's artwork, icons, or logos. The DOT symbol signs are public domain, but still redraw any concept from native shapes.

### Grid and spacing

- **Columns**: 12 columns across the layout's content area, with 16 pt gutters. Column width = (content width − 11 × 16 pt) / 12. Every element's left and right edges sit on a column edge.
- **Spacing scale**: use only 8, 16, 24, 32, 48, and 64 pt for gaps, padding, and offsets.
- **Alignment**: one shared left edge for the headline and the main evidence on each slide. Never center body text, labels, or numbers, except text inside an icon card or a table cell where centering reads better. Never justify text.
- **Vertical rhythm**: the headline sits at the same position on every content slide; the evidence starts 32 or 48 pt below it.

### Type scale

| Role | Size | Weight | Line spacing |
|---|---|---|---|
| Headline | 32 pt | Bold | 1.1 |
| Body | 20 pt | Regular | 1.2 |
| Label (chart labels, card labels, icon captions) | 16 pt | Regular, or bold for a card title | 1.2 |
| Hero number | 96-120 pt | Bold | 1.0 |
| Source line | 11 pt | Regular, mid gray | 1.1 |

If a template placeholder sets a size, keep the template's size for that role and use it consistently. Use italic only for titles of works. No underline except hyperlinks in notes. No all caps except a short label of four words or fewer.

### Composition presets

Every slide uses one of these six compositions. Name the preset for each slide in the outline.

1. **Statement**: the headline alone, set larger (up to 40 pt), in the upper-left third, with the rest empty. For the bottom line and the ask.
2. **Hero number**: one number at 96-120 pt, flush left in columns 1-7; a 20 pt label under it; a 16 pt plain comparison under that, such as "about the size of Rhode Island." The right side stays empty or holds one Isotype block.
3. **Third and two-thirds**: the headline across the top; a short supporting statement or key figure in columns 1-4; the evidence (chart, map, photo, or Isotype) in columns 5-12.
4. **Full-width evidence**: the headline across the top; one chart, table, or map across columns 1-12; the source line below.
5. **Cards**: two to four grey cards of equal width with 16 pt gutters and 24 pt inside padding. Each card has an icon at the top left, a 16 pt bold title, and two lines or fewer of 16 pt text. Highlight one card's icon in light blue only if one option is recommended.
6. **Flow**: three to five icon steps left to right on one baseline, joined by thin (1.5 pt) mid-gray connectors, each with a two-to-four-word label below.

The title and section breaks use the template's own layouts. Don't use the same preset on more than two consecutive slides.

### Icons (native shapes only)

All icons are drawn as native PowerPoint shapes and grouped. Never insert an icon as a picture, SVG, emoji, or font glyph.

- **Build**: combine three to six primitives: rectangle, rounded rectangle, ellipse, triangle, chord, arc, block arc, line, and freeform. Snap primitives to an internal 4 pt grid inside the icon's box.
- **Box**: every icon fits a square box. Use one size per deck: 48 pt in cards and flows, 32 pt in Isotype blocks.
- **Style**: solid fills, no outlines, no gradients, no shadows. Dark blue by default; light blue for the one icon that carries the point.
- **Consistency**: same box, same visual weight, same corner radius, and same angle vocabulary (0°, 45°, 90°) across the deck.
- **Meaning**: one concept per icon, always paired with a text label. Use the plainest form: a tower is a triangle with a mast line, a person is a circle over a rounded rectangle, a building is a rectangle with a grid of square windows, a dollar is a circle with a bold "$" from the theme font.
- **Accessibility**: group each icon and give the group alt text naming the concept.
- **Reuse**: once an icon is drawn, reuse the same group for that concept everywhere in the deck.

### Isotype counts

Use an Isotype block to make a large quantity concrete:

- One identical icon per stated unit, with the key in the label, such as "Each figure = 1 million people."
- Arrange icons in even rows on the 8 pt spacing scale; 10 per row reads fastest. Use 50 icons or fewer.
- Color the portion that makes the point in light blue and the rest in mid gray.
- Round to whole icons and say so in the label or notes. Never scale an icon to show quantity.

### Charts

- The headline states the finding; the chart title, if any, names what is plotted in plain words.
- Gray first: every series mid gray (#8A8D91), then one series or bar in light blue. Purple only for a second required highlight.
- Direct labels at line ends or on bars; delete the legend.
- Delete the chart border, background fill, and plot-area fill. Use no gridlines, or light gray horizontal gridlines only when readers need to read values.
- Bar and column charts start at zero. Use horizontal bars when category labels are long.
- Add one annotation, a short 16 pt label with a thin connector, on the data point that proves the headline.
- No pie charts except a two-part split, no donut charts, no dual axes, no 3-D, and no markers on dense lines.
- Source line at the bottom left in 11 pt mid gray.

### Tables

No vertical rules and no cell fills except a grey header row or one light-blue-tinted highlighted row. Thin (0.75 pt) horizontal rules in mid gray. Right-align numbers; left-align text.

### Photos

One photo per slide at most. Crop it to grid edges or run it full bleed on section breaks if the layout allows. No borders, rounded corners, shadows, or frames.

### Never

- No animation and no slide transitions. Remove any inherited from the template file.
- No drop shadows, glows, bevels, reflections, gradients, WordArt, or 3-D effects.
- No outlines on shapes or cards.
- No clip art, stock icons, decorative stripes, or accent lines under titles.
- No more than one highlight color per slide, except one purple for a required comparison.
