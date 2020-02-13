# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Thu Jan  4 09:46:21 2018


5. DATA STRUCTURES
==================
(p. 31)
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/Tutorial/
ls

import importlib ## may come in handy

# importlib.reload(pd)

#%%
'''
5.1 More on Lists
-----------------

You will notice that methods like
insert(), remove() or sort()
that only modify the list have no return value printed – they return the default None.
This is a design principle for all mutable data structures in
Python.

'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits
type(fruits)
len(fruits)
fruits

fruits.count('apple')
fruits.count('tangerine')

fruits.count('banana')
fruits.index('banana')      ## 3 -- only first instance

fruits.index('banana', 4)   ## 6 -- Find next banana starting a position 4

fruits.reverse()
fruits

## it does not return a value, only changes object  (works "in place"):
frev = fruits.reverse()
frev
type(frev)   ## NoneType  !!!
len(frev)    ## TypeError: object of type 'NoneType' has no len()
## while
fruits

fruits.append('grape')
fruits
## equivalent to
fruits[len(fruits):] = ['cherry']
fruits

fruits.sort()
fruits


fruits.pop()  ## takes off the last element
fruits
## at least returns value...
last = fruits.pop()
last
type(last)
len(last)
fruits.pop(0)  ## takes off the first element (with given index)
fruits


fruits.remove('kiwi')  ## Remove the first item from the list whose value is x. It is an error if there is no such item.
fruits
fruits.remove('kiwi')  ## ValueError: list.remove(x): x not in list

fruits.clear()
fruits
## equivalent to del a[:]
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[:]
fruits      ## empty list
## while
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits  ## deleting whole list
fruits      ## NameError: name 'fruits' is not defined


#%%
### Other methods

frus = fruits
frus

#%%
## list.extend(iterable)
## Extend the list by appending all the items from the iterable.
frus.extend(range(3,6))
frus
## Equivalent to a[len(a):] = iterable
frus[len(frus):] = range(7,10)
frus

## notice the difference
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append(['durian','berry']); fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.extend(['durian','berry']); fruits

#%%
frus = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
frus
frus.insert(2,'tomato')
frus

frus.insert(0,'berry')   ## at the beginning
frus
frus.insert(len(frus),'durian')  ## to the end == .append()
frus

#%% !!! BTW
ll = list(range(2,5))
ll
kk = ll
kk
ll.append('sth')
kk
ll
kk = 2
ll
kk = list(range(3,6))
kk
ll
kk.append('qq')
kk
ll

## WTF!!!

#%%
## solution:
## list.copy()

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits
frus = fruits.copy()
frus

frus.append('rotten tomato')
frus
fruits

## equivalent to list[:]
frus2 = fruits[:]
frus2
frus2.pop()
frus2
fruits
frus

#%%
### 5.1.1 Using Lists as Stacks

stack = [3,4,5]
stack.append(6)
stack.append(7)
stack

stack.pop()
stack.pop()
stack

#%% 

#%%
### list (sequence) unpacking
ll = [1, [2,3], 'qq']
a, b, c = ll
a
b
c

#%%
'''
### 5.1.2 Using Lists as Queues

It is also possible to use a list as a queue,
where the first element added is the first element retrieved (“first-in, first-out”);
however, lists are NOT efficient for this purpose.
While append()s and pop()s from the end of list are fast,
doing inserts or pops from the beginning of a list is SLOW
(because all of the other elements have to be shifted by one).

To implement a queue, use  `collections.deque`
which was designed to have fast appends and pops from both ends.
For example:
'''

from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue
queue.popleft()
queue.popleft()
queue

#%%
### 5.1.3 List Comprehensions

squares = []
for x in range(10):
    squares.append(x**2)
squares

squares = list(map(lambda x: x**2, range(10)))
squares

squares = [x**2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
## [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs

#%%
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x,x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]  ## SyntaxError: invalid syntax ; File "<stdin>", line 1, in <module>

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec
[elem for elem in vec]
[num for elem in vec for num in elem]     ## !!! ??? from outermost to innermost

#%%
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#%%
### 5.1.4 Nested List Comprehensions

matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
matrix

[[row[i] for row in matrix] for i in range(4)]

## equivalent to

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

## equivalent to

transposed = []
for i in range(4):
    trans_row = []
    for row in matrix:
        trans_row.append(row[i])
    transposed.append(trans_row)
transposed

'''
In the real world, you should prefer built-in functions to complex flow statements.
The zip() function would do a great job for this use case:
'''

list(zip(*matrix))
zip(*matrix)          ## ???

#%%
'''
5.2 The del statement
---------------------
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a           ## empty list

del a
a           ## name 'a' is not defined

#%%
'''
5.3 Tuples and Sequences
------------------------
'''
t = 12, 34, 'qq'   ## tuple packing, i.e. without parenthesis you create a tuple -- a default type of SEQUENCE
                   ## (unlike lists which need [])
t
t[0]
len(t)

x, y, z = t   ##  tuple (sequence) unpacking
x
y
z

u = t, (1, 2, 'c')
u

u1, u2 = u
u1
u2

'''
Tuples are _immutable_, and _usually contain a heterogeneous_ sequence of elements that are accessed via
UNPACKING (see later in this section) or indexing (or even by attribute in the case of _namedtuples_).
Lists are _mutable_, and their elements are _usually homogeneous_ and are accessed by iterating over the list.
'''

## tuples are immutable
t[0] = 1   ## TypeError: 'tuple' object does not support item assignment

## however they can contain mutable object
v = [1,2,3], ['a','b','c']
v
v[0] = []  ## TypeError: 'tuple' object does not support item assignment
## but
v[0][0] = 0   ## OK!!
v
## or
v[0][:] = []
v

## empty tuple
empty = ()
empty

one = (2,)
one
## or
one = 2,
one

(2)   ## just a number not a tuple


#%%
'''
5.4 Sets
--------
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket

###############################################################################
a = 'abracadabra'
set(a)
list(a)
tuple(a)

b = 'alacazam'
set(b)
list(set(b))
tuple(set(b))
set(list(range(6)))         ## set from list
###############################################################################

##
a = set('abracadabra')
a
b = set('alacazam')
b
a | b
a - b
a & b
a ^ b    ## symmetric diff. == no common elements

### set comprehension

a = { x for x in 'abracadabra' if x not in 'abc' }
a

## empty set
empty = set()
empty
type(empty)

## this is empty dictionary (not set)
{}
type({})

#%%
'''
5.5 Dictionaries
'''
tel = {'jack': 4098, 'sape': 4139}
tel
tel['kolo'] = 6666
tel
tel['jack'] = 1234
tel
del tel['jack']
tel
tel['bolo'] = 8888

list(tel.keys())
sorted(tel.keys())

tel.keys()

'kolo' in tel
'bolo' in tel
'jack' in tel

## numeric indices are not valid (unless they are used as keys)
tel[0]  ## KeyError: 0

## any _immutable_ can be a dictionary key, e.g.
tel[(1,2,'qq')] = 'jazz'
tel

## dictionary from **list/set/tuple** of key:value pairs (tuples)
dict( [ ('sape', 4139), ('guido', 4127), ('jack', 4098) ] )
dict( { ('sape', 4139), ('guido', 4127), ('jack', 4098) } )
dict( ( ('sape', 4139), ('guido', 4127), ('jack', 4098) ) )

## dictionary comprehension
{ x: x**2 for x in (2,4,6)}

## When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)


#%%
'''
5.6 Looping Techniques
'''
#%% over list
for v in ['tere','fere','qq!']:
    print(v)

#%% in reversed order
for v in reversed(['tere','fere','qq!']):
    print(v)

#%% over set
for i, v in enumerate({'tere','fere','qq!'}):
    print(i, v)
## in random order !!!

#%% in reversed order
for v in reversed({'tere','fere','qq!'}):
    print(v)
## TypeError: 'set' object is not reversible     !!!

#%% over tuple
for i, v in enumerate(('tere','fere','qq!')):
    print(i, v)

#%% in reversed order
for v in reversed(('tere','fere','qq!')):
    print(v)

#%% over dictionaries returning key:value pars using .items()
tel
for k, v in tel.items():
    print(k, v)

#%% over lists returning index, value using enumerate():
for i, v in enumerate(['tere','fere','qq!']):
    print(i, v)

for i, v in enumerate(reversed(['tere','fere','qq!'])):
    print(i, v)

#%% over two lists at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

#%% sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#%%
'''
It is sometimes tempting to change a list while you are looping over it;
however, it is often simpler and safer to create a new list instead:
'''
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data

## using filter()
list(filter(math.isnan,raw_data))  ## but how to negate() ???

#%%
'''
5.7 More on Conditions
'''
## Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
a, b, c = 1, 2, 3
a < b == c
a < b < c
a < c < b

#%%
## prcedence of operators

a = True
b = True
c = False

a and not b or c
## the same as
(a and (not b)) or c

#%%
s1, s2, s3 = '', 'abc', 'pqr'
s1
s2
s3

s1 or s2
s2 or s3
s1 and s2
s2 and s3
not s1
not s2

non_null = s1 or s2 or s3
non_null

#%%


#%%
'''
5.8 Comparing Sequences and Other Types
'''

(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
