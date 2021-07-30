# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:30:53 2019

@author: kasprark
"""
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
dir(mo)
mo.group()
mo.groups()

dir(phoneNumRegex)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
dir(mo)
mo.group()
mo.group(0)
mo.group(1)
mo.group(2)
mo.groups()
mo.groups()[0]

#%%

import os

cd D:\ROBOCZY\Python\help\RegExp
ls 

pth = os.getcwd()

reg = re.compile(r'^.+help')
m1 = reg.search(pth)
m1.group()

pth1 = reg.sub(".", pth)
pth1
