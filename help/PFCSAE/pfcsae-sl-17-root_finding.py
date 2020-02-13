# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 13 13:52:02 2017

16. Root finding
================
"""
## •

#%% bisection

'''
Bisection method
• Requires root in bracket [a; b]
• guaranteed to converge (for single roots)
• Library function: `scipy.optimize.bisect`
'''

def mybisect(a,b,f,tol=1e-10):
    '''
    finding root of f between a and b by bisection
    f(a)*f(b) < 0
    '''

    if a == b:
        raise ValueError("must be a!= b")
    elif a > b:
        x=a; a=b; b=x; del(x)
    else:
        pass

    if f(a)*f(b) > 0:
        raise ValueError("must be f(a)*f(b) < 0")
    else:
        x = (a + b)/2
        k = 0
        while abs(f(x)) > tol:
            k += 1
            print(k,end=", ")
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
            x = (a + b)/2
        print()
        return x


mybisect(-1,1,lambda x: x**3)
mybisect(-2,1,lambda x: x**3)
mybisect(-2,1,lambda x: x**3,tol=1e-16)

import math as m

mybisect(-2,1,m.sin)

#%%
from scipy.optimize import bisect

fun = lambda x: x**3 - 2*x**2
fun(1)

x = bisect(fun, a=1.5, b=3, xtol=1e-6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))


#%% Newton-Raphson
'''
Newton method
• Requires good initial guess x for root x0
• may never converge
• but if it does, it is quicker than the bisection method and better (more exact)
• Library function: `scipy.optimize.Newton`
'''

from scipy.optimize import newton

x = newton(fun, x0=1.6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))

#%%
## Related problems
'''
Given the function f(x), applications for root finding include:
• to find x1 so that f(x1) = y for a given y (this is equivalent to computing the inverse of the function f).
• to find crossing point xc of two functions f1(x) and f2(x)
  (by finding root of difference function g(x) = f1(x) - f2(x))
• Recommended method: `scipy.optimize.brentq` which combines
  the safe feature of the bisect method with the speed of the Newton method.
• For multi-dimensional functions f(x), use `scipy.optimize.fsolve`.
'''

#%%
## Using BrentQ algorithm from scipy

from scipy.optimize import brentq

x = brentq(fun, a=1.5, b=3, xtol=1e-6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))

#%%
## Using fsolve algorithm from scipy

from scipy.optimize import fsolve

x = fsolve(fun, x0=[1.6])
x

print("Root x is approx. x={:14.12g}.".format(x[0]))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x[0]))

#%%


