# Decluttering a chart

Default charts from PowerPoint, Excel, MATLAB, and matplotlib carry a lot of
ink that doesn't help anyone read the data. Strip it in this order. After
each step, ask whether the chart still makes the headline obvious. If it
does, the removed element wasn't needed.

## Procedure

1. **Remove the chart title** inside the chart area. The slide headline or
   figure title already says it, as a sentence.
2. **Remove the border** around the chart and the plot area.
3. **Remove background fills** and any shading behind the plot.
4. **Lighten or remove gridlines.** Keep light gray (`#E6E6E6`) horizontal
   gridlines only if readers need to estimate values. Remove vertical
   gridlines.
5. **Remove tick marks.** Keep the tick labels.
6. **Remove the axis line** on the value axis. Keep the baseline (the zero
   line) on bar charts, in medium gray.
7. **Remove the legend** and label series directly: at the end of each line,
   or inside or next to each bar.
8. **Replace the value axis with data labels** when there are about 10 bars
   or fewer. Then remove the value axis entirely.
9. **Cut data label precision.** Use whole numbers or one decimal at most,
   and put units on the first label only or in the axis title.
10. **Gray everything,** then color the one series, bar, or point that
    carries the headline in light blue.
11. **Remove markers** from lines with many points. Keep one marker at the
    point you annotate.
12. **Remove effects:** 3D, shadows, gradients, bevels, glows, and rounded
    corners.
13. **Shorten axis labels** to plain words with units, such as "Revenue
    ($B)" or "Distance (km)." Don't rotate text. If labels are long, switch
    to horizontal bars.
14. **Add one annotation** where the audience should look, in light
    blue or dark gray, two to six words long.

## Tool-specific defaults to change

### PowerPoint and Excel native charts

- Delete the chart title and legend.
- Set the gap width on bar charts to 50–80%.
- Format the value axis: no line, light gray labels, or delete it if you add
  data labels.
- Format the major gridlines to 0.75 pt, `#E6E6E6`, or delete them.
- Format each data series individually to apply gray and light blue.
- To apply these settings in code, use `scripts/pptx_chart_style.py`.

### MATLAB

MATLAB defaults to a full box around the axes, inward ticks, a default color
order, and small fonts.

- Turn off the box: `box(ax, "off")`.
- Set ticks outward or remove them: `ax.TickDir = "out"` or
  `ax.TickLength = [0 0]`.
- Set font size for the final output size, not the screen.
- Replace the color order with gray plus light blue.
- Replace the legend with `text` labels at the line ends.
- Use `exportgraphics(fig, "name.emf", ContentType="vector")` for Office, or
  `.pdf` or `.png` with `Resolution=300`.
- To apply these settings in one call, use `scripts/briefing_style.m`.

### matplotlib

- Hide the top and right spines; lighten the others. For horizontal bars,
  move the gridlines to the x-axis and use the left spine as the zero
  baseline (see the comment in `assets/briefing.mplstyle`).
- Use `assets/briefing.mplstyle` with `plt.style.use(path)`.
- Save with `fig.savefig("name.svg")` or `dpi=300` for PNG, and
  `bbox_inches="tight"`.

## Before and after test

Look at the original and the decluttered version side by side. The
decluttered version should make the headline faster to see. If it made the
chart harder to read (for example, you removed the only cue for the scale),
put that element back.
