#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 11:55:55 2023

@author: arek
"""
# %%
"""
Test Outcomes

Tests have 3 possible outcomes, described in the table below.

Outcome 	Description
ok 	        The test passes.
FAIL 	    The test does not pass, and raises an AssertionError exception.
ERROR 	    The test raises any exception other than AssertionError.

There is no explicit way to cause a test to “pass”,
so a test’s status depends on the presence (or absence) of an exception.

"""
import unittest


class OutcomesTest(unittest.TestCase):

    def testPass(self):
        """ok"""
        return

    def testFail(self):
        """will FAIL -- raises an AssertionError"""
        self.assertFalse(True)

    def testError(self):
        """will ERROR -- raises exception other than AssertionError"""
        raise RuntimeError('Test error!')

    def testFail_msg(self):
        """
        To make it easier to understand the nature of a test failure, the fail*() and assert*() methods
        all accept an argument msg, which can be used to produce a more detailed error message.
        """
        self.assertFalse(True, "it's True while should be False")


class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)

"""
$ python3 -m unittest 02-outcomes.py

EFF...
======================================================================
ERROR: testError (02-outcomes.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arek/Roboczy/Python/testing/unittest/pmotw/02-outcomes.py", line 35, in testError
    raise RuntimeError('Test error!')
RuntimeError: Test error!

======================================================================
FAIL: testFail (02-outcomes.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arek/Roboczy/Python/testing/unittest/pmotw/02-outcomes.py", line 32, in testFail
    self.assertFalse(True)
AssertionError: True is not false

======================================================================
FAIL: testFail_msg (02-outcomes.OutcomesTest)
To make it easier to understand the nature of a test failure, the fail*() and assert*() methods
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arek/Roboczy/Python/testing/unittest/pmotw/02-outcomes.py", line 42, in testFail_msg
    self.assertFalse(True, 'failure message goes here')
AssertionError: True is not false : it's True while should be False

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=2, errors=1)


"""

# %%
""" for more use cases see the source page starting from
https://pymotw.com/3/unittest/index.html#testing-equality
"""