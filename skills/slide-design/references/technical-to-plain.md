# Turning technical results into plain visuals

Leadership audiences decide based on consequences, not methods. Your job is
to carry the technical result across to their terms without losing accuracy.
Use this ladder for every technical number.

## The translation ladder

Move each result as far down this ladder as accuracy allows.

1. **Technical metric** (−6 dB I/N, 95th percentile path loss)
2. **What it means physically** (interference adds 25% to the receiver's
   noise)
3. **What it means operationally** (the radar loses track of targets beyond
   X km)
4. **What it means for the decision** (a 20 km zone protects the radar; a
   5 km zone doesn't)
5. **What it means in their units** (dollars, people, missions, years,
   square miles)

Put level 4 or 5 in the headline. Put levels 1–3 in the caption, speaker
notes, or a backup slide.

## Converting common spectrum quantities

| Technical | Plain equivalent |
|---|---|
| +3 dB | About twice the power |
| +10 dB | 10 times the power |
| +20 dB | 100 times the power |
| −6 dB I/N | Interference adds about 25% to the background noise |
| 0 dB I/N | Interference equals the background noise, so the noise doubles |
| 95th percentile | 19 times out of 20 |
| 1% exceedance (locations) | Exceeds the limit at 1 in 100 locations |
| 1% exceedance (time) | Exceeds the limit about 15 minutes a day |
| Probability of 0.02 | 2 in 100 |
| MHz of spectrum | Compare to a known band: "about the width of all Wi-Fi channels at 5 GHz" |
| Coordination distance in km | Compare to a known distance: "about the distance from the Capitol to Dulles" |
| Area in km² | Compare to a known area: "about the size of Rhode Island" |

Check every comparison you use. An analogy that's off by a factor of two is
worse than no analogy.

## Patterns that work

- **Lead with the answer, then the evidence.** Headline: "A 20 km zone
  protects the radar." Visual: exceedance curves for 5, 10, and 20 km with
  the 20 km curve highlighted and the limit line labeled.
- **Replace a curve with a crossing point.** Most leadership questions about
  a CDF are "how often does it exceed the limit?" Show that one number big,
  and keep the curve for backup.
- **Use natural frequencies.** "2 in 100 locations" is understood faster and
  more accurately than "2%" or "0.02," especially for small probabilities.
- **Compare against something familiar.** A number alone has no meaning.
  Compare it to last year, the target, another band, or a known quantity.
- **Show the decision space.** When the question is "how big should the zone
  be," show the options side by side with the trade-off (protection versus
  revenue) as two simple bars per option.
- **Name the threshold.** Draw the protection criterion or legal limit as a
  line and label it in words: "Protection limit." The audience can then see
  above and below without reading the axis.
- **Show the model as a diagram, not an equation.** If the audience needs to
  trust the method, use a three- to five-box flow diagram (inputs, model,
  output). Put equations in the report appendix.

## What to cut

- Equations, parameter tables, and propagation model names on leadership
  slides. Move them to the appendix.
- Axis labels in technical units when a plain label works, such as "How
  often interference is too high" instead of "P(I/N > −6 dB)."
- Every scenario except the baseline, the recommendation, and at most one
  alternative.

## Accuracy guard

Simplifying isn't the same as rounding the truth away. Before you finish:

- Confirm that the plain statement is still true for the cases the decision
  depends on.
- Keep caveats that would change the decision. Move caveats that wouldn't
  to the notes.
- If you can't simplify a result without making it wrong, say so and keep
  the technical version with a strong annotation.
