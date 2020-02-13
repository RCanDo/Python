# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec 22 12:29:34 2017

25. ODEs - Ordinary Differencial Equations
==========================================
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

import importlib ## may come in handy

import pylab as pl
import scipy as sp
## importlib.reload(sp)
import numpy as np

#%%
'''
1. 1st order ODE
----------------

Aim: solve dy/dt = f(y; t)

* get access to “odeint”:
  `from scipy.integrate import odeint`
* `odeint()` has the following input and output parameters:

   `ys = odeint(f, y0, ts)`

   Input:

       - `f` is function f(y, t) that returns the right-hand side
       - `y0` is the initial value of the solution at time `t0`
       - `ts` is a numpy array containing times `ti` for which we would like to know the solution `y(ti)`
       - the first value in the array has to be `t0` (with y(t0) = y0)

   Output:

       - `ys` is the numpy array that contains the solution
'''

#%%
## Example 1
ts = np.arange(0, 2.1, 0.1)
ts
ts.shape

## btw. compare with
 np.linspace(0, 2.1, 100)
##

y0 = 17
ys = sp.integrate.odeint( lambda y, t: -2*y, y0, ts)
ys
type(ys)

#%%
pl.plot(ts, ys, 'x', label='$dy/dt=f(y,t), y_0=17$')
pl.grid()
pl.xlabel('t')
pl.ylabel('y')
pl.legend('top right')
pl.savefig('odeint_ex1.pdf')
pl.show()

#%%
'''
Analytical solution is  $y(t) = C\exp{-2t}$ where $C=y(0)$
'''

tt = np.arange(0, 2.1, .02)
pl.plot(tt, y0*np.exp(-2*tt), 'b', label='analytical, $y_0=17$')
pl.legend()

ys2 = sp.integrate.odeint( lambda y, t: -2*y, 13, ts)

pl.plot(ts, ys2, '.g', label='$dy/dt=f(y,t), y_0=13$' )
pl.plot(tt, 13*np.exp(-2*tt), 'g', label='analytical, $y_0=13$')
pl.legend()


#%%
## Example 2

def ode2(y,t):
    return -.01*y + np.sin(10 * np.pi * t)

ts = np.arange(0, 2.01, .01)
y0 = -2

ys = sp.integrate.odeint( ode2, y0, ts)
ys
ys.shape

#%%

pl.plot(ts, ys, label='ode2 solution')
pl.xlabel('t')
pl.ylabel('y(t)')
pl.grid()
pl.legend('top left')
pl.savefig('odeint_ex2.pdf')
pl.show()

#%%
'''
2. 2nd Order ODEs: Harmonic Oscillator (HO)
-------------------------------------------

Any second order ODE can be re-written as two coupled first order ODE

Example: Harmonic Oscillator (HO)

* Differential equation
  $d^2 r/dt^2 = -\omega^2 r$ or short $r′′ = -\omega^2 r$
* Introduce $v = r′$
* rewrite equation as two first order equations
$$
$r′′ = -\omega^2 r
 \rightarrow
v′ = -\omega^2 r,
r′ = v
$$
* General strategy:
    - convert higher order ODE into a set of (coupled) first order ODE
    - use computer to solve set of 1st order ODEs
* $y = (r, v)$  thus  $dy/dt = f(y, t) = (dr/dt, dv/dt) = (r', t')$
* `odeint` returns a vector `y` for every time step i.e. a matrix,
from which one need to extract results for r and v
(rows are time, first column is r, second column is v)
'''

def oscharm(y, t):      ## rhs takes array y

    omega = 1
    r, v = y[0], y[1]   ## v and r from array y

    ## ode relations
    drdt, dvdt = v, -omega**2 * r

    return np.array([drdt, dvdt])


ts = np.arange(0, 20, .1)
r0, v0 = 1, 0
y0 = np.array([r0, v0])

ys = sp.integrate.odeint( oscharm, y0, ts)

r, v = ys[:, 0], ys[:, 1]

ys.shape

#%%
pl.plot(ts, r, 'b', label='$r(t)$')
pl.plot(ts, v, 'g', label='$v(t)$')
pl.xlabel('t')
pl.ylabel('y(t)')
pl.grid()
pl.legend()
pl.show()

#%%
'''
### Strategy:
• transform one 2nd order ODE into 2 (coupled) first order ODEs
• solve both first order ODEs simultaneously
• nothing conceptually complicated
• but need to use matrices (“arrays”) in Python to shuffle the data around.
• Warning: the meaning of y; x depends on context:
  often x = t and y = x. It helps to write down equations before coding them.
• Use example on previous slides as guidance.
'''

#%%
'''
3. Coupled ODEs: Predator-Prey problem
--------------------------------------
...

'''

def predprey(y, t):     ## t is not used
    b = .7      ## prey Birth rate
    c = .007    ## predator-prey Collision rate
    d = 1       ## predator Death rate

    p1, p2 = y[0], y[1]     ## nr of preys, predators

    ## odes relation
    dp1dt = b*p1 - c*p1*p2
    dp2dt = c*p1*p2 - d*p2

    return np.array([dp1dt, dp2dt])

p0 = np.array([70, 50])
ts = np.arange(0, 30, .1)

sol = sp.integrate.odeint( predprey, p0, ts )

#%%

p1, p2 = sol[:, 0], sol[:, 1]
pl.plot(ts, p1, 'g', label='prey')
pl.plot(ts, p2, 'r', label='predator')
pl.grid()
pl.xlabel('t'); pl.ylabel('y(t)')
pl.legend()
pl.show()

#%%
'''
Do it in a functional way to have easy access to parameters
'''

def predprey_fun(b=.7, c=.007, d=1):

    def predprey(y, t=0):       ## t is not used
        p1, p2 = y[0], y[1]
        ## ode ralations
        dp1dt = b*p1 - c*p1*p2
        dp2dt = c*p1*p2 - d*p2
        return np.array([dp1dt, dp2dt])

    return predprey

## plotting function
def plotak(ts, sol):
    p1, p2 = sol[:, 0], sol[:, 1]
    pl.plot(ts, p1, 'g', label='prey')
    pl.plot(ts, p2, 'r', label='predator')
    pl.grid()
    pl.xlabel('t'); pl.ylabel('y(t)')
    pl.legend()
    pl.show()
    return None


#%%

predprey = predprey_fun()
type(predprey)

predprey(np.array([70, 50]))

predprey_fun(.8, .009, .99)(np.array([70, 50]))

#%%

ts.shape

## the same parameters as above
sol = sp.integrate.odeint( predprey_fun(), np.array([70, 50]), ts )
plotak(ts, sol)


#%%

ts = np.arange(0,500,1)
sol = sp.integrate.odeint( predprey_fun(.2, .001, .8), np.array([10,50]), ts )
plotak(ts, sol)

#%%
'''
...
'''



