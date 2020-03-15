#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:34:22 2020

@author: arek
"""

#%%
import re

ll = ['ab', 'cde', '10pqr', 'qq', '34rq', '235344', 'adgf544']

for ss in ll: print(re.search('^[a-z]+', ss))

list(filter(lambda ss: re.search('^[a-z]+', ss), ll))

#%%
