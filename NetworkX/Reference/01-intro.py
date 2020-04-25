#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
subtitle:
version: 1.0
type: tutorial
keywords: [, NetworkX]   # there are always some keywords!
description: |
    Description of what is in the file.
    Detailed but do not make lectures here!
remarks:
    - 
todo:
    - problem 1
sources:
    - title: 
      chapter: 
      pages: 
      link: https://networkx.github.io/documentation/stable/reference/introduction.html
      date: 
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not onnly copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ~/Works/Python/NetworkX/01-Intro/
    file: 01-intro.py
    date: 2020-04-14
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
G = nx.Graph()
G
dir(G)

#%%
G.add_edge(1, 2)  # default edge data=1
G.add_edge(2, 3, weight=0.9)  # specify edge data

G
G.edges
G.nodes

G[0 ]  #! KeyError: 0
G[1]   # AtlasView({2: {}})   -- neighbour of 1
G[2]   # AtlasView({1: {}, 3: {'weight': 0.9}})   -- neighbours of 2

G[1][2]
G[2][1]
G[2][3]  # {'weight': 0.9}

G.edges[1, 2]   # {}
G.edges[2, 3]   # {'weight': 0.9}
G.edges[2, 3]['weight']
G.edges[2, 3]['color']  # KeyError: 'color'

G.add_edge(2, 3, color='red')
G.edges[2, 3]['color']
G[2][3]  # {'weight': 0.9, 'color': 'red'}

#%%
import math
G.add_edge('y', 'x', function=math.cos)
G.add_node(math.cos)  # any hashable can be a node

#%%
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)

elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)

for e in list(G.edges): print(e)
for e, v in G.edges.items():   print("{} : {}".format(e, v))

for v in G.edges.values():   print(v)

for c in G.edges.data('color'): print(c)
for c in G.edges.data('weight'): print(c)

G.edges.data

#%% adjacency structure -- dict-of-dicts-of-dicts
G.adj
for node, neighbr in G.adj.items(): print("{} : {}".format(node, neighbr))

#%% simpler example
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
print(G.adj)

#%%
"""
Graphs provide two interfaces to the edge data attributes: 
adjacency and edges. 
So G[u][v]['width'] is the same as G.edges[u, v]['width'].
"""

G = nx.Graph()
G.add_edge(1, 2, color='red', weight=0.84, size=300)

print(G[1][2]['size'])
print(G.edges[1, 2]['color'])


#%%
#%%
G = nx.Graph()
e = [('a', 'b', 0.3), ('b', 'c', 0.9), ('a', 'c', 0.5), ('c', 'd', 1.2)]
G.add_weighted_edges_from(e)

print(nx.dijkstra_path(G, 'a', 'd'))

#%% Drawing
#%%
G = nx.cubical_graph()

plt.subplot(121)
nx.draw(G)   # default spring_layout

plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')


#%% Data

