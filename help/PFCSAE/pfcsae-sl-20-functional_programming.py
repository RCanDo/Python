# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec 15 17:32:51 2017

20. Higher Order Functions 2: Functional tools
==============================================
"""
## •

#%%
'''
* So far, have processed lists by iterating through them using for-loop
* perceived to be conceptually simple (by most learners) but
* not as compact as possible and not always as fast as possible
* Alternatives:
    - list comprehension
    - `map`, `filter`, `reduce`, often used with `lambda`
'''

#%%
'''
`lambda`: _anonymous_ function (_function literal_)
Useful to define a small helper function that is only needed once
'''

lambda a: a  ## there's no use of it...

lambda a: 2*a  ## "

## but

(lambda a: 2*a)(10)  ## this has some sense
(lambda x: x**x)(10)
(lambda x, y: x**y)(3,4)
(lambda x, y, z: x*y**z)(3,4,5)

type(lambda x: x)

#%% better example

from scipy.integrate import quad

## defined function
def fun(x):
    return x**2

y, abserr = quad(fun, a=0, b=2)

print("Int f(x)=x^2 from 0 to 2 = {:f} +- {:g}".format(y, abserr))

## anonymous (lambda) function

y, abserr = quad(lambda x: x**2, a=0, b=2)

print("Int f(x)=x^2 from 0 to 2 = {:f} +- {:g}".format(y, abserr))

#%%
'''
* map(function, iterable) -> iterable: apply function to all elements in iterable
* filter(function, iterable) -> iterable: return items of iterable for which function(item) is true.
* reduce(function, iterable, initial) -> value: apply function(x,y) from left to right to reduce iterable to a
  single value.
Note that sequences are __iterables__.
'''

map(lambda x: x**2 , [0, 1, 2, 3, 4] )         ## this is iterable
list(map(lambda x: x**2 , [0, 1, 2, 3, 4] ))   ## convert to list

list(map(lambda x: x**2 , range(5) ))   ## works too

## the same by list comprehension
[x**2 for x in range(5)]

#%%
import math as m
list(map(m.exp, [0, .1, 1.]))

#%% map

news = '''Python programming occasionally
more fun then expected'''

news.split()
"".join(news.split())
"_".join(news.split())
"\n".join(news.split())
print("\n".join(news.split()))

## but we want only first 3 letters of each word
slug = "-".join(map(lambda w: w[0:3], news.split()))
print(slug)

## via list comprehension
slug2 = "-".join( [w[0:3] for w in news.split()] )
print(slug2)

#%% filter

string = "The quick brown fox jumps over the lazy dog"

filter( lambda s: len(s)>4, string.split() )    ## iterable

list(map( lambda s: len(s)>4, string.split() ))
list(filter( lambda s: len(s)>4, string.split() ))

[s for s in string.split() if len(s)>4]

#%%
list(filter(lambda n: n>0, range(-3,4)))
list(filter(lambda n: n>0, [-3, -2, -1, 0, 1, 2, 3]))
[n for n in range(-3,4) if n>0]

## functions returning boolean are called "predicates"
## define predicate directly

def is_positive(n): return n>0

is_positive(5)
is_positive(-1)

list(map(is_positive, range(-3,4)))
list(filter(is_positive, range(-3,4)))
[n for n in range(-3,4) if is_positive(n)]

#%%
'''
Reduce

functools.reduce( fun , iterable , initial ) -> value

applies fun(x,y) (binary operator x ~ y) from left to right to reduce iterable to a single value
'''

from functools import reduce

def fun(x,y):
    print("Called with x={}, y={}".format(x, y))
    return x+y

reduce(fun, [1, 2, 5], 0)

reduce(fun, [1, 2, 5], 10)

reduce(fun, "test", "")    ## string as list
reduce(fun, ["q","Q","ry","kiu"] )
reduce(fun, ["q","Q","ry","kiu"] , "HEY!")

reduce(lambda x, y: x*y, range(1,10))
reduce(lambda x, y: x*y, range(1,10), -1)

#%%
'''
Operator Module contains functions which are typically
accessed not by name, but via some symbols or special syntax.
* For example 3 + 4 is equivalent to
'''
import operator as o

o.add(3, 4)

reduce(o.add, range(10))
## the same (BUT FASTER!) as
reduce(lambda x,y: x+y, range(10))

'''
Functions like `map`, `reduce` and `filter` are found in just about any lanugage supporting functional programming.
* provide functional abstraction for commonly written loops
* Use those (and/or `list comprehension`) instead of writing loops, because
    - Writing loops by hand is quite tedious and error-prone.
    - The functional version is often clearer to read.
    - The functional version can result in faster code
      (if you can avoid `lambda` !!!)

Hint: if you need to use a `lambda` in a `map`, you are probably better off using `list comprehension`.
'''

#%% alternatives

res = []

for x in range(5): res.append(x**2)
print(res)

[x**2 for x in range(5)]

list(map(lambda x: x**2, range(5)))

#%%
'''
Returning function objects
'''

def make_add42():
    def add42(x):
        return x+42
    return add42

add42 = make_add42()
add42   ## function

print(add42(2))

#%%
'''
A CLOSURE is a function with bound variables.
We often create closures by calling a function that returns a (specialised) function.
For example (closure_adder.py):
'''

def make_adder(y):
    def adder(x):
        return x+y
    return adder

add42 = make_adder(42)
add42

add42(2)
add42(3.1415)






