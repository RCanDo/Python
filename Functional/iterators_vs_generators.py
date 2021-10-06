#! python3
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: What is the difference between iterators and generators?
subtitle:
version: 1.0
type: examples and explanations
keywords: [iterators, generators, yield]
description: Examples and explanations for the question in title.
sources:
    - link: https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
      usage: examples and explanations
      remark: READ IT!!
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: iterators_vs_generators.py
    path: D:/ROBOCZY/Python/help/
    date: 2019-07-13
    authors:
        - nick: RCanDo
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""

#%% 1.
#%%
"""
`iterator` is a more general concept:
any object whose class has a `next` method (`__next__` in Python 3)
and an `__iter__` method that does return `self`.

Every `generator` is an `iterator`, but not vice versa.
A generator __is built by__ calling a function that has one or more `yield` expressions
(`yield` statements, in Python 2.5 and earlier),
and is an object that meets the previous paragraph's definition of an iterator.

You may want to use a custom iterator, rather than a generator,
when you need a class with somewhat complex state-maintaining behavior,
or want to expose other methods besides `next` (and `__iter__` and `__init__`).
Most often, a _generator_ (sometimes, for sufficiently simple needs, a _generator expression_)
is sufficient, and it's simpler to code because _state maintenance_ (within reasonable limits)
is basically "done for you" by the frame getting suspended and resumed.
"""
#%%
"""
For example, a generator such as:
"""
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

dir(squares)        #!!! no __next__ nor __iter__ because this is a _generator function_  !!!
dir(squares(2, 5))  #!!! "__next__" and "__iter__"  !!!

generator = squares(2, 5)
dir(generator)  # "__next__" and "__iter__"

next(generator)
[k for k in generator]
next(generator)  # StopIteration
[k for k in generator]  # empty because `generator` is fully 'utilised'

[k for k in squares(2, 5)]  # generator here is recreated

"""
or the equivalent generator expression (genexp)
"""
generator = (i*i for i in range(2, 5))
dir(generator)  # "__next__" and "__iter__"

[k for k in generator]
next(generator)  # StopIteration
[k for k in generator]  # empty

#%% the simplest generator function:

def gen0():
    # generator function
    yield 1
    yield 2
    yield 4

dir(gen0)   # no __next__ nor __iter__ because this is a _generator function_
gen = gen0()
dir(gen)    # __next__ and __iter__  present :)
gen    # _generator_

next(gen)  # 1
next(gen)  # 2
next(gen)  # 4
next(gen)  # StopIteration

next(gen0())  # 1
next(gen0())  # always 1 because we recreate gen0 this way

[k for k in gen0()]  # but here it is created only once

gen = gen0()
[k for k in gen]
[k for k in gen]  # empty

#%% even easier way of creating iterators:

itr = iter([1, 3, 2, 5, 0])
dir(itr)    # __next__ and __iter__  present :)
next(itr)
next(itr)
[k for k in itr]
[k for k in itr]  # empty

#%% but
[k for k in iter([1, 2, 3])]
# is the same as
[k for k in [1, 2, 3]]

# So what is the non trivial example of using iter()?
# Only when we are forced to use next() directly. When?

#%% infinite generator
import random as rnd
def random_gen(seed=0):
    rnd.seed(seed)
    while True:      # infinite !!!  be carefull when using it !!!
        yield rnd.randint(0, 100)

rg = random_gen(0)
next(rg)

#  [k for k in rg]   !!! DANGER !!! infinite loop !!!

[r for (k, r) in zip(range(10), rg)]
[r for (k, r) in zip(range(100), rg)]

#
[r for (k, r) in zip(range(10), random_gen(2))]   # try it
[r for (k, r) in zip(range(10), random_gen(3))]


#%%
#%% iterative calculations
#%%

def sqrt_gen(number):
    res = 1
    while True:
        res = (res + number/res)/2
        yield res

sqrt = sqrt_gen(9)
next(sqrt)

[r for (k, r) in zip(range(10), sqrt_gen(2))]

#%%
#%% self-limiting iterative calculations

def sqrt_step(z, x0=1):
    # iteration step for square root of z
    xn = (x0 + z/x0)/2
    return xn

#%% using it in a loop
x = 1
for k in range(10):
    x = sqrt_step(2, x)
    print(x)

#%% or better with a natural 'delta' limit:
x = 1
delta = 1
while delta > 1e-10:
    xn = sqrt_step(2, x)
    delta = abs(xn - x)
    x = xn
    print(x)

#%% a generator for any such iteration step  together with 'delta' (accuracy) limit

def iter_fun(step, x=1, accuracy=1e-10):
    # step(x)   iteration step
    delta = 1
    while delta > accuracy:    # limiting condition
        xn = step(x)
        delta = abs(xn - x)
        x = xn
        yield x

#%% use it for sqrt_step
from functools import partial
sqrt2_step = partial(sqrt_step, 2)

sqrt2_gen = iter_fun(sqrt2_step, 1)
[k for k in sqrt2_gen]

#%% one-line
[k for k in iter_fun(partial(sqrt_step, 3))]
[k for k in iter_fun(partial(sqrt_step, 33))]
lst = [k for k in iter_fun(partial(sqrt_step, 33))]
lst[-1]**2


#%%
"""
would take more code to build an iterator:
"""

class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
    def __iter__(self): return self
    def __next__(self): # next in Python 2
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current
    """
    But, of course, with class Squares you could easily offer extra methods, e.g.
    """
    def current(self):
       return self.start
    """
    if you have any actual need for such extra functionality in your application.
    """

iterator = Squares(2, 5)

#%%
dir(iterator)    #
iterator.current()
next(iterator)
[k for k in iterator]
next(iterator)  # StopIteration


#%% 2.
#%%
"""
In summary: Iterators are objects that have an __iter__ and a __next__
(next in Python 2) method.
Generators provide an easy, built-in way to create instances of Iterators.
...
"""

#%%
#%% Examples

#%% 1. Group Adjacent Lists                                                       #!!! ???

group_adjacent = lambda a, p: zip(*([iter(a)] * p))
[k for k in group_adjacent(a, 3)]  # [(1, 2, 3), (4, 5, 6)]
list(group_adjacent(a, 3))         # "
list(group_adjacent(a, 2))         # [(1, 2), (3, 4), (5, 6)]
list(group_adjacent(a, 1))         # [(1,), (2,), (3,), (4,), (5,), (6,)]

#%% step by step
a = [1, 2, 3, 4, 5, 6]
itera = iter(a)
itera           # <list_iterator at 0x1968e308c70>

next(itera)     # 1
list(itera)     # [2, 3, 4, 5, 6]
next(itera)     #! StopIteration

pitera = [iter(a)] * 3
pitera
#  [<list_iterator at 0x1968e3087f0>,
#   <list_iterator at 0x1968e3087f0>,
#   <list_iterator at 0x1968e3087f0>]
# NOTICE exactly the same address -- all three are the same object !

#? What about:
pitera = iter(a) * 3
    #! TypeError: unsupported operand type(s) for *: 'list_iterator' and 'int'

#%%


