#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Geopandas
subtitle: Data Structures
version: 1.0
type: tutorial/examples
keywords: [GeoSeries, GeoDataFrame]
description: |
    Introduction to GeoPanas data structures
sources:
    - title: Data Structures
      link: https://geopandas.org/data_structures.html
      date: 2020-07-07
      usage: |
          source of examples
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    path: ~/Works/Python/geospatial/geopandas/
    date: 2020-07-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% 
cd ~/Works/Python/geospatial/geopandas/

#%% 

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#%%

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.precision', 3)

# %%
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world.head()
world.columns
world.geometry.name   # 'geometry'

world['name']
world.loc[world['name'] == 'Poland', :]
world.loc[world['name'] == 'Poland', 'geometry']


#%%
wg = world.geometry
wg
wg[0]
wg[1]
wg[3]
list(wg[3])
wg[3][0]
dir(wg[3][0])
wg[3][0].length
len(wg[3][0])   # TypeError: object of type 'Polygon' has no len()


#%%
world.plot()

#%% rename geometry column for sth less generic

world = world.rename(columns={'geometry': 'states'}).set_geometry('states')
# simpler
world = world.rename_geometry('states')
world.geometry.name
world.columns

world.plot()
world.plot(column='pop_est', cmap='plasma')

#%%
world['log_pop'] = np.log(world['pop_est'])
world.plot(column='log_pop', cmap='plasma')

#%%
world['centroids'] = world.centroid
world = world.set_geometry('centroids')
world.plot()
world.plot(column='log_pop',cmap='plasma')
world.plot(markersize='log_pop')
world.plot(markersize='pop_est')


#%%