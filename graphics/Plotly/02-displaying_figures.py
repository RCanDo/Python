#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Displaying Figures in Python 
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly, renderers]
description: |
remarks:
todo:
sources:
    - title: Displaying Figures in Python 
      link: https://plotly.com/python/renderers/
      date: 2020-07-08
      authors:
          - nick: plotly
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: "~/Python/graphics/Plotly/"
    date: 2020-07-08
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% 
cd "~/Works/Python/graphics/Plotly"

#%%
"""
Plotly's Python graphing library, plotly.py, gives you a wide range of options for how and where to display your figures.

In general, there are three different approaches you can take in order to display figures:

    Using the `renderers` framework in the context of a script or notebook
    Using a `FigureWidget` in an `ipywidgets` context
    Using `Dash` in a web app context

"""
#%% Displaying Figures Using The renderers Framework

import plotly.graph_objects as go

fig = go.Figure(
          data=[go.Bar(y=[2, 1, 3])],
          layout_title_text="A Figure Displayed with fig.show()"
        )
fig.show()

#%% 
# In most situations, you can omit the call to .show() 
# and allow the figure to display itself.
fig

"""
To be precise, figures will display themselves using the current default renderer 
when the two following conditions are true:
1. the last expression in a cell must evaluate to a `figure`,
2. `plotly.py` must be running from within an IPython kernel.
"""

#%%
import plotly.io as pio
pio.renderers

pio.renderers.default
pio.renderers.default = "firefox"
fig.show()

#%% Overriding The Default Renderer
fig.show(renderer="svg")

#%% Built-in Renderers
#In this section, we will describe the built-in renderers so that you can choose the one(s) that best suit your needs.

# Interactive Renderers
# ...

# Static Renderers
# ...


#%% Multiple Renderers

#%% Customizing Built-In Renderers
pio.renderers["png"]
pio.renderers["png"].width
pio.renderers["png"].height

pio.renderers["png"].width = 500
pio.renderers["png"].height = 500

fig.show(renderer="png")

# one can also override the values of renderer parameters temporarily
fig.show(renderer="png", width=300, height=300)

#
pio.renderers["firefox"]

#%%