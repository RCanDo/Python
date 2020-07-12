#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Getting Started with Plotly in Python
subtitle: Installation
version: 1.0
type: tutorial/examples
keywords: [plotly, dash, installation]
description: |
remarks:
todo:
sources:
    - title: Getting Started with Plotly in Python
      link: https://plotly.com/python/getting-started/
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
    date: 2020-07-09
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
conda install -c plotly plotly=4.8.2
"""
import plotly
plotly.__version__   # 4.8.2

import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('figure_01.html', auto_open=True)

#%% Jupyter Notebook Support
"""
conda install "notebook>=5.3" "ipywidgets>=7.2"

within the jupyter notebook file:
"""
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()

## or using FigureWidget objects.

import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig

#%% JupyterLab Support (Python 3.5+)
"""
conda install jupyterlab "ipywidgets=7.5"

#!!! the rest requires https://nodejs.org/en/ to be installed ... :(

# JupyterLab renderer support
jupyter labextension install jupyterlab-plotly@4.8.2

# OPTIONAL: Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.8.2

# These packages contain everything you need to run JupyterLab...
$ jupyter lab

# and display plotly figures inline using the plotly_mimetype renderer...
"""
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()

#%% Static Image Export Support
"""
...
conda install -c plotly plotly-orca==1.2.1 psutil requests

# These packages contain everything you need to save figures 
as static images.
"""
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig.write_image('figure_01.png')

"""
https://plotly.com/python/static-image-export/
"""
#%% Extended Geo Support
"""
conda install -c plotly plotly-geo=1.0.0

go to 
https://plotly.com/python/county-choropleth/
for example
"""

#%% Chart Studio Support
"""
The chart-studio package can be used to upload plotly figures 
to Plotly's Chart Studio Cloud or On-Prem services.

conda install -c plotly chart-studio=1.0.0
"""

