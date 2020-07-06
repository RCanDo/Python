#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
subtitle:
version: 1.0
type:          # possible values: ...
keywords: [kw1, kw2, ..., kwn]   # there are always some keywords!
description: |
    Description of what is in the file.
    Detailed but do not make lectures here!
remarks:    # additional notes worth emphasising
    - eg. work interactively (in Spyder)
    - install PackageX first
    - etc.
todo:
    - problem 1
    - problem 2   # and so on...
sources:   # there may be more sources
    - title: Introduction to Geospatial Data in Python
      link: https://www.datacamp.com/community/tutorials/geospatial-data-python
      date: 2018-10-24
      authors:
          - fullname: Duon Vu
      usage: |
          In this tutorial, you will use geospatial data to plot the path of Hurricane Florence
          from August 30th to September 18th.
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/geospatial/DataCamp/
    date: 2020-07-05
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
cd  "D:/ROBOCZY/Python/geospatial/DataCamp/"


#%%
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import missingno as msn
import seaborn as sbn
import matplotlib.pyplot as plt

import descartes

#%%
pd.options.display.max_colwidth = 80

#%% Getting to know GEOJSON file:
country = gpd.read_file("../data/gz_2010_us_040_00_5m.json")
country.head()
type(country)    # geopandas.geodataframe.GeoDataFrame
type(country.geometry)   # geopandas.geoseries.GeoSeries

#%%
country.columns
country.iloc[0,:].to_dict()

#%%
cg0 = country.geometry[0]
type(cg0)        # shapely.geometry.multipolygon.MultiPolygon

""" Each value in the GeoSeries is a Shapely Object. It can be:
    Point
    Line
    Polygon
    MultiPolygon
https://shapely.readthedocs.io/en/stable/manual.html#geometric-objects
"""

list(cg0)
cg0[0]
cg0[1]
cg0

#%%
country.plot()
country2 = country[country['NAME'].isin(['Alaska', 'Hawaii']) == False]
country2.plot(figsize=(20, 30), color='#777777')

#%%
florence = pd.read_csv('../data/florence.csv')
florence.head()
florence.columns
florence.iloc[0,:].to_dict()
florence.info()
florence.describe()

msn.bar(florence)  #! RuntimeError: adjustable='datalim' is not allowed when both axes are shared

#%% dropping all unused features:
florence = florence.drop(['AdvisoryNumber', 'Forecaster', 'Received'], axis=1)
florence.info()
florence.head()

florence['Long'] = - florence['Long']

#%% Combining Lattitude and Longitude to create hurricane coordinates:
florence['Coordinates'] = florence[['Long', 'Lat']].values.tolist()

# Change the coordinates to a geoPoint
florence['Coordinates'] = florence['Coordinates'].apply(Point)

type(florence)   # pandas.core.frame.DataFrame
type(florence['Coordinates'])  # pandas.core.series.Series

# Convert the count df to geodf
florence = gpd.GeoDataFrame(florence, geometry='Coordinates')
florence.head()

type(florence)   # geopandas.geodataframe.GeoDataFrame
type(florence['Coordinates'])   # geopandas.geoseries.GeoSeries

#%%

florence.plot(figsize=(20, 10))

#%%
fig, ax = plt.subplots(1) #, figsize=(30, 20))
base = country2.plot(ax=ax, color='gray')
florence.plot(ax=base, column='Wind', marker='o', markersize=10, cmap='cool',
              label='Wind speed(mph)')
ax.axis('off')
plt.legend()
ax.set_title("Hurricane Florence in US Map", fontsize=25)
plt.savefig(fname="Hurricane_footage.pdf", bbox_inches='tight')  #! OSError: [Errno 22] Invalid argument: 'Hurricane_footage.pdf'

#%%

