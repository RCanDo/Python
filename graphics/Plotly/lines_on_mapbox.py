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

import plotly.io as pio
pio.renderers