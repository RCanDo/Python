# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:01:16 2018

@author: akasprzy
"""


#%%
lis = list(map(int, input().split()))
lis

#%%
a,b,*c = [1,2,3,4,5]
print(a,b,c)

#%% Deleting all even
a = [1,2,3,4,5]
del a[1::2]
print(a)

#%% fast notes
list[:]  ## slice copy; see below
list.pop()

################
## set operators

## on sets  {}
| & -
a ^ b    ## symmetric diff. == no common elements

## on lists  []
and  or
## but there's no  A - B
##  and not   except   do not work

dict.keys() .values() .items()

#%% `==` vs `is`
#%%
a = 1
b = 1.0

a == b    ## true
a is b    ## false

id(a)
id(b)

c = a
id(c)
a is c   # True

#%% For lists:
d = [1, 2, 3]

f = d
f is d   #!!! True

e = d[:] #!!! slice copy                                                        #!!!
e == d   # True
e is d   #!!! False

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
b     # [7, 8, 9]
b is lst # False

lst[0] = 0
lst   # [0, 8, 9]

b     # [7, 8, 9]    -- (shallow) copy
b is lst # False

a     # [0, 8, 9]
a is lst # True

#%%
#%% finding elements
ll = [2, 4, 2, 2, 3, 4, 1, 5, 3]
ll.index(2)  # 0,  only first appearance is considered
ll.index(4)  # 1
ll.index(-1) #! ValueError: -1 is not in list; nothing to do with that;
             # should be `None`
help(ll.index)

#%% item getting
ll[1]

from operator import itemgetter
itemgetter(1)      # function
itemgetter(1)(ll)

getfirst = itemgetter(1)   # function
getfirst(ll)

# works on dicts too:
itemgetter('x')({'x':1, 'y':2})

#%%
#%%
ll = [['a', 'b'], ['c', 'd'], ['e', 'f', 'g']]
sum(ll, [])      # specifying start value for sum(); default is 0.
sum(ll, ['p'])

#%%
ll = [1, 4, 2, 1, 0]
ll.sort()
ll

ll = list('pghjskenga')
ll.sort()
ll

ll = [(1, 2), (0, 3), (2, 0)]
ll.sort()
ll

# how to sort with the second dim ?
import operator as op

ll = [(1, 2), (0, 3), (2, 0)]
ll.sort(key=op.itemgetter(1))
ll

# more in sorting.py; especially:
sorted([1, 4, 2, 1, 0])
sorted([(1, 2), (0, 3), (2, 0)], key=op.itemgetter(1))


#%% primes in a range (works but very suboptimal)
list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 13)))

#%% 9. Transpose
"""
This snippet can be used to transpose a 2D array.
"""
arr = [['a', 'b'], ['c', 'd'], ['e', 'f']]
list(zip(*arr))  #!!!
[list(k) for k in zip(*arr)]
list(map(list, zip(*arr)))

tuple(zip(*arr))

#%% 28. Flatten
"""
This method flattens a list similarly like [].concat(…arr) in JavaScript.
Notice that only ONE level is flattened:
"""
def flatten(lst):
    res = []
    for l in lst:
        if isinstance(l, list):
            res.extend(l)
        else:
            res.append(l)
    return res

flatten([1, 2, 3, [4, [5, 6]], [7], 8, 9])  # [1, 2, 3, 4, [5, 6], 7, 8, 9]


#%% 14. Flatten deep
#!!!
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

#%% 24. Most frequent
"""
This method returns the most frequent element that appears in a list.
"""
numbers = [1,2,1,2,3,2,1,4,2]
max(numbers, key=numbers.count)
max(*numbers, key=numbers.count)
max(set(numbers), key=numbers.count)

numbers.count(1)
numbers.count(2)
numbers.count(3)

#%%
max([(1, 2), (1, 3), (3, 1)], key=lambda x: x[1])
min([(1, 2), (1, 3), (3, 1)], key=lambda x: x[1])
sorted([(1, 2), (1, 3), (3, 1)], key=lambda x: x[1])
sorted([(1, 2), (1, 3), (3, 1)], key=lambda x: x[0]/x[1])

from operator import itemgetter
max([(1, 2), (1, 3), (3, 1)], key=itemgetter(1))

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

# list(set(y))
# order not preserved...

#%%
#??? How to make unique() which preserves order?
def unique(ll):
    order = list(map(lambda x: ll.index(x), ll))  # only first appearance of the item in the list    #!!!
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

#%%
#%% 7. Chunks a list into smaller lists of a specified size.

def chunk(lst, step):
    return [lst[i:i+step] for i in range(0, len(lst), step)]

lst = list("abcdefghijklmnopqrst")
lst
chunk(lst, 3)

#%% 8. removing nulls
"""
This method removes falsy values (False, None, 0 and “”) from a list
by using filter().
"""
lst = [0, 1, False, 2, '', 3, 'a', 's', 34, None, True]
lst
list(filter(bool, lst))

#%%
#%% 15. Difference
"""
This method finds the difference between two iterables
by keeping only the values that are in the first one.
"""
def difference(a, b):
    return list(set(a).difference(set(b)))

difference([1,2,3], [1,2,4]) # [3]

# BUT
difference([1,2,3, 3], [1,2,4]) # [3]    #... pity!

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

#%%
