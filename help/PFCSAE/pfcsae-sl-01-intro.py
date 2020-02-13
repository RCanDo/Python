# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Tue Dec  5 12:42:41 2017


1. Intro
========
"""
#%%

dir()
%reset

#%%

print("qq")

## notice ta difference
"qq"
print("qq")

#%%
## Calculator

type(2)
print(type(2))
2+3
print(2+3)
type(2+3)
print(type(2+3))

## print() returns more then bare command through IPython console

42 - 15.3
type(42-15.3)
100*11
type(100*11)
2400/20
type(2400/20)   ## float
100/11
type(100/11)
100//11
type(100//11)
100 % 11
type(100 % 11)

2**3            ## power
type(2**3)

2**-2
type(2**-2)
9**.5
type(9**.5)

#%%

a=10
a
print(a)

b=20
b
type(a)
type(b)

a+b
b/a
type(b/a)
a/b
type(a/b)

## integer division in Python 3
b//a

## Notice that in Python 2
## integer division always returned integers (as in C, Fortran, Java, SQL, etc.)
## and you had to do things like this
1.0/2 ## to obtain float .5 (not 0)
## This is no longer the case in Python 3.

b**a
type(b**a)
b**-a
type(b**-a)

#%%

c = 1 + 1j
c
print(c)
type(c)

c**2
abs(c)

d = complex(-1,1)
d
print(d)

d.conjugate()
d.imag
d.real
d.__doc__
print(d.__doc__)

d.__abs__()
abs(d)

"""
Basic commands
==============
"""
#%%

print(c)
type(c)
print(type(c))
help(c)
dir(d)

help("abs")
help(abs)       ## ok

#%%
## text

word = "text"
word
print(word)
type(word)

word + "\nnext line"
word += "\nnext line"
word
print(word)

dir(word)
print(word.upper())

word.capitalize()
word.endswith('ne')
word.endswith('ee')

#%%
## Functions

def mysum(a,b):
    '''
    Sum of a and b.
    By ak.
    '''
    return a+b

mysum(1,2)
print("The sum of 3 and 4 is:",mysum(3,4))   ##
print("The sum of 3 and 4 is:",mysum(3,4),sep="")   ## default sep=" "

help(mysum)

#%%
## Function returning None

def nonefun(a,b):
    '''
    Sum of a and b.
    By ak.
    '''
    c = a+b
    ## no return ...

nonefun(1,2)
type(nonefun(1,2))

z = nonefun(1,2)
type(z)

#%%
## print() and return() is not the same

def fprint(a):
    print(2*a)

def fret(a):
    return(2*a)

z = fprint(2)
z               ## nothing i.e. None
type(z)

z = fret(2)
z
type(z)

#%%
## default arguments & interactive use

def myfun(a=1,b=1):
    '''
    Takes 2 numbers and adds them
    By AK.
    '''
    a0 = input("input a: ")
    b0 = input("input b: ")

    if a0=='': a0=a
    else: a0 = int(a0)

    if b0=='': b0=b
    else: b0 = int(b0)

    res=a0+b0
    print(res)      ## not necessary...
    return(res)     ## Absolutely necessary!!!

myfun()         ## try it putting values on demand and/or not putting
myfun(0,0)

#%%
## math module

import math as m

m.sqrt(4)
m.sqrt(1+1j)  ## ooops! :( very pity!!!

m.pi
m.e

dir(m)
help(m.acosh)
help(m.exp)

m.exp(1j)     ## doesn't work on complex... PITY!!! :(
m.exp(m.exp(2))


#%%
'''
Logicals & conditions
=====================
'''
...
#%%
'''
if ... else ...
---------------
'''
...
##
