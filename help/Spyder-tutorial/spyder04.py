# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:58:45 2017

@author: kasprark
"""

def demo(x):
    for i in range(5):
        print("i={}, x={}".format(i, x))
        x = x + 1

demo(0)

#%%

import pylab

## as is setup in Spyder
pylab.plot( range(10) , 'o' )

## change setup
%matplotlib qt

pylab.plot( range(10) , 'o' )

#%%
