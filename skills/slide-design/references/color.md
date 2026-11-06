# Color

Color is for meaning, not decoration. The approach is **gray plus one
accent**: draw everything in mid gray, then use one NTIA accent color for the
single thing the audience should look at.

Every slide, figure, map, and table uses the NTIA palette from the NTIA Brand
Style Guide. The authoritative values and roles are in the `ntia-talking-deck`
skill's `references/brand-and-design.md`; this file repeats them for charts
and figures and adds data-visualization rules. If the two ever disagree, the
brand file wins. On slides, use the template's theme colors
(`MSO_THEME_COLOR`) wherever the theme defines a matching slot.

## NTIA palette

| Role | Name | Hex | Notes |
|---|---|---|---|
| Text, headlines, icons, focal dark elements | Dark blue | `#163353` | Default text color |
| The one highlight per slide or chart | Light blue | `#5674C4` | About 4.48:1 on white: for text, use only at 24 pt or larger, or bold (brand rule) |
| Second highlight, only for a required comparison | Purple | `#6E4F92` | Also the "alert" or "exceeds limit" color, since the brand has no red |
| Context data: series, bars, connectors, baselines | Mid gray | `#8A8D91` | Not a brand color; 3.3:1 on white, so fine for graphics and text 18 pt or larger, but not for small text. Source lines are dark blue |
| Card and panel fills | Grey | `#E8E9EA` | Fills only. Never for text, lines, or chart series on white |
| Fill behind dark blue text | Yellow | `#D9CFA0` | Fills only |
| Gridlines | Light gray | `#E6E6E6` | Barely visible, which is the point |
| Logo on dark backgrounds | Logo light blue | `#617ECC` | Logo only; don't use elsewhere |

## How many colors

- Use mid gray for everything, plus light blue for the one element that
  proves the headline. Label the light blue element directly, because mid
  gray and light blue are close in lightness.
- Add purple only when a slide must compare two highlighted items, or flag
  an item that needs action.
- Don't use more than these two highlight colors on one slide.
- If a chart needs more than three distinguishable series, it has too many.
  Use small multiples, or gray most series and highlight one.

## Semantic color

The brand has no red or green, so don't add them.

- **Good versus bad:** use light blue for the outcome that meets the goal
  and purple for the outcome that fails it, and always add a word label
  ("Within limit," "Exceeds limit"). Never rely on color alone.
- **Recurring entities:** pick one color for each entity that appears
  throughout a deck or report, such as federal or non-federal, and never
  change it.
- **Don't reuse a color** for an unrelated meaning on a later slide.

## Sequential and diverging scales

Build scales from the brand blues so maps and heatmaps still look like NTIA.

- **Sequential** (low to high): a single-hue ramp from very light blue to
  dark blue. A five-class ramp: `#E4E9F6`, `#B4C2E6`, `#7F96D3`, `#3F5FA8`,
  `#163353`. Use four to six classes on maps.
- **Diverging** (above and below a meaningful midpoint): dark blue on one
  side, purple on the other, and light gray (`#E8E9EA`) in the middle. Use a
  diverging scale only when the midpoint means something, such as an
  interference threshold, zero change, or a target.
- **Never use rainbow or jet scales.** They create false boundaries and fail
  for colorblind viewers. In MATLAB, replace `jet` with a custom ramp from the
  values above. In matplotlib, use a `LinearSegmentedColormap` built from
  them.
- **Technical backup only:** if a continuous scientific colormap is
  unavoidable (for example, a dense contour plot), use `cividis`, which is
  colorblind-safe and blue-based.

## Contrast

- Text needs a contrast ratio of at least 4.5:1 against its background
  (WCAG AA). Large text (18 pt and up, or 14 pt bold) needs at least 3:1.
- Chart elements that carry meaning, such as lines, bars, and points, need at
  least 3:1 against the background.
- Light blue on white is about 4.48:1, just under the limit. Following the
  brand file, use it for text only at 24 pt or larger, or in bold.
- Mid gray on white is about 3.3:1. Use it for chart marks and large text
  only. Small text, including source lines, is dark blue.
- Grey and yellow fail on white. Use them only as fills behind dark blue
  text.
- Projectors wash out light colors. Check light fills at reduced brightness.

## Grayscale and colorblind check

Before you finish, check that the chart still works when:

- It's printed in grayscale. Dark blue, light blue, purple, and mid gray
  must still separate by darkness. Light blue and purple are close in
  lightness, so when both appear, also separate them with labels, position,
  or line style.
- It's viewed with a red-green color vision deficiency. The NTIA palette has
  no red-green pair, but direct labels are still required.

If a chart only works in color, add direct labels, line styles, markers, or
hatching so color isn't the only cue.
