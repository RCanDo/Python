#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Missing Integer
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    Write a function `def solution(A)` that, given an array A of N integers,
    returns the smallest positive integer (greater than 0) that does not occur in A.
    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
difficulty:
    - medium ? (rather easy)
sources:
    - title: Missing Integer (Codility excericise)
      link: https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: MissingInteger.py
    path: .../ROBOCZY/Python/Codility
    date: 2021-09-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp@int.pl
"""

#%%
# 100%; O(N) or O(N * log(N))
def solution(A: list) -> int:

    A = [v for v in A if v > 0]

    if len(A) == 0:
        return 1

    A = sorted(set(A))

    if A[0] != 1:
        return 1

    result = 0
    for k in range(len(A)-1):
        val = A[k] + 1
        if val < A[k+1]:
            result = val
            break
    else:
        result = A[-1] + 1

    return result

#%%
solution([1, 3, 6, 4, 1, 2])
solution([1, 2, 3])
solution([-1, -3])
solution([-11])
solution([1])
solution([3, 2, 5, 0, -2, 7])
solution([3, 1, 2, 5, 0, -2, 7])
solution([3, 1, 6, 2, 5, 0, -2, 4, 7])

#%%