#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:11:04 2025

@author: arek
"""

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('--aa', action="store_true", default=None)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
args = parser.parse_args() #['-a', '-bval', '-c', '3'])

print(args)
print(dir(args))
print(args.__dict__)
print(args.__dict__['a'])
print(args.__getattribute__('a'))
print(args.__dict__['aa'])
if args.__dict__['aa']:
    print('aa!')
else:
    print('~aa')
