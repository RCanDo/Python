# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:25:55 2019

@author: staar
"""

#%%

s = 0
try:
    for k in [1, 2, '3']:
        s += k
finally:
    print(s)

#%%

s = 0
for k in [1, 2, '3', 4, '5', 6]:
    try:
        print("add {}".format(k))
        s += k
    except Exception as e:
        print('cannot add a string "{}"'.format(k))
    finally:
        print(s)


#%%