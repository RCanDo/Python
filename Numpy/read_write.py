#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Reading/writing from/to text file
version: 1.0
type: tutorial
keywords: [array, numpy, read, write, file, text]
sources:
    - title: Python Numpy Array Tutorial
      chapter:
      link: https://www.datacamp.com/community/tutorials/python-numpy-tutorial
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: read_write.py
    path: ~/Works/Python/Numpy/
    date: 2021-09-17
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%% from text
# This is your data in the text file
# Value1  Value2  Value3
# 0.2536  0.1008  0.3857
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  0.5929
# 0.1781  0.3049  0.8928
# 0.6253  0.3486  0.8791

# Import your data
x, y, z = np.loadtxt('data.txt', skiprows=1, unpack=True,
                     delimiter=None,    # default
                     dtype='float64'   # defult?
                     )
"""
you skip the first row,
and you return the columns as separate arrays with  `unpack=TRUE`.
This means that the values in column Value1 will be put in x, and so on.
"""
x
y
z
#%%
# Your data in the text file
# Value1  Value2  Value3
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  MISSING
# 0.1781  0.3049  0.8928
# MISSING 0.5801  0.2038
# 0.5993  0.4357  0.7410

my_array2 = np.genfromtxt('data2.txt', skip_header=1,
                          missing_values='MISSING', filling_values=-999)
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt

"""
loadtxt(), only works when each row in the text file has the same number of values;
So when you want to handle missing values easily,
you’ll typically find it easier to use genfromtxt().

there is really a lot more things that you can specify in your import,
using genfromtxt(), such as the
- maximum number of rows to read or
- the option to automatically strip white spaces from variables.
"""
#%%
x = np.arange(0.0, 5.0, 1.0)
np.savetxt('test.out', x, delimiter=',')
ls

y = np.loadtxt('test.out')
y
y == x
y is x  # False
np.array_equal(x, y)

"""
save() 	    Save an array to a _binary_ file in NumPy .npy format
savez() 	Save several arrays into an _uncompressed_ .npz archive
savez_compressed() 	Save several arrays into a _compressed_ .npz archive
"""

#%%