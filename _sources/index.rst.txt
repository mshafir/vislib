.. vislib documentation master file, created by
   sphinx-quickstart on Tue May 22 20:50:20 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

vislib
==================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Introduction
----------------------------------
vislib is a library that wraps common javascript visualization libraries. The variety and capabilities of javascript
visualization libraries far exceed what exists in python. Though native python libraries will always have better
integration support, the goal here is to provide a quick and dirty way to embed rich html visualizations as iframes into an
iptyhon environment or generate them as standalone html files.

The core vislib package provides an abstraction that makes it easy to add new wrappers for additional javascript libraries.
It uses the jinja2 templating library and some standard boilerplate templates to just expose the raw capabilities of
each library.

Each visualization is an attempt to strike a balance between completeness, consistency, and simplicity for the visualization API.
Feedback is welcome!

Currently Supported Visualizations
-----------------------------------

vis.js
^^^^^^^^^^^^^^^^^^
A library for rich interactive timelines: `visjs timelines <http://visjs.org/docs/timeline/>`_

.. automodule:: vislib.visjs
    :members:
    :show-inheritance:

Taucharts
^^^^^^^^^^^^^^^^^^
A d3 based charting library that elegantly mixes power and simplicity, allowing for unique faceted charts: `taucharts <https://www.taucharts.com/>`_

.. automodule:: vislib.taucharts
    :members:
    :show-inheritance:

Treant
^^^^^^^^^^^^^^^^^^
A tree generation library that generates customizable interactive tree hierarchies: `Treant <http://fperucic.github.io/treant-js/>`_

.. automodule:: vislib.treant
    :members:
    :show-inheritance:

Indices and tables
----------------------------------

:ref:`modindex`

:ref:`genindex`

