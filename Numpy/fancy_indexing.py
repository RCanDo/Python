#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Numpy fancy indexing
subtitle:
version: 1.0
type: tutorial
keywords: [fancy indexing, numpy]
description: |
remarks:
todo:
sources:
    - title: Python Data Science Handbook
      chapter: Fancy Indexing
      link: https://jakevdp.github.io/PythonDataScienceHandbook/02.07-fancy-indexing.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "fancy_indexing.py"
    path: "~/Works/Python/Numpy/"
    date: 2019-11-26
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
pwd
cd D:/ROBOCZY/Python/Numpy/
cd ~/Works/Python/Numpy/
ls

#%%
import numpy as np
rand = np.random.RandomState(42)

#%%
"""
Fancy indexing is conceptually simple:
it means passing an array of indices to access multiple array elements at once.
For example, consider the following array:
"""
#%%
x = rand.randint(100, size=10)
x
#%%
[x[3], x[7], x[2]]

x[[3, 7, 2]]

"""
When using fancy indexing, the shape of the result
reflects the shape of the index arrays
rather than the shape of the array being indexed:
"""
idx = np.array([[3, 7], [4, 5]])
x[idx]

#%% Fancy indexing also works in multiple dimensions.
# Consider the following array:
X = np.arange(12).reshape((3, 4))
X

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]
row[:, np.newaxis]
row[:, np.newaxis] * col
X[row[:, np.newaxis], col]

#%% Combined Indexing
"""
For even more powerful operations, fancy indexing can be combined
with the other indexing schemes we've seen:
"""
print(X)

# We can combine fancy and simple indices:
X[2, [2, 0, 1]]
X[2, [2, 0, 1, 1, 0, 2]]
X[1:, [2, 0, 1]]
X[1:, [2, 0, 1, 1, 0, 2]]

# And we can combine fancy indexing with masking:
mask = np.array([1, 0, 1, 0], dtype=bool)
X[:, mask]

X[row[:, np.newaxis], mask]
#! BUT:
X[row, mask]   #! IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (3,) (2,)
#!!!

#%% Example: Selecting Random Points
"""
One common use of fancy indexing is the selection of subsets of rows from a matrix.
For example, we might have an N by D matrix representing N points in D dimensions,
such as the following points drawn from a two-dimensional normal distribution:
"""
mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape
X

# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()   # for plot styling

plt.scatter(X[:, 0], X[:, 1]);

"""
Let's use fancy indexing to select 20 random points.
We'll do this by first choosing 20 random indices with no repeats,
and use these indices to select a portion of the original array:
"""
idx = np.random.choice(X.shape[0], 20, replace=False)
idx

selection = X[idx]
selection.shape

plt.scatter(X[:, 0], X[:, 1], alpha=.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', s=200)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='red', s=20)

#%% Modifying Values with Fancy Indexing
# we have an array of indices and we'd like to set the corresponding items in an array to some value:
x = np.arange(10)
x
i = np.array([2, 1, 8, 4])
x[i] = 99
x

x[i] -= 100
x

# Notice, though, that repeated indices with these operations can cause some potentially unexpected results
x = np.zeros(10)
x[[0, 0]] = [4, 6]
x

i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x

"""
So what if you want the other behavior where the operation is repeated?
For this, you can use the at() method of ufuncs (available since NumPy 1.8),
and do the following:
"""
x = np.zeros(10)
np.add.at(x, i, 1)   # in-place         #!!!
x

"""
Another method that is similar in spirit is the reduceat() method of ufuncs,
which you can read about in the NumPy documentation.
"""
x = np.ones(10)
np.add.reduceat(x, i)   # NOT in-place !
# ???
x


#%% Example: Binning Data & histograms
np.random.seed(42)
x = np.random.randn(100)
x

# compute a histogram by hand
bins = np.linspace(-5, 5, 21)
counts = np.zeros_like(bins)            #!!!
counts

# find the appropriate bin for each x
i = np.searchsorted(bins, x)            #!!!
i

# add 1 to each of these bins
np.add.at(counts, i, 1)                 #!!!
counts

# plot the results
plt.plot(bins, counts, linestyle='steps');


# all of this in one line using matplotlib function
res = plt.hist(x, bins, histtype='step')
res
#!!! matplotlib uses the np.histogram() function

counts, bins = np.histogram(x, bins)
counts
bins

counts, edges, sth = plt.hist(x, bins, histtype='step')
counts
edges
sth

#%% compare both ways

print('NumPy routine:')
%timeit res = np.histogram(x, bins)

print('Custom routine:')
%timeit np.add.at(np.zeros_like(bins), np.searchsorted(bins, x), 1)

"""for such a relatively small dataset custom routine is faster
"""

#%%
np.histogram??

#%%
"""do the same for large dataset
"""
x = np.random.randn(int(1e6))

print('NumPy routine:')
%timeit res = np.histogram(x, bins)

print('Custom routine:')
%timeit np.add.at(np.zeros_like(bins), np.searchsorted(bins, x), 1)

#%%
"""
What this comparison shows is that algorithmic efficiency is almost never
a simple question.
An algorithm efficient for large datasets will not always be the best choice
for small datasets, and vice versa (see Big-O Notation).
But the advantage of coding this algorithm yourself is that
with an understanding of these basic methods,
you could use these building blocks to extend this
to do some very interesting custom behaviors.
The key to efficiently using Python in data-intensive applications
is knowing about general convenience routines like np.histogram
and when they're appropriate, but also knowing how to make use
of lower-level functionality when you need more pointed behavior.
"""







#%%
