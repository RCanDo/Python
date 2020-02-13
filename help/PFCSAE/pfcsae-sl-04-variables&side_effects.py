# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec  8 10:58:27 2017


4. Variables
============
"""

#%%

'''
In Python, variables are references (or names) to objects.
This is why in the following example, a and b represent the
same list: a and b are two different references to the same
object:
'''

a = [1,3,5,6,9]
a
b = a
b
b[0]
b[0] = 0
b
a      ## a = b  !!!

a == b
a is b

'''
Two objects a and b are the same object if they live in the
same place in memory.
• Python provides the id function that returns the identity
of an object. (It is the memory address.)
• We check with id(a) == id(b) or a is b wether a and b
are the same object.
• Two different objects can have the same value. We check
with ==
'''

a = 1
b = 1.0

a == b    ## true
a is b    ## false

id(a);
id(b)


#%%

'''
5. Side effects
===============

If we carry out some activity A, and this has an
(unexpected) effect on something else, we speak about
side effects. Example:
'''

def mysum(xs):
    s = 0
    for i in range(len(xs)):
        s += xs.pop()
    return s

xs = [10,20,30]
print("xs = {};   ".format(xs), end='')
print("mysum(xs) = {};   ".format(mysum(xs)), end='')
print("xs = {};   ".format(xs), end='')

## xs is empty now; this is side effect of mysum()

#%%
xs = [10,20,30]

## obviously it's better to

## use builtin function
sum(xs)

## do not use .pop()

def mysum(xs):
    s = 0
    for k in range(len(xs)):
        s += xs[k]
    return s

mysum(xs)
xs

## or simply

def mysum(xs):
    s = 0
    for k in xs:
        s += k
    return s

mysum(xs)
xs

'''
* A function that returns the control flow through the return keyword, will return the object given after return.
* A function that does not use the return keyword, returns the special object  None.
* Generally, functions should return a value
* Generally, functions should not print anything
* Calling functions from the prompt can cause some confusion here:
  if the function returns a value and the value is not assigned, it will be printed.
'''


