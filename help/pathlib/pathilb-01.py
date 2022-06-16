#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 08:08:24 2022

@author: arek
"""
#%%
import os
import pathlib as pl

#%%

# create file
pl.Path('abc').touch()

pl.Path('abc').is_dir()  # False  ok
os.path.exists('abc')    # True   ??

# now, when the file 'abc' exists you cannot create a FOLDER with this name:

pl.Path('abc').mkdir(exist_ok=True)     # FileExistsError: [Errno 17] File exists: 'abc'
os.makedirs('abc', exist_ok=True)       # FileExistsError: [Errno 17] File exists: 'abc'

#!!! THIS IS BUG !!!

#%%
pl.Path('pqr/').mkdir(exist_ok=True)
pl.Path('pqr/xyz/').mkdir(exist_ok=True)

#%%
if __name__ == "__main__":
    #print(os.path(__file__))  ???
    pass
