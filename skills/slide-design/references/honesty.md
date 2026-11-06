# Honest charts

A chart that misleads, even by accident, costs you credibility with the
audience the moment someone notices. With political appointees and
oversight audiences, someone always notices. Check every chart against these
rules.

## Axes and baselines

- **Bar, column, and area charts start at zero.** Length encodes the value,
  so a truncated axis exaggerates differences.
- **Line charts and dot plots can start above zero** when the variation is
  the point, but the axis must be labeled, and the title shouldn't overstate
  the change.
- **Don't break axes** on bar charts. If one bar dwarfs the rest, show it
  with a label, or use two charts.
- **Use consistent scales** across small multiples and across slides that the
  audience will compare. If two maps or charts sit side by side, they use the
  same extent, scale, and color classes.
- **Don't use dual y-axes.** Two scales let the chart maker set any apparent
  relationship. Use two aligned charts that share the x-axis instead.

## Logarithmic scales and decibels

- Decibels are already logarithmic, which most non-technical viewers don't
  know. A 3 dB difference looks small on a chart but means twice the power.
- On leadership slides, either convert to linear terms ("about twice the
  power," "10 times the interference") or annotate the meaning next to the
  value. See `technical-to-plain.md`.
- Label any log axis clearly, such as "Probability (log scale)," and use
  plain tick labels (1%, 10%, 100%) rather than exponents.

## Areas and sizes

- When size encodes value, scale by area, not by diameter or height.
  Doubling a circle's diameter quadruples its area and overstates the
  difference.
- Don't use 3D. Perspective makes near items look bigger than far ones.
- On maps, large, sparsely populated areas dominate visually. Pair zone maps
  with population or market numbers so the visual size doesn't stand in for
  impact.

## Selection and context

- Show the full time range that matters, not just the slice that supports
  the headline. If you crop, say why.
- Compare against a fair baseline, such as the status quo or the statutory
  target, not a hand-picked worst case.
- When the result depends on an assumption, say which one in the caption or
  a footnote, for example "Assumes 2% building penetration loss."

## Uncertainty

Model and Monte Carlo results have spread. Show it when it would change the
decision. For methods and cautions, see `uncertainty.md`.

- **For leadership:** state a range in words ("between $3 billion and $5
  billion in 9 of 10 runs") or use a range bar or fan chart with plain
  labels.
- **For technical audiences:** use error bars, confidence bands, CDFs, or
  box plots, and state what the bands mean (for example, "shaded area is the
  10th to 90th percentile").
- Don't show more precision than the model supports. "$4.2B" implies a
  precision that a model with ±30% uncertainty doesn't have. Say "about $4
  billion."

## Sources

- Put a source line on every chart that shows data: who produced the data,
  what analysis, and the date.
- Mark preliminary or draft results clearly, for example "Preliminary,
  subject to change" in the source line.
