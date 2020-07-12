#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Geopandas
subtitle: Reading and Writing Files
version: 1.0
type: tutorial/examples
keywords: [GeoSeries, GeoDataFrame]
description: |
    Introduction to GeoPanas Reading and Writing Files
sources:
    - title: Reading and Writing Files
      link: https://geopandas.org/io.html
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
help(gpd.read_file)

df = gpd.read_file("../data/nybb/nybb.shp")
df.plot()
df.head()

# pointig only to the folder
df = gpd.read_file("../data/nybb/")
df.head()
#%%
df.geometry
df.geometry.name

#%%
import fiona
help(fiona.open)

#%%
## Reading subsets of the data

#%% geometry filter      version 0.7.0.

gdf_mask = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
gdf_mask
gdf_mask.plot()
gdf_mask.geometry.name
gdf_mask.columns
gdf_mask.continent
gdf_mask.continent.unique()
gdf_mask.continent.value_counts()

#%%
gdfa = gpd.read_file(gpd.datasets.get_path("naturalearth_cities"),
                     mask=gdf_mask[gdf_mask.continent=='Africa'])
gdfa.plot()
#! not filtered - whole world! :(

#%% bounding box filter
bbox = (1031051.7879884212, 224272.49231459625,    # x_min, y_min
        1047224.3104931959, 244317.30894023244 )   # x_max, y_max

gdfny = gpd.read_file(gpd.datasets.get_path("nybb"),
                      bbox=bbox)
gdfny.plot()
gdfny.columns
gdfny.BoroName

#%% row filter        version 0.7.0.
gdfw = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"),
                     rows=10)
gdfw.plot()
#! not filtered - whole world! :(

#%%
gdfw = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"),
                     rows=slice(10, 20))
gdfw.plot()
#! not filtered - whole world! :(

gdfw.shape

"""
???
"""

#%% Field/Column Filters
# Requires Fiona 1.8+

gdf = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
gdf.columns    # 'pop_est', 'continent', 'name', 'iso_a3', 'gdp_md_est', 'geometry'

gdf = gpd.read_file(
    gpd.datasets.get_path("naturalearth_lowres"),
    ignore_fields=["iso_a3", "gdp_md_est"],
)
gdf.columns    # 'pop_est', 'continent', 'name', 'geometry'


#%% Skip loading geometry from the file:
# Requires Fiona 1.8+

pdf = gpd.read_file(
    gpd.datasets.get_path("naturalearth_lowres"),
    ignore_geometry=True,
)
#! KeyError: 'geometry'


#%%
#%% Writing Spatial Data
# https://geopandas.org/io.html#writing-spatial-data
# GeoDataFrames can be exported to many different standard formats using the 
 geopandas.GeoDataFrame.to_file() # method. 
# For a full list of supported formats, type 

import fiona; fiona.supported_drivers

# In addition, GeoDataFrames can be uploaded to PostGIS database 
# (starting with GeoPandas 0.8) by using the 
 geopandas.GeoDataFrame.to_postgis()  # method.

""" Note
GeoDataFrame can contain more field types than supported by most of the file formats. 
For example tuples or lists can be easily stored in the GeoDataFrame, 
but saving them to e.g. GeoPackage or Shapefile will raise a ValueError. 
Before saving to a file, they need to be converted to a format supported by 
a selected driver.
"""
#%% Writing to Shapefile:
countries_gdf.to_file("countries.shp")

#%% Writing to GeoJSON:
countries_gdf.to_file("countries.geojson", driver='GeoJSON')

#%% Writing to GeoPackage:
countries_gdf.to_file("package.gpkg", layer='countries', driver="GPKG")
cities_gdf.to_file("package.gpkg", layer='cities', driver="GPKG")

#%% Writing to PostGIS:
from sqlalchemy import create_engine
db_connection_url = "postgres://myusername:mypassword@myhost:5432/mydatabase";
engine = create_engine(db_connection_url)
countries_gdf.to_postgis(name="countries_table", con=engine)



