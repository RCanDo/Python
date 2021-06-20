#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: 30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
subtitle:
version: 1.0
type: code snippets
keywords: [Python]
description: code snippets
sources:
    - title: 30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
      link: https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
      date: 2019-09-13
      authors:
          - fullname: Fatos Morina
            www: https://www.fatosmorina.com/
      usage: copy
file:
    usage:
        interactive: True
        terminal: False
    name: tips02.py
    path: D:/ROBOCZY/Python/help/
    date: 2019-09-13
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%% 23. Try else
try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("No exceptions were raised")

#%% 21. Use enumerate

lst = list('abcdefgh')
for i, l in enumerate(lst):
    print(i, l)

#%% 10. Chained comparison
"""
You can do multiple comparisons with all kinds of operators in a single line.
"""
a=3
2 < a < 8
1 == a < 8

#%% 8. Compact
"""
This method removes falsy values (False, None, 0 and “”) from a list
by using filter().
"""

lst = [0, 1, False, 2, '', 3, 'a', 's', 34, None, True]
lst
list(filter(bool, lst))

#%% 17. Chained function call
"""
You can call multiple functions inside a single line.
"""
import operator as op

a, b = 1, 2
(op.subtract if a>b else op.add)(a, b)

#%% user defined operators (functions in general!)
def op1(x, y): return x/y
def op2(x, y): return x/(y+1)

x, y = 1, 0
(op1 if y != 0 else op2)(x, y)


#%% 20. Convert two lists into a dictionary

keys = ["a", "b", "c"]
values = [2, 3, 4]
dict(zip(keys, values))  # {'a': 2, 'c': 4, 'b': 3}

#%% X. Dictionary from tuples (key: value)
# we want
{1:10, 2:20, 3:30}   # and so on...

dict(zip([1, 2], [10, 20]))
dict(zip([1, 2, 3], [10, 20, 30]))
dict(zip((1, 2), (10, 20)))
dict(zip((1, 2, 3), (10, 20, 30)))  # (*)

# but we have data like:  (1, 10), (2, 20), (3, 30), ...
dict(zip((1,10), (2,20), (3, 30)))  #! ValueError: dictionary update sequence element #0 has length 3; 2 is required
dict((1,10), (2,20), (3, 30))   #! TypeError: dict expected at most 1 arguments, got 3

# SOLUTION(s):
dict(((1,10), (2,20), (3, 30)))    # (!!!)   #!!! WOW !!!
dict([(1,10), (2,20), (3, 30)])    # (!!!)   #!!! WOW !!!
dict(([1,10], [2,20], [3, 30]))    # (!!!)   #!!! WOW !!!
dict([[1,10], [2,20], [3, 30]])    # (!!!)   #!!! WOW !!!


# See the story below:

#
list(zip((1,10), (2,20), (3, 30)))
[k for k in zip((1,10), (2,20), (3, 30))]
#> [(1, 2, 3), (10, 20, 30)]

#!!! BUT !!!
(k for k in zip((1,10), (2,20), (3, 30)))
#> <generator object <genexpr> at 0x00000164800086C8>
#
# so the above is the same as
dict(((1, 2, 3), (10, 20, 30)))  #! ValueError: dictionary update sequence element #0 has length 3; 2 is required

# we must transform our sequence to the form (*)
dict(zip(*list(zip((1,10), (2,20), (3, 30)))))   # good!

# what is the same as
dict(zip(*zip((1,10), (2,20), (3, 30))))

#!!! BUT as we see in (!!!)  zip(*zip(...)) is the same as (...)

dict(((1,10), (2,20), (3, 30)))

#!!! INCREDIBLE !!!

#%% the same with map()

def fun(x):
    return x, 10*x

dict(map(fun, [1, 2, 3]))
dict(map(fun, range(10)))

import numpy as np
def fun2(x):
    return x, np.log2(x)

dict(map(fun2, range(10)))

dict(map(lambda x: (x, np.log(x)), range(10)))
dict(map(lambda x: np.log(x), range(10)))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

#%%