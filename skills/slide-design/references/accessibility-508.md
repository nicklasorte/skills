# Accessibility and Section 508

Federal agencies must make electronic documents, including slide decks and
reports, conform to the Section 508 standards (which incorporate WCAG 2.0
Level AA). Accessible decks also read better for everyone. Apply these
checks to every deck and report you build for Nick.

## Slides

- **Use real slide titles.** Every slide has a unique title in the layout's
  title placeholder, not in a loose text box. Screen readers navigate by
  these titles. If a slide shouldn't show a title visually, keep the title
  placeholder and move it off the slide or hide it, rather than deleting it.
- **Use slide-master layouts and placeholders** for content, so structure is
  consistent and machine-readable.
- **Set the reading order.** In the Selection Pane, order objects so a screen
  reader reads them in the same order a sighted person would: title first,
  then the main visual, then annotations, then the source line. Note that
  the Selection Pane lists objects bottom to top.
- **Use built-in lists** for any list, not typed characters.
- **Don't use flashing content.** No animation is the default anyway.

## Alt text

- Give every meaningful image, chart, map, diagram, and native-shape icon
  alt text.
- For charts, write the takeaway and the chart type, then the key values:
  "Bar chart. Three markets account for most of the lost revenue: New York
  $820 million, Los Angeles $610 million, Chicago $450 million. Two other
  markets are under $150 million each."
- For maps, state what the zones show and the key number, not a description
  of the geography.
- For complex charts, keep alt text short and put the data in a table in
  backup or the report, and say where it is.
- Mark purely decorative shapes (dividers, background accents) as decorative
  so screen readers skip them.
- Group the shapes of a native-shape icon or diagram, then put alt text on
  the group.

## Color and contrast

- Never use color as the only way to convey meaning. Add a label, pattern,
  shape, or position cue.
- Text contrast is at least 4.5:1 against its background, and at least 3:1
  for large text (18 pt or larger, or 14 pt bold).
- See `color.md` for palettes that pass.

## Tables

- Build tables with the table feature, never as images.
- Mark the header row in table properties.
- Don't merge or split cells.
- Keep tables simple. Complex tables may need fixing in Acrobat after PDF
  export.

## Links and files

- Make link text describe the destination ("2026 spectrum strategy"), not
  "click here."
- Give the file a descriptive name, such as
  `7GHz-coordination-zones-briefing-2026-10.pptx`.
- Fill in the file's Title property.
- Keep the deck in .pptx format.

## Check before delivery

1. Run the PowerPoint Accessibility Checker (Review > Check Accessibility)
   and fix every error.
2. Check the reading order of each slide in the Selection Pane.
3. Read the alt text of every chart and map once more for accuracy.
4. Automated checkers miss problems, so do a manual review too.

When building with python-pptx, set alt text with `set_alt_text(shape,
text)` from `scripts/pptx_chart_style.py`, put titles in the layout's title
placeholder, and run the Accessibility Checker in PowerPoint before delivery.
