from vislib.core.core_utils import convert_data
from vislib.core.visualization import BasicVisualization, Asset


class Taucharts(BasicVisualization):
    def __init__(self, x, y, color=None):
        BasicVisualization.__init__(self,
                                    'Timeline',
                                    [Asset('//cdn.jsdelivr.net/d3js/3.5.17/d3.min.js', 'js'),
                                     Asset('//cdn.jsdelivr.net/npm/taucharts@1/build/production/tauCharts.min.js', 'js'),
                                     Asset('//cdn.jsdelivr.net/npm/taucharts@1/build/production/tauCharts.min.css', 'css')],
                                    """
                                    var options = {{ options }};
                                    options['plugins'] = [
                                        tauCharts.api.plugins.get('tooltip')(),
                                        tauCharts.api.plugins.get('legend')()
                                    ];
                                    var chart = new tauCharts.Chart(options);
                                    chart.renderTo('#visualization');
                                    """,
                                    {
                                        "type": 'line',
                                    })
        self.x = x
        self.y = y
        self.color = color

    def get_parameters(self, data):
        params = self.options
        params['x'] = self.x
        params['y'] = self.y
        if self.color is not None:
            params['color'] = self.color

        params['data'] = convert_data(data)
        return {'options': params}


def chart(data, x, y, color=None,
          title=None, width=800, height=400, **options):
    return Taucharts(x, y, color=color).set_options(**options).display(data=data, title=title, width=width, height=height)
