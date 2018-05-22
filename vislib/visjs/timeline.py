import pandas as pd
import json

from vislib.core.time_utils import convert_timestamp
from vislib.core.visualization import Visualization


def add_field(data, field_name, field_values, convert=None):
    if field_values is not None:
        for i, value in enumerate(field_values):
            if convert is not None:
                value = convert(value)
            data[i][field_name] = value


def timeline(title, text_values, start_values, end_values=None,
             type_values=None, group_values=None,
             type='point', locale='en_US', horizontalScroll=True, stack=True,
             orientation='top', zoomKey='ctrlKey',
             **kwargs):
    """
    Renders a vis.js timeline component

    :param title: the title for the output
    :type title: str

    :param df: the data frame containing the data to plot
    :type df: pd.DataFrame

    :param text_values: an iterable that determines how to populate the text of each timeline entry
    :param start_values: an iterable that determines the start timestamp of each timeline entry
    :param end_values: an optional iterable that determines the end timestamp of each timeline entry
    :param type_values: an optional iterable that determines the type of each timeline entry
    :param group_values: an optional iterable that determines the group name of each timeline entry

    :param type: the type of vis.js timeline to render. Can be point (default), box, range, or background
    :param locale: the locale for the timeline

    :param height: the height in pixels of the rendered output
    :param width: the width in pixels of the rendered output
    :return:  the visualized timeline as displayed HTML ipython content
    """
    data = [{"id": i,
             "content": text,
             "start": convert_timestamp(start_values[i])} for i, text in enumerate(text_values)]

    add_field(data, "end", end_values, lambda v: convert_timestamp(v))
    add_field(data, "type", type_values)

    groups = {}

    def register_group(name):
        if not name in groups:
            groups[name] = len(groups)
        return groups[name]
    add_field(data, "group", group_values, register_group)

    if len(groups) > 0:
        kwargs["groups"] = json.dumps([{"id": id, "content": group} for group, id in groups.items()])

    return Visualization("vis.js Timeline", "visjs/timeline.html").display(
        title=title,
        data=json.dumps(data),
        type=type,
        locale=locale,
        horizontalScroll=horizontalScroll,
        stack=stack,
        orientation=orientation,
        zoomKey=zoomKey,
        **kwargs
    )

