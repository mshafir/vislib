# vislib
vislib is a library that wraps common javascript visualization libraries. The variety and capabilities of javascript
visualization libraries exceed what exists in python. Though native python libraries will always have better
integration support, the goal here is to provide a quick and dirty way to embed rich html visualizations as iframes into an
ipython environment or generate them as standalone html files.

The core vislib package provides an abstraction that makes it easy to add new wrappers for additional javascript libraries.
It uses the jinja2 templating library and some standard boilerplate templates to expose the raw capabilities of
each library.

Each visualization is an attempt to strike a balance between completeness, consistency, and simplicity for the visualization API.
Feedback is welcome!

## Set Up / Usage

```
pip install vislib
```

*vislib* is set up to optionally be used within an ipython interactive environment.
If used outside of ipython, it will generate html files and open
the default browser with the created visualizations.

## Visualizations

### vis.js timeline

A library for rich interactive timelines.
Renders a vis.js timeline component. See http://visjs.org/docs/timeline/

```python
from vislib.visjs import timeline
timeline([{'text': 'first item', 'start': '2018-05-21 17:30:08.202'},
          {'text': 'second item', 'start': "2018-05-21 17:31:53.712"},
          {'text': 'third item', 'start': "2018-05-21 18:14:05.843"}], content_field='text', title='example1')
```

### Taucharts

A d3 based charting library that elegantly mixes power and simplicity.
Renders a basic taucharts chart with the given data. See https://www.taucharts.com/

```python
from vislib.taucharts import chart
chart([{'item': 'car', 'amount': 1},
       {'item': 'book', 'amount': 10},
       {'item': 'bed', 'amount': 3}], x='item', y='amount', title='Taucharts example')
```

### Treant

Renders a Treant.js tree. See http://fperucic.github.io/treant-js/

```python
from vislib.treant import tree
tree({
        'text': { 'name': "Parent node" },
        'children': [{
            'text': { 'name': "First child" }
        },{
            'text': { 'name': "Second child" }
        }]
    })
```

## Development

### Generate Documentation

```
 cd docs
 rm -rf _build
 make html
```

### Publish
```
rm -rf dist
python setup.py sdist bdist_wheel
twine upload dist/*
```

