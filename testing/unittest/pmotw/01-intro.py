#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
title: PMOTW - unittest
subtitle: Automated Testing Framework
version: 1.0
type: tutorial
keywords: [unittest, ...]
description: |
remarks:
todo:
    -
sources:
    - title: unittest - Automated Testing Framework
      link: https://pymotw.com/3/unittest/index.html
file:
    date: 2023-12-31
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
"""
Python’s unittest module is based on the XUnit framework design by Kent Beck and Erich Gamma.
The same pattern is repeated in many other languages, including C, Perl, Java, and Smalltalk.
The framework implemented by unittest supports
- fixtures,
- test suites,
- test runner
to enable automated testing.

Basic Test Structure

Tests, as defined by unittest, have two parts: code to manage test dependencies (called fixtures), and the test itself.
Individual tests are created by subclassing TestCase and overriding or adding appropriate methods.
In the following example, the SimplisticTest has a single test() method, which would fail if a is ever different from b.
"""
import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)

"""
In console run (from this dir)
$ python3 -m unittest 01-intro.py
the output is

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

"""

# %%


