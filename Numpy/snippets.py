#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Numpy snippets
version: 1.0
type: tutorial
keywords: [array, numpy]
sources:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: snippets.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-06
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
pwd
cd E:/ROBOCZY/Python/Numpy/
cd ~/Works/Python/Numpy/
ls

#%%
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#%%
help(np.geomspace)
# geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)
#  Return numbers spaced evenly on a log scale (a geometric progression).
#  This is similar to `logspace`, but with endpoints specified directly.
#! Each output sample is a constant multiple of the previous. !!
np.geomspace(1, 1000, 4)   #
np.geomspace(1, 1000, 4, endpoint=False)   # is ALMOST the same as:
np.geomspace(1, 1000, 5)                   # endpoint (1000) is here!

np.geomspace(1, 81, 3)
np.geomspace(1, 81, 5)
np.geomspace(1, 1024, 11)
# Note that the above may not produce exact integers:  !!!
np.geomspace(1, 1024, 11, dtype=int)   #!!!  SHIT  !!!

# decreasing
np.geomspace(1000, 1, num=4)    # array([1000.,  100.,   10.,    1.])
# negative
np.geomspace(-1000, -1, num=4)  # array([-1000.,  -100.,   -10.,    -1.])
# complex
np.geomspace(1j, 1000j, num=4)  # Straight line  array([0.   +1.j, 0.  +10.j, 0. +100.j, 0.+1000.j])
zz = np.geomspace(-1+0j, 1+0j, num=5)  # Circle
zz
#    array([-1.00000000e+00+1.22464680e-16j, -7.07106781e-01+7.07106781e-01j,
#            6.12323400e-17+1.00000000e+00j,  7.07106781e-01+7.07106781e-01j,
#            1.00000000e+00+0.00000000e+00j])
plt.plot(zz.real, zz.imag)

zzu = np.geomspace(-1+0j, 1+0j, num=22)  # Circle
zzd = np.geomspace(1+0j, -1+0j, num=22)  # Circle
plt.plot(zzu.real, zzu.imag)
plt.plot(zzd.real, zzd.imag)    # tyhe same -- upper semi circle
plt.plot(np.r_[zzd.real, zzd.real], np.r_[zzd.imag, -zzd.imag])
plt.axis('scaled')

# Graphical illustration of ``endpoint`` parameter:
N = 10
y = np.zeros(N)
plt.semilogx(np.geomspace(1, 1000, N, endpoint=True), y + 1, 'o')
plt.semilogx(np.geomspace(1, 1000, N, endpoint=False), y + 2, 'o')
plt.axis([0.5, 2000, 0, 3])
plt.grid(True, color='0.7', linestyle='-', which='both', axis='both')

#%%
help(np.logspace)
# logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
#  Return numbers spaced evenly on a log scale.
#  In linear space, the sequence starts at ``base ** start``
#  (`base` to the power of `start`) and ends with ``base ** stop``

np.logspace(2, 6, num=5)
np.logspace(1, 10, num=10, base=2)
np.logspace(1, 4, num=4, base=3)

np.logspace(2.0, 3.0, num=4)    # array([ 100., 215.443469, 464.15888336, 1000.])
# the same as
y = np.linspace(start=2, stop=3, num=4, endpoint=True)
y
np.power(10, y)

# Graphical illustration of ``endpoint`` parameter:
N = 10
x1 = np.logspace(0.1, 1, N, endpoint=True)
x2 = np.logspace(0.1, 1, N, endpoint=False)
y = np.zeros(N)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])

#%%
#%%
x, y = np.ogrid[:3, :4]
x
y
x + y

np.meshgrid(x, y)

#%%
help(np.where)
# where(condition, [x, y])
#   Return elements chosen from `x` or `y` depending on `condition`.
a = np.arange(10)
a
np.where(a < 5, a, 10*a)

# This can be used on multidimensional arrays too:
np.where([[True, False], [True, True]],
         [[1, 2], [3, 4]],
         [[9, 8], [7, 6]])
#    array([[1, 8],
#           [3, 4]])

# The shapes of x, y, and the condition are broadcast together:
x, y = np.ogrid[:3, :4]

np.where(x < y, x, 10 + y)      # both x and 10+y are broadcast
"""
array([[10,  0,  0,  0],
       [10, 11,  1,  1],
       [10, 11, 12,  2]])
"""

a = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])
np.where(a < 4, a, -1)  # -1 is broadcast
"""
array([[ 0,  1,  2],
       [ 0,  2, -1],
       [ 0,  3, -1]])
"""
#%%
help(pd.Series.where)
# where(self, cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)
#   Replace values where the condition is False.
s = pd.Series(range(5))

s.where(s > 0)
s.mask(s > 0)
s.where(s > 1, 10)
df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])

m = df % 3 == 0
df.where(m, -df)
df.where(m, -df) == np.where(m, df, -df)
df.where(m, -df) == df.mask(~m, -df)

#%%
#%%
np.hstack()

np.vstack()

np.stack()

#%%
np.c_[]
np.c_[[0, 1, 2], [2, 3, 1]]
np.c_[[0, 1, 2], [2, 3]]    #! ValueError: all the input array dimensions for the concatenation axis must match exactly,
                            #  but along dimension 0, the array at index 0 has size 3 and the array at index 1 has size 2

#%%
np.r_[]
np.r_[[0, 1, 2], [2, 3, 1]]
np.r_[[0, 1, 2], [2, 3]]
np.r_[[[0], [1], [2]], [[2], [3], [1]]] #???
np.r_[[[0], [1], [2]], [[2], [3]]]      #???

#%%

from sklearn.model_selection import StratifiedKFold, KFold

X, y = np.ones((50, 1)), np.hstack(([0] * 45, [1] * 5))
X
y

skf = StratifiedKFold(n_splits=3)

for train, test in skf.split(X, y):
    print(train)
    print(y[train])
    print(test)
    print(y[test])

#%%
for train, test in skf.split(X, y):
    print('train -  {}   |   test -  {}'.format(
        np.bincount(y[train]), np.bincount(y[test])))

#%%
kf = KFold(n_splits=3)
for train, test in kf.split(X, y):
    print('train -  {}   |   test -  {}'.format(
        np.bincount(y[train]), np.bincount(y[test])))

#%%
help(np.bincount)

x = np.array([0, 1, 1, 3, 2, 1, 7, 23])
np.bincount(x)

np.bincount(x).size == np.amax(x)+1

#%%
np.amax(x)

help(np.amax)
"""
amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the maximum of an array or maximum along an axis.
"""
#%%