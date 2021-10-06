# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:29:23 2021

@author: staar
"""
#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Counting elements in array
version: 1.0
type: tutorial
keywords: [array, numpy, count]
sources:
    - title: How to count the occurrence of certain item in an ndarray?
      chapter:
      link: https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: counting_elements.py
    path: ~/Works/Python/Numpy/
    date: 2021-09-17
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import numpy as np
a = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])
unique, counts = np.unique(a, return_counts=True)
unique
counts
dict(zip(unique, counts))

#%%
np.count_nonzero(a == 0)
np.count_nonzero(a == 1)

#%%
(a == 0).sum()
(a == 1).sum()

#%%
a.tolist().count(0)
a.tolist().count(1)
"""
This code may be one of the fastest solutions for larger arrays.
Getting the result as a list is a bonus, too.
If 'a' is an n-dimensional array, we can just use:
    np.bincount(np.reshape(a, a.size))

This rounds down non-integers. e.g.
    np.bincount([0, 0.5, 1.1])  # -> array([2, 1])
If you have an array with large integers, you will get a long output, e.g.
    len(np.bincount([1000]))   # 1001.
"""

#%%
from collections import Counter
Counter(a)

#%%
a = np.array([0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1])
np.bincount(a)
# array([8, 4])    # count of zeros is at index 0 : 8
                   # count of ones is at index 1 : 4

#%%