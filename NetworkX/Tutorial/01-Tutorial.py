#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: NetworkX Tutorial
subtitle:
version: 1.0
type: tutorial
keywords: [, NetworkX]   # there are always some keywords!
description: |
    Tutorial interactive file
remarks:    
todo:
sources:   # there may be more sources
    - title: NetworkX Tutorial
      link: https://networkx.github.io/documentation/stable/tutorial.html
      date:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-Tutorial.py
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

import pprint

from rcando.ak.graphs import plot_graph   # my function

#%%
G = nx.Graph()
G
G.nodes
G.edges

#%% Nodes

G.add_node(1)
G.add_nodes_from([2, 3])
plot_graph(G)

H = nx.path_graph(10)
H.nodes
H.edges
plot_graph(H)

G.add_nodes_from(H)
"""
Note that G now contains the nodes of H as nodes of G. In contrast, 
you could use the graph H as a node in G.
"""
G.add_node(H)   #! graph as a node
 
"""!!!
Note that adding a node to G.nodes does not add it to the graph, 
use G.add_node() to add new nodes. 
Similarly for edges.
"""

#%% Edges
G.add_edge(1, 2)

e = (2, 3)
G.add_edge(*e)
plot_graph(G)

# edge with attributes
eat = (3, 4, {'weight': 2.71, 'color': 'blue'})
G.add_edge(*eat) #! TypeError: add_edge() takes 3 positional arguments but 4 were given
G.add_edge(eat)  #! TypeError: add_edge() missing 1 required positional argument: 'v_of_edge'

G.add_edges_from([eat])  # OK!

#%%
G.clear()
G.nodes  # empty
G.edges  # empty

#%% (1)
G.add_edges_from([(1, 2), (2, 3)])
G.nodes   # 1, 2, 3   OK!
G.add_node(1)
G.add_edge(1, 2)
G.add_node('spam')
#!
G.add_nodes_from('spam')
G.add_edge(3, 'm')

G.number_of_edges()
G.number_of_nodes()
#%%
G.nodes
list(G.nodes)

G.edges                # list of edges
G.edges([2, 'm'])      # EdgeDataView([(2, 1)])
G.edges([2, 3, 'm'])

#%% Adjacency

G.adj
G.adj[1]  # AtlasView({2: {}})
G[1]      # AtlasView({2: {}})    the same!
G[1][2]   # edge 1-2 as dict of its attrs

G[3]
G[3][2]
G[3]['m']

G.adj([2, 3])  #! TypeError: 'AdjacencyView' object is not callable
list(G.adj)  # just list of all nodes
pprint.pprint(dict(G.adj))
pprint.pprint(G.adj)
G.adj[2]
G.adj[3]

list(G.adj[2])  #  list of keys of node 2,  the same as
dict(G.adj[2]).keys()   # almost... :P

G.degree         # degree of each node
G.degree([2, 3]) # degrees of nodes 2, 3 - dict
G.degree[2]      # degree of node 2 - number

#%% removing
G.nodes
G.edges

#!!! cannot remove what is not in the graph...

G.remove_node(1)
G.remove_node(1)   #! NetworkXError: The node 1 is not in the graph.
G.remove_nodes_from('spam')  # removes all of {s, p, a, m}

G.remove_edge(1, 3)   #! NetworkXError: The edge 1-3 is not in the graph
G.remove_edge(2, 3)

plot_graph(G)

#%%
G.add_edge(1, 2)
G.nodes
G.edges

H = nx.DiGraph(G)
H.edges

edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.DiGraph(edgelist)

plot_graph(H)

#%% Accessing edges and neighbors
# recreate G from (1) 
G = nx.Graph()
G.edges                     # EdgeView of all edges
G.add_edge(1, 3)
G.add_edges_from([(1, 2), (2, 3)])
G[1]                        # AtlasView of adjacency
G[1][3]                     # edge 1-3 as dict of its attrs
G.edges[1, 3]               #  "
G.edges([1, 3])             # EdgeDataView([(1, 2), (1, 3)]) -- edges from 1 and 3
G[1][3]['color'] = 'red'

G.edges[1, 2]['color'] = 'blue'
G.edges[1, 2]

#%%
"""
Fast examination of all (node, adjacency) pairs is achieved using G.adjacency(), 
or G.adj.items(). 
Note that for undirected graphs, 
adjacency iteration sees each edge twice !!!
"""
FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
# 3d item is by default called 'weight' !!!

FG.nodes.data()
FG.edges.data()
FG.edges.data('weight')  # the same as input list


FG.edges    # EdgeView
FG.edges([1, 2])   # EdgeDataView -- edges from 1 and 2
FG.edges[1, 2]     # dict of attrs of edge (1, 2)       (*)   

FG[1]       # AtlasView
FG[1][2]    # dict   the same as (*)

FG.adj      # AdjacencyView dict (from) of dicts (to) of dicts (attrs)
FG.adj[1]   # AtlasView                    dict  (to) of dicts (attrs)
FG.adj[1][2]      # the same as (*)                      dict  (attrs)

list(FG.adj) # list of nodes
pprint.pprint(dict(FG.adj))

#%%
for n, nbrs in FG.adj.items():
    print("{} : {}".format(n, nbrs))

for n, nbrs in FG.adj.items():
    for nbr, attr in nbrs.items():
        print("{}--{} : {}".format(n, nbr, attr))

for n, nbrs in FG.adj.items():
    for nbr, attr in nbrs.items():
        print("{}--{} : {}".format(n, nbr, attr['weight']))

FG.adjacency()  #! iterator
[(n, nbrdict) for n, nbrdict in FG.adjacency()]

for (u, v, wt) in FG.edges.data('weight'):
    print("{} {} {}".format(u, v, wt))


#%%
#%% Adding attributes

G.graph
G.nodes
G.edges
plot_graph(G)

#%%
G = nx.Graph(day='Friday')
G.graph  # {'day': 'Friday'}  -- empty graph with attribute

# how to add attr to existig graph?

#%% Node attributes

G.add_node(1, time='5pm')
G.add_nodes_from([3, 4], time='2pm')
G.nodes   # no attributes visible
G.nodes.data()   # !!!  dict of dicts

G.adj     # no edges
G.edges

G.nodes[1]          # {'time': '5pm'}
G.nodes[1]['time']

#! BUT NOTICE THAT
G[1]    
#! is NOT about node 1 but about all edges coming out of node 1 !!!
# see below

G.nodes.data('time')     # only time   NodeDataView = dict of values
G.nodes.data()  # !!!  dict of dicts

# How to add attribute to the existing node?
G.nodes[1]['room'] = 714
G.nodes[1]
G.nodes.data()

G.node[4]['qq'] = 'ryq!'
G.nodes.data()

G.nodes([1, 3])   #! TypeError: unhashable type: 'list'

#%% Edge Attributes
G.edges
G.add_edge(1, 2, weight=4.7)    
G.edges    # no attributes...


G.adj       # OK!!!
# or
[(n, nbrdict) for n, nbrdict in G.adjacency()]
# or
for n, nbrs in G.adj.items():
    print("{} : {}".format(n, nbrs))
# or
for (u, v, wt) in G.edges.data('weight'):    # only weight
    print("{} {} {}".format(u, v, wt))
# or
for (u, v, wt) in G.edges.data():
    print("{} {} {}".format(u, v, wt))    


G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G[1]
G[1][2]
G.edges[3, 4]['weight'] = 4.2
plot_graph(G)
"""!!!
The special attribute weight should be numeric as it is used by algorithms 
requiring weighted edges.
"""
   
#%%
#%% Directed graphs
"""
The DiGraph class provides additional properties specific to directed edges, e.g., 
"""
DiGraph.out_edges() 
DiGraph.in_degree()
DiGraph.out_degree()
DiGraph.predecessors()
DiGraph.successors() 
"""
etc. To allow algorithms to work with both classes easily, 
the directed versions of  neighbors()  is equivalent to  successors() 
while degree reports the sum of  in_degree  and  out_degree  even though 
that may feel inconsistent at times.
"""
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, .5), (3, 1, .75)])
DG.nodes
plot_graph(DG)

DG.adj
DG.edges.data()
[(n, nbrdict) for n, nbrdict in DG.adjacency()]  # 0 repetitions now as in indirected graph
# ...

DG.in_degree(1, weight='weight')
DG.out_degree(1, weight='weight')
DG.degree(1, weight='weight')

DG.successors(1)          # iterator
list(DG.successors(1))
list(DG.neighbors(1))     #!!! neighbor (AmEng!) not neghbour !!!

"""
Some algorithms work only for directed graphs and others are not well defined 
for directed graphs. 
!!! Indeed the tendency to lump directed and undirected graphs together is dangerous. !!!
If you want to treat a directed graph as undirected for some measurement you should probably
convert it using 
"""
g = DG.to_undirected()
g.adj
[(n, nbrdict) for n, nbrdict in g.adjacency()]   # repetitions now, OK it's UNdirected
g.edges.data()
# or
g = nx.Graph(DG)

#%%
#%% Multigraphs

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, .5), (1, 2, .75), (2, 3, .5)])
plot_graph(MG)   #! ValueError: too many values to unpack (expected 2)

for n, nbrs in MG.adjacency():
    print("{} : {}".format(n, nbrs))

for n, nbrs in MG.adjacency():
    for nbr, edict in nbrs.items():
        print("{} : {} : {}".format(n, nbr, edict))

MG.degree(weight='weight')
dict(MG.degree(weight='weight'))
MG.edges.data()

GG = nx.Graph()
for n, nbrs in MG.adjacency():
    for nbr, edict in nbrs.items():
        minval = min([d['weight'] for d in edict.values()])
        print(minval)
        GG.add_edge(n, nbr, weight=minval)
nx.shortest_path(GG, 1, 3)   # [1, 2, 3]

#%%
#%% Drawing graphs
"""
NetworkX is not primarily a graph drawing package 
but basic drawing with Matplotlib as well as an interface to use 
the open source Graphviz software package are included. 
These are part of the networkx.drawing module and will be imported if possible.
"""
import matplotlib.pyplot as plt

G = nx.petersen_graph()   # see below to "Graph generators ..."
G.edges
G.nodes

plt.figure()
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

#%%
options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3
    }

plt.figure()
plt.subplot(221)
nx.draw_random(G, **options)
plt.subplot(222)
nx.draw_circular(G, **options)
plt.subplot(223)
nx.draw_spectral(G, **options)
plt.subplot(224)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], **options)

#%%
"""
You can find additional options via  draw_networkx()  and layouts via layout. 
You can use multiple shells with  draw_shell().
"""
G = nx.dodecahedral_graph()
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
plt.figure()
nx.draw_shell(G, nlist=shells, with_labels=True, font_color='red', **options)

#%% To save drawings to a file, use, for example

nx.draw(G)
plt.savefig("path.png")
"""
writes to the file `path.png` in the local directory. 
If  Graphviz  and  PyGraphviz  or  pydot,  are available on your system, 
you can also use 
"""
nx_agraph.graphviz_layout(G) # or 
nx_pydot.graphviz_layout(G) 
"""
to get the node positions, or write the graph in dot format for further processing.
"""

from networkx.drawing.nx_pydot import write_dot
pos = nx.nx_agraph.graphviz_layout(G)
nx.draw(G, pos=pos)
write_dot(G, 'file.dot')

"""
See Drawing for additional details.
"""

#%%
def draw(G):
    plt.figure()
    nx.draw(G, with_labels=True, font_color='black',
        node_color='yellow',
        node_size=100,
        width=1)
draw(G)

from rcando.ak.graphs import plot_graph
plot_graph(G)
plot_graph(G, 'circular')

#%%
#%% Graph generators and graph operations

G = nx.Graph([(1, 2), (2, 3), (2, 4), (3, 4), (4, 4)])
G.add_node(5)
G.edges
G.nodes

G1 = nx.Graph([(10, 20), (10, 30), (20, 20)])
G1.add_node(50)
G1.edges
G1.nodes

G2 = nx.Graph([(100, 200), (200, 300), (300, 100)])
G2.add_node(500)
G2.edges
G2.nodes


"""
In addition to constructing graphs node-by-node or edge-by-edge, 
they can also be generated by
"""
## 1. Applying classic graph operations, such as:

nx.subgraph(G, nbunch)      # induced subgraph view of G on nodes in nbunch
G.subgraph([1, 2, 3, 5]).edges

G3 = nx.union(G1,G2)             # graph union
G3.edges

nx.disjoint_union(G1,G2)    # graph union assuming all nodes are different
nx.cartesian_product(G1,G2) # return Cartesian product graph
nx.compose(G1,G2)           # combine graphs identifying nodes common to both
nx.complement(G)            # graph complement
nx.create_empty_copy(G)     # return an empty copy of the same graph class
nx.to_undirected(G)         # return an undirected representation of G
nx.to_directed(G)           # return a directed representation of G

## 2. Using a call to one of the classic small graphs, e.g.,

petersen = nx.petersen_graph()
tutte = nx.tutte_graph()
maze = nx.sedgewick_maze_graph()
tet = nx.tetrahedral_graph()

## 3. Using a (constructive) generator for a classic graph, e.g.,

K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)

## 4. Using a stochastic graph generator, e.g.,

er = nx.erdos_renyi_graph(100, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(100, 5)
red = nx.random_lobster(100, 0.9, 0.9)

## 5. Reading a graph stored in a file using common graph formats, 
##    such as edge lists, adjacency lists, GML, GraphML, pickle, LEDA and others.

nx.write_gml(red, "path.to.file")
mygraph = nx.read_gml("path.to.file")

"""
For details on graph formats see Reading and writing graphs and for graph generator 
functions see Graph generators
"""

#%% Analyzin graphs

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node("spam")
plot_graph(G)

list(nx.connected_components(G))
sorted(d for n, d in G.degree())
nx.clustering(G)

sp = dict(nx.all_pairs_shortest_path(G))
sp
sp[1]

#%%


#%%


