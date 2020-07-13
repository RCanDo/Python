#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Lines on Mapbox in Python
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly, plotly.express]
description: |
remarks:
todo:
sources:
    - title: Lines on Mapbox in Python
      link: https://plotly.com/python/lines-on-mapbox/
      date: 2020-07-13
      authors:
          - nick: plotly
      usage: |
          not only copy
    - link: https://plotly.com/python/mapbox-layers/
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: "~/Python/graphics/Plotly/"
    date: 2020-07-13
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
cd "~/Works/Python/graphics/Plotly"

#%%
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 150)
pd.set_option('display.max_rows', 150)

#%%
import plotly.express as px
px.set_mapbox_access_token('pk.eyJ1IjoibWFybGVuYWR1ZGEiLCJhIjoiY2tjYW1kY2g0MXU5ZjJzcXA0MWN4dWIwYSJ9.ZSaNpYw_pWxdaY9gMNNTpQ')

import plotly.io as pio
pio.renderers

#%%
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
us_cities = us_cities.query("State in ['New York', 'Ohio']")
us_cities.head()

#%% using Plotly Express

fig = px.line_mapbox(us_cities, lat="lat", lon="lon", color="State", zoom=3, height=500)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show(renderer='firefox')

#%% using Scattermapbox traces

import plotly.graph_objects as go

pio.orca.config.mapbox_access_token = 'pk.eyJ1IjoibWFybGVuYWR1ZGEiLCJhIjoiY2tjYW1kY2g0MXU5ZjJzcXA0MWN4dWIwYSJ9.ZSaNpYw_pWxdaY9gMNNTpQ'

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30],
    lat = [10, 20, 30],
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [-50, -60,40],
    lat = [30, 10, -20],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show()


#%%


#%%


#%%
