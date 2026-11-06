# Tables

Use a table when the audience needs to look up exact values, or when the data
has too many dimensions for one chart. Use a chart when the pattern matters
more than the numbers.

## Ten guidelines (after Jon Schwabish)

1. **Right-align numbers** so digits line up. Use the same number of decimals
   in a column.
2. **Left-align text.** Center nothing except short column headers over
   narrow columns.
3. **Cut decimals** to one or two at most; zero is often right for briefings.
4. **Show units once,** in the column header or the first row, not in every
   cell: "Revenue ($M)."
5. **Make outliers and key values stand out** with bold or a light-blue
   tinted row.
6. **Make headers distinct** from the body with bold text and a rule under
   them.
7. **Use thin rules and light fills,** or none. Use thin (0.75 pt) mid-gray
   horizontal rules and no vertical rules. The only fills are a grey header
   row or one light-blue-tinted highlighted row. Don't use zebra striping.
8. **Leave white space** between rows and columns. Cell padding does the job
   that gridlines usually do.
9. **Group related rows** with extra space or a light divider, and label the
   group.
10. **Switch to a chart** when a table gets too big to read at a glance.

## Size limits

- **Slides:** four rows × three columns or fewer, at 16 pt. Move anything
  larger to the appendix or a read-ahead page.
- **Read-ahead pages:** up to about 12 rows × 6 columns, at 12 pt or larger.
- **Reports:** any size that fits the page, at 9 pt or larger at final size.
  Repeat the header row on each page.

## Highlight tables and heat tables

- To make one comparison obvious, tint the row that supports the headline
  light blue, and leave the rest white.
- To show patterns across a whole table (read-ahead pages and reports
  only), shade cells with the sequential blue ramp in `color.md`, and keep
  the numbers in the cells.
- Add a tiny sparkline column to show each row's trend, when trends matter.

## Construction

- Build real tables with PowerPoint's or Word's table feature, never as an
  image or as separate text boxes. Real tables are editable and accessible.
- Don't merge or split cells. Merged cells break screen readers and fail
  Section 508 checks. Use a group label row instead.
- Mark the first row as the header row in table properties.
- Put the takeaway in the slide title or the table title, as a sentence.
- Add a source line under the table.
