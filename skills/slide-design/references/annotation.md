# Annotation

Annotation is the layer that tells the audience what to see. An unannotated
chart asks the audience to find the point; an annotated chart hands it to
them. A 2024 IEEE VIS study of more than 1,800 published charts found that
strong charts usually combine annotation types instead of relying on one.

## Annotation types

| Type | What it is | Use it to |
|---|---|---|
| Text label | A short phrase placed on the chart | State what a point, line, or region means |
| Connector | A thin line or arrow from text to a data point | Link a label to a mark when the label can't sit next to it |
| Enclosure | A circle, box, or shaded region around marks | Group marks that belong together, such as a peak or a cluster |
| Reference line | A horizontal or vertical line at a meaningful value | Show a limit, target, average, or event date |
| Reference band | A shaded range | Show an acceptable range, a study period, or uncertainty |
| Highlight color | Light blue on one mark or series | Make the focal element pop, with everything else gray |
| Direct series label | A series name placed at the end of a line or on a bar | Replace the legend |
| Value label | The number on or next to a mark | Give exact values for the few marks that matter |

## Common combinations

- **Highlight + text:** color the one bar that matters and label why.
- **Reference line + text:** draw the protection limit and label it
  "Protection limit" in plain words.
- **Enclosure + text:** shade the period of interest and label it, such as
  "Auction window."
- **Text + connector:** call out an outlier from open space nearby.

## Rules

- **Annotate the headline.** The main annotation should prove the slide
  title. If the title says "Interference exceeds the limit in 2 of 100
  locations," the annotation marks that crossing point.
- **Use one to three annotations per chart.** More than that turns the chart
  into a reading exercise. In read-ahead mode, you can use up to five.
- **Keep text to two to eight words.** Write it as a fact or a meaning, not a
  description: "Rule change takes effect," not "Vertical line at 2027."
- **Place text in open space** near the mark. Don't cover data.
- **Match the text color to what it describes,** or use dark blue. Don't use
  a new color for annotations.
- **Use thin connectors** (0.75–1 pt, gray), straight or with one elbow.
  Don't use curved, decorative arrows.
- **Size annotation text like data labels:** 16 pt on slides and at least
  8 pt at final size in report figures.
- **Use hatching or a dashed outline** to mark uncertain or preliminary
  regions, so the meaning doesn't depend on color alone.

## Native PowerPoint construction

Build annotations as native text boxes, lines, and shapes on top of the
native chart. Group them with the chart only after the chart is final,
because regrouping breaks if the chart data changes. Give each annotation
alt text or include it in the chart's alt text (see `accessibility-508.md`).
