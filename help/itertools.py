python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Itertools
subtitle:
version: 1.0
type: tutorial
keywords: [itertools]
description: |
    Itertools library:
    chain()
    chain.from_iterable()
    islice()
    zip_longest()
    tee()
    starmap()
    count()
    cycle()
    repeat()
    dropwhile()
    takewhile()
    filter()
    filterfalse()
    compress()
    groupby()
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: itertools — Iterator Functions
      link: https://pymotw.com/3/itertools/index.html
    - title: Itertools
      link: https://docs.python.org/3.7/library/itertools.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: itertools.py
    path: .../Python/help
    date: 2021-09-15
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
import utils.ak as ak
import utils.builtin as bi

#%%
from itertools import *
from pprint import pprint

#%%
"""
Purpose: The itertools module includes a set of functions for working with sequence data sets.

The functions provided by itertools are inspired by similar features
of functional programming languages such as Clojure, Haskell, APL, and SML.
They are intended to be fast and use memory efficiently,
and also to be hooked together to express more complicated iteration-based algorithms.

Iterator-based code offers better memory consumption characteristics than code that uses lists.
Since data is not produced from the iterator until it is needed,
all of the data does not need to be stored in memory at the same time.
This “lazy” processing model can reduce swapping and other side-effects of large data sets,
improving performance.

In addition to the functions defined in itertools,
the examples in this section also rely on some of the built-in functions for iteration.
"""

#%% Merging and Splitting Iterators

# %%
accumulate
combinations
combinations_with_replacement
pairwise
permutations
product

# %%
prod = product(list("abc"), range(2), list("ABC"), [0, -1])
prod    # <itertools.product at 0x7f14f82a4080>

for k in prod:
    print(k)

for k in prod:
    ["/".join(map(str, p)) for p in prod]

#%%  chain()
"""
The chain() function takes several iterators as arguments and returns a single iterator
that produces the contents of all of the inputs as though they came from a single iterator.
"""

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
# 1 2 3 a b c

for i in chain(range(4), range(10, 20, 2)):
    print(i, end=' ')

"""
chain() makes it easy to process several sequences without constructing one large list.
If the iterables to be combined are not all known in advance, or need to be evaluated lazily,
chain.from_iterable() can be used to construct the chain instead.
"""
def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']

it = make_iterables_to_chain()
it  # <generator object make_iterables_to_chain at 0x7f33b41e0890>
list(it)    # [[1, 2, 3], ['a', 'b', 'c']]
next(it)    # ! StopIteration

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
# 1 2 3 a b c

#%%
def make_iterables_to_chain():
    yield range(4)
    yield range(10, 20, 2)

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')

#%%
#%%  zip_longest()

for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)
"""
As with the other functions in this module, the return value is an iterable object
that produces values one at a time.
(1, 'a')
(2, 'b')
(3, 'c')
zip() stops when the first input iterator is exhausted.
To process all of the inputs, even if the iterators produce different numbers of values,
use zip_longest().  !!!
"""
r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))                                              #!!!
"""
By default, zip_longest() substitutes None for any missing values.
Use the fillvalue argument to use a different substitute value.
"""

r1 = range(3)
r2 = range(2)

list(zip_longest(r1, r2, fillvalue=-1))

#%%  islice()
"""
The islice() function returns an  iterator  which returns selected items
from the input iterator, by index.
islice() takes the same arguments as the slice operator for lists:
    start, stop, and step.
The start and step arguments are optional.
"""

for i in islice(range(100), 5):
    print(i, end=' ')

list(islice(range(100), 5))

for i in islice(range(100), 5, 10):
    print(i, end=' ')

for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')

for i in islice(range(30), 0, 100, 10):
    print(i, end=' ')
# 0 10 20

#%%
lst = list('abhgfjkelopswy')
lst
next(lst)   # TypeError: 'list' object is not an iterator
next(iter(lst))   # 'a'
next(iter(lst))   # 'a'

next(islice(lst, 2))  # 'a'
next(islice(lst, 2, 4))  # 'h'
next(islice(lst, 2, 4, 1))  # 'h'

next(range(3))    #! TypeError: 'range' object is not an iterator
next(iter(range(3)))  # 0

#%% sth more useful
def get_primes():
    """Lazy implementation of Sieve of Eratosthenes
    """
    candidate = 2     ## do not start from 1 --- infinite loop happens --- see (*) below
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

for prime in islice(get_primes(), 10):  #!!!
    print(prime, end=" ")

# istead of
for _, prime in zip(range(10), get_primes()):  #!!!
    print(prime, end=" ")

"""
Notice that using enumerate() is awkward and dangerous:
"""
for _, prime in enumerate(get_primes()):  #!!!
    print(f"{_}: {prime}")
    if _ >= 9:             #!!! without this - INFINITE !!!
        break

#%%
for prime in islice(get_primes(), 4, 10, 2):  #!!!
    print(prime, end=" ")

# istead of...
for _, prime in zip(range(4, 10, 2), get_primes()):  #!!!
    print(prime, end=" ")
#!!! NO !!! WRONG !!!

for _, prime in zip(range(0, 10, 2), get_primes()):  #!!!
    if _ >= 0:
        print(prime, end=" ")
#!!! NO !!! WRONG !!!

for _, prime in zip(range(10), get_primes()):  #!!!
    if _ >= 4 and _ % 2 == 0:    #! TERRIBLE !
        print(prime, end=" ")
# the same problems with enumerate()

#%%
#%%  tee()
"""
The tee() function returns several independent iterators (defaults to 2)
based on a single original input.
"""

r = islice(count(), 5)
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))

"""
tee() has semantics similar to the Unix tee utility,
which repeats the values it reads from its input and writes them to a named file
and standard output.
The iterators returned by tee() can be used to feed the same set of data
into multiple algorithms to be processed in parallel.

!!!  The new iterators created by tee() share their input,   !!!
so the original iterator should not be used after the new ones are created.
"""

r = islice(count(), 5)
i1, i2 = tee(r)
r
i1
i2
# different place in memory  and  different id:
id(i1)
id(i2)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

print('i1:', list(i1))
print('i2:', list(i2))

""" !!!
If values are consumed from the original input, the new iterators will not produce those values.
BUT copies works independently of each other !!!
"""

r = islice(count(), 10)
i1, i2 = tee(r)
list(islice(i1, 4))  # [0, 1, 2, 3]
# list(r)
list(islice(i2, 8))  # [0, 1, 2, 3, 4, 5, 6, 7]
# but they influence original
list(r)  # [8, 9]

# %%
i1, i2 = tee(r, 2)  # the second argument means number of replicas, default is 2.

#%%
list(map(lambda x, y: (x, y), cycle(range(3)), chain( *tee(range(5), 2) ) ))
list(zip(cycle(range(3)), chain( *tee(range(5), 2) ) ) )
list(map(list, zip(cycle(range(3)), chain( *tee(range(5), 2) ) ) ))

#%%
#%% starmap()

# Where the mapping function to map() is called f(i1, i2), the mapping function passed to starmap() is called f(*i).

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))

# or

for i in starmap(lambda x, y: (x, y, x * y), zip(range(5), range(5, 10))):
    print('{} * {} = {}'.format(*i))

#%% the same via map()
def multiply(x, y):
    return (x, y, x * y)

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):         # r1, r2 must be passed as separate arguments
    print('{} * {} = {}'.format(*i))

#%% notice how map() works when iterators are not aligned
print('\nStopping:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print('{} * {} = {}'.format(*i))

#%%
#%% count()
"""
The count() function returns an iterator that produces consecutive integers, indefinitely.
The first number can be passed as an argument (the default is zero).
There is no upper bound argument (see the built-in range() for more control over the result set).
"""

# This example stops because the list argument is consumed.
for i in zip(count(1), ['a', 'b', 'c']):
    print(i)

# not that neat with range():
for i in zip(range(1, 4), ['a', 'b', 'c']):     # we need to provide `stop` to range(start, ...)
    print(i)


#%%
list(islice(count(), 2, 6))
# is the same as
list(range(2, 6))

#!!! BUT
list(count(2, ...))  #! DANGER!!! there is no `stop` argument for count() only `start` and `step`:

#%%
"""
The `start` and `step` arguments to count() can be any numerical values that can be added together.
!!! There is NO `stop` argument !!!
"""
import fractions

start = fractions.Fraction(1, 3)
step = fractions.Fraction(1, 3)
print(start)
print(step)
start + step
start > 1   # False

for i in count(start, step):  # potentially infinite !
    print(i)
    if i > 2:
        break     # endless without this !

for i in zip(count(start, step), list('abcdef')):
    print('{}: {}'.format(*i))

# In this example, the start point and steps are Fraction objects from the fraction module.
#  1/3: a
#  2/3: b
#  1: c
#  4/3: d
#  5/3: e
#  2: f

#%%  range() doesn't work here !!!
list(range(start, 4, step))
#! TypeError: 'Fraction' object cannot be interpreted as an integer


#%%
#%% cycle()
"""
The cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely.
Since it has to remember the entire contents of the input iterator, it may consume quite a bit of memory if the iterator is long.
"""
for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
#  (0, 'a')
#  (1, 'b')
#  (2, 'c')
#  (3, 'a')
#  (4, 'b')
#  (5, 'c')
#  (6, 'a')

#%% especially useful when length of iterator to recycle is not known
import numpy as np

v = np.random.randint(int(1e9))
v
for _, d in zip(range(22), cycle(list(str(v)))):
    print(d, end=" ")

#%% repeat()
"""
The repeat() function returns an iterator that produces the same value each time it is accessed.
The iterator returned by repeat() keeps returning data forever, unless the optional times argument is provided to limit it.
"""
for i in repeat('over-and-over', 5):
    print(i)

# repeats only ONE value! list() is NOT recycled but repeated as a whole:
for i in repeat([1, 2], 5):
    print(i)

#%%
for i in ['over-and-over'] * 5:
    print(i)

list(repeat('aqq', 5))
tuple(repeat('aqq', 5))
list(repeat(list('aqq'), 5))

# BUT repeat() returns ITERATOR !

rr = repeat('aqq', 3)
next(rr)   # 'aqq'
next(rr)   # 'aqq'
next(rr)   # 'aqq'
next(rr)   # StopIteration


#%%
"""
It is useful to combine repeat() with zip() or map() when invariant values need to be included
with the values from the other iterators.
"""
for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)
#  0 over-and-over
#  1 over-and-over
#  2 over-and-over
#  3 over-and-over
#  4 over-and-over

#%%
"""
This example uses map() to multiply the numbers in the range 0 through 4 by 2.
The repeat() iterator does not need to be explicitly limited,
since map() stops processing when any of its inputs ends, and the range() returns only five elements.
"""
for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))
#  2 * 0 = 0
#  2 * 1 = 2
#  2 * 2 = 4
#  2 * 3 = 6
#  2 * 4 = 8

#%%
#%% Filtering

#%%  dropwhile()
"""
The dropwhile() function returns an iterator that
PRODUCES elements of the input iterator
AFTER a condition becomes __False for the first time__ !!!
"""

def should_drop(x):
    print(f'Testing - {x < 1}:', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

"""
dropwhile() does not filter every item of the input;
after the condition is False the first time, all of the remaining items in the input are returned.
"""
#  Testing - True: -1
#  Testing - True: 0
#  Testing - False: 1       #! the first is still NOT yielding !
#  Yielding: 1
#  Yielding: 2
#  Yielding: -2

#%%  takewhile()
"""
The opposite of dropwhile() is takewhile().
It returns an iterator that RETURNS items from the input iterator
AS LONG AS the test function returns true.
"""

def should_take(x):
    print(f'Testing - {x < 1}:', x)
    return x < 1

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

"""
As soon as should_take() returns False, takewhile() stops processing the input.
"""
#  Testing - True: -1
#  Yielding: -1
#  Testing - True: 0
#  Yielding: 0
#  Testing - False: 1   # not yielding

#%%  filter()
"""
The built-in function filter() returns an iterator that includes only items for which the test function returns true.
"""
def check_item(x):
    print(f'Testing - {x < 1}:', x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

""" !!!
filter() is different from dropwhile() and takewhile() in that every item is tested before it is returned.
"""

# Testing - True: -1
# Yielding: -1
# Testing - True: 0
# Yielding: 0
# Testing - False: 1
# Testing - False: 2
# Testing - True: -2
# Yielding: -2

#%%  filterfalse()
"""
filterfalse() returns an iterator that includes only items where the test function returns false.
"""
def check_item(x):
    print(f'Testing - {x < 1}:', x)
    return x < 1

for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

"""
The test expression in check_item() is the same, so the results in this example with filterfalse()
are the opposite of the results from the previous example.
"""
# Testing - True: -1
# Testing - True: 0
# Testing - False: 1
# Yielding: 1
# Testing - False: 2
# Yielding: 2
# Testing - True: -2

#%%  compress(data, selectors)  ==  lookup operator
"""
Return data elements corresponding to true selector elements.
!!!  Notice that `selector` is recycled to the lenght of `data`  !!!

compress() offers another way to filter the contents of an iterable.
Instead of calling a function, it uses the values in another iterable to indicate
when to accept a value and when to ignore it.

The first argument is the `data` iterable to process
and the second is a `selector` iterable producing Boolean values
indicating which elements to take from the data input
(a true value causes the value to be produced, a false value causes it to be ignored).
"""
every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):    # selector is recycled !
    print(i, end=' ')

# 3 6 9

some_pattern = [1, 0, 0, 1, 0, 1, 1, 0]
for i in compress(data, some_pattern):
    print(i, end=' ')
# 1 4 6 7


#%%
#%%  Grouping Data
"""
The groupby() function returns an iterator that produces sets of values organized by a common key.
This example illustrates grouping related values based on an attribute.
"""
import functools
from itertools import *
import operator as op
from pprint import pprint


@functools.total_ordering     # sutomatically adds remaining comparison methods infering them from provided methods (if any)
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)    # only first elements are compared !

    #!!! notice that __eq__ and __gt__ determines all other comparison methods

    def __getitem__(self, i: int):
        """to make Point subscriptable"""
        return {0: self.x, 1: self.y}[i]

#%%
pt = Point(3, 1)
pt
pt[0]
pt.x

#%% Create a dataset of Point instances

data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))

pprint(data, width=35)

#  [(0, 0),
#   (1, 1),
#   (2, 2),
#   (0, 3),
#   (1, 4),
#   (2, 5),
#   (0, 6)]
#%% the same as
list(map(Point, cycle(range(3)), range(7)))
list(starmap(Point, zip_longest(range(3), range(7))))    # no!  -- Nones appear

#%% Try to group the unsorted data based on X values

for k, g in groupby(data, op.attrgetter('x')):
    print(k, list(g))

#  Grouped, unsorted:
#  0 [(0, 0)]
#  1 [(1, 1)]
#  2 [(2, 2)]
#  0 [(0, 3)]
#  1 [(1, 4)]
#  2 [(2, 5)]
#  0 [(0, 6)]

# no effect

#%% Sort the data
data.sort()  # in-place !!!
print('Sorted:')
pprint(data, width=35)

#  [(0, 0),
#   (0, 3),
#   (0, 6),
#   (1, 1),
#   (1, 4),
#   (2, 2),
#   (2, 5)]

#%% Group the sorted data based on X values
#!!! The input sequence needs to be sorted on the key value !!!
#    in order for the groupings to work out as expected.

data.sort()  # in-place !!!
print('Grouped, sorted:')
for k, g in groupby(data, op.attrgetter('x')):
    print(k, list(g))

#  0 [(0, 0), (0, 3), (0, 6)]
#  1 [(1, 1), (1, 4)]
#  2 [(2, 2), (2, 5)]

#%% so:
data = list(map(Point, cycle(range(3)), range(7)))

for k, g in groupby(sorted(data), op.attrgetter('x')):
    print(k, list(g))

#%% or
data = list(map(Point, cycle(range(3)), chain(*tee(range(7), 2)) ))             #!!!

y_coord = op.attrgetter('y')

for k, g in groupby(sorted(data, key=y_coord), y_coord):
    print(k, list(g))

#%%
#%% Combining Inputs

#%% accumulate()
"""
The accumulate() function processes the input iterable,
passing the nth and n+1st item to a function and producing the return value instead of either input.
The default function used to combine the two values adds them,
so accumulate() can be used to produce the cumulative sum of a series of numerical inputs.
"""
list(accumulate(range(5)))  # [0, 1, 3, 6, 10]

list(accumulate('abcde'))   # ['a', 'ab', 'abc', 'abcd', 'abcde']

#%% It is possible to combine accumulate() with any other function
# that takes two input values to achieve different results.

def f(a, b):
    print(a, b)
    return b + a + b

list(accumulate('abcde', f))

#  a b
#  bab c
#  cbabc d
#  dcbabcd e
#  ['a', 'bab', 'cbabc', 'dcbabcd', 'edcbabcde']

#%%
"""
Nested for loops that iterate over multiple sequences can often be replaced with product(),
which produces a single iterable whose values are the Cartesian product of the set of input values.

The values produced by product() are tuples,
"""

FACE_CARDS = ('J', 'Q', 'K', 'A')
list(chain(range(2, 11), FACE_CARDS))
SUITS = ('H', 'D', 'C', 'S')

DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)
DECK

#%%
for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()

# 2H  2D  2C  2S
# 3H  3D  3C  3S
# 4H  4D  4C  4S
# 5H  5D  5C  5S
# 6H  6D  6C  6S
# 7H  7D  7C  7S
# 8H  8D  8C  8S
# 9H  9D  9C  9S
#10H 10D 10C 10S
# JH  JD  JC  JS
# QH  QD  QC  QS
# KH  KD  KC  KS
# AH  AD  AC  AS
#%%
"""
To change the order of the cards, change the order of the arguments to product().
"""
for card in product(SUITS, chain(range(2, 11), FACE_CARDS)):
    print('{:>2}{}'.format(card[1], card[0]), end=' ')
    if card[1] == FACE_CARDS[-1]:
        print()

# 2H  3H  4H  5H  6H  7H  8H  9H 10H  JH  QH  KH  AH
# 2D  3D  4D  5D  6D  7D  8D  9D 10D  JD  QD  KD  AD
# 2C  3C  4C  5C  6C  7C  8C  9C 10C  JC  QC  KC  AC
# 2S  3S  4S  5S  6S  7S  8S  9S 10S  JS  QS  KS  AS

#%%
"""
To compute the product of a sequence with itself, specify how many times the input should be repeated.
"""

list(product(range(3), repeat=2))
list(product(range(2), repeat=3))

#%%
"""
The permutations() function produces items from the input iterable combined in the possible permutations
of the given length.
It defaults to producing the full set of all permutations.
"""

list(permutations('abcd'))

#%%
def show(iterable):
    """ GOOD !!! """
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('All permutations:\n')
show(permutations('abcd'))

#%% Use the r argument to limit the length and number of the individual permutations returned.
print('\nPairs:\n')
show(permutations('abcd', r=2))
list(permutations('abcd', r=2))

show(permutations('abcd', r=3))

#%%
"""
To limit the values to unique combinations rather than permutations, use combinations().
As long as the members of the input are unique, the output will not include any repeated values.
Unlike with permutations, the r argument to combinations() is required.
"""
show(combinations('abcd', r=2))
#  ab ac ad
#  bc bd
#  cd

show(combinations('abcd', r=3))
#  abc abd acd
#  bcd

#%%
"""
While combinations() does not repeat individual input elements, sometimes it is useful
to consider combinations that do include repeated elements.
For those cases, use combinations_with_replacement().
"""
show(combinations_with_replacement('abcd', r=2))
#  aa ab ac ad
#  bb bc bd
#  cc cd
#  dd

show(combinations_with_replacement('abcd', r=3))
#  aaa aab aac aad abb abc abd acc acd add
#  bbb bbc bbd bcc bcd bdd
#  ccc ccd cdd
#  ddd

#%%
"""!!!
Notice though that itertools.combinations is very slow!
e.g. in comparison with numpy: see combinations.py in this folder.
About 100 times slower !!!
"""
