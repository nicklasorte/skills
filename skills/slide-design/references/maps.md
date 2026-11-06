# Maps

Maps are persuasive because people trust them, and misleading for the same
reason. Large, empty areas dominate visually, and the classification choice
can change what the map seems to say. Use these rules for every map. For map
chart types, see `chart-types.md`.

## Choose what to map

- **Map rates and shares with a choropleth,** such as percentage of
  population inside a zone. Fill color for raw counts misleads, because big
  areas look important regardless of their values.
- **Map counts and totals with proportional symbols,** such as number of
  affected sites or license value, sized by area.
- **Map individual sites with dots** or a dot density map.
- **Map areas where a rule applies with outlined, semi-transparent zones**
  over a light basemap.
- **Map value per area with a tile map or cartogram** when population or
  dollars matter more than land area.
- **Pair the map with a number.** A zone map shows where; a big number
  beside it shows how much ("12 million people," "$4 billion in license
  value").

## Classify choropleth data on purpose

The method you choose to group values into classes changes the story. Pick
it deliberately and say which one in the caption.

| Method | How it works | Use when | Watch out for |
|---|---|---|---|
| Equal interval | Splits the value range into equal-sized classes | Data is spread evenly, or the units are familiar (such as percentages) | Data often bunches into one or two classes |
| Quantile | Puts the same number of regions in each class | You want to show relative rank | Very different values can share a class; nearly equal values can split |
| Natural breaks (Jenks) | Finds gaps in the data | Data is uneven but not heavily skewed | Breaks are hard to compare across maps |
| Standard deviation | Classes are steps above and below the mean | Data is roughly normal and "above or below average" is the point | Hard for lay audiences to read |
| Manual | You set the breaks | A meaningful threshold exists, such as a protection limit or policy target | Must be justified in the caption |

For briefings, manual breaks at meaningful values are often the clearest
choice, rounded to clean numbers (for example, 0–10%, 10–25%, 25–50%, more
than 50%).

**Number of classes:** use four to six. Fewer can hide patterns; more make
the colors hard to tell apart.

## Design rules

- **Basemap:** light gray land, white or very light water, thin gray
  boundaries. Remove terrain, roads, and labels you don't need.
- **Data layer:** NTIA light blue for a single zone layer, or the
  sequential blue ramp in `color.md` for classed data. Use purple only for a
  second highlighted zone type.
  Semi-transparent fills (about 40–60%) let the basemap show through.
- **Labels:** only the places the headline mentions, plus two or three
  reference cities for orientation.
- **Legend:** short, plain labels with clean breaks, placed in open space on
  the map. For a single zone layer, label the zone directly instead.
- **Scale:** add a simple scale bar, or a familiar comparison such as "about
  the distance from Washington to Baltimore."
- **Extent:** crop tightly to the area that matters. Keep the extent and
  scale identical across maps the audience will compare.
- **Projection:** use an equal-area projection (such as Albers for the
  contiguous U.S.) when area comparisons matter. Don't use Web Mercator for
  national maps; it inflates northern areas.
- **Uncertainty:** use hatching or a dashed outline for areas that are
  uncertain, under study, or preliminary.
- **North arrow:** omit it unless the map isn't north-up.
- **Location precision:** show federal sites and coordination zones only at
  the precision public sources already show (see the clearance check in
  `ntia-talking-deck`).

## Tools

- **MATLAB:** use Mapping Toolbox (`geoaxes`, `geoplot`, `geobasemap`) and
  set a light basemap such as `"grayland"` or `"none"` with your own
  boundaries. See the `matlab-builtin-first` skill.
- **Python:** use GeoPandas with matplotlib and the style in
  `assets/briefing.mplstyle`. Use `mapclassify` for classification.
- Export maps as vector (SVG, PDF, or EMF) when the layer count allows, or as
  PNG at 300 dpi.
