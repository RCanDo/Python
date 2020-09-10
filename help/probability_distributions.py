#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Probability Distributions
subtitle:
version: 1.0
type: examples
keywords: [probability, distribution, density, CDF, PDF, random, ]
description: |
    How to work with probability distributions
remarks:
todo:
sources:
    - title: Python for Probability 
      link: http://web.stanford.edu/class/archive/cs/cs109/cs109.1192/handouts/pythonForProbability.html
      date: 2018
      usage: |
          not only copy
    - title: Statistics (scipy.stats)
      link: https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: probability_distributions.py
    path: D:/ROBOCZY/Python/help/
    date: 2020-09-04
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% #%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/help/")
print(os.getcwd())

#%% 
import math as m
from scipy import special 
from scipy import stats

#%% factorial
m.factorial(5)

for k in range(20):
    print("{}! = {}".format(str(k).rjust(2), m.factorial(k)))

#%% choose (n over k)
special.binom(3, 2)

print("Pascal triangle")
for n in range(7):
    print()
    print("{}: ".format(n), end="")
    for k in range(n+1):
        print(int(special.binom(n, k)), end="  ")

#%%
#%%
X = stats.binom(10, 0.2) # Declare X to be a binomial random variable
help(X)
X.pmf(3)           # P(X = 3)     probability Mass function
X.cdf(4)           # P(X <= 4)    cumulated distribution function
X.mean()           # E[X]
X.var()            # Var(X)
X.std()            # Std(X)
X.rvs()            # random sample from X
X.rvs(10)          # 10 random samples form X

X.kwds             # {}

#%%
Y = stats.poisson(2) # Declare Y to be a poisson random variable
Y.pmf(3)       # P(Y = 3)
Y.rvs()        # Get a random sample from Y
Y.mean()       # 2  ok

Y.kwds         # {} 

#%%
Z = stats.geom(.75)
Z.pmf(3)
Z.pdf(3)       #! AttributeError: 'geom_gen' object has no attribute 'pdf'     :(
Z.rvs()        # random sample from Z
Z.rvs(4)       # " of size 4 ->  array([2, 1, 1, 1])   

#%% continuous
"""!!!
All continuous distributions take `loc` and `scale` as keyword parameters 
to adjust the location and scale of the distribution, e.g., 
for the standard normal distribution, 
the `loc`ation is the _mean_ and the `scale` is the _standard deviation_.
"""
#%% Normal
"""!!! 
In literature the second parameter to a normal is the _variance_ (σ^2). 
In the `scipy` the second parameter is the _standard deviation_ (σ): 
"""
N = stats.norm(3, 2)
# is the same as
N = stats.norm(loc=3, scale=2)
N.mean()       # 3
N.std()        # 2
N.var()        # 4

N.pdf(0)       # f(0)             probability Density function  at 0
N.pmf(0)       #! AttributeError: 'norm_gen' object has no attribute 'pmf'
               #!!!   BUT it is displayed in dir(N)                            #!!!
N.cdf(0)       # F(0)             cumulated distribution function  at 0    
N.cdf(3)       # 1/2
N.rvs()        # radom sample
N.rvs(4)
N.rvs([4, 3])
N.rvs([4, 3, 2])
 
N.kwds         # {'loc': 3, 'scale': 2}

N.stats()                 # mean, variance  -- defaults
N.stats(moments='mv')     # mean, variance
N.stats(moments='mvk')    # mean, variance, kurtosis (?)
N.stats(moments='mvs')    # mean, variance, skew (?)
N.stats(moments='mvks')   # mean, variance, kurtosis, skew (?)
N.stats(moments='mvsk')   # mean, variance, skew, kurtosis (?)

#%%
N0 = stats.norm(scale=2)
N0.mean()      # 0
N0.std()       # 2
N0.var()       # 4

#%% Exponential
E = stats.expon(4)
E.mean()       # 5  !!! ???
E.support()    # (4, inf)
# cause we set up `loc` par not a `scale` 
E.std()        # 1

#%% Exp(lambda) -> E X = lambda 
#!!!  i.e. f(x) = exp(x / lambda) / lambda  
E = stats.expon(0, 2)
# the same as
E = stats.expon(scale=2)
E.support()    # (0, inf)
E.mean()       # 2        -- !!!
E.std()        # 2
E.var()        # 4

#%% moments via .stats() -- mean, variance, skew, kurtosis
E.stats()                 # mean, variance  -- defaults
E.stats(moments='m')      # mean, variance
                          # array(2.)
E.stats(moments='v')      # mean, variance
                          # array(4.)
E.stats(moments='mv')     # mean, variance
                          # (array(2.), array(4.))
E.stats(moments='vm')     # mean, variance
                          # (array(2.), array(4.))
#!!! YEAH!!! The same order of numbers !!!
# WTF!!!???
                          
E.stats(moments='mvk')    # mean, variance, kurtosis (?)
                          # (array(2.), array(4.), array(6.))
E.stats(moments='mvs')    # mean, variance, skew (?)
                          # (array(2.), array(4.), array(2.))
E.stats(moments='mvks')   # mean, variance, kurtosis, skew (?)
                          # (array(2.), array(4.), array(2.), array(6.))
E.stats(moments='mvsk')   # mean, variance, kurtosis, skew (?)
                          # (array(2.), array(4.), array(2.), array(6.))
#!!! YEAH!!! The same order of numbers !!!
# WTF!!!???

E.stats(moments='k')      # array(6.)
E.stats(moments='s')      # array(2.)
E.stats(moments='sk')     # (array(2.), array(6.))  -- skew, kurtosis
E.stats(moments='ks')     # (array(2.), array(6.))  -- skew, kurtosis -- the same order !!!

#%% Beta
B = stats.beta(1, 3)
B.kwds       # {}
B.support()  # 0, 1

B.mean()     #  .25
B.std()      # 0.1936
B.var()      # 0.0375

B.stats()                 # mean, variance  -- defaults
B.stats(moments='mv')     # mean, variance
B.stats(moments='mvk')    # mean, variance, kurtosis (?)
                          # (array(0.25), array(0.0375), array(0.0952381))  
B.stats(moments='mvs')    # mean, variance, skew (?)
                          # (array(0.25), array(0.0375), array(0.86066297)) 
B.stats(moments='mvks')   # mean, variance, skew, kurtosis (?)
                          # (array(2.), array(4.), array(2.), array(6.))
B.stats(moments='mvsk')   # mean, variance, kurtosis, skew (?)
                          # (array(2.), array(4.), array(2.), array(6.))
#!!! YEAH!!! The same order of numbers !!!
# WTF!!!???

stats.beta.numargs        # 2
stats.beta.shapes         # 'a, b'
                          # see below      

# do NOT do it on instances (only on generators as above)
B.numargs                 #! AttributeError: 'rv_frozen' object has no attribute 'numargs'         
B.shapes                  #! AttributeError: 'rv_frozen' object has no attribute 'shapes'
stats.beta           # scipy.stats._continuous_distns.beta_gen

#%%
#%% shape parameter                      
# https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html#shifting-and-scaling
"""Note
Distributions that take shape parameters may require more than simple application 
of `loc` and/or `scale` to achieve the desired form. 
For example, the distribution of 2-D vector lengths given a constant vector of length
perturbed by independent N(0, s^2) deviations in each component is 
`rice(R/s, scale=s)`. 
The first argument is a shape parameter that needs to be scaled along with `x`.
"""
#%%
# https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html#shape-parameters
"""
While a general continuous random variable can be shifted and scaled 
with the `loc` and `scale`, 
some distributions require additional `shape` parameters. 
For instance, the gamma distribution with density
    g(x, a) = l (lx)^(a-1) exp(-lx) / Gamma(a)
requires the shape parameter a.
Observe that setting `l` can be obtained by setting the `scale` keyword to `1/l`.

Let’s check the number and name of the `shape` parameters of the gamma distribution. 
(We know from the above that this should be 1.)
"""
stats.gamma.numargs    # 1
stats.gamma.shapes     # 'a'

#%%
G = stats.gamma()      #! TypeError: _parse_args() missing 1 required positional argument: 'a'
G = stats.gamma(1)
G = stats.gamma(a=1)
G.kwds                 # {'a': 1}
G.mean()               # 1
G.var()                # 1

G = stats.gamma(a=1, scale=2)
G.kwds                 # {'a': 1, 'scale': 2}
G.mean()               # 2
G.var()                # 4

#%%



#%%



#%%



#%%



#%%

