#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: NetworkX
subtitle:
version: 1.0
type: tutorial
keywords: [, NetworkX]   # there are always some keywords!
description: |
    Tutorial interactive file
remarks:    
    - 
todo:
    - problem 1
sources:   # there may be more sources
    - title:
      chapter:
      pages:
      link: https://networkx.github.io/documentation/stable/tutorial.html
      date:
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ~/Works/Python/NetworkX/
    date: 2020-04-16
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - arek@staart.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import networkx as nx

#%%

