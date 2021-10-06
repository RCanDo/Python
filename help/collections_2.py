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
keywords: [collections, containers, deque, namedtuple, OrderedDict]
description: |
    Collections library
    deque(), namedtuple(), OrderedDict()
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: collections — Container Data Types
      link: https://pymotw.com/3/collections/index.html
    - title: Collections
      link: https://docs.python.org/3.7/library/html
    - title: collections.abc — Abstract Base Classes for Containers
      link: https://pymotw.com/3/collections/abc.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: collections_2.py
    path: .../Python/help/
    date: 2021-09-23
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
from collections import deque, namedtuple, OrderedDict

#%%
"""
see
https://pymotw.com/3/collections/abc.html
for collections.abc — Abstract Base Classes for Containers
"""

#%%
#%% deque() — Double-Ended Queue
"""
A double-ended queue, or deque, supports adding and removing elements from either end of the queue.
The more commonly used __stacks__ and __queues__ are degenerate forms of deques,
where the inputs and outputs are restricted to a single end.
"""

d = deque('abcdefg')
d               # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
len(d)          # 7
d[0]            # 'a'
d[-1]           # 'g'

d.remove('c')
d               # deque(['a', 'b', 'd', 'e', 'f', 'g'])

"""
Since deques are a type of sequence container, they support some of the same operations as list,
such as examining the contents with __getitem__(), determining length,
and removing elements from the middle of the queue by matching identity.
"""

#%% Populating
"""
A deque can be populated from either end, termed “left” and “right” in the Python implementation.
"""
# Add to the right
d1 = deque()
d1.extend('abcdefg')
d1              # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

d1.append('h')
d1              # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

d1.extendleft(range(6))
d1              # deque([5, 4, 3, 2, 1, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

d1.appendleft(6)
d1              # deque([6, 5, 4, 3, 2, 1, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

#%% Consuming
"""
Similarly, the elements of the deque can be consumed from both ends or either end, depending on the algorithm being applied.

Use pop() to remove an item from the “right” end of the deque and popleft() to take an item from the “left” end.
"""

d = deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print()

d = deque(range(6))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
print()

#%%
"""
Since deques are thread-safe, the contents can even be consumed from both ends at the same time from separate threads.
"""
import threading
import time

candle = deque(range(5))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))

right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

"""The threads in this example alternate between each end, removing items until the deque is empty.

 Left: 0
Right: 4
Right: 3
 Left: 1
Right: 2
 Left done
Right done
"""
#%% Rotating
"""
Another useful aspect of the deque is the ability to rotate it in either direction, so as to skip over some items.
"""
d = deque(range(10))
print('Normal        :', d)

d = deque(range(10))
d.rotate(2)
print('Right rotation:', d)

d = deque(range(10))
d.rotate(-2)
print('Left rotation :', d)

#%% Constraining the Queue Size
"""
A deque instance can be configured with a maximum length so that it never grows beyond that size.

!!! When the queue reaches the specified length, existing items are discarded as new items are added. !!!

This behavior is useful for finding the last n items in a stream of undetermined length.
"""

import random
random.seed(1)

d1 = deque(maxlen=3)
d2 = deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)

# The deque length is maintained regardless of which end the items are added to.

#%%
#%% namedtuple — Tuple Subclass with Named Fields
"""
The standard tuple uses numerical indexes to access its members.
"""
bob = ('Bob', 30, 'male')
jane = ('Jane', 29, 'female')

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))

"""
This makes tuples convenient containers for simple uses.
In contrast, remembering which index should be used for each value can lead to errors,
especially if the tuple has a lot of fields and is constructed far from where it is used.
A namedtuple assigns names, as well as the numerical index, to each member.
"""
#%% Defining
"""
namedtuple instances are just as memory efficient as regular tuples
because they do not have per-instance dictionaries.
Each kind of namedtuple is represented by its own class,
which is created by using the namedtuple() factory function.
The arguments are the name of the new class and a string containing the names of the elements.
"""
Person = namedtuple('Person', 'name age')
Person   # ~= class Person, subclass of namedtuple

bob = Person(name='Bob', age=30)
bob[0]
bob[1]

jane = Person(name='Jane', age=29)

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

print()
for p in [bob, jane]:
    print(f'{p.name} is {p.age} years old')

#%%
"""
Just like a regular tuple, a namedtuple is __immutable__.
This restriction allows tuple instances to have a consistent hash value,
which makes it possible to use them as keys in dictionaries and to be included in sets.
"""
pat = Person(name='Pat', age=12)
pat.age = 21   #! AttributeError: can't set attribute

#%% Invalid Field Names
"""
Field names are invalid if they are repeated or conflict with Python keywords.
"""
try:
    namedtuple('Person', 'name class age')
except ValueError as err:
    print(err)
#! AttributeError: can't set attribute  ('class')

#%%
try:
    namedtuple('Person', 'name age age')
except ValueError as err:
    print(err)
# Encountered duplicate field name: 'age'

#%%
"""
In situations where a namedtuple is created based on values outside the control of the program
(such as to represent the rows returned by a database query, where the schema is not known in advance),
the rename option should be set to True so the invalid fields are renamed.
"""

with_class = namedtuple('Person', 'name class age', rename=True)
with_class._fields   # ('name', '_1', 'age')

two_ages = namedtuple('Person', 'name age age', rename=True)
two_ages._fields     # ('name', 'age', '_2')
"""
The new names for renamed fields depend on their index in the tuple,
so the field with name class becomes _1 and the duplicate age field is changed to _2.
"""
#%% Special Attributes
"""
`namedtuple` provides several useful attributes and methods for working with subclasses and instances.

All of these built-in properties have names prefixed with an underscore (_),
which by convention in most Python programs indicates a private attribute.
For namedtuple, however, the prefix is intended to protect the name
from collision with user-provided attribute names.

The names of the fields passed to namedtuple to define the new class
are saved in the _fields attribute.
"""
Person = namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
bob             # Person(name='Bob', age=30)
bob._fields     # ('name', 'age')


#%%
"""
namedtuple instances can be converted to OrderedDict instances using _asdict().
"""
Person = namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
bob._asdict()   # {'name': 'Bob', 'age': 30}

#%%
"""
The _replace() method builds a new instance, replacing the values of some fields in the process.
"""
Person = namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
bob             # Person(name='Bob', age=30)
bob2 = bob._replace(name='Robert')
bob2            # Person(name='Robert', age=30)
"""
Although the name implies it is modifying the existing object,
because namedtuple instances are immutable the method actually returns a new object.
"""

#%%
#%% OrderedDict — Remember the Order Keys are Added to a Dictionary
"""
An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

Before Python 3.6 a regular dict did not track the insertion order,
and iterating over it produced the values in order based on how the keys are stored in the hash table,
which is in turn influenced by a random value to reduce collisions.
In an OrderedDict, by contrast, the order in which the items are inserted is remembered and used when creating an iterator.

Under Python 3.6, the built-in dict does track insertion order,
!!! although this behavior is a side-effect of an implementation change and should not be relied on.  !!!
"""
d = {}
d['c'] = 'C'
d['a'] = 'A'
d['b'] = 'B'
d               # {'c': 'C', 'a': 'A', 'b': 'B'}

d = OrderedDict()
d['c'] = 'C'
d['a'] = 'A'
d['b'] = 'B'
d               # OrderedDict([('c', 'C'), ('a', 'A'), ('b', 'B')])

#%%
"""
A regular dict looks at its contents when testing for equality.
!!! An OrderedDict also considers the order in which the items were added. !!!
"""

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

d1 == d2        # True

#%%
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

d1 == d2        # False

#%%  Reordering
"""
It is possible to change the order of the keys in an OrderedDict by moving them
to either the beginning or the end of the sequence using move_to_end().
"""
d = OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
d               # OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])

d.move_to_end('b')
d               # OrderedDict([('a', 'A'), ('c', 'C'), ('b', 'B')])

d.move_to_end('b', last=False)
d               # OrderedDict([('b', 'B'), ('a', 'A'), ('c', 'C')])

#%%
#%%