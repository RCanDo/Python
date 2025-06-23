# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:30:53 2019

@author: kasprark
"""
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex           # re.compile(r'\d\d\d-\d\d\d-\d\d\d\d', re.UNICODE)
type(phoneNumRegex)     # re.Pattern
dir(phoneNumRegex)

mo = phoneNumRegex.search('My number is 415-555-4242.')
mo          # <re.Match object; span=(13, 25), match='415-555-4242'>
type(mo)    # re.Match
print('Phone number found: ' + mo.group())
dir(mo)
mo.group()
mo.groups()


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
mo.group()
mo.group(0)
mo.group(1)
mo.group(2)
mo.groups()
mo.groups()[0]

# %%
re0 = re.compile(r"\s+")
re0.sub(" ", "  ajnin   okmo om")   # ' ajnin okmo om'

#%%

import os

pth = os.getcwd()

reg = re.compile(r'^.+help')
m1 = reg.search(pth)
m1.group()
dir(m1)

pth1 = reg.sub(".", pth)
pth1
