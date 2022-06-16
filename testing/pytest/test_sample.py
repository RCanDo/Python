#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:23:26 2022

@author: arek

https://docs.pytest.org/en/7.1.x/getting-started.html#getstarted
"""
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
