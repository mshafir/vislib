import json

from vislib.core.core_utils import convert_data
from vislib.core.time_utils import convert_timestamp
from vislib.core.visualization import BasicVisualization, Asset


def add_field(data, source_data, field_target, field_source, convert=None):
    if field_source is not None:
        for i, value in enumerate(source_data):
            if convert is not None:
                value = convert(value[field_source])
            data[i][field_target] = value


class Timeline(BasicVisualization):
    def __init__(self, content_field, start_field, end_field=None, type_field=None, group_field=None):
        BasicVisualization.__init__(self,
                                    'Timeline',
                                    [Asset('https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js', 'js'),
                                     Asset('https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css', 'css')],
                                    """
                                    var container = document.getElementById('visualization');
                                    var items = new vis.DataSet({{ data }});
                                    var timeline = new vis.Timeline(
                                        document.getElementById('visualization'), items,
                                        {% if groups is defined %}{{ groups }}, {% endif %}
                                        {{ options }});
                                    """,
                                    {
                                        "type": 'point',
                                        "locale": 'en_US',
                                        "maxHeight": "100vh",
                                        "maxWidth": "100vw",
                                        "horizontalScroll": True,
                                        "stack": True,
                                        "orientation": 'top',
                                        "zoomKey": 'crtlKey'
                                    })
        self.content_field = content_field
        self.start_field = start_field
        self.end_field = end_field
        self.type_field = type_field
        self.group_field = group_field

    def get_parameters(self, data):
        params = {}
        data = convert_data(data)
        timeline_data = [{"id": i,
                          "content": d[self.content_field],
                          "start": convert_timestamp(d[self.start_field])} for i, d in enumerate(data)]

        add_field(timeline_data, data, "end", self.end_field, lambda v: convert_timestamp(v))
        add_field(timeline_data, data, "type", self.type_field)
        groups = {}

        def register_group(name):
            if not name in groups:
                groups[name] = len(groups)
            return groups[name]

        add_field(timeline_data, data, "group", self.group_field, register_group)
        params['data'] = timeline_data
        if len(groups) > 0:
            params["groups"] = json.dumps([{"id": id, "content": group} for group, id in groups.items()])

        return params


def timeline(data, content_field, start_field, end_field=None, type_field=None, group_field=None,
             title=None, width=600, height=400, **options):
    """
    Renders a vis.js timeline component

    :param data:
    :param content_field:
    :param start_field:
    :param end_field:
    :param type_field:
    :param group_field:
    :param title:
    :param height:
    :param width:
    :param options:
    :return:
    """
    return Timeline(
        content_field=content_field,
        start_field=start_field,
        end_field=end_field,
        type_field=type_field,
        group_field=group_field
    ).set_options(**options).display(data=data, title=title, width=width, height=height)
