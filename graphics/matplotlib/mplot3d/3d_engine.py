#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: Custom 3D engine in Matplotlib
sources:
    - title: Custom 3D engine in Matplotlib
      link: https://matplotlib.org/matplotblog/posts/custom-3d-engine/
file:
    name: 3d_engine.py
    date: 2022-06-12
    author:
        email: akasp@int.pl
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

#%%
V, F = [], []       # vertices, faces
with open("bunny.obj") as f:
   for line in f.readlines():
       if line.startswith('#'):
           continue
       values = line.split()
       if not values:
           continue
       if values[0] == 'v':
           V.append([float(x) for x in values[1:4]])
       elif values[0] == 'f':
           F.append([int(x) for x in values[1:4]])
V = np.array(V)
F = np.array(F) - 1     # to index from 0 like python

#%%
V.shape     # (2503, 3)
V
F.shape     # (4968, 3)
F
#%% normalisation
V = (V - (V.max(0) + V.min(0))/2) / max(V.max(0) - V.min(0))

#%% see the points
ax = plt.figure().add_subplot(projection="3d")
ax.scatter(V[:,2], V[:,0], V[:,1], marker=".")   # !!!  x,y,z == 2,0,1

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#%%
T = V[F]
T.shape     # (4968, 3, 3)
T = T[...,:2]
T.shape     # (4968, 3, 2)

fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0,0,1,1], xlim=[-1,+1], ylim=[-1,+1],
                  aspect=1, frameon=False)
collection = PolyCollection(T, closed=True, linewidth=0.1,
                            facecolor="None", edgecolor="black")
ax.add_collection(collection)
plt.show()

#%%
"""
... define a viewing volume, that is,
the volume in the 3D space we want to render on the screen.
To do that, we need to consider 6 clipping planes
 (left, right, top, bottom, far, near)
that enclose the viewing volume (frustum) relatively to the camera
"""
def frustum(left, right, bottom, top, znear, zfar):
    M = np.zeros((4, 4), dtype=np.float32)
    M[0, 0] = +2.0 * znear / (right - left)
    M[1, 1] = +2.0 * znear / (top - bottom)
    M[2, 2] = -(zfar + znear) / (zfar - znear)
    M[0, 2] = (right + left) / (right - left)
    M[2, 1] = (top + bottom) / (top - bottom)
    M[2, 3] = -2.0 * znear * zfar / (zfar - znear)
    M[3, 2] = -1.0
    return M

def perspective(fovy, aspect, znear, zfar):
    h = np.tan(0.5*np.radians(fovy)) * znear
    w = h * aspect
    return frustum(-w, w, -h, h, znear, zfar)

# homogeneous coordinates
V = np.c_[V, np.ones(len(V))] @ perspective(25,1,1,100).T

# re-normalize the homogeneous coordinates
V /= V[:,3].reshape(-1,1)

#%%
"""bunny-2.py
"""
T = V[F][...,:2]

# Rendering
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0,0,1,1], xlim=[-1,+1], ylim=[-1,+1], aspect=1, frameon=False)
collection = PolyCollection(T, closed=True, linewidth=0.1,
                            facecolor="None", edgecolor="black")
ax.add_collection(collection)
plt.show()

# plt.savefig("bunny-2.png", dpi=300)

#%%
"""
To have a proper rendering,
we need to move the bunny away from the camera
or move the camera away from the bunny
bunny-3.py
"""
...

""" Model, view, projection (MVP)
bunny-4.py
"""
...

""" Let's now play a bit with the aperture
such that you can see the difference.
Note that we also have to adapt the distance to the camera in order for the bunnies
to have the same apparent size
bunny-5.py
"""
...
"""Depth sorting
Let's try now to fill the triangles
bunny-6.py
...
As you can see, the result is “interesting” and totally wrong.
The problem is that the PolyCollection will draw the triangles in the order they are given
while we would like to have them from back to front.
...
bunny-7.py
"""
#%%
""" Let's add some colors using the depth buffer.
We'll color each triangle according to its depth.
The beauty of the PolyCollection object is that
you can specify the color of each of the triangle using a NumPy array,
"""
zmin, zmax = Z.min(), Z.max()
Z = (Z-zmin)/(zmax-zmin)
C = plt.get_cmap("magma")(Z)
I = np.argsort(Z)
T, C = T[I,:], C[I,:]
"""
bunny-8.py
"""
