import json

from jinja2 import Environment, PackageLoader, Template
from vislib.core.core_utils import display_html

env = Environment(
    loader=PackageLoader('vislib', 'templates'))


class Visualization:
    def __init__(self, type, template):
        self.type = type
        self.template = template

    def render(self, data):
        raise NotImplementedError

    def render_template(self, **kwargs):
        template = env.get_template(self.template)
        return template.render(**kwargs)

    def display(self, data, title=None, width=600, height=400):
        display_html(self.render(data), title, width, height)


class Asset:
    def __init__(self, url, type):
        self.url = url
        self.type = type

    def generate_code(self):
        if self.type == 'css':
            return '<link rel="stylesheet" type="text/css" href="{url}">'.format(url=self.url)
        else:
            return '<script src="{url}" charset="utf-8" type="text/javascript"></script>'.format(url=self.url)


class BasicVisualization(Visualization):
    def __init__(self, type, assets, initial_js, default_options, template='basic.html'):
        Visualization.__init__(self, type, template)
        self.assets = assets
        self.initial_js = initial_js
        self.options = default_options

    def set_option(self, name, value):
        self.options[name] = value

    def set_options(self, **kwargs):
        for k,v in kwargs.items():
            self.options[k] = v
        return self

    def generate_assets(self):
        return '\n'.join([a.generate_code() for a in self.assets])

    def get_parameters(self, data):
        raise NotImplementedError

    def render(self, data):
        params = self.get_parameters(data)
        params['options'] = json.dumps(self.options)
        params['assets'] = self.generate_assets()
        params['js'] = Template(self.initial_js).render(**params)
        return self.render_template(**params)

