#! python3
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: Lazy Evaluation
subtitle: On iterators and generators
version: 1.0
type: examples and explanations
keywords: [lazy evaluation, iterator, generator, iter, next]
description: |
remarks:
    - itertools, collections
sources:
    - title: Functional Programming in Python
      chapter: Lazy Evaluation
      pages: 25-32
      link: "D:/bib/Python/Functional/Mertz - Functional Progrmming In Python (49).pdf"
      date: 2015-05-27
      authors:
          - fullname: David Mertz
      usage: examples and explanations
    - link: https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
    - link: D:/ROBOCZY/Python/help/iterators_vs_generators.py
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: mertz03.py
    path: D:/ROBOCZY/Python/Functional/Mertz/
    date: 2019-07-14
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

#%%  Lazy evaluation --- iterators/generators
#%%

""" Before one should know a diff between iterators and generators
see: https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
or file ../../help/iterators_vs_generators.py

Every iterator has "__next__" and "__iter__" method.
Every generator is iterator but not vv.
generator function is created by `yield` (instead of `return`) in its body.
generator function returns generator object (see below).
generator [object] == iterator defined by generator function
                      (f. with keword `yield` instead of `return`)
This is just convienient way of creating iterators (objects) which however
may be defined directly, see examples below.
"""

#%% e.g. remind from previous sections

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

# Notice that this _generator function_ returns _infinite generator_ [object].

#%%
get_primes()

primes = get_primes()
primes
next(primes), next(primes), next(primes)     #!#! DANGER !!!  (*)

for n, p in zip(range(10), primes):
    print(p, end=" ")

primes[10]    # :(
len(primes)   # ...
next(primes)

#%% better lazy iterator (indexable)

from collections.abc import Sequence

class ExpandingSequence(Sequence):
    def __init__(self, it):
        self.it = it
        self._cache = []
    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]
    def __len__(self):
        return len(self._cache)

primes = ExpandingSequence(get_primes())

#%%

primes[1]
len(primes)
primes[4]
len(primes)

# print all first n primes
for _, p in zip(range(10), primes): print(p, end=" ")

len(primes)

primes[1000]
len(primes)

# more useful features may be added but it's quite a work
# while in e.g. Haskell iterables just got it all

#%%
#%% The Iterator Protocol
"""
What an `iterator` is is the object returned by a call to iter(something),
which itself has a method named .__iter__() that simply
returns the object itself, and another method named .__next__().
The reason the iterable itself still has an .__iter__() method is to make iter() idempotent.
That is, this identity should always hold (or raise TypeError("object is not iterable")):
"""

lazy = open("glowny.tex")
"__iter__" in dir(lazy)   # True
"__next__" in dir(lazy)   # True


plus1 = map(lambda x: x+1, range(10))
plus1
list(plus1)
list(plus1)   # empty!  this is stateful

"__iter__" in dir(plus1)   # True
"__next__" in dir(plus1)   # True

# again
plus1 = map(lambda x: x+1, range(10))
next(plus1)  # 1
next(plus1)  # 2
next(plus1)  # 3  ...

dir(plus1)
iter(plus1)

#%%
"""
_generator function_ return _generator object_
"generator" unqualified means "generator object"
see:
https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
or file ../../help/iterators_vs_generators.py
"""

def to10():
    """ generator function
    """
    for i in range(10):
        yield i

to10    # function NOT generator object
"__iter__" in dir(to10)
toten = to10()  # generator function  returns  generator object
toten           # generator object == iterator defined by generator function
                # (f. with kw `yield` instead of `return`)
"__iter__" in dir(toten)
"__next__" in dir(toten)
next(toten)
next(toten)
[k for k in toten]
next(toten)   # StopIteration

# but
[k for k in to10()]
[k for k in to10()]  # still the same -- this way we recreate generator each time

#%%

ll = [1, 3, 4, 7, 8]
ll
dir(ll)    # there is __iter__ but no __next__ --- thus it's not an iterator
next(ll)   # TypeError: 'list' object is not an iterator

"""
IT IS POSSIBLE TO MAKE ITERATOR FROM LIST!!!
"""
itll = iter(ll)
itll
dir(itll)  # there is __iter__ and __next__

next(itll)
next(itll)
[k for k in itll]
next(itll)  # StopIteration

#%%
""" iter() is idempotent
"""
itll == iter(ll)   # False...
itll == iter(itll)   # True...

itll = iter(ll)
itll == iter(ll)   # False...
itll is iter(ll)   # False
# so internal state does not matter here

[k for k in itll]
itll2 = iter(itll)
[k for k in itll2]
# so iter() does not rejuvenate an iterator

#%%

"""
In a functional programming style — or even just generally for readability —
writing custom `iterators` as `generator` functions is most natural.
However, we can also create custom classes that obey the protocol;
often these will have other behaviors (i.e., methods) as well,
but most such behaviors necessarily rely on statefulness and side effects to be meaningful.
For example:
"""

from collections.abc import Iterable

class Fibonacci(Iterable):
    def __init__(self):
        self.a = 0
        self.b = 1
        self._total = 1
        self._ratio = None
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self._total += self.b
        self._ratio = self.b / self.a
        return self.b
    def running_sum(self):
        return self._total
    def ratio(self):
        return self._ratio

fib = Fibonacci()

#%%

fib
fib.running_sum()
fib.ratio()
next(fib)
fib.running_sum()
fib.ratio()
next(fib)
fib.running_sum()
fib.ratio()

[k for _, k in zip(range(10), fib)]

for k in range(10):
    next(fib)
    print(fib.ratio())

fib = Fibonacci()

for k in range(20):
    next(fib)
    print(fib.ratio())

fib.running_sum()


#%% Module: Itertools
#%%
"""
Iterators are lazy sequences rather than realized collections, and when combined
with functions or recipes in itertools they retain this property.
Here is a quick example of combining a few things.
Rather than the _stateful_ Fibonacci class to let us keep a running sum,
we might simply create a single lazy iterator to generate both the current number
and this sum:
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

#%%

from itertools import tee, accumulate

s, t = tee(fibonacci())   # double fibonacci()
pairs = zip(t, accumulate(s))
for k, (f, ss) in zip(range(10), pairs):
    print(f, ss)

#%% how tee() works:  https://docs.python.org/3.5/library/itertools.html#itertools.tee
s, t = tee(fibonacci())
pairs = zip(s, t)
for k, (s, t) in zip(range(10), pairs):
    print(s, t)

#%%
s, t, u = tee(fibonacci(), 3)   # default 2 as above
triples = zip(s, t, u)
for k, (s, t, u) in zip(range(10), triples):
    print(s, t, u)

triples = zip(s, accumulate(t), accumulate(accumulate(u)))
for k, (s, t, u) in zip(range(10), triples):
    print(s, t, u)


#%%



