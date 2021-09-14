# -*- coding: utf-8 -*-
"""
001-dict_get
2018-03-10

1. How to merge two dictionaries in Python 3.5+
2. Different ways to test multiple flags at once in Python
3. How to sort a Python dict by value (== get a representation sorted by value) -- see also sorting.py
4. The get() method on dicts and its "default" argument
5. Namedtuples
6. Using "json.dumps()" to pretty-print Python dicts -- see strings02.py
7. Function argument unpacking -- see kwargs.py
8. Measure the execution time of small bits of Python code with the "timeit" module
    -- see size_memory_time.py
9. In-place value swapping
10. "is" vs "=="  -- see also lists.py
11. Functions are first-class citizens in Python
12. Dicts can be used to emulate switch/case statements
13. Python's built-in HTTP server
14. Python's list comprehensions are awesome. -- see lists.py
15. Python 3.5+ supports 'type annotations'
16. Python's list slice syntax can be used without indices -- see lists.py

"""

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

#%% simpler but less safe (no .get())
"""
The following snippet shows how you can write a simple calculator
without the need to use if-else conditions.
"""

import operator as op
do = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, '^':op.pow}

do['^'](2, 3)
do['/'](2, 3)

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
# 10. "is" vs "=="  -- see also lists.py

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
ll = [['a', 'b'], ['c', 'd'], ['e', 'f', 'g']]
sum(ll, [])      # specifying start value for sum(); default is 0.
sum(ll, ['p'])
help(sum)

#%%
#%%
# 5. Namedtuples

# Using namedtuple is way shorter than defining a class manually:

from collections import namedtuple
help(namedtuple)

NT = namedtuple(typename='NT', field_names=['a', 'b', 'c'])
NT
 # __main__.NT
nt = NT('a', 1, lambda x: x - 1/x)  # works !!!
nt  # NT(a='a', b=1, c=<function <lambda> at 0x00000295C63B1378>)
nt.a
nt.b
nt.c
nt.c(3)
nt.c(nt.b)

for f in list('abc'): print(nt[f])   #! TypeError: tuple indices must be integers or slices, not str
for f in range(3): print(nt[f])

# field names may be passed in one string separated with space
NT = namedtuple(typename='NT', field_names='a b c')
nt = NT('a', 1, lambda x: x - 1/x)
nt.a
nt.b
nt.c

nt._asdict()  # OrderedDict
nt._fields    # ('a', 'b', 'c')
nt.index(1)   # ???
nt.index(0)   # ValueError: tuple.index(x): x not in tuple

#%%
Car = namedtuple('Car', 'color mileage')  #
Car
    ## ~= class with attributes 'color' and 'mileage'
Car()

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

dir(my_car)
my_car._asdict()
my_car._fields      # ('color', 'mileage')
my_car.index((1))   # ???



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
#!!! see sorting.py
# 3. How to sort a Python dict by value (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs

sorted(xs.items(), key=lambda x: x[1])
## [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

sorted(xs, key=lambda x: x[1])  # IndexError: string index out of range
#! because
[x for x in xs]  # only keys/indices

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

#%% Most frequent
"""
This method returns the most frequent element that appears in a list.
"""
numbers = [1,2,1,2,3,2,1,4,2]
numbers.count(1)
numbers.count(4)

max(numbers, key=numbers.count)
max(*numbers, key=numbers.count)

set(numbers)
max(set(numbers), key=numbers.count)

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

#%% older method

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}

c = a.copy()
c.update(b)    #!!! in-place
c

c = a.copy()
d = c.update(b)    #!!! in-place
d                  #!!! None
c

def merge_dicts(a, b):
    c = a.copy()   # make a copy of a
    c.update(b)    # modify keys and values of a with the ones from b
    return c

d = merge_dicts(a, b)
d
#%%
