python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Collections
subtitle:
version: 1.0
type: tutorial
keywords: [collections, containers, ChainMap, Counter, defaultdict]
description: |
    Collections library
    ChainMap, Counter, defaultdict
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: collections — Container Data Types
      link: https://pymotw.com/3/collections/index.html
    - title: Collections
      link: https://docs.python.org/3.7/library/collections.html
    - title: collections.abc — Abstract Base Classes for Containers
      link: https://pymotw.com/3/collections/abc.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: collections_1.py
    path: .../Python/help/
    date: 2021-09-22
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
from collections import ChainMap, Counter, defaultdict

#%%
"""
see
https://pymotw.com/3/collections/abc.html
for collections.abc — Abstract Base Classes for Containers
"""

#%%
#%% ChainMap() — Search Multiple Dictionaries
# https://pymotw.com/3/collections/chainmap.html
"""
The ChainMap class manages a sequence of dictionaries,
and searches through them in the order they are given to find values associated with keys.
A ChainMap makes a good “context” container, since it can be treated as a stack
for which changes happen as the stack grows,
with these changes being discarded again as the stack shrinks.
"""
#%% Accessing Values
"""
The ChainMap supports the same API as a regular dictionary for accessing existing values.
"""
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = ChainMap(a, b)
m    # ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

m['a']   # 'A'
m['b']   # 'B'
m['c']   # 'C'    !!!

m.keys()            # KeysView(ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}))
list(m.keys())      # ['b', 'c', 'a']
m.values()          # ValuesView(ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}))
list(m.values())    # ['B', 'C', 'A']

m.items()           # ItemsView(ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}))
list(m.items())     # [('b', 'B'), ('c', 'C'), ('a', 'A')]

'a' in m  # True
'A' in m  # False
'd' in m  # False

"""
The child mappings are searched in the order they are passed to the constructor,
so the value reported for the key 'c' comes from the a dictionary.
"""

#%% Reordering
"""
The ChainMap stores the list of mappings over which it searches in a list in its maps attribute.
This list is mutable, so it is possible to add new mappings directly
or to change the order of the elements to control lookup and update behavior.
"""
m.maps   # [{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
m['c']   # 'C'

# reverse the list
m.maps = list(reversed(m.maps))

m.maps   # [{'b': 'B', 'c': 'D'}, {'a': 'A', 'c': 'C'}]
m['c']   # 'D'
"""
When the list of mappings is reversed, the value associated with 'c' changes.
"""
#%%  Updating Values
"""
A ChainMap does not cache the values in the child mappings.
Thus, if their contents are modified, the results are reflected when the ChainMap is accessed.
"""

aa = {'a': 'A', 'c': 'C'}
bb = {'b': 'B', 'c': 'D'}
m = ChainMap(aa, bb)

m['c']          # 'C'
aa['c'] = 'E'
m['c']          # 'E'

aa['p'] = 0
m['p']          # 0

m['a'] = 'AA'
m['a']          # 'AA'
aa['a']         # 'AA'

m['c'] = 1
m['c']          # 1   but which 'c' ?
m               # ChainMap({'a': 'AA', 'c': 1, 'p': 0}, {'b': 'B', 'c': 'D'})
aa              # {'a': 'AA', 'c': 1, 'p': 0}

bb['a'] = 'BB'
m
m['a']          # 'AA'

"""
Changing the values associated with existing keys and adding new elements works the same way.
"""
#%%
"""
ChainMap provides a convenience method for creating a new instance with one extra mapping
at the front of the maps list to make it easy to avoid modifying the existing underlying data structures.
"""
m1 = ChainMap(aa, bb)
m2 = m1.new_child()
m2              # ChainMap({},         {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

m2['c'] = 'E'
m2              # ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

#%%
"""
This stacking behavior is what makes it convenient to use ChainMap instances as template or application contexts.
Specifically, it is easy to add or update values in one iteration, then discard the changes for the next iteration.
For situations where the new context is known or built in advance, it is also possible to pass a mapping to new_child().
"""

cc = {'c': 'E'}

m2 = m1.new_child(cc)
m2              # ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

# This is the equivalent of
m2 = ChainMap(cc, *m1.maps)              #!!!
m2              # ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})

m1["c"] = 'E'
m1              # ChainMap({'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})
m2["c"] = 'E'
m2              # ChainMap({'c': 'E'}, {'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})   # !!! look carefully

#%%
#%% Counter() — Count Hashable Objects
"""
A Counter is a container that keeps track of how many times equivalent values are added.
It can be used to implement the same algorithms for which other languages commonly use
_bag_ or _multiset_ data structures.
"""

#%% Initializing
"""
Counter supports three forms of initialization.
Its constructor can be called with a sequence of items, a dictionary containing keys and counts,
or using keyword arguments that map string names to counts.
"""

Counter(['a', 'b', 'c', 'a', 'b', 'b'])
Counter({'a': 2, 'b': 3, 'c': 1})
Counter(a=2, b=3, c=1)

"""
The results of all three forms of initialization are the same.
"""
#%%
"""
An empty Counter can be constructed with no arguments and populated via the update() method.
"""
c = Counter()
c               # Counter()

c.update('abcdaab')
c               # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

c.update({'a': 1, 'd': 5})
c               # Counter({'a': 4, 'b': 2, 'c': 1, 'd': 6})

c.update({'b':1, 'c':2})
c               # Counter({'a': 4, 'b': 3, 'c': 3, 'd': 6})

#%% Accessing counts
"""
Once a Counter is populated, its values can be retrieved using the dictionary API.
"""
c['a']    # 4
"""
Counter does not raise KeyError for unknown items.
If a value has not been seen in the input (as with e in this example), its count is 0.
"""
c['e']    # 0

#%%
"""
The elements() method returns an iterator that produces all of the items known to the Counter.
"""
list(c.elements())
"""
The order of elements is not guaranteed, and items with counts less than or equal to zero are not included.
"""
c['z'] = 0
list(c.elements())  # no 'z'

#%% Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts.
c.most_common()
c.most_common(2)

#%% Arithmetic
"""
Counter instances support arithmetic and set operations for aggregating results.
This example shows the standard operators for creating new Counter instances,
but the in-place operators +=, -=, &=, and |= are also supported.
"""

c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c1              # Counter({'a': 2, 'b': 3, 'c': 1})

c2 = Counter('alphabet')
c2              # Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})

# Combined counts
c1 + c2         # Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

# Subtraction
c1 - c2         # Counter({'b': 2, 'c': 1})

# Intersection (taking positive minimums)
c1 & c2         # Counter({'a': 2, 'b': 1})

# Union (taking maximums)
c1 | c2         # Counter({'a': 2, 'b': 3, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

#%% example ak1
"""
The task is to count instances of each word within a corpus, i.e. finding out its frequency.
Case-insensitive, only words (get rid of all other characters like periods, hyphens, exclamations, etc.).
"""
corpus = ['NYC is the Big Apple.',
 'NYC is known as the Big Apple.',
 'I love NYC!',
 'I wore a hat to the Big Apple party in NYC.',
 'Come to NYC. See the Big Apple!',
 'Manhattan is called the Big Apple.',
 'New York is a big city for a small cat.',
 'The lion, a big cat, is the king of the jungle.',
 'I love my pet cat.',
 'I love New York City (NYC).',
 'Your dog chased my cat.']

#%%
from functools import reduce, partial

def repl(string: str, noise: str):
    return reduce(lambda s, z: s.replace(z, ""), list(noise), string)
# repl("pr!zs$-ab_", "!$-_")   # 'przsab'

docs = [d.lower() for d in map(partial(repl, noise="!?,.()"),  corpus)]

## in one line (horrible to understand! just as excercise)
[d.lower() for d in map(lambda s: reduce(lambda s, z: s.replace(z, ""), list("!?,.()"), s),  corpus)]

#%%
counter = Counter()

for d in docs:
    counter.update(d.split())
counter.most_common()


#%%
#%% defaultdict() — Missing Keys Return a Default Value
"""
The standard dictionary includes the method setdefault() for retrieving a value
and establishing a default if the value does not exist.
"""
dd = {'a':1, 'b':2}
help(dd.setdefault)
dd.setdefault('c', 0)  # 0
dd              # {'a': 1, 'b': 2, 'c': 0}
dd['c']         # 0
dd.setdefault('c', 1)  # 0
dd['c']         # 0

dd.update(d=-1)
dd              # {'a': 1, 'b': 2, 'c': 0, 'd': -1}

#%%
"""
By contrast, defaultdict lets the caller specify the default up front when the container is initialized.
"""
d = defaultdict('default value')   #! TypeError: first argument must be callable or None

# hence one must define some function returning constant, e.g.
def default_factory():
    return 'default value'

d = defaultdict(default_factory, foo='bar')
d      # defaultdict(<function __main__.default_factory()>,  {'foo': 'bar'})
d['foo']   # 'bar'
d['bar']   # 'default value'
d['qq']    # 'default value'
d      # defaultdict(<function __main__.default_factory()>,
       #     {'foo': 'bar', 'bar': 'default value', 'qq': 'default value'})

# ...
d.update(ryqu=-1)
d      # defaultdict(<function __main__.default_factory()>,
       #     {'foo': 'bar', 'bar': 'default value', 'qq': 'default value', 'ryqu': -1})

"""
THUS items are created on call if not defined earlier; then they get default value.
"""
#%% example ak2
#%% built-in  dict.setdefault()
import numpy as np
dd = {}
for k, v in zip(np.random.choice(list('abc'), 10, replace=True), np.random.randint(2, size=10)):
    dd.setdefault(k, []).append(v)
dd

#%% defaultdict()
dd = defaultdict(list)
for k, v in zip(np.random.choice(list('abc'), 10, replace=True), np.random.randint(2, size=10)):
    dd[k].append(v)
dd

#%%
"""
This method works well as long as it is appropriate for all keys to have the same default.
It can be especially useful if the default is a type used for aggregating or accumulating values,
such as a list, set, or even int.
The standard library documentation includes several examples in which defaultdict is used in this way.
"""

#%% example 1
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)
d   # defaultdict(list, {})

for k, v in s:
    d[k].append(v)
d   # defaultdict(list, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

sorted(d.items())
    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#%% This technique is simpler and faster than an equivalent technique using dict.setdefault():
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

sorted(d.items())
    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#%% example 2
# Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items())
    # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

#%% example 3
"""
The function int() which always returns zero is just a special case of constant functions.
A faster and more flexible way to create constant functions is to use a lambda function
which can supply any constant value (not just zero):
"""
def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d
         # 'John ran to <missing>'

d        # defaultdict(<function __main__.constant_factory.<locals>.<lambda>()>,
         #    {'name': 'John', 'action': 'ran', 'object': '<missing>'})

#%%
"""
Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:
"""
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())   # [('blue', {2, 4}), ('red', {1, 3})]

#%%
#%%
