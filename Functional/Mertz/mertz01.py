#! python3
# -*- coding: utf-8 -*-
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: Avoiding Flow Controll; Callables
subtitle:
version: 1.0
type: examples and explanations
keywords: [flow control, recursion, lambda, map, reduce, filter, closure, yield, lazy evaluation]
description: |
remarks:
    - functools, operator
sources:
    - title: Functional Programming in Python
      chapter: Multiple Dispatch
      pages: 1-19
      link: "D:/bib/Python/Functional/Mertz - Functional Progrmming In Python (49).pdf"
      date: 2015-05-27
      authors:
          - fullname: David Mertz
      usage: examples and explanations
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: mertz01.py
    path: D:/ROBOCZY/Python/help/Functional/Mertz/
    date: 2019-07-10
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl
"""
#%%

cd E:/ROBOCZY/Python/Functional/Mertz
pwd
ls

#%%

import time

#%%

f = open('EnglishNotes.tex')
# you need to restart it frequntly (after every use of iterator)

for line in open('EnglishNotes.tex'): print(len(line), end="|")

gen_lines = (print(line) for line in open('EnglishNotes.tex') if len(line) < 50)
# this must be restarted too

for l in gen_lines: l

[l for l in gen_lines]

#%%

class GetLines():
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name)
        self.line = None
    def __iter__(self):
        return self
    def __next__(self):
        self.line = self.file.readline()
        while self.condition(self.line):
            self.line = self.file.readline()
        return self.line
    def condition(self, line):
        return len(line) < 30

#%%

get_lines = GetLines('EnglishNotes.tex')

for l in get_lines: print(len(l))  ## ooops! infinite!!!

#!!! Doesn't work !!!
#??? why ???

#%%
#%%
chr(65)
chr(90)

chr(97)
chr(122)

{i: chr(i+65) for i in range(6)}    # dict
{chr(i+65) for i in range(6)}       # set

{k: chr(k) for k in range(256)}    # dict

# the reverse is
ord('A')

#%%
""" RECURSION
"""

"""
Example of BAD recursion
where we still use state variables (mutables)
and the code is more messy then by using simple iteration
"""

def running_sum(numbers, start=0):
    if len(numbers) == 0:
        print()
        return
    total = numbers[0] + start
    print(total, end=" ")
    running_sum(numbers[1:], total)

running_sum([1, 5, 3, 6, 2, 4, 1])

# notice also that it returns Nothing what is really bad...  (easy to repair !)

#%% better --- without mutable
#   (but some problems with printing...)

def running_sum(numbers):
    if len(numbers) > 0:
        rs = numbers[-1] + running_sum(numbers[:-1])  # this mutable is NOT passed (good!)
        print(rs, end=" ")
        return rs
    else:
        print("\n")     # no use...
        return 0

running_sum([1, 5, 3, 6, 2, 4, 1])

#%%
"""
It prints FINALLY (i.e. recursion go to its end first)
and there is no way of printing "\n" ONLY at the beginning of recurssion...
which is printed LAST!!!
It is possible only if some state will be passed --- BAD RECURSION!...
"""

#%% FACTORIAL
#%% recursive

def factorial_r(N):
    """Recursive factorial function  -- good!"""
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N * factorial_r(N-1)

t0 = time.time()
print(factorial_r(1000))
print(time.time() - t0)

#%% iterative

def factorial_i(N):
    """Iterative factorial function -- week..."""
    assert isinstance(N, int) and N >= 1
    product = 1
    while N >= 1:
        product *= N
        N -= 1
    return product

t0 = time.time()
print(factorial_i(1000))
print(time.time() - t0)

#%%
"""
So recursive is more elegant but generally slower...
Moreover Python has default recurrence max depth set to 1000
(may be changed by `sys.setrecursionlimit()` but better not!)
"""

#%% best version

from functools import reduce
from operator import mul

def factorial_x(N):
    assert isinstance(N, int) and N >= 1
    return reduce(mul, range(1, N+1), 1)

t0 = time.time()
print(factorial_x(1000))
print(time.time() - t0)

## too fast to measure... :)

#%%
"""
Good example of using recursion is a "conquer and win" type of algorithm,
e.g. quick sort:
"""

def quicksort(lst):
    """Quicksort over a list-like sequence"""
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [l for l in lst if l == pivot]
    small = quicksort([l for l in lst if l < pivot])
    large = quicksort([l for l in lst if l > pivot])
    return small + pivots + large


import random
lst = [random.choice(range(100)) for _ in range(200)]
lst
#lst = [5, 7, 2, 9, 0, 1, 2, 4, 6]    # do it better!!!
quicksort(lst)

#%%
# The general scheme
#%%

#%% map()

def f1(x, y): return x + y

list(map(f1, [1], [2]))
list(map(f1, 1, 2))           #! TypeError: 'int' object is not iterable
list(map(f1, [1, 3], [2, 4]))
list(map(f1, [1, 3], [2]))

list(map(f1, ['a'], ['d']))
list(map(f1, 'a', 'd'))       #! OK  !!!  string is treated as a list of letters!  list('abc')
list(map(f1, ['a', 'b'], ['d', 'e']))
list(map(f1, ['a', 'b'], ['d']))
list(map(f1, 'ab', 'de'))
list(map(f1, ['ab'], ['de']))
list(map(f1, 'ab', 'd'))

#%%

do_it = lambda f, *args: f(*args)

do_it(f1, 1, 2)
do_it(f1, 'a', 'd')

do_it(f1, [1, 4], [2, 5])
do_it(f1, ['a', 'b'], ['d', 'e'])
do_it(f1, 'ab', 'de')

#%% e.g.
def f2(x, y): return x - y

do_it(f2, 1, 2)
do_it(f2, 1, 2, 3)  # ERROR

list(map(do_it, [f1, f2], [1, 2], [3, 4]))
list(map(do_it, [f1], [1, 2], [3, 4]))
list(map(do_it, [f1], [1], [3]))

list(map(do_it, [f1], [1], [2], [3]))  # TypeError: f1() takes 2 positional arguments but 3 were given

#%% function with arbitrary nr of arguments
def f3(*args):
    res = args[0]
    for k in args[1:]:
        res += k
    return res

#%%
list(map(f3, [1, 2]))
list(map(f3, [1, 2], [3, 4], [5, 6]))
list(map(f3, [1, 2], [3, 4], [5, 6], [7, 8]))
list(map(f3, [[1, 2]], [[3, 4]], [[5, 6]]))

#%%
do_it(f3, 1)
do_it(f3, 1, 2, 3)
do_it(f3, 1, 2, 3, 4)
do_it(f3, [1, 2], [3, 4], [5])

list(map(do_it, [f3], [1], [2]))
list(map(do_it, [f3], [1, 2], [2, 2]))
list(map(do_it, [f3]*2, [1, 2], [2, 2]))
list(map(do_it, [f3], [1, 2], [2, 2], [3, 4]))
list(map(do_it, [f3]*2, [1, 2], [2, 2], [3, 4]))
list(map(do_it, [f3], [1, 2, 3], [2, 2, 4], [3, 4]))
list(map(do_it, [f3], [[1, 2, 3]], [[2, 2, 4]], [[3, 4]]))

#%%
#%%
hello = lambda first, last: print("Hello", first, last)
bye = lambda first, last: print("Bye", first, last)

list(map(hello, 'AB', 'XY'))
_ = list(map(hello, 'AB', 'XY'))
_ = list(map(hello, ['AB'], ['XY']))

list(map(do_it, [hello, bye], ["A", "B"], ["X", "Y"]))
_ = list(map(do_it, [hello, bye], ["A", "B"], ["X", "Y"]))

#%%
do_all = lambda fs, *args: [list(map(f, *args)) for f in fs]

_ = do_all([hello, bye], ["A", "B"], ["X", "Y"])

#%%
#  functional version of WHILE
#
#%%

#%%
# by the way

x = 3
5 < x < y  ## works!!!
# although `y` is undefined!!!
# this is "short-circuit" version of boolean operation
# -- evalution halts as soon as the result is determined e.g. ...
(5 < x) and (x < y)
5 < x and x < y

#! BUT:
(5 < x) & (x < y)  #! NameError: name 'y' is not defined
# this is "eager" evaluation -- all expressions are evaluated before the operators' value
# never mind that the result is determined regardless of the second expressions value

#%%
# imperative version of echo

def echo_imp():
    while 1:
        x = input("IMP -- ")
        if x == 'quit':
            break
        else:
            print(x)

echo_imp()

#%%
# functional version of echo

def identity_print(x):
    print(x)
    return x

echo_fp = lambda: identity_print(input("FP -- "))=="quit" or echo_fp()
#!!! short circuit is applied here: "loop" halts as soon as the first operand is True  #!!!

echo_fp()
# btw: lambda always return sth. in this case True
_ = echo_fp()

#%%
def echo_fp(): identity_print(input("FP -- "))=="quit" or echo_fp()

echo_fp()

#%%
# Callables
#
#%%
def hello_d(name): print("Hello", name)

hello_d("Qrak")

hello_l = lambda name: print("Hello", name)

hello_l("Qrak")

hello_d.__qualname__
hello_l.__qualname__

hello_d
hello_l

hello_2 = hello_l
hello_2.__qualname__

hello_2.__qualname__ = "hello_2"
hello_2.__qualname__
hello_l.__qualname__

#%%
# function created via OO

class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        """
        makes class instance work as function
        """
        return self.n + m

add5_i = Adder(5)
add5_i(10)

#%%
"""
However the internal parameter (attribute) is mutable and may be freely changed
what may lead to mess
"""
add5_i.n = 10
# now it adds 10 instead of 5 (against name)
add5_i(10)

#%%
# function created functionally i.e. via function factory:

def make_adder(n):
    def adder(m):
        return m + n
    return adder

add5_f = make_adder(5)
add5_f(10)

#%%
"""
Python binds variables _by name_ rather then _by value_ what may cause confusion
"""
n = 10
add5_f(10)
# that's OK
# "internal" `n` is still 5

#%%
# BUT
adders = []

for n in range(5):
    # `n` is not an internal parameter of lambda function but is taken from envir
    adders.append(lambda m: m+n)

n

[adder(10) for adder in adders]

n = 10

[adder(10) for adder in adders]

# `n` value is taken from the envir
#%%                                                                            #!!!
"""
fortunately it has easy solution
"""
adders = []

for n in range(5):
    # `n` is not external variable any more but internal parameter (with set value)
    adders.append(lambda m, n=n: m+n)

n

[adder(10) for adder in adders]

n = 10
[adder(10) for adder in adders]

# that's OK

#%%
# Methods Of Classes
#
#%% Accessors And Operators

class Car(object):
    def __init__(self):
        self._speed = 100

    @property
    def speed(self):
        print("speed is ", self._speed)
        return self._speed

    @speed.setter
    def speed(self, value):
        print("Setting speed to: ", value)
        self._speed = value

#%%
car = Car()

car._speed
car.speed
car.speed()    #! TypeError: 'int' object is not callable !!!

car.speed = 80
car.speed

car.speed(70)  #! TypeError: 'int' object is not callable !!!

"""
Even _accessors_, whether created with the @property decorator or otherwise,
are technically _callables_,
albeit _accessors_ are _callables_ with a limited use
(from a functional programming perspective)
in that they take no arguments as getters,
and return no value as setters.
"""
#%%
class TalkativeInt(int):
    def __lshift__(self, other):
        print("Shift", self, "by", other)
        return int.__lshift__(self, other)

t = TalkativeInt(8)
t
t << 3

#%% Static Method Of Instances
"""
One use of classes and their methods that is more closely aligned with
a functional style of programming is to use them simply as namespaces to hold
a variety of related functions:
"""

import  math

class RightTriangle(object):
    """Class used solely as namespace for related functions
    """
    @staticmethod
    def hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)

    @staticmethod
    def sin(a, b):
        return a / RightTriangle.hypotenuse(a, b)

    @staticmethod
    def cos(a, b):
        return b / RightTriangle.hypotenuse(a, b)

#%%

RightTriangle.hypotenuse(3, 4)

rt = RightTriangle()
rt.sin(3, 4)
rt.cos(3, 4)

#%%
"""
from Python 3.x you don't need to use @staticmethod decorator --
it's possible to pull out from a class every functions
which is not a method (does not have `self` as [first] argument).
"""
import functools
import operator     # !!!!

dir(operator)

class Math(object):
    def product(*nums):
        return functools.reduce(operator.mul, nums)
    def power_chain(*nums):
        return functools.reduce(operator.pow, nums)

#%%
Math.product(3, 4, 5)

Math.power_chain(3, 4, 5)

#%%
"""
However it does not work on the instance as `self` is needed!
(if not used @staticmethod)
"""
m = Math()
m.product(3, 4, 5)

#%%
# !!! see  ../iterators_vs_generators.py
#
#%% Generator Functions - `yield`
#

def get_primes():
    """
    Lazy implementation of Sieve of Eratosthenes
    """
    candidate = 2     ## do not start from 1 --- infinite loop happens --- see (*) below
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

#%%

get_primes()

next(get_primes())
next(get_primes())
next(get_primes())

primes = get_primes()
next(primes), next(primes), next(primes)     #!#! DANGER !!!  (*)

for _, prime in zip(range(10), primes):
    print(prime, end=" ")

for _, prime in zip(range(10), get_primes()):  #!!!
    print(prime, end=" ")

# best:
from itertools import islice
for prime in islice(get_primes(), 10):  #!!!
    print(prime, end=" ")

# or e.g.
for prime in islice(get_primes(), 4, 20, 3):  #!!!
    print(prime, end=" ")

#%%
