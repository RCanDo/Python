#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: 30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
subtitle:
version: 1.0
type: code snippets
keywords: [Python]
description: code snippets
sources:
    - title: 30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
      link: https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
      date: 2019-09-13
      authors:
          - fullname: Fatos Morina
            www: https://www.fatosmorina.com/
      usage: copy
file:
    usage:
        interactive: True
        terminal: False
    name: tips02.py
    path: D:/ROBOCZY/Python/help/
    date: 2019-09-13
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%% 17. Chained function call
"""
You can call multiple functions inside a single line.
"""
import operator as op

a, b = 1, 2
(op.subtract if a>b else op.add)(a, b)

#%% user defined operators (functions in general!)
def op1(x, y): return 1/x + y
def op2(x, y): return x + 1/y

(op1 if a>b else op2)(a, b)


#%% 1. All unique
"""
The following method checks whether the given list has duplicate elements.
It uses the property of set() which removes duplicate elements from the list.
"""
def all_unique(lst):
    return len(lst) == len(set(lst))

x = [3, 2, 1]
y = x*2

all_unique(x)
all_unique(y)

list(set(y))
# order not preserved...

#%%
#? How to make unique() which preserves order?
def unique(ll):
    order = list(map(lambda x: ll.index(x), ll))
    print(order)  # for check
    lst = []
    s = -1
    for k in order:
        if k > s:
            # smaller idx in `order` never appears for the first time after bigger idx
            s = k
            lst.append(ll[k])
    return lst

ll = [1, 4, 4, 2, 6, 0, 4, 0, 3, 1, 3]
unique(ll)

from numpy.random import randint
ll = list(randint(0, 9, 20))
ll
unique(ll)

#%% 2. Anagrams
"""
This method can be used to CHECK IF two strings are anagrams.
An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters
exactly once.
"""

from collections import Counter

Counter("aabbbcddeeee")
Counter([1, 2, 1, 3, 2, 4, 3, 2, 1])

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb")
anagram("abcd3", "3acd")

#%% 3. Memory
"""
This snippet can be used to check the memory usage of an object.
"""

import sys
variable = 30
sys.getsizeof(variable) # 28

#%% 4. Byte size
"""
This method returns the length of a string in bytes.
"""
def byte_size(string):
    return(len(string.encode('utf-8')))

byte_size('Hello world!')  # 11
byte_size('😀')  # 4

#%% 5. Print a string N times without using loop

print("string"*2)

#%% 6. Capitalize first letters of every word

print("what the hell...!".title())

#%% 13. Decapitalize
"""
This method can be used to turn the first letter of the given string into lowercase.
"""
def decapitalize(ss):
    return ss[:1].lower() + ss[1:]

decapitalize('FooBar')

'FooBar'.lower()  # not the same!
'Foo Bar'.lower()
'Foo BAR'.lower()

#%% 11. Comma-separated
hobbies = ["basketball", "football", "swimming"]
print("My hobbies are:")
print(", ".join(hobbies))

#%% 12. Count vowels

import re

def count_vowels(ss):
    return len(re.findall(r'[aeiouy]', ss, re.IGNORECASE))

count_vowels('foobar')
count_vowels('gym')

#%% 7. Chunks a list into smaller lists of a specified size.

def chunk(lst, step):
    return [lst[i:i+step] for i in range(0, len(lst), step)]

lst = list("abcdefghijklmnopqrst")
lst
chunk(lst, 3)

#%% 8. Compact
"""
This method removes falsy values (False, None, 0 and “”) from a list
by using filter().
"""

lst = [0, 1, False, 2, '', 3, 'a', 's', 34, None, True]
lst
list(filter(bool, lst))

#%% 9. Transpose
"""
This snippet can be used to transpose a 2D array.
"""

arr = [['a', 'b'], ['c', 'd'], ['e', 'f']]
list(zip(*arr))  #!!!
[list(k) for k in zip(*arr)]

tuple(zip(*arr))

list(map(list, zip(*arr)))

#%%
# we want
{1:10, 2:20, 3:30}   # and so on...

dict(zip([1, 2], [10, 20]))
dict(zip([1, 2, 3], [10, 20, 30]))
dict(zip((1, 2), (10, 20)))
dict(zip((1, 2, 3), (10, 20, 30)))  # (*)

# but we have data like:  (1, 10), (2, 20), (3, 30), ...
dict(zip((1,10), (2,20), (3, 30)))  #! ValueError: dictionary update sequence element #0 has length 3; 2 is required
dict((1,10), (2,20), (3, 30))   #! TypeError: dict expected at most 1 arguments, got 3

# SOLUTION(s):
dict(((1,10), (2,20), (3, 30)))    # (!!!)   #!!! WOW !!!
dict([(1,10), (2,20), (3, 30)])    # (!!!)   #!!! WOW !!!
dict(([1,10], [2,20], [3, 30]))    # (!!!)   #!!! WOW !!!
dict([[1,10], [2,20], [3, 30]])    # (!!!)   #!!! WOW !!!


# See the story below:

#
list(zip((1,10), (2,20), (3, 30)))
[k for k in zip((1,10), (2,20), (3, 30))]
#> [(1, 2, 3), (10, 20, 30)]

#!!! BUT !!!
(k for k in zip((1,10), (2,20), (3, 30)))
#> <generator object <genexpr> at 0x00000164800086C8>
#
# so the above is the same as
dict(((1, 2, 3), (10, 20, 30)))  #! ValueError: dictionary update sequence element #0 has length 3; 2 is required

# we must transform our sequence to the form (*)
dict(zip(*list(zip((1,10), (2,20), (3, 30)))))   # good!

# what is the same as
dict(zip(*zip((1,10), (2,20), (3, 30))))

#!!! BUT as we see in (!!!)  zip(*zip(...)) is the same as (...)

dict(((1,10), (2,20), (3, 30)))

#!!! INCREDIBLE !!!

#%% the same with map()

def fun(x):
    return x, 10*x

dict(map(fun, [1, 2, 3]))
dict(map(fun, range(10)))

import numpy as np
def fun2(x):
    return x, np.log2(x)

dict(map(fun2, range(10)))

dict(map(lambda x: (x, np.log(x)), range(10)))
dict(map(lambda x: np.log(x), range(10)))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

#%% 10. Chained comparison
"""
You can do multiple comparisons with all kinds of operators in a single line.
"""
a=3
2 < a < 8
1 == a < 8

#%% 28. Flatten
"""
This method flattens a list similarly like [].concat(…arr) in JavaScript.
Notice that only ONE level is flattened:
"""
def flatten(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

flatten([1, 2, 3, [4, [5, 6]], [7], 8, 9]) # [1, 2, 3, 4, [5, 6], 7, 8, 9]


#%% 14. Flatten deep
"""
The following methods flatten a potentially deep list using recursion.
"""

def deep_flatten(lst):
    flat = []
    for l in lst:
        if isinstance(l, list):
            flat.extend(deep_flatten(l))
        else:
            flat.append(l)
    return flat

deep_flatten([1, [2], [[3], 4], 5])

# is it full functional i.e. stateless? rather yes! `flat` is only local

#%% 15. Difference
"""
This method finds the difference between two iterables
by keeping only the values that are in the first one.
"""

def difference(a, b):
    return list(set(a).difference(set(b)))

difference([1,2,3], [1,2,4]) # [3]

#%% 16. Difference by
"""
The following method returns the difference between two lists
after applying a given function to each element of both lists.
"""
def difference_by(a, b, fun):
    fun_b = set(map(fun, b))
    return [item for item in a if fun(item) not in fun_b]

from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]


#%% 19. Merge two dictionaries

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}

c = a.copy()
c.update(b)    # in-place!!!
c

c = a.copy()
d = c.update(b)    # in-place!!!
d                  # None!!!
c

def merge_dicts(a, b):
    c = a.copy()   # make a copy of a
    c.update(b)    # modify keys and values of a with the ones from b
    return c

d = merge_dicts(a, b)
d

# In Python 3.5 and above, you can also do it like the following:

{**a, **b}
c = {**a, **b}
c

#%% 20. Convert two lists into a dictionary

keys = ["a", "b", "c"]
values = [2, 3, 4]
dict(zip(keys, values))  # {'a': 2, 'c': 4, 'b': 3}

#%% 21. Use enumerate

lst = list('abcdefgh')
for i, l in enumerate(lst):
    print(i, l)

#%% 22. Time spent
"""
This snippet can be used to calculate the time it takes to execute
a particular code.
"""
import time
start_time = time.time()
a=1
b=2
c=a+b
print(c)
end_time = time.time()
total_time = end_time - start_time

print("Time: ", total_time)

#%% %timeit -- IPython magic command
import numpy as np
arr = np.arange(1000)
%timeit arr**3
# 2.73 µs ± 53.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

arr = range(1000)
%timeit [i**3 for i in arr]
# 326 µs ± 11.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#%% 23. Try else

try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("No exceptions were raised")

#%% 24. Most frequent
"""
This method returns the most frequent element that appears in a list.
"""
numbers = [1,2,1,2,3,2,1,4,2]
max(numbers, key=numbers.count)
max(*numbers, key=numbers.count)
max(set(numbers), key=numbers.count)

#%% 25. Palindrome

def palindrome(a):
    return a == a[::-1]

palindrome('mom')
palindrome('mama')
palindrome('kobylamamalybok')

#%% 26. Calculator without if-else
"""
The following snippet shows how you can write a simple calculator
without the need to use if-else conditions.
"""

import operator as op
do = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, '^':op.pow}

do['^'](2, 3)
do['/'](2, 3)

#%% 27. Shuffle
"""
This snippet can be used to randomize the order of the elements in a list.
Note that shuffle works in place, and returns None.
"""

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
foo

#%% 29. Swap values
"""
A really quick way for swapping two variables
without having to use an additional one.
"""
a, b = 1, 2
b, a = a, b

a
b

#%% 30. Get default value for missing keys
"""
This snippet shows how you can get a default value in case
a key you are looking for is not included in the dictionary.
"""
d = {'a': 1, 'b': 2}
d['c']        # KeyError
d.get('c')    # None
d.get('c', 3) # 3
