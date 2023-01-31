#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:52:34 2022

@author: arek
"""
#%%
import numpy as np
from typing import Tuple
from collections import Counter, defaultdict

#%%
def parse_obj(file: str, load_class: bool = False) -> Tuple[np.array, list, defaultdict]:
    """
    Arguments:
        file: str
        load_class: bool; do load or not info on edge class?
            if not, all edges will be in one class 0
    Returns:
        vs: 2d np.array
        faces: list of lists of indices of rows from vs
        edges: dict of lists of lists
    Remark:
        1.
        .obj file format is very simple here, consists only of 3 line types:
            v x y z
            f v1 v2 v3
            e v1 v2 c
        where
        v, f, e are literal 'v', 'f' 'e' indicating if the line is about vertex, face or edge;
        x, y, z are real coordinates (floats) of vertex;
        v1, v2, v3 are indices of corresponding vertices
        (where index means position on the list == line nr in a file
        -- notice that list of vertices is the first in the file);
        c is a class (category) number for given edge; this is translated to color when plotting.
        color of each face is taken from its edges by majority voting.
        2.
        we assume format is proper -- no sanity checks
    """
    # Nv = number of vertices
    # Nf = number of faces
    # Nc = number of classes/segments/colors
    # Ne_c = number of edges within class `c`
    vs = []         # Nv x 3  (3 coordinates)  vertices
    faces = []      # Nf x 3  (3 indices of respective vertices)
    edges = defaultdict(list)     # Nc x Ne_c x 2   (2 vertices to define edge)

    with open(file) as f:

        for line in f:
            line = line.strip()
            line_split = line.split()

            if not line_split:
                continue

            elif line_split[0] == 'v':
                vs.append([float(c) for c in line_split[1:]])       # c ~ coordinate: x, y, z

            elif line_split[0] == 'f':
                faces.append([int(i) - 1 for i in line_split[1:]])  # i ~ index of a vertex (position in vs)

            elif line_split[0] == 'e':

                if len(line_split) >= 4 and load_class:            # 4 elements: 'e v0 v1 c'
                    color = int(line_split[-1])     # ~= color / class / segment id
                    edge_vs = [int(i) - 1 for i in line_split[1:3]]    # i ~ index of a vertex
                    edge_vs.sort()      # to improve lookup -- see  get_face_color()
                    edges[color].append(edge_vs)

                else:               # 3 elements: 'e v0 v1', NO additional attributes like color / class / segment
                    color = 0       # only one segment (default color ~= skin color)
                    edge_vs = [int(i) - 1 for i in line_split[1:3]]    # i ~ index of a vertex
                    edge_vs.sort()      # to improve lookup -- see  get_face_color()
                    edges[color].append(edge_vs)

    vs = np.array(vs)   # necessary for spatial transformations

    return vs, faces, edges


#%%
file = 'shrec__2_0.obj'
vs, faces, _ = parse_obj(file)

type(vs)        # np.array
vs.shape        # (752, 3)

type(faces)     # list
type(faces[0])  # list
np.array(faces).shape   # (1500, 3)

vs[faces]       # ok
# BUT
vs[faces[:9]]   #! IndexError: too many indices for array: array is 2-dimensional, but 9 were indexed
vs[np.array(faces[:9])]   #! ok
vs[faces[:]]    # ok
vs[faces[:31]]  #! IndexError: too many indices for array: array is 2-dimensional, but 31 were indexed
vs[np.array(faces[:31])]  # ok

# and then...
vs[faces[:32]]  # ok
vs[faces[:32]].shape  # (32, 3, 3)
# above this is ok
vs[faces[:33]]   # ok
vs[faces[:99]]   # ok

"""
??? !!! ???
"""

#%% simpler example
arr = np. array([[0, 1, 2],
                 [1, 3, 5],
                 [2, 5, 8],
                 [3, 7, 11]])

fcs = [[0, 1, 2], [2, 1, 0]]

arr[fcs]        # array([1, 1, 7])   works like fancy indexing
arr[fcs*2]      #! IndexError: too many indices for array: array is 2-dimensional, but 4 were indexed
arr[fcs*9]      #! IndexError: too many indices for array: array is 2-dimensional, but 18 were indexed
arr[fcs*15]     #! IndexError: too many indices for array: array is 2-dimensional, but 30 were indexed

# and then...
arr[fcs*16]     # ok
arr[fcs*16].shape   # (32, 3, 3)
arr[fcs*17]   # ok
# above this is ok
arr[fcs*99]   # ok


#%%
fcs = [[0, 1, 2], [2, 1, 0]]

nfcs = np.array(fcs)
nfcs
arr[nfcs]
arr[nfcs[:,np.newaxis]]
arr[nfcs[np.newaxis,:]]

#%%
