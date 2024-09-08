#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:40:36 2024

@author: arek

https://docs.pytest.org/en/stable/getting-started.html#request-a-unique-temporary-directory-for-functional-tests
"""

def test_needsfiles(tmp_path):
    # print(tmp_path)
    tp = str(tmp_path)
    assert tp == 'temp_path'