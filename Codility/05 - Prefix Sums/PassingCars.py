#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: PassingCars
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    A non-empty array A consisting of N integers is given.
    The consecutive elements of array A represent consecutive cars on a road.
    Array A contains only 0s and/or 1s:
    0 represents a car traveling east,
    1 represents a car traveling west.
    The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N,
    is passing when P is traveling to the east and Q is traveling to the west.
    For example, consider array A such that:
      A[0] = 0
      A[1] = 1
      A[2] = 0
      A[3] = 1
      A[4] = 1
    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
    Write a function:
    def solution(A)
    that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
    The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
    For example, given:
      A[0] = 0
      A[1] = 1
      A[2] = 0
      A[3] = 1
      A[4] = 1
    the function should return 5, as explained above.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer that can have one of the following values: 0, 1.
difficulty:
    - easy
sources:
    - title: PassingCars (Codility excericise)
      link:
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: PassingCars.py
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
# 50%;  Task Score 50%; Correctness 100%; Performance 0%;  O(N ** 2)
def solution(A):

    result = 0

    for k in range(len(A) - 1):
        if A[k] == 0:
            result += sum(A[k:])
        if result > int(1e9):
            result = -1
            break

    return result

#%%
solution([0, 1, 0, 1, 1])

#%%
# 100%;  Task Score 100%; Correctness 100%; Performance 100%;  O(N)
def solution(A):

    N = len(A)

    idx = [N - i - 1 for i, v in enumerate(A) if v==0]

    result = sum(v - i for i, v in enumerate(idx[::-1]))

    if result > int(1e9):
        result = -1

    return result

#%%
solution([0])
solution([1])
solution([0, 1, 0])

solution([0, 1, 0, 1, 1])

#%%