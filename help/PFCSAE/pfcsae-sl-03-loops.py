# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec  8 09:27:17 2017


3. Loops
============
"""

#%%
'''
range() reminder
----------------
'''
## at the end of previous file we've seen

r = range(10)
type(r)

## in general 'range' is ITERATOR

## list and tuple from iterator
list(r)
tuple(r)

r = range(-3,3)
list(r)
tuple(r)
list(tuple(r))
tuple(list(r))

r = range(-3,3,2)   ## (start,stop,step)
list(r)

#%%
'''
for
---
'''

animals = ['dog','cat','mouse']

for animal in animals:
    print("This is the {}".format(animal))

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("the square for {} is {}".format(i, i**2))

## simpler?
for i in [k for k in range(10)]:
    print("the square for {} is {}".format(i, i**2))

## still simpler
for i in range(10):     ## !!!
    print("the square for {} is {}".format(i, i**2))

#%%
# you may iterate across strings

i = 0
for s in "qqryq na patyku":
    i += 1
    print("sign {} is {}".format(i,s))

i

#%%
## Fibonacci series
def fib(m):
    k0 = 0
    k1 = 1
    fibs = [k0,k1]
    for k in range(1,m+1):
        k = k0 + k1
        k0 = k1
        k1 = k
        print(k)
        fibs.append(k)
    return fibs

fib(10)

## simpler

def fib(m):
    fibs = [0,1]
    for k in range(1,m+1):
        fibs.append(fibs[k]+fibs[k-1])
        print(fibs[k+1])
    return fibs

fib(10)

#%%

def skip13(a,b):
    result = []
    for k in range(a,b):
        if k==13:
            pass            ## !!!
        else:
            result.append(k)
    return result

skip13(10,15)

#%%

def range_double(a,b,s=1):
    result = []
    for k in range(a,b,s):
        result.append(k*2)
    return result

range_double(0,10)

#%%
#    Write a First-In-First-Out queue implementation, with
#    functions:
#    • add(name) to add a customer with name name (call this
#    when a new customer arrives)
#    • next() to be called when the next customer will be
#    served. This function returns the name of the customer
#    • show() to print all names of customers that are currently
#    waiting
#    • length() to return the number of currently waiting
#    customers
#    Suggest to use a global variable q and define this in the first
#    line of the file by assigning an empty list: q = [].


#%%
'''
while
-----
'''

x = 64
while x > 10:
    x = x // 2
    print(x)

#%%
## determine epsilon

eps = 1.0
while 1 + eps > 1:
    eps = eps/2.0
    print("epsilon is {}".format(eps))

#%%
eps = 1.0
## notice a difference:
while 1 + eps > 1:
    eps = eps/2.0
print("epsilon is {}".format(eps))