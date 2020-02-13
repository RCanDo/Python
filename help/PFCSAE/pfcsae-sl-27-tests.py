# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 28 08:45:02 2017

27. Testing
===========
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

import importlib ## may come in handy
## importlib.reload(sp)


#%%
'''
1. Testing - context
--------------------

We use Python extension tool  `py.test`, see [pytest.org](http://pytest.org)

'''

def mixstrings(s1, s2):
    """
    Given two strings s1, s2, create and return a new string
    that contains the letters from s1 and s2 mixed, i.e.
    s[0] = s1[0], s[1] = s2[0],
    s[2] = s1[1], s[3] = s2[1],
    ...
    If one string is longer then the other,
    the extra characters in the longer string are ignored.

    Example:
    In []: mixstrings('Hello','12345678')
    Out[]: 'H1e2l3l4o5'
    """

    # what length to process
    n = min(len(s1), len(s2))
    # collect chars in this list
    s = []

    for i in range(n):
        s.append(s1[i])
        s.append(s2[i])

    return("".join(s))



