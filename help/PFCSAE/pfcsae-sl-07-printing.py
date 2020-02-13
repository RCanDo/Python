# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Tue Dec 12 13:52:36 2017

7. Printing
=============
"""

print("qq")
print("qq","ryq",42)

print("qq",end='');  print('ryq')

#%%

import math as m
p = m.pi

"%f" % p    # format p as float (%f)
"%d" % p    # format p as integer (%d)
"%e" % p    # exponential
"%g" % p    # short

"the value of pi is approximately %f" % p
"the value of pi is approximately %f but my prefferred number is %d" % (p, 13) ## cannot ommit () !!!

"pi=%f and 3*pi=%f is approx %d" % (p, 3*p, 3*p)

'%f' % 3.14         # default width and precision
'%10f' % 3.14       # 10 characters long

'%10.2f' % 3.14     # 10 long, 2 post-dec digits

'%.2f' % 3.14       # 2 post-decimal digits
'%.14f' % 3.14      # 14 post-decimal digits

print("%10s" % "apple"); print("%10s" % "banana")

#%%
AU = 149597870700 # astronomical unit [m]
"%f" % AU   ## floating point
"%e" % AU   ## exponential
"%g" % AU   ## shorter
"%d" % AU   ## integer
"%s" % AU   ## str()
"%r" % AU   ## repr()

#%%
print("My pi = %.3f." % p)
print("a=%d b=%d" % (10, 20))

#%%
## New style string formatting (format method) Python3
"{} needs {} pints".format('Peter', 4)
"{0} needs {1} pints".format('Peter',4)
"{1} needs {0} pints".format('Peter',4)

"{name} needs {number} pints".format(name='Peter',number=4)

## Formatting behaviour of %f can be achieved through {:f}, (same for %d, %e, etc)
"Pi is approx {:f}.".format(p)
"Pi is approx {:d}.".format(p)   ## ValueError: Unknown format code 'd' for object of type 'float'
"Pi is approx {:e}.".format(p)

## Width and post decimal digits can be specified as before:
"Pi is approx {:6.2f}.".format(p)
"Pi is approx {:.2f}.".format(p)

"Pi is approx {:6.2f}.".format(2)
"Pi is approx {:6}.".format(2)

## rounding float to integer
"{:d}".format(10.)      ## ValueError: Unknown format code 'd' for object of type 'float'
"{:2.0f}".format(10.)   ## this is solution
"{:.0f}".format(10.)
## the value preceding . is unnecessary :
"{:2.0f}".format(10.9)
"{:.0f}".format(10.9)
"{:1.0f}".format(1000.9)
"{:.0f}".format(1000.9)

## notice that %d works for floats in old style formatting
print("%d" % 10.4)


#%%

a = 3.1415926535
a.__str__()
str(a)

b = [3, 4.2, ['apple', 'banana'], (0, 1)]

str(b)
print(b)
"%s" % b
"{}".format(b)

#%%
'''
* The repr function should convert a given object into an as accurate as possible string representation
* The str function, in contrast, aims to return an “informal” representation of the object that is useful to humans.
* The repr function will generally provide a more detailed string than str.
* Applying repr to the object x will attempt to call   x.__repr__().
'''

import datetime
t = datetime.datetime.now()     ## current date and time
str(t)
repr(t)

#%%
## eval & repr
x = 1
eval('x+1')

s = "[10, 20, 30]"
type(s)
eval(s)

type(eval(s))

i = 42
type(i)

repr(i)
type(repr(i))
eval(repr(i))
type(eval(repr(i)))

import datetime as dt
t = dt.datetime.now()
t_as_string = repr(t)
t_as_string
t2 = eval(t_as_string)
t2
type(t2)
t == t2
t is t2


#%%
pi = 3.1415926535; e = 2.718281828

"{:f}, {:f}".format(pi, e)
"%s, %s" % (pi, e)
ss = "%s, %s" % (pi, e)
ss

agent_number = 2
log_date_time = "2019-02-25"
filename = "car-agent%s_%s.log" % (agent_number, log_date_time)
filename

"a".rjust(4, "_")
"a".ljust(4, "_")
"a".center(4, "_")
