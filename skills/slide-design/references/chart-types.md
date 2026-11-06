# Chart types catalog

Use this catalog to pick a chart that proves the headline. Each entry says
what the chart shows, when to use it, when not to, how to design it, and an
example from spectrum work.

Pick by the message, then check the "Avoid when" line. If two charts fit,
choose the one the audience has seen most often. Familiar charts cost the
audience less attention.

## Contents

1. [Find a chart by relationship](#find-a-chart-by-relationship)
2. [Single values](#single-values)
3. [Comparison and ranking](#comparison-and-ranking)
4. [Deviation](#deviation)
5. [Change over time](#change-over-time)
6. [Part to whole](#part-to-whole)
7. [Distribution and probability](#distribution-and-probability)
8. [Relationship](#relationship)
9. [Flow and process](#flow-and-process)
10. [Geographic and spatial](#geographic-and-spatial)
11. [Frequency and spectrum](#frequency-and-spectrum)
12. [Schedules](#schedules)
13. [Tables](#tables)
14. [Techniques borrowed from strong examples](#techniques-borrowed-from-strong-examples)
15. [Charts to avoid](#charts-to-avoid)
16. [Audience fit at a glance](#audience-fit-at-a-glance)

---

## Find a chart by relationship

This table follows the nine relationships in the Financial Times Visual
Vocabulary. Name the relationship in your headline, then pick from that row.

| Relationship | Headline sounds like... | Charts in this catalog |
|---|---|---|
| Deviation | "Above or below the target or baseline" | Diverging bar, diverging stacked bar, surplus/deficit filled line |
| Correlation | "X rises as Y rises" | Scatter, connected scatter, heatmap |
| Ranking | "These are the largest" | Sorted bar, dot plot, lollipop, slope, bump chart |
| Distribution | "Most results cluster here" | Histogram, strip plot, beeswarm, quantile dotplot, range bar, CDF or exceedance curve, back-to-back bars, cumulative curve |
| Change over time | "It grew, fell, or shifted" | Line, column, slope, fan chart, step, calendar or time-of-day heatmap, duration timeline |
| Part to whole | "This share of the total" | Single stacked bar, waffle, treemap, waterfall, nested shading |
| Magnitude | "A is bigger than B" | Bar, column, grouped bar, bar with reference marker, bullet chart, scale comparison |
| Spatial | "It happens here" | Choropleth, proportional symbol, dot density, zone map, tile or hex map, cartogram, flow map |
| Flow | "It moves from here to there" | Sankey, alluvial, waterfall, flow map, network diagram |

---

## Single values

### Big number

- **Shows:** one figure that matters most.
- **Use when:** the slide's point is a single number, such as a dollar
  amount, a distance, or a percentage.
- **Avoid when:** the number means nothing without a comparison. Then add a
  comparison or use a bar chart.
- **Design:** set the number at 96–120 pt in light blue or dark blue. Add a
  20 pt label below it and a 16 pt plain comparison under that. Round hard: "$4.2 billion," not
  "$4,213,887,102."
- **Example:** "$4.2B: estimated revenue at risk from coordination zones."

### Big number with comparison

- **Shows:** one number next to a reference point.
- **Use when:** the number is only meaningful relative to something, such as
  last year, a target, or another band.
- **Design:** show two numbers side by side. Make the important one large and
  colored and the reference smaller and gray. Add an arrow or a short phrase
  such as "up from."

### Icon array (pictogram)

- **Shows:** a proportion as a grid of repeated shapes, for example 10 × 10.
- **Use when:** you're explaining a probability or a share to a non-technical
  audience, as in "3 in 100 locations."
- **Avoid when:** precision matters, or the share is very small (below 1%).
- **Design:** use native shapes (circles or squares), with the highlighted
  ones in light blue and the rest in light gray.
- **Example:** "Interference exceeds the threshold at 3 in 100 sites."

---

## Comparison and ranking

### Bar chart (horizontal)

- **Shows:** the size of values across categories.
- **Use when:** category names are long, there are more than about five
  categories, or you're ranking items. This is the default comparison chart.
- **Avoid when:** the categories are time periods; use a column or line
  chart.
- **Design:** sort largest to smallest unless the categories have a natural
  order. Start at zero. Label values at the bar ends and remove the value
  axis. Make the gap between bars about half a bar's width. Color the bar
  that matters and gray the rest.
- **Example:** auction revenue lost per market area, ranked.

### Column chart (vertical bar)

- **Shows:** values across a few categories or discrete time periods.
- **Use when:** there are seven or fewer categories with short labels, or
  you're showing discrete periods such as fiscal years.
- **Avoid when:** labels are long (they get rotated, which is hard to read);
  use horizontal bars instead.
- **Design:** same rules as the bar chart. Never rotate labels.

### Grouped bar chart

- **Shows:** two or three series compared across categories.
- **Use when:** the comparison within each group is the point, such as
  baseline versus proposed for each band.
- **Avoid when:** there are more than three series. Use small multiples or a
  dot plot.
- **Design:** use gray for the baseline and light blue for the scenario that
  matters. Label the series once, directly, on the first group.

### Bar chart with reference marker

- **Shows:** each bar's value plus a dot or tick for a reference value on the
  same bar, such as the national average, last year, or the target.
- **Use when:** each category needs its own comparison, not just one shared
  baseline. Pew used this to compare each news outlet's audience to the
  U.S. adult population.
- **Design:** use a gray bar for the value and a dark dot or short vertical
  tick for the reference. Label the reference once, on the first bar.
- **Example:** each market's share of revenue at risk versus its share of
  population.

### Bump chart

- **Shows:** how the rank of several items changes across several time
  points.
- **Use when:** rank order matters more than the values, such as which bands
  or markets moved up or down.
- **Avoid when:** values matter. Ranks hide the size of the gaps.
- **Design:** label items at both ends. Gray all lines but the one or two
  that matter.

### Dot plot (Cleveland dot plot)

- **Shows:** values as dots on a common scale, one row per category.
- **Use when:** you have many categories, or the values don't start near zero
  so a bar would be mostly empty.
- **Avoid when:** the audience has never seen one and you have no time to
  explain it. Use a bar chart instead.
- **Design:** sort the rows. Use thin, light gridlines to guide the eye
  across. Dots can be a different scale than bars because they don't need a
  zero baseline.

### Lollipop chart

- **Shows:** the same as a bar chart, drawn as a thin line with a dot at the
  end.
- **Use when:** you have many categories and bars would feel heavy.
- **Design:** start at zero, like a bar.

### Dumbbell chart

- **Shows:** two values per category connected by a line, such as before and
  after, or two scenarios.
- **Use when:** the gap between two values is the message.
- **Design:** use gray for the "before" dot and light blue for the "after"
  dot. Sort by the size of the gap.
- **Example:** required separation distance per site under the old rule
  versus the proposed rule.

### Slope chart

- **Shows:** change between exactly two points in time for several items.
- **Use when:** you want to show which items rose, which fell, and by how
  much, in one view.
- **Avoid when:** you have more than about eight items or more than two time
  points.
- **Design:** label both ends of each line directly. Color the one or two
  lines that matter.

### Bullet chart

- **Shows:** one measure against a target with qualitative ranges.
- **Use when:** you're showing progress toward a goal, such as megahertz
  identified versus the statutory target.
- **Design:** use a thick bar for actual, a thin vertical line for target,
  and light gray shaded bands for the ranges.

### Small multiples

- **Shows:** the same simple chart repeated for each category, on the same
  scale.
- **Use when:** a single chart would have too many overlapping lines or bars.
- **Avoid when:** the audience needs one takeaway quickly. Small multiples
  invite study, which suits reports better than live slides.
- **Design:** keep the axes identical across panels. Use a minimum of axis
  labels, only on the outer edge. Highlight the panel that carries the point.
- **Example:** interference probability over time, one small panel per band.

### Scale comparison graphic

- **Shows:** something unfamiliar drawn at true scale next to something the
  audience already knows.
- **Use when:** size is the message and the number alone won't land, such as
  the area of a coordination zone compared to a state or a metro area.
- **Design:** draw both shapes to the same scale, outline only, with the
  unfamiliar one in light blue. Label both with one number each.

---

## Deviation

Deviation charts show values above and below a meaningful reference: zero,
a target, a protection limit, or the status quo.

### Diverging bar

- **Shows:** positive and negative values as bars extending from a shared
  center line.
- **Use when:** the message is gain versus loss, or above versus below a
  limit.
- **Design:** sort by value. Use one color for one side (for example, blue
  for gains) and purple for the other side (losses), with word labels. Put
  category labels on the side opposite the bar or at the center line.
- **Example:** change in auction revenue by market under the proposed zone
  sizes, compared to the current rule.

### Diverging stacked bar

- **Shows:** shares on a scale (for example, oppose, neutral, support) for
  several groups, centered on the neutral point.
- **Use when:** you're summarizing positions, such as how commenters in a
  proceeding lined up by stakeholder type.
- **Design:** center the neutral segment on the zero line, or show it as a
  separate bar to the side. Use a diverging palette with gray for neutral.

### Surplus/deficit filled line

- **Shows:** two lines over time, with the area between them shaded by which
  one is higher.
- **Use when:** the gap between two series is the story, such as spectrum
  demand versus available supply.
- **Design:** shade the surplus area in one light color and the deficit area
  in another. Label the crossover year.

---

## Change over time

### Line chart

- **Shows:** a continuous trend over time.
- **Use when:** you have many time points and the shape of the trend is the
  message. This is the default time chart.
- **Avoid when:** you have only two or three time points. Use bars or a
  slope chart.
- **Design:** use no more than four lines. Gray the context lines and put
  light blue on one. Label lines at their right ends instead of using a
  legend. Don't use markers unless there are fewer than about 10 points. The
  y-axis doesn't need to start at zero, but label it clearly.
- **Example:** commercial demand for mid-band spectrum, 2015–2030.

### Annotated line chart

- **Shows:** a line chart with short text callouts at key events.
- **Use when:** events explain the trend, such as an auction, a rule change,
  or a launch.
- **Design:** use a thin vertical line or a dot at the event and a two- to
  five-word label.

### Area chart

- **Shows:** a single quantity over time with the area under the line filled.
- **Use when:** you want to emphasize volume or cumulative totals.
- **Avoid when:** you have several overlapping series. Stacked areas are hard
  to read except for the bottom layer.

### Step chart

- **Shows:** values that change in jumps rather than smoothly.
- **Use when:** you're showing things like rule changes, allocations, or
  power limits that hold until they change.

### Sparkline

- **Shows:** a tiny, axis-free line showing a trend.
- **Use when:** you need a trend next to a number in a table or a summary
  row.
- **Avoid when:** the exact values matter.

### Calendar or time-of-day heatmap

- **Shows:** a value for each day, or for each hour by day of week, as color
  in a grid.
- **Use when:** you're showing when something happens, such as when a
  federal system actually transmits. This often supports a sharing argument.
- **Avoid when:** precise values matter. Color is a low-precision encoding.
- **Design:** use a sequential single-hue palette. Label the busiest and
  quietest periods directly.

### Fan chart (uncertainty band)

- **Shows:** a central forecast with shaded bands for uncertainty.
- **Use when:** you're showing a projection or a Monte Carlo result over
  time.
- **Design:** draw the median line in light blue. Use one or two
  light bands (for example, 50% and 90%) and label what they mean in plain
  words: "9 in 10 simulations fall in this range."

---

## Part to whole

### Single stacked bar (100% bar)

- **Shows:** how one total splits into a few parts.
- **Use when:** there are two to four parts.
- **Design:** put the part that matters first (at the left), in light
  blue. Label percentages inside the segments.
- **Example:** share of a band that is shared, exclusive federal, or
  exclusive commercial.

### Stacked bar chart (multiple bars)

- **Shows:** composition across several categories.
- **Use when:** you need both the total and the composition.
- **Avoid when:** the middle segments matter. Only the bottom segment shares
  a baseline, so the others are hard to compare. Use small multiples or
  grouped bars instead.

### Waffle chart

- **Shows:** a part-to-whole split as a 10 × 10 grid of squares.
- **Use when:** you're showing a percentage to a general audience. It's more
  readable than a pie.

### Nested shading

- **Shows:** a total as one shape, with a darker shape inside it for the
  subset that matters. Florence Nightingale used this to show deaths from
  preventable disease inside total deaths.
- **Use when:** the message is "this much of the total is X."
- **Design:** use a light gray outer bar or area for the total and light
  blue for the subset. Label both values.
- **Example:** total licensed area versus the area inside coordination
  zones, by market.

### Treemap

- **Shows:** a hierarchy of parts as nested rectangles sized by value.
- **Use when:** there are many parts with a hierarchy, and only the biggest
  few matter.
- **Avoid when:** you need precise comparisons. Area is hard to judge.

### Pie or donut chart

- **Shows:** parts of a whole as slices.
- **Use when:** only for a two-part split where one part is clearly
  dominant, such as "two thirds." This matches the NTIA chart rules.
- **Avoid when:** there are more than two slices, or you're comparing two
  pies. Never use donut charts. Use a single stacked bar or a bar chart.
- **Design:** start the main slice at 12 o'clock. Label slices directly. No
  3D, no exploded slices.

---

## Distribution and probability

### Histogram

- **Shows:** how many observations fall in each range of values.
- **Use when:** the shape of the data matters, for example whether most
  results cluster near the threshold or a long tail exists.
- **Design:** choose bin widths that match meaningful units (for example,
  1 dB or 1 km). Draw a vertical line at the threshold and label it.

### Box plot

- **Shows:** median, middle half, and range for one or more groups.
- **Use when:** you're comparing spread across several groups with a
  technical audience.
- **Avoid when:** the audience is non-technical. Most people can't read box
  plots. Use a strip plot or a range bar with plain labels.
- **Variant:** a violin plot adds the shape of the distribution. It's useful
  for technical audiences when the distribution has two peaks or a long tail.

### Strip plot (jitter plot)

- **Shows:** every observation as a dot along one axis.
- **Use when:** you have fewer than a few hundred points and want to show
  the real data, including outliers.

### Beeswarm plot

- **Shows:** every item as a dot along one axis, packed so dots don't
  overlap. Dot size can add a second measure.
- **Use when:** you have 20–300 items and want to show both the spread and
  individual items, grouped into a few rows. Pew used this to show trust in
  30 news sources, split by party.
- **Design:** label only the few dots the headline mentions. Gray the rest.

### Quantile dotplot

- **Shows:** a distribution as 20 to 100 stacked dots, each one an equally
  likely outcome.
- **Use when:** you're showing Monte Carlo or forecast results to a
  non-technical audience. People judge counts of dots more accurately than
  areas under a curve. See `uncertainty.md`.
- **Design:** use 20 or 50 dots so each dot is a round percentage. Color the
  dots past the threshold in light blue and say how many there are:
  "4 of 50 runs exceed the limit."

### Back-to-back bars (population pyramid)

- **Shows:** two distributions mirrored on either side of a center axis.
- **Use when:** you're comparing two groups across the same categories, such
  as federal versus non-federal assignments by band.
- **Design:** use one color per side, and label the two sides at the top.
  Use the same scale on both sides.

### Cumulative curve

- **Shows:** what share of the total comes from the top items, sorted from
  largest to smallest.
- **Use when:** the message is concentration, such as "five markets account
  for 80% of the revenue at risk."
- **Design:** mark and label the point that carries the headline. A sorted
  bar chart with a running-total line is a more familiar alternative.

### Range bar (floating bar)

- **Shows:** a minimum-to-maximum (or 10th-to-90th percentile) range per
  category with the median marked.
- **Use when:** you need to show uncertainty to a non-technical audience. It's
  a plain-language box plot.
- **Design:** label the range in words, such as "9 in 10 runs fall here."

### CDF or exceedance curve

- **Shows:** the probability that a value is at or below (CDF) or above
  (exceedance) each level.
- **Use when:** the decision depends on "how often does X exceed a limit?"
  This is the standard way to show interference results such as I/N.
- **Avoid when:** you can say it in a single number. For leadership, the
  answer is often "exceeds the limit 2% of the time," which needs a big
  number, not a curve.
- **Design:** for non-technical audiences, use an exceedance curve, which
  answers the natural question ("how often is it worse than this?"). Draw
  the protection criterion as a vertical line, mark the point where the
  curve crosses it, and label that point with the answer in words. Gray out
  scenarios that don't matter.
- **Example:** "Aggregate interference exceeds −6 dB I/N at 2% of locations."

### Heatmap

- **Shows:** values in a grid of rows and columns, with color as the value.
- **Use when:** you're showing patterns across two categorical dimensions,
  such as hour of day by day of week, or band by region.
- **Design:** use a sequential palette from one hue, light to dark. Use a
  diverging palette only if a meaningful midpoint exists. Add values in the
  cells if there are fewer than about 50 cells.

---

## Relationship

### Scatter plot

- **Shows:** the relationship between two numeric measures.
- **Use when:** you're showing correlation, clusters, or outliers.
- **Design:** label the axes in plain words with units. Highlight and label
  the points that matter. Add a trend line only if the relationship is the
  point, and say what it means in the title.
- **Example:** distance from a federal site versus interference level.

### Bubble chart

- **Shows:** a scatter plot with a third measure as dot size.
- **Use when:** rarely. Area is hard to compare.
- **Avoid when:** the third measure matters. Encode it some other way, such
  as small multiples or a label.

### Connected scatter plot

- **Shows:** how two measures moved together over time.
- **Use when:** you're presenting to technical audiences and the path is the
  story. Most non-technical audiences find these confusing.

---

## Flow and process

### Flow diagram

- **Shows:** steps, decisions, or how parts of a system connect.
- **Use when:** you're explaining a process, such as how a coordination
  request moves between agencies.
- **Design:** build from native shapes. Use a left-to-right or top-to-bottom
  flow, use five to seven boxes at most, and keep one consistent shape per
  type of element. Use a short verb phrase in each box.

### Sankey diagram

- **Shows:** how quantities flow from sources to destinations, with band
  width proportional to amount.
- **Use when:** you're showing reallocation, such as how much spectrum moves
  from federal to shared to commercial use.
- **Avoid when:** you have more than about 10 flows. It becomes spaghetti.

### Alluvial diagram (paneled)

- **Shows:** how members of groups move between categories across two or
  more stages. It's a Sankey with a time or stage axis.
- **Use when:** you need to show how a shift happened, not only that it
  happened. Pew used paneled alluvials to walk readers through voter flows
  one group at a time.
- **Design:** split a complex alluvial into panels, each highlighting one
  starting group in light blue with the rest gray. That keeps each
  panel to one message.
- **Example:** how spectrum in a band moves from federal exclusive to shared
  to commercial across three stages of a transition.

### Network diagram

- **Shows:** entities as nodes and relationships as lines.
- **Use when:** connections are the story, such as which agencies must
  coordinate on a band.
- **Avoid when:** you have more than about 15 nodes on a slide. It becomes a
  hairball.
- **Design:** place the most connected node in the center. Use line
  thickness for strength only if it matters. Build from native shapes.

### Waterfall chart

- **Shows:** how a starting value becomes an ending value through positive
  and negative steps.
- **Use when:** you're explaining what drives a change, such as total
  potential revenue minus each exclusion zone, equals net revenue.
- **Design:** use gray for the starting and ending totals, one color for
  decreases, and one for increases. Label each step's value. Sort the steps
  by size unless they have a natural order.

---

## Geographic and spatial

### Choropleth map

- **Shows:** a value for each region, encoded as fill color.
- **Use when:** the value is a rate or a share per area, such as the
  percentage of a county's population inside a zone.
- **Avoid when:** you're showing raw counts. Big, empty counties dominate
  visually. Use proportional symbols instead.
- **Design:** use a sequential, single-hue palette with five to seven
  classes. Show state outlines for orientation. Add a simple legend with
  plain labels.

### Point or proportional symbol map

- **Shows:** locations, with symbol size for magnitude.
- **Use when:** you're showing sites, such as federal installations, radars,
  or base stations, or counts by place.
- **Design:** use a light, simple basemap in gray. Make the points the
  light blue. Label only the few points the headline mentions.

### Zone or contour map

- **Shows:** areas where a condition holds, such as coordination zones,
  exclusion zones, or coverage contours.
- **Use when:** the audience needs to see where the restriction applies and
  how big it is.
- **Design:** use a light gray basemap, the zones in light blue with
  about 40–60% transparency, and a few city labels for scale. Add a short
  comparison of scale: "Zone covers an area about the size of Maryland."
  Show population or market impact as a big number beside the map.
- **Example:** DoD coordination zones in 7125–7400 MHz overlaid on top
  markets.

### Dot density map

- **Shows:** individual sites or events as dots at their real locations.
- **Use when:** clustering is the point. John Snow's cholera map used this
  to reveal a common cause.
- **Design:** use small, semi-transparent dots so dense areas read as
  darker. Annotate the cluster the audience should notice.

### Tile or hex map

- **Shows:** each region as an equal-sized square or hexagon, arranged
  roughly by geography.
- **Use when:** every region deserves equal visual weight, such as states or
  license areas, and large rural regions would otherwise dominate.
- **Design:** label each tile with a short code. Use hatching (diagonal
  lines) to mark uncertain or "toss-up" regions, so uncertainty doesn't rely
  on color alone.

### Cartogram

- **Shows:** regions resized by a value, such as population or license
  value, instead of land area.
- **Use when:** the decision depends on people or dollars, not acres. It
  fixes the "big empty county" problem directly.
- **Avoid when:** the audience needs to recognize exact locations. Put a
  small normal map beside it for orientation.

### Flow map

- **Shows:** movement between places, with arrow width for volume.
- **Use when:** you're showing movement across geography. Minard's map of
  Napoleon's march is the classic example: line width for army size and a
  linked temperature chart below.
- **Design:** use arrow width for volume and circle size at endpoints for
  totals. Keep it to the few largest flows.

### Before and after maps (small multiples)

- **Shows:** two maps side by side on the same extent.
- **Use when:** you're comparing zone sizes under two rules or two
  assumptions.
- **Design:** use an identical extent and scale on both maps, and the same
  colors. Put the headline difference as a number above them.

---

## Frequency and spectrum

### Band plan chart

- **Shows:** who uses which frequencies, as horizontal bars on a frequency
  axis.
- **Use when:** you're showing allocations, a proposed reallocation, or
  where a band sits relative to its neighbors.
- **Design:** draw frequency on the x-axis in MHz or GHz, with only the
  band edges labeled. Use one row per user type (federal, non-federal,
  shared) or one row per scenario. Highlight the band under discussion and
  gray its neighbors. For a non-technical audience, add a plain description,
  such as "Wi-Fi lives here."
- **Example:** current versus proposed use of 7125–7400 MHz.

### Spectrum mask or emission plot

- **Shows:** power versus frequency, with a limit line.
- **Use when:** your audience is technical, or the slide is a backup slide.
- **Avoid when:** you're presenting to leadership. Summarize the result
  instead: "Out-of-band emissions stay below the limit by a wide margin."

---

## Schedules

### Timeline

- **Shows:** events in order along a single time axis.
- **Use when:** you're showing milestones, such as statutory deadlines,
  comment cycles, or auction dates.
- **Design:** draw a horizontal line with labeled markers. Highlight
  "today" and the next decision point. Use no more than seven milestones on
  one slide.

### Duration timeline (Priestley timeline)

- **Shows:** parallel bars for things that last over time, arranged in rows.
  Joseph Priestley used this layout for historical lifespans.
- **Use when:** durations and overlaps matter, such as how long
  authorizations, studies, or transitions run, and which overlap.
- **Design:** sort rows by start date. Mark today with a vertical line.

### Gantt chart

- **Shows:** tasks as horizontal bars over time.
- **Use when:** overlapping work streams and their durations matter.
- **Design:** sort tasks by start date. Mark today with a vertical line.
  Color the critical path.

---

## Tables

### Highlight table

- **Shows:** exact values in rows and columns, with the key cells
  highlighted.
- **Use when:** the audience needs to look up exact values, or the data has
  many dimensions and no single chart works.
- **Design:** remove vertical lines and most horizontal lines. Right-align
  numbers and use consistent decimals. Shade or bold the cells that support
  the headline. On a slide, keep tables to four rows × three columns or
  fewer.
  Larger tables go in the appendix or the report.

---

## Techniques borrowed from strong examples

These techniques come from award-winning and widely cited visualizations
(Pew Research Center, the Financial Times, Minard, Nightingale, Snow,
Priestley). Each one works in a static slide or printed figure.

| Technique | What it does | Use it for |
|---|---|---|
| Reference marker on each bar | Gives every category its own comparison point | Share of risk versus share of population, by market |
| Second value as an annotation | Puts a related number next to each bar so readers see over- and under-representation without a second chart | "18% of revenue, 6% of area" labels on each bar |
| Paneling a complex chart | Splits one busy chart into panels, each highlighting one group in light blue | Alluvials, multi-scenario lines, before and after maps |
| Linked secondary chart | Puts a small chart under a map or main chart on the same axis, so a second variable explains the first | A coverage map with a distance-versus-I/N chart below it |
| Nested shading | Shows a subset inside its total in one shape | Area inside zones versus total area |
| Hatching for uncertainty | Marks uncertain categories with a pattern instead of a new color | Maps with "under study" or "not yet coordinated" regions |
| Scale against the familiar | Draws an unfamiliar size next to a known one | Zone area next to a state outline |
| Size plus width on flow maps | Uses circle size for totals and line width for flows | Where interference sources concentrate |
| Equal-sized geography | Uses tiles or a cartogram so small, dense areas aren't lost | License areas by population or value |

### What to skip from showcase galleries

Many "best of" galleries feature work that doesn't fit a briefing. Skip
these:

- **Interactive filters, tooltips, and search.** Slides and reports are
  static. Decide what to show instead.
- **3D globes and 3D renders.** They look impressive and distort size.
- **Animation and video.** Out of scope for this skill.
- **Dark backgrounds for drama.** They project poorly in lit rooms and print
  badly. Use the template background.
- **Radial and circular layouts** (rose plots, radial bars, circular
  packing). They're eye-catching but hard to compare. Use a bar chart.
- **Data art.** Abstract compositions trade accuracy for beauty.

---

## Charts to avoid

- **3D charts of any kind.** Perspective distorts the values.
- **Pie charts with more than two slices, donut charts,** or comparisons
  between pies.
- **Dual-axis charts.** Two scales imply relationships that may not exist.
  Use two charts aligned on the same x-axis.
- **Radar (spider) charts.** Area and angle are hard to read, and the
  category order changes the shape.
- **Rose (polar area) charts and radial bars.** Angle and area are hard to
  compare. Nightingale's rose was persuasive in 1858, but a bar chart shows
  the same data more accurately.
- **Line and column combinations on two axes.** This is a dual-axis chart in
  disguise. Use two charts aligned on the same x-axis.
- **Packed bubble charts.** Area is hard to compare. Use a sorted bar.
- **Gauges and speedometers.** They take a lot of space for one number. Use
  a big number or a bullet chart.
- **Word clouds.** Size by frequency is imprecise and says little.
- **Rainbow (jet) color scales.** They create false boundaries and fail for
  colorblind viewers. Use viridis or a single-hue scale.

---

## Audience fit at a glance

| Chart | Leadership | Technical |
|---|---|---|
| Big number, bar, line, slope, waterfall, timeline | Yes | Yes |
| Map with zones, band plan, icon array, waffle | Yes | Yes |
| Diverging bar, bar with reference marker, nested shading, scale comparison | Yes | Yes |
| Tile map, dot density map, flow map, duration timeline | Yes | Yes |
| Dumbbell, dot plot, small multiples, bump chart | Yes, with one sentence of explanation | Yes |
| Quantile dotplot, back-to-back bars, paneled alluvial | Yes, with one sentence of explanation | Yes |
| Exceedance curve or CDF | Only if annotated with the answer in words | Yes |
| Range bar or fan chart | Yes, with plain range labels | Yes |
| Histogram, scatter, beeswarm, cumulative curve, cartogram | Sometimes, with a strong annotation | Yes |
| Box plot, violin, connected scatter, network, spectrum mask | Backup slides only | Yes |
