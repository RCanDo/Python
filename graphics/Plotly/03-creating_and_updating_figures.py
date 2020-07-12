#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Creating and Updating Figures 
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly, renderers]
description: |
remarks:
todo:
sources:
    - title: Creating and Updating Figures 
      link: https://plotly.com/python/creating-and-updating-figures/
      date: 2020-07-10
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
    date: 2020-07-10
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

import plotly.io as pio
pio.renderers.default
# pio.renderers.default = "firefox"

#%% plain python's dict
fig0 = dict({'data': [{"type": "bar",
                      "x": [1, 2, 3],
                      "y": [1, 3, 3]
                     }
                    ],
            'layout': {"title": "figure by python dict"} 
           })
fig0

pio.show(fig0)

#%% plotly graph object -- better

import plotly.graph_objects as go

fig1 = go.Figure(
         data = [go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
         layout = go.Layout(
               go.Layout(title = go.layout.Title(text="figure by graph object"))     
            )
      )
fig1

#%%

fig2 = go.Figure(
         data = [go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
         layout_title_text = "figure by graph object"     
      )
fig2

#%% from predefined dictionary

fig01 = go.Figure(fig0)
fig01

#%%
fig1.to_json()
fig1.layout.template = None   # to slim down the output  #!!!
fig1.to_json()
fig1.to_dict()

#%%
#%% Creating Figures

#%% Plotly Express
import plotly.express as px

iris = px.data.iris()
fig3 = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 title="A Plotly Express Figure")
fig3
fig3.to_dict()

#%% Graph Objects Figure Constructor
import plotly.graph_objects as go

fig4 = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Figure Specified By A Graph Object"))
)

fig4.show()

#%%
# ???
fig5 = go.Figure( go.Scatter(
            mode='markers',
            x=iris["sepal_width"], 
            y=iris["sepal_length"], 
            #marker={'color': iris["species"], 'symbol': 'circle'},
          ),
          layout_title_text="..."
       )
fig5

#%% Figure Factories

import numpy as np
import plotly.figure_factory as ff

x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig6 = ff.create_quiver(x1, y1, u1, v1)

fig6.show()

#%% Make Subplots

from plotly.subplots import make_subplots

fig7 = make_subplots(rows=1, cols=2)
fig7.add_trace(go.Scatter(y=[4,2,1], mode="lines"), row=1, col=1)
fig7.add_trace(go.Bar(y=[2,1,3]), row=1, col=2)
fig7

#%%  
#%%  Updating Figures

#%% Adding Traces
fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig

fig.add_trace(go.Scatter(y=[2,1,3]))
fig.add_trace(go.Scatter(y=[3,1,2], x=[2,3,4], mode='markers'))

#%%
fig3
fig3.add_trace(go.Scatter(x=[2, 4], y=[4, 8], mode="lines", 
                          line=go.scatter.Line(color="gray"),
                          showlegend=False
              ))

#%% Adding Traces To Subplots
# as already shown

#%% Plotly Express using the `facet_row` and or `facet_col`
fig8 = px.scatter(iris, x="sepal_width", y="sepal_length", 
                  color="species", facet_col="species",
                  title="Adding Traces To Subplots Witin A Plotly Express Figure")
fig8

reference_line = go.Scatter(x=[2, 4], y=[4, 8], 
                            mode="lines", 
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)


fig8.add_trace(reference_line)
fig8.add_trace(reference_line, col=2)  #! ValueError: Received col parameter but not row.
                                       # row and col must be specified together
fig8.add_trace(reference_line, row=1, col=2)  
fig8.add_trace(reference_line, row=1, col=3)  

#%% Add Trace Convenience Methods
"""
As an alternative to the  add_trace()  method, graph object figures have a family 
of methods of the form  add_{trace}  (where {trace} is the name of a trace type) 
for constructing and adding traces of each trace type.
eg.  add_scatter(),  add_bar()
"""
fig9 = make_subplots(1, 2)
fig9
fig9.add_scatter(y=[4, 2, 1])
fig9.add_bar(y=[2,3,1], row=1, col=2)

fig9.add_bar(y=[2,1,3])
fig9.add_scatter(y=[1.5]*3, row=1, col=2, mode="lines")

#%% Magic Underscore Notation
"""
For example, specifying the figure title in the figure constructor without magic 
underscore notation requires setting the layout argument to 
dict(title=dict(text="A Chart")).

Similarly, setting the line color of a scatter trace requires setting 
the marker property to  dict(color="crimson").
"""

fig  = go.Figure(
          data=[go.Scatter(y=[1, 3, 2], 
                           line=dict(color="crimson"))],
          layout=dict(title=dict(text="A Graph Object Figure"))
       )
fig

#%%
fig = go.Figure(
         data = [go.Scatter(y=[1, 3, 2], line_color="crimson")],
         layout_title_text = "Graph Object Figure With Magic Underscore Notation"
      )
fig

#%% Updating Figure Layouts
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_layout(title_text="Using update_layout() With Graph Object Figures",
                  title_font_size=8)
fig

#%% Note that the following update_layout() operations are equivalent:

fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font_size=30)

fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font=dict(size=30))


fig.update_layout(title=dict(text="update_layout() Syntax Example"),
                             font=dict(size=30))

fig.update_layout({"title": {"text": "update_layout() Syntax Example",
                             "font": {"size": 30}}})

fig.update_layout(title=go.layout.Title(text="update_layout() Syntax Example",
                                        font=go.layout.title.Font(size=30)))

#%% Updating Traces



