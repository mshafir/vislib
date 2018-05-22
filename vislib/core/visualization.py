from jinja2 import Environment, PackageLoader
from IPython.core.display import display, HTML
import webbrowser, os


env = Environment(
    loader=PackageLoader('vislib', 'templates'))


def run_from_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


class Visualization:
    def __init__(self, type, template):
        self.type = type
        self.template = template

    def render(self, **kwargs):
        template = env.get_template(self.template)
        return template.render(**kwargs)

    def display(self, width=600, height=400, **kwargs):
        title = kwargs['title'] if 'title' in kwargs else 'untitled_'+self.type
        outfile = 'output/'+title+'.html'
        fout = open(outfile, 'w')
        fout.write(self.render(**kwargs))
        fout.close()
        if run_from_ipython():
            return display(HTML("""
                <iframe src="{source}" width="{width}" height="{height}" style="border: none">
            """.format(source=outfile, width=width, height=height)))
        else:
            webbrowser.open('file://' + os.path.realpath(outfile))
