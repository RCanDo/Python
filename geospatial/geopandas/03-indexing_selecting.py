#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Geopandas
subtitle: Indexing and Selecting Data
version: 1.0
type: tutorial/examples
keywords: [GeoSeries, GeoDataFrame]
description: |
    Introduction to GeoPanas Indexing and Selecting Data
sources:
    - title: Indexing and Selecting Data
      link: https://geopandas.org/indexing.html
      date: 2020-07-07
      usage: |
          source of examples
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    path: ~/Works/Python/geospatial/geopandas/
    date: 2020-07-08
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
"""
In addition to the standard pandas methods, 
GeoPandas also provides coordinate based indexing with the `cx` indexer, 
which slices using a bounding box. 
Geometries in the GeoSeries or GeoDataFrame that intersect the bounding box 
will be returned.
"""
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

southern_world = world.cx[:, :0]

southern_world.plot(figsize=(10, 3));

equ_world = world.cx[:,-1:1]
equ_world.plot()

my_world = world.cx[:, 50:51]
my_world.plot()

#%%
