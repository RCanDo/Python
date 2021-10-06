#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Can you solve these 3 (seemingly) easy Python problems?
subtitle:
version: 1.0
type: examples
keywords: [immutable, closure, copy, list]
description: |
remarks:
todo:
    - title: Can you solve these 3 (seemingly) easy Python problems?
      link: https://levelup.gitconnected.com/can-you-solve-these-3-seemingly-easy-python-problems-2c793967cd2c
      date: 2020-mm-dd
      authors:
          - fullname: Maria Fabiańska
      usage: |
    - title:
      link: https://towardsdatascience.com/you-are-telling-people-that-you-are-a-python-beginner-if-you-ask-this-question-fe35514ca091
      authors:
          - fullname: WY Fok
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: three_things.py
    path: ~/Python/help/
    date: 2020-08-
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
#%% Problem 1
x = 1
id(x)
y = 2
l = [x, y]
id(l[0]) # the same as id(x)
x += 5
l        # [1, 2]
x        # 6  ... although x IS mutable
id(x)    # new id
id(l[0]) # old id !

#%% from article
"""
Since x is immutable (int), the operation x+=5 does not alter the original object,
but creates a new one.
The first element of the list still points to the original object,
therefore its value remains the same.
"""
# x IS mutable -- it's 5 which is IMmutable
# no matter -- IT IS A MESS !!!

#%%
a = [1]
b = [2]
s = [a, b]
a.append(5)  # takes effect -- a is mutable (list)
s        # [[1, 5], [2]]
a

#%% deeper:
x = 1
y = 2
a = [x]
b = [y]
ll = [a, b]
ll
x += 5
x      # 6
a      # [1]
ll     # [[1], [2]]

#%%
#%% Problem 2
# Let’s define a simple function:

def f(x, s=set()):
    s.add(x)
    print(s)

#%% What will happen if you call:

f(7)          # {7}
f(6, {4, 5})  # {4, 5, 6}
f(2)          # {2, 7}

#! Never use mutable as default argument value !!!
#%% better way:

def f(x, s=None):
    s = set() if s is None else s
    s.add(x)
    print(s)

#%%
f(7)          # {7}
f(6, {4, 5})  # {4, 5, 6}
f(2)          # {2}

#%%
#%% Problem 3
# Let’s define three simple functions:

def f():
    l = [1]
    def inner(x):
        l.extend([x])
        # compiler call LOAD_DEREF instruction which will load
        # the non-local list l (and then the list will be modified)
        return l
    return inner

def g():
    y = 1
    def inner(x):
        y += x
        return y
    return inner

def h():
    l = [1]
    def inner(x):
        l += [x]
        # compiler call LOAD_FAST which looks for the variable l
        # to in the local scope of the inner function and therefore fails
        return l
    return inner

#%% What will be the result of the following commands?

f_inner = f()
print(f_inner(2))  # [1, 2]

g_inner = g()
print(g_inner(2))  # UnboundLocalError: local variable 'y' referenced before assignment

h_inner = h()
print(h_inner(2))  # UnboundLocalError: local variable 'l' referenced before assignment

#%%
"""
In this problem we deal with closures
— the fact that inner functions remember how their enclosing namespaces
looked at the time of definition.
"""

#%% remedy
def g():
    y = 1
    def inner(x):
        nonlocal y
        y += x
        return y
    return inner

def h():
    l = [1]
    def inner(x):
        nonlocal l
        l += [x]
        return l
    return inner

g_inner = g()
print(g_inner(2))   # 3

h_inner = h()
print(h_inner(2))   # [1, 2]

#%%
#%%
""" Conclusion

Be mindful of the distinction between mutable and immutable variables.

Do not use mutable default arguments.

Be careful when altering closure variables in inner functions.
Use nonlocal keyword to declare that the variable is not local.

Please feel free to share other examples of potential problems
resulting from misuse of mutable and immutable objects in your responses.
If you want to learn what role do mutable and immutable objects
play in list copying check out my next article.
"""
#%%
