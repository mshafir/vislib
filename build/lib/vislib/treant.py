from vislib.core.visualization import BasicVisualization, Asset
import json


class Treant(BasicVisualization):
    def __init__(self, styling=''):
        BasicVisualization.__init__(self,
                                    'Tree',
                                    [Asset('//cdnjs.cloudflare.com/ajax/libs/raphael/2.2.7/raphael.min.js', 'js'),
                                     Asset('//cdnjs.cloudflare.com/ajax/libs/treant-js/1.0/Treant.min.js', 'js'),
                                     Asset('//cdnjs.cloudflare.com/ajax/libs/treant-js/1.0/Treant.css', 'css')],
                                    """
                                    var my_chart = new Treant({
                                        chart: {{ options }},
                                        nodeStructure: {{ chart_data }}
                                    });
                                    """,
                                    {
                                        "container": '#visualization'
                                    },
                                    styling)

    def get_parameters(self, data, options):
        return {'chart_data': json.dumps(data)}


def tree(data, title=None, width=800, height=400, styling='', **options):
    """Renders a Treant.js tree. See http://fperucic.github.io/treant-js/

    :Example:
    >>> from vislib.treant import tree
    >>> tree({
    >>>         'text': { 'name': "Parent node" },
    >>>         'children': [{
    >>>             'text': { 'name': "First child" }
    >>>         },{
    >>>             'text': { 'name': "Second child" }
    >>>         }]
    >>>     })

    :param data: A dict in the json format specified for treant.
    :param title: A title to assign to your timeline view, this will be the filename of the saved html file on disk
    :param width:
    :param height:
    :param styling: Custom raw css to apply to the chart
    :param options: Additional chart options for the treant tree
    :return: in ipython, a visualized tree, otherwise None, but triggers opening your default browser with the generated file
    """
    return Treant(styling).set_options(**options).display(data=data, title=title, width=width, height=height)
