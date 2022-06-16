#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:53:10 2022

@author: arek

https://docs.pytest.org/en/7.1.x/getting-started.html#getstarted
"""

import pytest
import sys

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1      # this will not propagate to test_two()
        assert self.value == 1

    def test_two(self):
        assert self.value == 1  # thus this will fail as here  self.value == 0


if __name__ == "__main__":
    sys.exit(pytest.main())
