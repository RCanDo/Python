#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:13:49 2025

https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html

@author: arek
"""
import numpy as np

random.Generator.multinomial(n, pvals, size=None)
"""
Draw samples from a multinomial distribution.
The multinomial distribution is a multivariate generalization of the binomial distribution.
Take an experiment with one of p possible outcomes.
An example of such an experiment is throwing a dice, where the outcome can be 1 through 6.
Each sample drawn from the distribution represents n such experiments.
Its values, X_i = [X_0, X_1, ..., X_p], represent the number of times the outcome was i.

Parameters
----------
n: int or array-like of ints
    Number of experiments.
pvals: array-like of floats
    Probabilities of each of the p different outcomes with shape (k0, k1, ..., kn, p).
    Each element pvals[i,j,...,:] must sum to 1
    (however, the last element is always assumed to account for the remaining probability,
     as long as sum(pvals[..., :-1], axis=-1) <= 1.0.
     Must have at least 1 dimension where pvals.shape[-1] > 0.
size: int or tuple of ints, optional
    Output shape.
    If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn each with p elements.
    Default is None where the output size is determined by the broadcast shape of n and all by the final dimension of pvals, which is denoted as b=(b0, b1, ..., bq). If size is not None, then it must be compatible with the broadcast shape b. Specifically, size must have q or more elements and size[-(q-j):] must equal bj.

Returns
-------
out: ndarray
    The drawn samples, of shape size, if provided.
    When size is provided, the output shape is size + (p,)
    If not specified, the shape is determined by the broadcast shape of n and pvals, (b0, b1, ..., bq) augmented with the dimension of the multinomial, p, so that that output shape is (b0, b1, ..., bq, p).

    Each entry out[i,j,...,:] is a p-dimensional value drawn from the distribution.
"""
# %%  Examples
# Throw a dice 20 times:
rng = np.random.default_rng()
rng.multinomial(20, [1/6.]*6, size=1)
# or just
np.random.multinomial(20, [1/6.]*6, size=1)
# array([[4, 1, 7, 5, 2, 1]])    # It landed 4 times on 1, once on 2, etc.

# Now, throw the dice 20 times, and 20 times again:
rng.multinomial(20, [1/6.]*6, size=2)
# array([[3, 4, 3, 3, 4, 3],
#        [2, 4, 3, 4, 0, 7]])  # random
# For the first run, we threw 3 times 1, 4 times 2, etc.
# For the second, we threw 2 times 1, 4 times 2, etc.

# Now, do one experiment throwing the dice 10 time, and 10 times again,
# and another throwing the dice 20 times, and 20 times again:

rng.multinomial([[10], [20]], [1/6.]*6, size=(2, 2))
# array([[[2, 4, 0, 1, 2, 1],
#         [1, 3, 0, 3, 1, 2]],
#        [[1, 4, 4, 4, 4, 3],
#         [3, 3, 2, 5, 5, 2]]])  # random
# The first array shows the outcomes of throwing the dice 10 times,
# and the second shows the outcomes from throwing the dice 20 times.

# A loaded die is more likely to land on number 6:
rng.multinomial(100, [1/7.]*5 + [2/7.])
# array([11, 16, 14, 17, 16, 26])  # random

# Simulate 10 throws of a 4-sided die and 20 throws of a 6-sided die
rng.multinomial([10, 20],[[1/4]*4 + [0]*2, [1/6]*6])
# array([[2, 1, 4, 3, 0, 0],
#        [3, 3, 3, 6, 1, 4]], dtype=int64)  # random

# Generate categorical random variates from two categories where the first has 3 outcomes and the second has 2.
rng.multinomial(1, [[.1, .5, .4 ], [.3, .7, .0]])
# array([[0, 0, 1],
#        [0, 1, 0]], dtype=int64)  # random

argmax(axis=-1) # is then used to return the categories:

pvals = [[.1, .5, .4 ], [.3, .7, .0]]
rvs = rng.multinomial(1, pvals, size=(4,2))
rvs
# array([[[0, 1, 0],
#         [0, 1, 0]],

#        [[0, 0, 1],
#         [0, 1, 0]],

#        [[0, 1, 0],
#         [1, 0, 0]],

#        [[0, 1, 0],
#         [1, 0, 0]]])

rvs.argmax(axis=-1)
# array([[1, 1],
#        [2, 1],
#        [1, 0],
#        [1, 0]])

# The same output dimension can be produced using broadcasting.
rvs = rng.multinomial([[1]] * 4, pvals)
rvs
# array([[[0, 1, 0],
#         [0, 1, 0]],

#        [[0, 0, 1],
#         [1, 0, 0]],

#        [[0, 0, 1],
#         [0, 1, 0]],

#        [[0, 0, 1],
#         [1, 0, 0]]])
rvs.argmax(axis=-1)
# array([[1, 1],
#        [2, 0],
#        [2, 1],
#        [2, 0]])

# The probability inputs should be normalized.
# As an implementation detail, the value of the last entry is ignored
# and assumed to take up any leftover probability mass, but this should not be relied on.
# A biased coin which has twice as much weight on one side as on the other should be sampled like so:

rng.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
# array([33, 67])

# not like:
rng.multinomial(100, [1.0, 2.0])  # WRONG
# Traceback (most recent call last):
# ValueError: pvals < 0, pvals > 1 or pvals contains NaNs

# %%
cats = list('abcdefghijklmnopqrstuvwxyz')
p = (np.arange(len(cats)) + 1)[::-1]
p = p / sum(p)
np.random.multinomial(100, p, size=1)

# sample of 100 observations from MN(p)
idx = np.random.multinomial(1, p, size=100).argmax(axis=-1)
idx
[cats[i] for i in idx]
np.array(cats)[idx]

# %%   simulation of large number of levels (categories)
N = 1000

def fac_sample_0(N, cats, p=None, nans=77):
    cats = np.array(cats)
    if p is None:
        p = ((np.arange(len(cats)) + 1) ** 1.1)[::-1]
        p = p / sum(p)
    # sample of N observations from MN(p)
    idx = np.random.multinomial(1, p, size=N).argmax(axis=-1)
    res = np.array(cats)[idx].astype('object')
    if nans > 0:
        res[np.random.choice(range(N), nans, False)] = None
    return res

cats_v = list('abcdefghijklmno')
cats_c = list('pqrstuvwxyz')

var = fac_sample_0(N, cats_v)
var
cov = fac_sample_0(N, cats_c, nans=66)
cov

df = pd.DataFrame({'a': var, 'b': cov})