#! python3
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: Higher-Order Functions
subtitle:
version: 1.0
type: examples and explanations
keywords: [higher order function, map, filter, reduce, compose]
description: |
remarks:
    - functools, operator, toolz.functoolz
sources:   # there may be more sources
    - title: Functional Programming in Python
      chapter: Higher-Order Functions
      pages: 33-
      link: "D:/bib/Python/Functional/Mertz - Functional Progrmming In Python (49).pdf"
      date: 2015-05-27
      authors:
          - fullname: David Mertz
      usage: examples and explanations
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: mertz04.py
    path: D:/ROBOCZY/Python/Functional/Mertz/
    date: 2019-07-16
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl
"""
#%%

cd D://ROBOCZY/Python/Functional/Mertz
pwd
ls

#%% map + filter  vs  comprehension

def fun(x): return 2*x + 1

# classic FP style
list(map(fun, range(5)))

# comprehension
[fun(x) for x in range(5)]

# + filter (predicate)
def pred(x): return x % 2 == 0

filter(pred, range(10))
list(filter(pred, range(10)))
list(map(fun, filter(pred, range(10))))

[fun(x) for x in range(10) if pred(x)]


#%% reduce
import functools as ft
import operator  as op

ft.reduce(op.add, range(4), 0)

#%% some digression - ROLLBACK problem
#%% reduce has one extra value in that it performs kind of a ROLLBACK
s = 0
s = ft.reduce(op.add, [int(k) for k in '1234'], s)
s

#%%
s = 0
s = ft.reduce(op.add, [int(k) for k in '12x4'], s)
s
# notice that state of s is preserved -- kind of a ROLLBACK is done; it's rather good!
# the same for:
s = 0
s = ft.reduce(op.add, iter(int(k) for k in '12x4'), s)
s

#%% if you have some doubts in what moment the error is thrown
# (e.g. before any addition was done) this should dispell them
def add(a, b):
    return a + int(b)

s = 0
s = ft.reduce(add, list('12x4'), s)
s
# good !!!

#! On the problem of ROLLBACK see: D:/ROBOCZY/Python/help/context_manager-with/
# and
# https://stackoverflow.com/questions/28031210/best-way-to-roll-back-actions-when-an-exception-is-raised-with-python
# https://stackoverflow.com/questions/4752356/changes-inside-try-except-persist-after-exception-is-caught


#%%
#%% map ~= reduce

def add5(x): return x + 5

ft.reduce(lambda l, x: l + [add5(x)], range(10), [])
# the same as
list(map(add5, range(10)))

#%% filter ~= reduce

def isOdd(n): return n % 2   # -> {0, 1} ~= {False, True}

ft.reduce(lambda l, x: l + [x] if isOdd(x) else l, range(10), [])
# the same as
list(filter(isOdd, range(10)))

#%% Fibonacci by reduce

ft.reduce(lambda l, k: l + [l[-1] + l[-2]] , range(10), [1, 1])

#%% sequential set difference
omega = {(i, j) for i in range(5) for j in range(5)}
s1 = {(0, 1), (1, 0), (2, 3), (1, 4), (3, 0)}
s2 = {(1, 1), (0, 2), (1, 2), (2, 2)}

ft.reduce(lambda a, b: a - b, [s1, s2], omega)  # omega - s2 - s1
...

#%% Utility Higher-Order Functions
#%%

#%% compose()

def compose(*funcs):
    def inner(data):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner

times2 = lambda x: 2*x
minus3 = lambda x: x - 3
mod6 = lambda x: x%6

f = compose(mod6, times2, minus3)
all(f(i) == ((i-3)*2)%6 for i in range(100000))

#%% compose() by reduce -- no `for` loop -- better = purely functional !!!

def compose(*funcs):
    def inner(data):
        fx = lambda x, f: f(x)
        return ft.reduce(fx, reversed(funcs), data)
    return inner

f = compose(mod6, times2, minus3)
f(6)
all(f(i) == ((i-3)*2)%6 for i in range(100000))

#%%
import numpy as np

arr = np.array([[1, 2], [5, 0]])
arr

lambda mm, idx: mm[idx] = 0     #!#! SyntaxError: can't assign to lambda
    #!#! SO HOW TO MANIPULATE WITH MATRICES IN LAMBDA CALC ???
    # HOW TO LIVE WITHOUT STATEMENTS ???
lambda mm, idx: mm[idx] = 0; return mm     #!#! SyntaxError: can't assign to lambda


def sub(mm, idx, x=0): mm[idx] = x; return mm


def sub0_factory(mm, idxs):
    psub = ft.partial(sub, mm)
    return list(map(psub, idxs))

sub0_factory(arr, [0, 1])

# nonsense...


#%%
"""
It is nice to be able to ask whether any/all of a collection of predicates
hold for a particular data item in a composable way.
"""

all_pred = lambda item, *tests: all(p(item) for p in tests)
any_pred = lambda item, *tests: any(p(item) for p in tests)

is_lt100 = ft.partial(op.gt, 100)
is_lt100(20)

is_gt10 = ft.partial(op.lt, 10)
is_gt10(20)

from nums import is_prime  # cannot install nums...

is_odd = lambda x: x%2

all_pred(71, is_lt100, is_gt10, is_odd)

predicates = (is_lt100, is_gt10, is_odd)
all_pred(107, *predicates)
any_pred(107, *predicates)

#%% using map()

predicates = [is_lt100, is_gt10, is_odd]
predicates[0](71)


list(map(lambda p: p(71), predicates))
all(map(lambda p: p(71), predicates))
any(map(lambda p: p(71), predicates))

# by comprehension
[p(71) for p in predicates]


#%%
"""
The library toolz has what might be a more general version of this called juxt()
that creates a function that calls several functions with the same arguments
and returns a tuple of results.
We could use that, for example, to do:
"""
from toolz.functoolz import juxt

juxt([is_lt100, is_gt10, is_odd])(71)
all(juxt([is_lt100, is_gt10, is_odd])(71))

all(juxt([is_lt100, is_gt10, is_odd])(107))
any(juxt([is_lt100, is_gt10, is_odd])(107))

#%% the operator module
import operator as op

iterable = [1, 3, 2, 5, -10, 20]

# using lambda
ft.reduce(lambda a, b: a + b, iterable, 0)

# using operator
ft.reduce(op.add, iterable, 0)

# Pythonic way
sum(iterable)

dir(op)


#%% decorators from functools
#%% ...


