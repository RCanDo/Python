#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: The Figure Data Structure in Python
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly]
description: |
remarks:
todo:
sources:
    - title: The Figure Data Structure in Python
      chapter:
      link: https://plotly.com/python/figure-structure/
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

"""
Note: the recommended entry-point into the plotly package is the high-level 
`plotly.express`  module, also known as Plotly Express, 
which consists of Python functions which return fully-populated 
`plotly.graph_objects.Figure`  objects. 

This page exists to document the architecture of the data structure 
that these objects represent, 
for users who wish to understand more about how to customize them, 
or assemble them from other  `plotly.graph_objects`  components.
"""

#%% 
cd "~/Works/Python/graphics/Plotly"

#%%
import plotly.express as px
import plotly.graph_objects as go

#!!!  https://plotly.com/python/renderers/  or see  02-displaying_figures.py
import plotly.io as pio
# pio.renderers
pio.renderers.default = 'firefox'

#%%
fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()
fig


#%%
#%% Figures as Trees of Attributes



#%%



#%%
