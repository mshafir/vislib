import json

from vislib.core.core_utils import convert_data
from vislib.core.time_utils import convert_timestamp
from vislib.core.visualization import BasicVisualization, Asset


class Timeline(BasicVisualization):
    def __init__(self, content_field='contents', start_field='start', end_field=None, type_field=None, group_field=None):
        BasicVisualization.__init__(self,
                                    'Timeline',
                                    [Asset('//cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js', 'js'),
                                     Asset('//cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css', 'css')],
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

    @staticmethod
    def add_field(data, source_data, field_target, field_source, convert=None):
        if field_source is not None:
            for i, value in enumerate(source_data):
                if convert is not None:
                    value = convert(value[field_source])
                data[i][field_target] = value

    def get_parameters(self, data, options):
        params = {}
        data = convert_data(data)
        timeline_data = [{"id": i,
                          "content": d[self.content_field],
                          "start": convert_timestamp(d[self.start_field])} for i, d in enumerate(data)]

        self.add_field(timeline_data, data, "end", self.end_field, lambda v: convert_timestamp(v))
        self.add_field(timeline_data, data, "type", self.type_field)
        groups = {}

        def register_group(name):
            if not name in groups:
                groups[name] = len(groups)
            return groups[name]

            self.add_field(timeline_data, data, "group", self.group_field, register_group)
        params['data'] = timeline_data
        if len(groups) > 0:
            params["groups"] = json.dumps([{"id": id, "content": group} for group, id in groups.items()])

        return params


def timeline(data, content_field='contents', start_field='start', end_field=None, type_field=None, group_field=None,
             title=None, width=600, height=400, **options):

    """Renders a vis.js timeline component (See http://visjs.org/docs/timeline/ for more information)

    :Example:
    >>> from vislib.visjs import timeline
    >>> timeline([{'text': 'first item', 'start': '2018-05-21 17:30:08.202'},
    >>>           {'text': 'second item', 'start': "2018-05-21 17:31:53.712"},
    >>>           {'text': 'third item', 'start': "2018-05-21 18:14:05.843"}], content_field='text', title='example1')

    :param data: a pandas DataFrame or list of dictionaries that specify the data to visualize
    :param content_field: the field representing the textual contents of each timeline node
    :param start_field: the field representing the start time (as a date or string) of each timeline node
    :param end_field: the field representing the end time of each timeline node
    :param type_field: the field representing the type of node. Can be 'box', 'point' (default), 'range', or 'background'
    :param group_field: the field representing the group name to assign the timeline node to. Groups appear as swimlanes
        in the timeline view if they exist
    :param title: A title to assign to your timeline view, this will be the filename of the saved html file on disk
    :param height:
    :param width:
    :param options: Additional options to specify for the timeline. See http://visjs.org/docs/timeline/#Configuration_Options
    :return: in ipython, a visualized timeline, otherwise None, but triggers opening your default browser with the generated file
    """
    return Timeline(
        content_field=content_field,
        start_field=start_field,
        end_field=end_field,
        type_field=type_field,
        group_field=group_field
    ).set_options(**options).display(data=data, title=title, width=width, height=height)
