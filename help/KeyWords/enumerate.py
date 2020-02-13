# -*- coding: utf-8 -*-
"""
title: enumerate()
doc: https://docs.python.org/3.6/library/functions.html#enumerate
author: akasprzy
date: Sun Mar  4 09:02:22 2018
"""


abc = list('abcdefg')
for i in enumerate(abc): print(i)

seasons =['spring','summer','automn','winter']
list(enumerate(seasons))
list(enumerate(seasons, start=1))

for s in enumerate(seasons): print(s)

#%%
## equivalent to:
def enum(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

for s in enum(seasons): print(s)

#%%

from cycler import cycler

cc2 = cycler(col = list('rgb'))
cc2
for k in cc2: print(k)

for j, k in enumerate(cc2):  print(j,k)
for t in enumerate(cc2):  print(t)


cc4 = cycler(nr = range(3))
cc4
for j, k in enumerate(cc4):  print(j,k)
for t in enumerate(cc4):  print(t)

## together with zip()
for j, (a, b) in enumerate(zip(cc2+cc4, cc4+cc2)):
    print('({j}) A: {A!r}  B: {B!r}'.format(j=j, A=a, B=b))
