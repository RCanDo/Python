#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Plotly Express in Python
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly express]
description: |
remarks:
todo:
sources:
    - title: Plotly Express in Python
      link: https://plotly.com/python/plotly-express/
      date: 2020-07-10
      authors:
          - nick: plotly
      usage: |
          not only copy
    - title: Pandas Plotting Backend in Python
      link: https://plotly.com/python/pandas-backend/
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

import plotly.io as pio
pio.renderers.default
# pio.renderers.default = "firefox"
# ...
# fig  #! Error: could not locate runnable browser
# solution?
# 1.
pio.renderers.default = "browser"

# 2. https://stackoverflow.com/questions/48056052/webbrowser-get-could-not-locate-runnable-browser
# not checked for Firefox
import webbrowser
urL='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(urL)

#%%
dir(px.data)
dir(px.colors)

#%% BTW:
#%% Plotly Express backend for Pandas
# https://plotly.com/python/pandas-backend/
pd.options.plotting.backend = "plotly"
df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot()
fig
fig.show(renderer="browser")

iris = px.data.iris()
iris.head()
iris.plot()  #! ValueError: Plotly Express cannot process wide-form data with columns of different type.
iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].plot()


#%%
#%% Gallery
"""
The following set of figures is just a sampling of what can be done with
Plotly Express.
"""

#%% Scatter, Line, Area and Bar Charts
# https://plotly.com/python/line-and-scatter/
# https://plotly.com/python/discrete-color/
#
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
fig

#%%
# https://plotly.com/python/linear-fits/
# https://plotly.com/python/templates/
#
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 marginal_y="violin", marginal_x="box",
                 trendline="ols", template="simple_white")
fig.show(renderer="browser")

#%%
# https://plotly.com/python/error-bars/
#
iris['err_width'] = iris['sepal_width']/100
iris['err_length'] = iris['sepal_length']/100
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 error_x = "err_width", error_y = "err_length")
fig.show(renderer="browser")


#%%
# https://plotly.com/python/bar-charts/
#
tips = df = px.data.tips()
fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group")
fig.show(renderer="browser")

#%% https://plotly.com/python/facet-plots/
#
fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
fig.show(renderer="browser")

#%%
# https://plotly.com/python/splom/
#
fig = px.scatter_matrix(iris,
        dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
        color="species")
fig.show(renderer="browser")

#%%

...

#%%
#%% Part to Whole Charts

#%%

...

#%%
#%% Distributions

#%%

...

#%%
#%% Images and Heatmaps


...

#%%
#%% Maps    https://plotly.com/python/plotly-express/#maps
# https://plotly.com/python/mapbox-layers/
# https://plotly.com/python/scattermapbox/

#%%

...

#%%
#%% Distributions

#%%

