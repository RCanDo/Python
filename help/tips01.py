# -*- coding: utf-8 -*-
"""
001-dict_get
2018-03-10

1. How to merge two dictionaries in Python 3.5+
2. Different ways to test multiple flags at once in Python
3. How to sort a Python dict by value (== get a representation sorted by value)
4. The get() method on dicts and its "default" argument
5. Namedtuples
6. Using "json.dumps()" to pretty-print Python dicts
7. Function argument unpacking
8. Measure the execution time of small bits of Python code with the "timeit" module
9. In-place value swapping
10. "is" vs "=="
11. Functions are first-class citizens in Python
12. Dicts can be used to emulate switch/case statements
13. Python's built-in HTTP server
14. Python's list comprehensions are awesome.
15. Python 3.5+ supports 'type annotations'
16. Python's list slice syntax can be used without indices

"""

#%%
#%%
# 16. Python's list slice syntax can be used without indices
#     for a few fun and useful things:

# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
lst # []

# You can replace all elements of a list without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
lst # [7, 8, 9]
a   # [7, 8, 9]
a is lst # True

# You can also create a (shallow) copy of a list:
b = lst[:]
b
[7, 8, 9]
b is lst # False

lst[0] = 0
lst   # [0, 8, 9]

b     # [7, 8, 9]    -- (shallow) copy
b is lst # False

a     # [0, 8, 9]
a is lst # True

#%%
#%%
# 15. Python 3.5+ supports 'type annotations'
# that can be used with tools like Mypy to write statically typed Python:

def my_add(a: int, b: int) -> int:
    return a + b

# designed for int
my_add(3, 2)
# but works also for floats (it's still Python!)
my_add(3., 2.)

#%%
#%%
# 14. Python's list comprehensions are awesome.
'''
vals = [expression
        for value in collection
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)
'''
# Example:

even_squares = [x * x for x in range(10) if not x % 2]
even_squares
# [0, 4, 16, 36, 64]


#%%
#%%
# 13. Python's built-in HTTP server

# Python has a HTTP server built into the standard library.
# This is super handy for previewing websites.

# Python 3.x
$ python3 -m http.server

# Python 2.x
$ python -m SimpleHTTPServer 8000

# (This will serve the current directory at
#  http://localhost:8000)

#%%
#%%
# 12. Dicts can be used to emulate switch/case statements

# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


dispatch_if('mul', 2, 8) # 16

dispatch_dict('mul', 2, 8) # 16

dispatch_if('unknown', 2, 8) # None

dispatch_dict('unknown', 2, 8) # None

#%%
#%%
# 11. Functions are first-class citizens in Python

# They can be passed as arguments to other functions, returned as values from other functions
# and assigned to variables and stored in data structures.

def myfunc(a, b):
     return a + b

funcs = [myfunc]
funcs[0]
## <function myfunc at 0x107012230>
funcs[0](2, 3)  ## 5

#%%
#%%
# 10. "is" vs "=="

a = [1, 2, 3]
b = a

a is b ## True
a == b ## True

c = list(a)

a == c ## True
a is c ## False

# • "is" expressions evaluate to True if two variables point to the same object
# • "==" evaluates to True if the objects referred to by the variables are equal

a[0] = 0
a
b  ## !!! b is not a copy of a! it's just different name for a

c  ## c didn't change as it was a copy a
   ## -- the same value at the moment it was created but then living it's own life !

# in other words if
a is b
# their values will always be the same (in case of changing the values of one of them)
# what is not the case when
a is not c

#%%
#%%
# 9. In-place value swapping

# Let's say we want to swap
# the values of a and b...
a = 23
b = 42

# The "classic" way to do it
# with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us
# use this short-hand:
a, b = b, a

#%%
#%%
# 8. Measure the execution time of small bits of Python code with the "timeit" module

# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

"-".join(str(n) for n in range(100))
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.3412662749997253

"-".join([str(n) for n in range(100)])
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.2996307989997149

"-".join(map(str, range(100)))
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.24581470699922647


#%%
#%%
# 7. Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)
# 1, 0, 1

myfunc(**dict_vec)
# 1, 0, 1

#%%
def argskwargs(*args, **kwargs):
    print(args)
    print(list(args))
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

argskwargs(1, 2, 3)
argskwargs(a=1, b=2, c=3)
argskwargs(-1, 0, 4, a=1, b=3, c=3)

#%%
arguments = [-2, -1, 0]

kwarguments = dict(a=1, b=2, c=3)
kwarguments

argskwargs(arguments)     # works but not the way we expect
argskwargs(*arguments)    # OK

argskwargs(kwarguments)   # works but not the way we expect
argskwargs(**kwarguments) # OK

#%%
#%%
# 6. You can use "json.dumps()" to pretty-print Python dicts
#    as an alternative to the "pprint" module

# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
# {'b': 42, 'c': 12648430. 'a': 23}  #


# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
#{
#    "a": 23,
#    "b": 42,
#    "c": 12648430
#}

# Note this only works with dicts containing primitive types (check out the "pprint" module):
json.dumps({all: 'yup'}) #!!! TypeError: keys must be a string

## WHAT'S all TYPE ???

#%%
# In most cases I'd stick to the built-in "pprint" module though :-)
# https://pymotw.com/3/pprint/index.html
import pprint as pp

pp.pprint(my_mapping)
pp.pprint(my_mapping, indent=4, depth=1)  # ?
pp.pformat(my_mapping)  # ?

#%%
data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]

pp.pprint(data)  # what the hell... ???!!!
pp.pprint(data, indent=4)

#%%
#%%
# 5. Namedtuples

# Using namedtuple is way shorter than defining a class manually:

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
Car  ## ~= class with attributes 'color' and 'mileage'

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
#'red'
my_car.mileage
#3812.4

# We get a nice string repr for free:
my_car
#Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue' #!!! AttributeError: "can't set attribute"

##
mycar = Car(10, 'blue')
mycar
## so there's no type checking

mycar = Car(10, 'blue', list(range(5)))
#!!! TypeError: __new__() takes 3 positional arguments but 4 were given
## we've declared only 2 attributes


#%%
#%%
# 4. The get() method on dicts and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

#%%

greeting(382)
## "Hi Alice!"

greeting(333333)
## "Hi there!"

"""
When "get()" is called it checks if the given key exists in the dict.
If it does exist, the value for that key is returned.
If it does not exist then the value of the default argument is returned instead.
"""


#%%
#%%
# 3. How to sort a Python dict by value (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs

sorted(xs.items(), key=lambda x: x[1])
## [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

sorted(xs, key=lambda x: x[1])  # IndexError: string index out of range
#! because
[x for x in xs]  # only indices


# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))  #???
## [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

operator.itemgetter(1)([1, 2])
operator.itemgetter(0)([1, 2])
operator.itemgetter(-1)([1, 2])
operator.itemgetter(-2)([1, 2])
operator.itemgetter(2)([1, 2])  #! IndexError: list index out of range

#%%
sorted([[1, 2], [0, 1], [-1, 4]], key=lambda x: sum(x))

#%%
#%%
# 2. Different ways to test multiple flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')

## Python coerces int to bools: 0 <-> False, all the other ints to True
any((2,))
any((-2,))
any((0,))


#%%
#%%
# 1. How to merge two dictionaries in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

z
## {'a': 1, 'b': 3, 'c': 4}
## noatice that 'b' is taken from y

{**y, **x}
## now 'b' is taken from x


# In Python 2.x you could
# use this:
z = dict(x, **y)
z
{'a': 1, 'b': 3, 'c': 4}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8


