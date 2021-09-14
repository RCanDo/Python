#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Triangle
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    An array A consisting of N integers is given.
    A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
    A[P] + A[Q] > A[R],
    A[Q] + A[R] > A[P],
    A[R] + A[P] > A[Q].
    For example, consider array A such that:
      A[0] = 10    A[1] = 2    A[2] = 5
      A[3] = 1     A[4] = 8    A[5] = 20
    Triplet (0, 2, 4) is triangular.
    Write a function `def solution(A)` that, given an array A consisting of N integers,
    returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
    For example, given array A such that:
      A[0] = 10    A[1] = 2    A[2] = 5
      A[3] = 1     A[4] = 8    A[5] = 20
    the function should return 1, as explained above. Given array A such that:
      A[0] = 10    A[1] = 50    A[2] = 5
      A[3] = 1
    the function should return 0.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
remarks:
    - easy
    - how to tackle negative values? it's nonsense!
    - easy for positive values
    - for negative - needs to consider number of cases: BORING!!!
sources:
    - title: Triangle (Codility excericise)
      link: https://app.codility.com/programmers/lessons/6-sorting/triangle/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: Triangle.py
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
def solution(N):

    pass


#%%


#%%