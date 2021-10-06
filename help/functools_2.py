python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: functools 2
subtitle:
version: 1.0
type: tutorial
keywords: [functools]
description: |
    functools library
    The functools module provides tools for adapting or extending functions and other callable objects,
    without completely rewriting them.
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: functools — Tools for Manipulating Functions
      link: https://pymotw.com/3/functools/index.html
    - title: functools
      subtitle: Higher-order functions and operations on callable objects
      link: https://docs.python.org/3.7/library/functools.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: functools_2.py
    path: .../Python/help/
    date: 2021-09-24
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/help/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

#%%
from pprint import pprint
from functools import lru_cache, reduce, singledispatch

#%%
#%% Caching

#%%  @lru_cache -- memoization
"""
The lru_cache() decorator wraps a function in a least-recently-used cache.

__Arguments__ to the function are used to build a hash key, which is then mapped to the result.
Subsequent calls with the same arguments will fetch the value from the cache instead of calling the function.

The decorator also adds methods to the function to examine the state of the cache (cache_info())
and empty the cache (cache_clear()).

See also ../Objects/decorators/practical_decorators.py : 4. Memoization.
The same thing by hand (although only the core, i.e. memoization).
"""

@lru_cache()
def expensive(a, b):
    result = a * b
    print('expensive({}, {}) = {}'.format(a, b, result))
    return result


MAX = 2

for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
# CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)

for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())
# CacheInfo(hits=4, misses=9, maxsize=128, currsize=9)

expensive.cache_clear()
print(expensive.cache_info())
# CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
# CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)

"""
This example makes several calls to expensive() in a set of nested loops.
The second time those calls are made with the same values the results appear in the cache.
When the cache is cleared and the loops are run again the values must be recomputed.
"""
#%%
"""
To prevent the cache from growing without bounds in a long-running process, it is given a maximum size.
The default is  128 entries,  but that can be changed for each cache using the `maxsize` argument.
"""

@lru_cache(maxsize=2)
def expensive(a, b):
    result = a * b
    print('expensive({}, {}) = {}'.format(a, b, result))
    return result

def make_call(a, b):
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')


print('Establish the cache')
make_call(1, 2)
make_call(2, 3)

print('\nUse cached items')
make_call(1, 2)     # cache hit
make_call(2, 3)     # cache hit

print('\nCompute a new value, triggering cache expiration')
make_call(3, 4)

print('\nCache still contains one old item')
make_call(2, 3)     # cache hit

print('\nOldest item needs to be recomputed')
make_call(1, 2)

"""
In this example the cache size is set to 2 entries.
When the third set of unique arguments (3, 4) is used the oldest item in the cache
is dropped and replaced with the new result.
"""
#%%
"""
!!!  The keys for the cache managed by lru_cache() must be hashable,   !!!
so all of the arguments to the function wrapped with the cache lookup must be hashable.
"""
make_call([1], 2)   #! TypeError: unhashable type: 'list'

make_call(1, {'2': 'two'})  #! TypeError: unhashable type: 'dict'


#%%
#%% Reducing a Data Set

#%% reduce()
"""
The reduce() function takes a callable and a sequence of data as input
and produces a single value as output based on invoking the callable
with the values from the sequence and accumulating the resulting output.
"""

def operator(a, b):
    print('operator({}, {})'.format(a, b))
    return a + b

data = range(1, 5)
reduce(operator, data)
#  operator(1, 2)
#  operator(3, 3)
#  operator(6, 4)
# 10

#%%
"""
The optional initializer argument is placed at the front of the sequence
and processed along with the other items.
This can be used to update a previously computed value with new inputs.
"""

data = range(1, 5)
reduce(operator, data, -10)
#  operator(1, 2)
#  operator(3, 3)
#  operator(6, 4)
# 0

#%%
"""
Sequences with a single item automatically reduce to that value when no initializer is present.
Empty lists generate an error, unless an initializer is provided.
"""

reduce(operator, [1])       # 1
reduce(operator, [1], -10)  # -9
reduce(operator, [])        #! TypeError: reduce() of empty sequence with no initial value

#%% example ak1
# see collections_1.py : example ak1  for Counter()


#%%
#%% Generic Functions
"""
In a dynamically typed language like Python it is common to need to perform slightly different operation
based on the type of an argument,
especially when dealing with the difference between a list of items and a single item.
It is simple enough to check the type of an argument directly,
but in cases where the behavioral difference can be isolated into separate functions
functools provides the singledispatch() decorator to register a set of generic functions
for automatic switching based on the type of the first argument to a function.
"""

@singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))

@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))

@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item), end=" ")

#%%
myfunc('string argument')       # default myfunc('string argument')
myfunc(1)                       # myfunc_int(1)
myfunc(2.3)                     # default myfunc(2.3)
myfunc(['a', 'b', 'c'])         # myfunc_list()   a   b   c

"""
The register() attribute of the new function serves as another decorator for registering
alternative implementations.
The first function wrapped with singledispatch() is the default implementation
if no other type-specific function is found, as with the float case in this example.

When no exact match is found for the type, the inheritance order is evaluated and the closest matching type is used.
"""
#%%
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass

@singledispatch
def myfunc(arg):
    print('default myfunc({})'.format(arg.__class__.__name__))

@myfunc.register(A)
def myfunc_A(arg):
    print('myfunc_A({})'.format(arg.__class__.__name__))

@myfunc.register(B)
def myfunc_B(arg):
    print('myfunc_B({})'.format(arg.__class__.__name__))

@myfunc.register(C)
def myfunc_C(arg):
    print('myfunc_C({})'.format(arg.__class__.__name__))


#%%
myfunc(A())         # myfunc_A(A)
myfunc(B())         # myfunc_B(B)
myfunc(C())         # myfunc_C(C)
myfunc(D())         # myfunc_B(D)
myfunc(E())         # myfunc_C(E)

#%%
In this example, classes D and E do not match exactly with any registered generic functions, and the function selected depends on the class hierarchy.

$ python3 functools_singledispatch_mro.py

myfunc_A(A)
myfunc_B(B)
myfunc_C(C)
myfunc_B(D)
myfunc_C(E)



#%%


#%%