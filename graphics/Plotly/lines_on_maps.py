#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Lines on Maps in Python
subtitle:
version: 1.0
type: tutorial/examples
keywords: [plotly, plotly.express]
description: |
remarks:
todo:
sources:
    - title: Lines on Maps in Python
      link: https://plotly.com/python/lines-on-maps/
      date: 2020-07-10
      authors:
          - nick: plotly
      usage: |
          not only copy
    - title: Map Trace Types and Subplots
      link: https://plotly.com/python/figure-structure/#map-trace-types-and-subplots
      usage: reference
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

"""
Base Map Configuration
Plotly figures made with px.scatter_geo, px.line_geo or px.choropleth functions 
or containing go.Choropleth or go.Scattergeo graph objects 
have a go.layout.Geo object which can be used to control the appearance 
of the base map onto which data is plotted.
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
pio.renderers

#%%
df = px.data.gapminder().query("year == 2007")
df.head()

#%%
fig = px.line_geo(df, locations="iso_alpha", color="continent", 
                  projection="orthographic")
fig.show()
fig.show(renderer = 'firefox')

#%%
#%%
import plotly.graph_objects as go

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()

df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()

#%%
fig = go.Figure()

fig.add_trace( go.Scattergeo(
    locationmode = 'USA-states',  #?
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(size = 2, 
                  color = 'rgb(255, 0, 0)',
                  line = dict(width = 3, color='rgba(70, 70, 70, 0)')
                 )
        
    ) )

for i in range(len(df_flight_paths)):
    fig.add_trace( go.Scattergeo(
        locationmode = 'USA-states',
        lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
        lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
        mode = 'lines',
        line = dict(width = 1, color = 'red'),
        opacity = df_flight_paths['cnt'][i] / df_flight_paths['cnt'].max()
    ) )
    
fig.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = dict(
            scope = 'north america',
            projection_type = 'azimuthal equal area',
            showland = True,
            landcolor = 'rgb(240, 240, 240)',
            countrycolor = 'rgb(200, 200, 200)'
          )
    )
    
fig.show(renderer = 'firefox')

#%% Performance improvement: put many lines in the same trace
"""
For very large amounts (>1000) of lines, performance may become critcal. 
If you can relinquish setting individual line styles (e.g. opacity), 
you can put multiple paths into one trace. 
This makes the map render faster and reduces the script execution time and memory consumption.

Use `None` between path coordinates to create a break in the otherwise connected paths.
"""

fig2 = go.Figure()

fig2.add_trace( go.Scattergeo(
    #locationmode = 'USA-states',
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(size = 2,
                  color = 'rgb(255, 0, 0)',
                  line = dict(width = 3, color = 'rgba(70, 70, 70, 0)')
                 )
    ) )

lons = np.empty(3 * len(df_flight_paths))
lons[::3] = df_flight_paths['start_lon']
lons[1::3] = df_flight_paths['end_lon']
lons[2::3] = None

lats = np.empty(3 * len(df_flight_paths))
lats[::3] = df_flight_paths['start_lat']
lats[1::3] = df_flight_paths['end_lat']
lats[2::3] = None

fig2.add_trace( go.Scattergeo(
        #locationmode = 'USA-states',
        lon = lons,
        lat = lats,
        mode = 'lines',
        line = dict(width=1, color='red'),
        opacity = .5
    ) )

fig2.update_layout(
        title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
        showlegend = False,
        geo = go.layout.Geo(
                scope = 'north america',
                projection_type = 'azimuthal equal area',   #!!!
                showland = True,
                landcolor = 'rgb(240, 240, 240)',
                countrycolor = 'rgb(200, 200, 200)'
              ),
        height = 700
    )

fig2.show(renderer = 'firefox')

#%% London to NYC Great Circle

fig3 = go.Figure( data = go.Scattergeo(
           lat = [40.7127, 51.5072],
           lon = [-74.0059, 0.1275],
           mode = 'lines',
           line = dict(width = 2, color = 'blue'),
       ) )

fig3.update_layout(
        title_text = 'London to NYC Great Circle',
        showlegend = False,
        geo = dict(resolution = 50,
                   showland = True,
                   showlakes = True,
                   landcolor = 'rgb(200, 200, 200)',
                   countrycolor = 'rgb(200, 200, 200)',
                   lakecolor = 'rgb(100, 100, 230)',
                   projection_type = "equirectangular",     #!!!
                   coastlinewidth = 2,
                   lataxis = dict( range = [20, 60],
                                   showgrid = True,
                                   dtick = 10
                                 ),
                   lonaxis = dict( range = [-100,20],
                                   showgrid = True,
                                   dtick = 20
                                 )
                  )
    )

fig3.show(renderer = 'firefox')

#%% Contour lines on globe

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/globe_contours.csv')
df.head()
# separate line in each row (5 lies )


scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]
n_colors = len(scl)

fig4 = go.Figure()

for i, (lat, lon) in enumerate(zip(df.columns[::2], df.columns[1::2])):
    # print(i, lat, lon)
    fig4.add_trace( go.Scattergeo(
        lon = df[lon],
        lat = df[lat],
        mode = 'lines',
        line = dict(width = 2, color = scl[i % n_colors])
    ) )

fig4.update_layout(
     title_text = 'Contour lines over globe<br>(Click and drag to rotate)',
     showlegend = False,
     geo = dict(showland = True,
                showcountries = True,
                showocean = True,
                countrywidth = 1,
                landcolor = 'rgb(230, 145, 56)',
                lakecolor = 'rgb(0, 255, 255)',
                oceancolor = 'rgb(0, 100, 255)',
                projection = dict(type = 'orthographic',     #!!!
                                  rotation = dict(lon=-100, lat=40, roll=0)
                                 ),
                lonaxis = dict(showgrid = True,
                               gridcolor = 'rgb(100, 100, 100)',
                               gridwidth = .5),
                lataxis = dict(showgrid = True, 
                               gridcolor = 'rgb(100, 100, 100)',
                               gridwidth = .5)
               ),
      #margin={"r":1,"t":1,"l":1,"b":1}  # does it work???
    )

fig4.show(renderer='firefox')

#%%