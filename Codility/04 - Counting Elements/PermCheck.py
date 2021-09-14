#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: PermCheck
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    A non-empty array A consisting of N integers is given.
    A permutation is a sequence containing each element from 1 to N once, and only once.
    For example, array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
    is a permutation, but array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
    is not a permutation, because value 2 is missing.
    The goal is to check whether array A is a permutation.
    Write a function `def solution(A)` that, given an array A,
    returns 1 if array A is a permutation and 0 if it is not.
    For example, given array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
    the function should return 1.
    Given array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
    the function should return 0.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [1..1,000,000,000].
remarks:
    - easy
sources:
    - title: PermCheck (Codility excericise)
      link: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: PermCheck.py
    path: .../ROBOCZY/Python/Codility
    date: 2021-09-06
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp@int.pl
"""

#%%
# 100% in Codility
def solution(A: list) -> int:

    A = sorted(A)

    if A[-1] < len(A) or A[0] > 1:
        return 0

    for k in range(len(A) - 1):
        if A[k] + 1 != A[k+1]:
            return 0
    else:
        return 1


#%%
import numpy as np

solution([1])
solution(np.random.choice(range(1, 11), 10, replace=False))
solution(np.random.choice(range(1, 101), 100, replace=False))


#%%