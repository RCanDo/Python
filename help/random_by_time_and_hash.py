#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Random numbers by time and hashing function
subtitle:
version: 1.0
type: help, examples
keywords: [time, hashlib, ssh, random]
description: |
remarks:
todo:
    - do some statistical analysis: check uniformity of resulting distributions
sources:
    - title: Python Get Current time
      link: https://www.programiz.com/python-programming/datetime/current-time
    - title: hashlib module
      link: https://docs.python.org/3/library/hashlib.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: random_by_time_and_hash.py
    path: D:/ROBOCZY/Python/help/
    date: 2020-09-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando as ak
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/help/")
print(os.getcwd())

#%%
import numpy as np

#%% 1
import time

time.time()           # float
tt = time.time()
tt                    # costant

#%% 2. get really random numbers using time and hashig function
import hashlib
# https://docs.python.org/3/library/hashlib.html

seed = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
seed   # hexadecimal
seedint = int(seed, 16)   # decimal BUT:
# it's a very great number while
np.random.seed(seed)   # ValueError: Seed must be between 0 and 2**32 - 1
# hence we must lessen it anyhow, e.g.
np.random.seed( sum(int(n) for n in str(seedint)) )    # small seeds
# or
np.random.seed( np.abs(np.prod([int(n)+1 for n in str(seedint)])) )   # big seeds
# still to big
np.random.seed( np.prod([int(n)+1 for n in str(seedint)[:10]]) )   # big seeds
# or simpler
np.random.seed(int(seed[:10], 16))   # still too much
np.random.seed(int(seed[:8], 16))    # OK

#%%
import matplotlib.pyplot as plt

#%%
xx = np.empty(100)
for k in range(100):
    #time.sleep(.1)   # seconds -- probably ot necessary
    seed = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
    np.random.seed(int(seed[:8], 16))
    xx[k] = np.random.randint(-100, 100)

print(xx)
plt.plot(xx)

#%%
#%% without even  np.random -- radomisatio by  time & hash
# v1: yy -- one series
N = 100
xx = list(range(N))
yy = np.empty(N)
for k in range(N):
    #time.sleep(.1)   # seconds -- probably ot necessary
    seed = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
    yy[k] = xx[int(seed, 16) % N]

print(yy)
#plt.scatter(xx, yy, )
plt.hist(yy)

#%% NOTICE
"""
We are takig modulo N from very large numbers thus any departure
from a uniform distribution U[1, N]
should be neither visible nor even detectable
for any reasonable N, i.e. much smaller then  int(hash(time))).
"""

#%% v2:  xx, yy
N = 1000
zz = list(range(N))
xx = np.empty(N)
yy = np.empty(N)
for k in range(N):
    #time.sleep(.1)   # seconds -- probably ot necessary
    seed = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
    xx[k] = zz[int(seed, 16) % N]
    seed = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
    yy[k] = zz[int(seed, 16) % N]

print(xx)
plt.scatter(xx, yy, )

#%%
import hashlib, time
def htrandint(max=100):
    N = int(max)
    hashtime = hashlib.sha224(str(time.time()).encode('ascii')).hexdigest()
    return int(hashtime, 16) % N

#%%
htrandint(10)
htrandint(1e7)

#%%