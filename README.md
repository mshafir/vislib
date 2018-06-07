# vislib
A library of web-based visualizations for python and ipython

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
 make html
```

### Publish
```
python setup.py sdist bdist_wheel
twine upload dist/*
```

