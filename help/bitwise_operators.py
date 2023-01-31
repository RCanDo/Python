#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Bitwise Operrators
subtitle:
version: 1.0
type: tutorial
keywords: [bitwise, operators, binary]
description: |
    About dates and time
remarks:
    - etc.
todo:
    - problem 1
sources:
    - link: https://note.nkmk.me/en/python-bit-operation/
    - title: Bitwise Operrators
      link: https://wiki.python.org/moin/BitwiseOperators
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ./help
    date: 2022-11-09
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

# %%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

# %%
import numpy as np
import pandas as pd

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

# other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500
# the same

pd.options.display.width = 120

# %% https://note.nkmk.me/en/python-bit-operation/

bin(7)          # '0b111'
type(bin(7))    # str

0b111           # 7    binary notation
int(0b111)      # 7
int('0b111')    #! ValueError: invalid literal for int() with base 10: '0b111'

hex(99)         # '0x63'
0xff            # 255  hexadecimal notation
bin(0xff)       # '0b11111111'  !
0x11            # 17
bin(0x11)       # '0b10001'

x = -9
print(bin(x))   # -0b1001

bin(x & 0xff)   # 0b11110111
format(x & 0xffff, 'x')     # fff7

# %% Bitwise NOT, invert: ~
# The ~ operator yields the bitwise inversion.
# The bitwise inversion of x is defined as
#     -(x+1)

# If the input value x is regarded as two's complement and all bits are inverted,
# it is equivalent to -(x+1).
# Converting ~x to a string does not result in a string with the bits of the original value inverted.

x = 9
bin(x)   # '0b1001'
~x       # -10
bin(~x)  # '-0b1010'

# By performing the AND operation to make a string of two's complement representation,
# you can obtain a string with the bits inverted.

# For example, to get a 4-digit bit inverted string, specify '04b' with format() and pad it with zeros.

bin(~x & 0xff)  # '0b11110110'
format(~x & 0b1111, '04b')  # '0110'
bin(~x & 0b1111)            # '0b110'
format(~x & 0b1111, 'b')    # '110'


# %%
# %% bit shifting
x = 9
bin(x)      # '0b1001'

x << 1       # 18
bin(x << 1)  # '0b10010'

x >> 1       # 4
bin(x >> 1)  # '0b100'

# For negative values, the sign bit is expanded and shifted,
# and the positive and negative signs do not change.
#!  Negative values are considered to have infinite 1 on the left side.

x = -9
bin(x)          # `-0b1001`
bin(x & 0xff)   # '0b11110111'

x << 1          # -18
bin(x << 1)     # '-0b10010'
bin((x << 1) & 0xff)  # 0b11101110

x >> 1          # -5
bin(x >> 1)     # '-0b101'
bin((x >> 1) & 0xff)  # '0b11111011'


# %% pandas & numpy

l1 = [0, 1, 3, 4, 5, 6, 7, 8, 9]

# right shift (removing bit from the right)
l1 >> 1     #! TypeError: unsupported operand type(s) for >>: 'list' and 'int'
[l >> 1 for l in l1]    # [0, 0, 1, 2, 2, 3, 3, 4, 4]
[l >> 2 for l in l1]    # [0, 0, 0, 1, 1, 1, 1, 2, 2]

# left shift (add 1 bit 0 on the right)
[l << 1 for l in l1]    # [0, 2, 6, 8, 10, 12, 14, 16, 18]
# left shift (add 2 bits 0 on the right)
[l << 2 for l in l1]    # [0, 2, 6, 8, 10, 12, 14, 16, 18]

# in pandas
s1 = pd.Series(l1)
s1

# bit shifting is not vectorised in pandas
s1 >> 1     # TypeError: unsupported operand type(s) for >>: 'Series' and 'int'
s1.apply(lambda x: x >> 1)
s1.apply(lambda x: x << 2)

# but is in numpy
s1.values >> 1      # array([0, 0, 1, 2, 2, 3, 3, 4, 4])
s1.values << 2      # array([ 0,  4, 12, 16, 20, 24, 28, 32, 36])

# %%
~s1
-s1

# %% xor (exclusive or)

s1 ^ True
s1 ^ False
s1 ^ (s1.values >> 1)
# 0     0
# 1     1
# 2     2
# 3     6
# 4     7
# 5     5
# 6     4
# 7    12
# 8    13
# dtype: int64

# %%
# sth useful
# 2 binary variables == 4 combinations of values
a1 = np.array([False, False, True, True])
a2 = np.array([False, True, False, True])

a1 << 1     # array([0, 2, 0, 2])
(a1 << 1) | a2  # array([0, 1, 2, 3])

bin((a1 << 1) | a2)  #! TypeError: only integer scalar arrays can be converted to a scalar index
format((a1 << 1) | a2, 'b')  #! TypeError: unsupported format string passed to numpy.ndarray.__format__

[bin(v) for v in (a1 << 1) | a2]            # ['0b0', '0b1', '0b10', '0b11']
[format(v, 'b') for v in (a1 << 1) | a2]    # ['0', '1', '10', '11']
[format(v, '02b') for v in (a1 << 1) | a2]  # ['00', '01', '10', '11']

2 * a1 + a2     # array([0, 1, 2, 3])
