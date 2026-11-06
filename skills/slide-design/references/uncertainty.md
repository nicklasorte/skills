# Showing uncertainty

Model results, Monte Carlo runs, and forecasts have spread. Show the spread
when it would change the decision. Hide it in the notes when it wouldn't.

## For non-technical audiences

These methods are read most accurately by lay audiences.

1. **Frequency framing.** State and draw probabilities as counts of discrete
   outcomes: "3 in 100 locations," shown as an icon array or waffle. People
   judge counts of discrete things more accurately than areas or
   percentages.
2. **Quantile dotplots.** Show a distribution as 20 or 50 stacked dots, each
   an equally likely outcome. Color the dots past the threshold and count
   them in the annotation: "4 of 50 runs exceed the limit." Keep the dot
   count small to moderate. Too many dots read as a smooth shape and lose the
   benefit.
3. **Range in words.** Put the range in the headline or a label: "between
   $3 billion and $5 billion in 9 of 10 runs."
4. **Range bars and fan charts** with plain labels such as "9 in 10
   simulations fall in this range." See `chart-types.md`.

## For technical audiences

- **Error bars:** always state what they show (standard deviation, standard
  error, or a confidence level) in the caption or legend.
- **Graded error bars or graded bands:** show two levels at once, such as 50%
  and 90%, with a darker inner band.
- **Confidence bands on fits:** use a light band around the trend line.
- **CDFs and exceedance curves:** mark the protection criterion and the
  crossing point.
- **Full distributions:** histograms, densities, or violin plots when the
  shape matters (two peaks, long tails).

## Cautions

- **People read error bars as hard limits.** Many viewers treat the ends of
  a bar or band as the minimum and maximum possible values. If that misreading
  would matter, say in words that values outside the range are possible.
- **Overlap doesn't show significance.** Don't let the audience (or yourself)
  judge whether two results differ by whether their error bars overlap. Compute
  the interval for the difference and show that instead.
- **Small samples widen intervals.** If two scenarios have different numbers
  of runs, say so. Different band widths may reflect sample size, not real
  differences in variability.
- **Curved fits wiggle.** The band around a nonlinear fit represents
  uncertainty in the shape, not just up-and-down shifts. Don't describe it as
  a simple plus-or-minus.
- **Avoid confidence strips and gradient-only displays.** Viewers can't tell
  where a given confidence level ends.
- **Don't show false precision.** Round headline numbers to match the
  uncertainty. "About $4 billion" is more honest than "$4.21 billion" from a
  model with wide spread.

## Out of scope

Hypothetical outcome plots, which cycle through outcomes as an animation, are
effective but excluded because this skill doesn't use animation or video.
Use a quantile dotplot instead; it shows the same idea as a static image.
