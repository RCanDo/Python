#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Distinct
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: [distinct values, list, array]
description: |
    Write a function `def solution(A)` that, given an array A consisting of N integers,
    returns the number of distinct values in array A.
    For example, given array A consisting of six elements such that:
     A[0] = 2    A[1] = 1    A[2] = 1
     A[3] = 2    A[4] = 3    A[5] = 1
    the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
remarks:
    - easy
    - assume that sorting algorithm is given (built-in sorted() in Python)
sources:
    - title: Distinct (Codility excericise)
      link: https://app.codility.com/programmers/lessons/6-sorting/distinct/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: Distinct.py
    path: .../ROBOCZY/Python/help/Codility
    date: 2021-09-06
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp@int.pl
"""

#%%
# 100% in Codility;  O(N*log(N)) or O(N)
def solution_0(A: list) -> int:
    return len(set(A))

#%%
# 100% in Codility;  O(N*log(N)) or O(N)
def solution(A: list) -> dict:
    if len(A) == 0:
        result = 0
    else:
        A = sorted(A)
        result = 1
        for i in range(1, len(A)):
            item = A[i]
            if item != A[i-1]:
                result += 1

    return result

#%%
solution_0([])
solution([])

solution_0([1])
solution([1])

#%%
import numpy as np
a = np.random.choice(range(7), size=10, replace=True)
a

solution_0(a)
solution(a)

#%%
a = np.random.choice(range(33), size=100, replace=True)
a

solution_0(a)
solution(a)

#%%



#%%


#%%
