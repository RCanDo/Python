# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 21 08:46:06 2017

23. Numpy usage examples
========================
"""
## •

import time as t
import math as m
import numpy as np
#import matplotlib as mpl
import pylab as pl

'''
Bigger example
--------------
Comparing efficiency of m.exp and np.exp via some more complicated function, namly:
    Mexican hat wavelet = Ricker wavelet, the second Hermite function (wavelet)
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet
'''


#%%

def mexhat_m(t, sigma=1):
    """
    Mexican hat wavelet = Ricker wavelet, the second Hermite function (wavelet)
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet
    using math  m.exp
    """
    c = 2. / m.sqrt(3*sigma) * m.pi**(.25)
    t2 = t**2 / sigma**2
    return c * (1 - t2) * m.exp( -t2/2 )

#%%

def mexhat_np(t, sigma=1):
    """
    Mexican hat wavelet = Ricker wavelet, the second Hermite function (wavelet)
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet
    using numpy  np.exp
    """
    c = 2. / m.sqrt(3*sigma) * m.pi**(.25)
    t2 = t**2 / sigma**2
    return c * (1 - t2) * np.exp( -t2/2 )

#%%

def time_this(f):
    starttime = t.time()
    ys = f()
    stoptime = t.time()
    return { 'result' : ys ,
             'time_diff' : stoptime - starttime
           }

#%%

def compare(f1,f2):
    """
    Comparing results of both fuctions
    """

    out1 = time_this(f1)
    ys1 = out1['result']
    t1 = out1['time_diff']

    out2 = time_this(f2)
    ys2 = out2['result']
    t2 = out2['time_diff']

    tprop = t1/t2
    print("f2 is %.1f times faster then f1" % tprop)

    dev2 = (ys1-ys2)**2
    pl.plot(dev2)
    dev = m.sqrt( sum(dev2) )

    return tprop, dev


#%%

if __name__ == "__main__":
    main()




