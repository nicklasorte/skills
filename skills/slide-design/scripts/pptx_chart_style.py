"""Declutter a python-pptx chart and apply the gray-plus-accent approach.

Usage:
    from pptx_chart_style import style_chart

    chart = graphic_frame.chart
    style_chart(chart, highlight=[2])          # bar chart: accent on point 2
    style_chart(chart, highlight_series=[0])   # line chart: accent on series 0

Defaults use the NTIA palette. Leave `font_name` as None so the chart
inherits the NTIA template's theme font.
"""

from pptx.dml.color import RGBColor
from pptx.enum.chart import (XL_CHART_TYPE, XL_LABEL_POSITION,
                             XL_MARKER_STYLE, XL_TICK_MARK)
from pptx.util import Pt

# NTIA palette (see references/color.md).
GRAY_CONTEXT = RGBColor(0x8A, 0x8D, 0x91)   # mid gray: context series
GRAY_TEXT = RGBColor(0x16, 0x33, 0x53)      # dark blue: labels and text
GRAY_GRID = RGBColor(0xE6, 0xE6, 0xE6)      # light gray: gridlines
GRAY_BASELINE = RGBColor(0x8A, 0x8D, 0x91)  # mid gray: axis baseline
ACCENT = RGBColor(0x56, 0x74, 0xC4)         # NTIA light blue: the highlight
SECOND = RGBColor(0x6E, 0x4F, 0x92)         # NTIA purple: second highlight

_BAR_TYPES = {
    XL_CHART_TYPE.BAR_CLUSTERED,
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    XL_CHART_TYPE.BAR_STACKED,
    XL_CHART_TYPE.COLUMN_STACKED,
    XL_CHART_TYPE.BAR_STACKED_100,
    XL_CHART_TYPE.COLUMN_STACKED_100,
}
_LINE_TYPES = {
    XL_CHART_TYPE.LINE,
    XL_CHART_TYPE.LINE_MARKERS,
}


def set_alt_text(shape, text, title=None):
    """Set alt text on any shape, picture, group, chart, or table frame.

    Section 508 requires alt text on meaningful visuals. Write the takeaway
    and the chart type, then the key values. Mark purely decorative shapes
    as decorative in PowerPoint (right-click > View Alt Text).
    """
    c_nv_pr = shape._element.xpath("./*[1]/p:cNvPr")[0]
    c_nv_pr.set("descr", text)
    if title:
        c_nv_pr.set("title", title)
    return shape


def strip_effects(shape):
    """Remove theme-inherited shadows and effects from an autoshape.

    python-pptx shapes carry a <p:style> element that pulls a shadow and an
    outline from the theme, and `shape.shadow.inherit = False` doesn't always
    remove the rendered shadow. Removing <p:style> does. Set the fill and line
    explicitly afterward, because they no longer come from the theme.
    """
    sp = shape._element
    for style in sp.xpath("./p:style"):
        sp.remove(style)
    return shape


def _hex(value):
    """Convert '#RRGGBB' or an RGBColor to an RGBColor."""
    if isinstance(value, RGBColor):
        return value
    return RGBColor.from_string(value.lstrip("#"))


def style_chart(chart, highlight=None, highlight_series=None,
                accent=ACCENT, font_name=None, font_size=16,
                data_labels=True, number_format="#,##0",
                keep_value_axis=None):
    """Apply decluttered, gray-plus-accent styling to a chart.

    Args:
        chart: A pptx.chart.chart.Chart.
        highlight: For single-series bar charts, indexes of points to color
            with the accent. Other points are gray.
        highlight_series: Indexes of series to color with the accent. Other
            series are gray. Defaults to [0] for multi-series charts.
        accent: Accent color as '#RRGGBB' or RGBColor.
        font_name: Font for all chart text. None keeps the template font.
        font_size: Chart text size in points. The NTIA label size is 16.
        data_labels: Add value labels (bar charts) and remove the value axis.
        number_format: Excel number format for data labels.
        keep_value_axis: Force the value axis on or off. Defaults to off when
            data labels are on.
    """
    accent = _hex(accent)
    chart_type = chart.chart_type
    is_bar = chart_type in _BAR_TYPES
    is_line = chart_type in _LINE_TYPES

    # Remove the in-chart title and legend; the slide headline does that job.
    chart.has_title = False
    chart.has_legend = False

    chart.font.size = Pt(font_size)
    chart.font.color.rgb = GRAY_TEXT
    if font_name:
        chart.font.name = font_name

    # Category axis: no tick marks, a quiet baseline.
    cat_axis = chart.category_axis
    cat_axis.major_tick_mark = XL_TICK_MARK.NONE
    cat_axis.minor_tick_mark = XL_TICK_MARK.NONE
    cat_axis.has_major_gridlines = False
    cat_axis.format.line.color.rgb = GRAY_BASELINE
    cat_axis.format.line.width = Pt(0.75)
    cat_axis.tick_labels.font.size = Pt(font_size)
    cat_axis.tick_labels.font.color.rgb = GRAY_TEXT

    # Value axis: off when data labels carry the values, else light.
    val_axis = chart.value_axis
    val_axis.major_tick_mark = XL_TICK_MARK.NONE
    val_axis.minor_tick_mark = XL_TICK_MARK.NONE
    val_axis.format.line.fill.background()
    show_val_axis = (keep_value_axis if keep_value_axis is not None
                     else not (is_bar and data_labels))
    val_axis.visible = show_val_axis
    if show_val_axis:
        val_axis.has_major_gridlines = True
        grid = val_axis.major_gridlines.format.line
        grid.color.rgb = GRAY_GRID
        grid.width = Pt(0.75)
        val_axis.tick_labels.font.size = Pt(font_size)
        val_axis.tick_labels.font.color.rgb = GRAY_TEXT
    else:
        val_axis.has_major_gridlines = False
    if is_bar:
        # Bars must start at zero.
        val_axis.minimum_scale = 0

    plot = chart.plots[0]
    series_list = list(plot.series)
    if highlight_series is None and len(series_list) > 1:
        highlight_series = [0]
    highlight_series = set(highlight_series or [])
    highlight = set(highlight or [])

    if is_bar:
        plot.gap_width = 60
        if len(series_list) > 1:
            plot.overlap = 0 if chart_type in (
                XL_CHART_TYPE.BAR_CLUSTERED,
                XL_CHART_TYPE.COLUMN_CLUSTERED) else 100

    for s_idx, series in enumerate(series_list):
        series_on = s_idx in highlight_series
        color = accent if series_on else GRAY_CONTEXT
        if is_line:
            series.smooth = False
            series.format.line.color.rgb = color
            series.format.line.width = Pt(3 if series_on else 2)
            series.marker.style = XL_MARKER_STYLE.NONE
        else:
            series.format.fill.solid()
            series.format.fill.fore_color.rgb = color
            series.format.line.fill.background()
            # Single-series bars: color individual points.
            if len(series_list) == 1 and highlight:
                n_points = len(list(series.values))
                for p_idx in range(n_points):
                    point = series.points[p_idx]
                    point.format.fill.solid()
                    point.format.fill.fore_color.rgb = (
                        accent if p_idx in highlight else GRAY_CONTEXT)
                    point.format.line.fill.background()

    if is_bar and data_labels:
        plot.has_data_labels = True
        labels = plot.data_labels
        labels.number_format = number_format
        labels.number_format_is_linked = False
        labels.font.size = Pt(font_size)
        labels.font.color.rgb = GRAY_TEXT
        if chart_type in (XL_CHART_TYPE.BAR_CLUSTERED,
                          XL_CHART_TYPE.COLUMN_CLUSTERED):
            labels.position = XL_LABEL_POSITION.OUTSIDE_END
        else:
            labels.position = XL_LABEL_POSITION.CENTER

    return chart
