# Native shapes, icons, and diagrams

Nick wants every icon and diagram built from native PowerPoint shapes. Don't
insert pictures, SVGs, emoji, or icon-set graphics. Native shapes stay
editable, scale cleanly, pick up theme colors, and don't break when the deck
moves between machines.

Don't add animation or slide transitions.

## Icon style

- Keep icons simple: one to four shapes each.
- Use solid fills, no outlines. Use dark blue by default and light blue only
  for the icon that carries the point.
- Fit every icon in a square box, one size per deck: 48 pt in cards and
  flows, 32 pt in icon arrays.
- Pair every icon with a short text label. Icons alone are ambiguous.
- Use icons only when they help scanning, such as three parallel ideas.
  Don't put an icon on every slide.

## Icon recipes

Build these from basic PowerPoint autoshapes.

| Concept | Shapes |
|---|---|
| Tower or antenna | Isosceles triangle (tall, thin) on a small rectangle, plus two or three arcs above for signal |
| Radar | Pie or chord shape (wedge) plus a small circle at the center |
| Satellite | Small rectangle body with two flat rectangles as panels |
| Location pin | Teardrop shape rotated 135° with a small circle inside |
| Building or agency | Rectangle with a triangle on top and three thin rectangles as columns |
| Money | Circle with a "$" text box centered |
| Person | Circle (head) above a rounded rectangle or a "flowchart: delay" shape (shoulders) |
| Clock or time | Circle with two thin rectangles as hands |
| Warning | Isosceles triangle with an "!" text box |
| Check or done | Circle with a "✓" character, or two rotated thin rectangles |
| Shield or protection | "Flowchart: off-page connector" shape, which reads as a shield |
| Frequency or wave | Wave shape or a series of arcs; or a freeform curve |
| Document | Folded-corner rectangle |
| Arrow for flow | Block arrow or a connector line with an arrowhead |

After building an icon, group its shapes so it moves as one object.

## Diagram rules

- Flow left to right or top to bottom. Don't mix directions.
- Use five to seven boxes at most per slide.
- Use one shape per type of element (for example, rounded rectangles for
  steps and diamonds for decisions) and keep it consistent.
- Use elbow or straight connectors, attached to the shapes so they move with
  them.
- Keep connector lines thin (1–1.5 pt) and gray. Use light blue only for the
  path that matters.
- Put a short verb phrase in each box, at 16 pt.
- Align boxes to a grid and space them evenly. Use PowerPoint's Align and
  Distribute commands, or set positions in code.

## Building shapes in code (python-pptx)

```python
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                             Inches(1), Inches(2), Inches(2.5), Inches(1))
box.fill.solid()
box.fill.fore_color.rgb = RGBColor(0xE8, 0xE9, 0xEA)   # NTIA grey
box.line.fill.background()            # no outline
strip_effects(box)                    # no theme shadow (scripts/pptx_chart_style.py)
tf = box.text_frame
tf.text = "Agency requests"
tf.paragraphs[0].runs[0].font.size = Pt(16)
tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x16, 0x33, 0x53)  # dark blue

line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                  Inches(3.5), Inches(2.5),
                                  Inches(4.5), Inches(2.5))
line.line.color.rgb = RGBColor(0x8A, 0x8D, 0x91)  # mid gray
line.line.width = Pt(1.5)
```

Call `strip_effects()` on every autoshape. python-pptx shapes inherit a
shadow from the theme, and `shape.shadow.inherit = False` doesn't reliably
remove it. Import it with
`from pptx_chart_style import strip_effects, set_alt_text`.
