#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:23:55 2022

https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block

https://pymotw.com/3/contextlib/index.html#ignoring-exceptions

@author: arek
"""

from contextlib import suppress

with suppress(IDontLikeYouException, YouAreBeingMeanException):
     do_something()
