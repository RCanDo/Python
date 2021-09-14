# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:34:49 2021

@author: staar
"""

#%%
from functools import reduce
from operator import mul

def factorial_x(N):
    assert isinstance(N, int) and N >= 1
    return reduce(mul, range(1, N+1), 1)

t0 = time.time()
res = factorial_x(1000)
print(time.time() - t0)
#%%
data = [int(d) for d in list(str(res).strip('0'))]
data

#%%
import matplotlib.pyplot as plt
plt.plot(data[:300])

#%%
# check if this sequence is random !

#%%