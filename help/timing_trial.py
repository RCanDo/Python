#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:23:46 2022

@author: arek
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def random_walk(n):

    l = [0]
    for k in range(int(n)):
        l.append( l[-1] + np.random.randn())

    print(len(l))

    plt.figure()
    plt.plot(l)

t0 = time.time()
random_walk(1e5)
t1 = time.time()

print(t1-t0)
