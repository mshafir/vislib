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

```
from vislib.visjs.timeline import timeline
timeline(
    title="example1",
    text_values=["first", "second", "third"],
    start_values=["2018-05-21 17:30:08.202", "2018-05-21 17:31:53.712", "2018-05-21 18:14:05.843"])
```
