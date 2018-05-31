import webbrowser
import pandas as pd
from IPython.core.display import display, HTML
import webbrowser, os


def convert_data(data):
    if isinstance(data, pd.DataFrame):
        return data.reset_index().to_dict('records')
    else:
        return data


def display_html(html, title, width=600, height=400):
    if not os.path.exists('output'):
        os.makedirs('output')
    if title is None:
        title = 'Untitled'
    outfile = 'output/' + title + '.html'
    fout = open(outfile, 'w')
    fout.write(html)
    fout.close()
    if run_from_ipython():
        return display(HTML("""
            <iframe src="{source}" width="{width}" height="{height}" style="border: none">
        """.format(source=outfile, width=width, height=height)))
    else:
        webbrowser.open('file://' + os.path.realpath(outfile))


def run_from_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


