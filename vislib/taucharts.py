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

    def get_parameters(self, data, options):
        params = options
        params['x'] = self.x
        params['y'] = self.y
        if self.color is not None:
            params['color'] = self.color

        params['data'] = convert_data(data)
        return {'options': params}


def chart(data, x, y, color=None, title=None, width=800, height=400, **options):
    """Renders a basic taucharts chart with the given data. See https://www.taucharts.com/

    >>> from vislib.taucharts import chart
    >>> chart([{'item': 'car', 'amount': 1},
    >>>        {'item': 'book', 'amount': 10},
    >>>        {'item': 'bed', 'amount': 3}], x='item', y='amount', title='Taucharts example')

    :param data: a pandas DataFrame or list of dictionaries that specify the data to visualize
    :param x: the field to map as the x coordinate
    :param y: the field to map as the y coordinate
    :param color: the field to map to the color of the datapoints
    :param title: A title to assign to your timeline view, this will be the filename of the saved html file on disk
    :param width:
    :param height:
    :param options: Additional options to pass as the chart definition (See https://api.taucharts.com/basic/index.html)
        Some common options include
        * type: scatterplot, line, bar, horizontalBar, stacked-bar, stacked-area
        * size: field to map to the size of a node
        * dimensions: allows setting custom axis labels and types
        * guide: allows customizing visual elements of the chart presentation
    :return: in ipython, a visualized chart, otherwise None, but triggers opening your default browser with the generated file
    """
    return Taucharts(x, y, color=color).set_options(**options).display(data=data, title=title, width=width, height=height)
