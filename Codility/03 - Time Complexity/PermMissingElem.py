#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Perm Missing Elem
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    An array A consisting of N different integers is given.
    The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
    Your goal is to find that missing element.
    Write a function `def solution(A)` that, given an array A, returns the value of the missing element.
    For example, given array A such that:
      A[0] = 2
      A[1] = 3
      A[2] = 1
      A[3] = 5
    the function should return 4, as it is the missing element.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    the elements of A are all distinct;
    each element of array A is an integer within the range [1..(N + 1)].
sources:
    - title: Perm Missing Elem (Codility excericise)
      link: https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: PermMissingElem.py
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
def solution(A: list) -> int:
    if len(A) == 0:
        result = 1
    else:
        A = sorted(A)
        if A[0] != 1:
            result = 1
        elif len(A) == 1:
            result = 1 if A[0] == 2 else 2
        else:
            for i in range(1, len(A)):
                print(i)
                if A[i] - A[i-1] != 1:
                    result = A[i] - 1
                    break
            if (i == len(A) - 1) and (A[i] == i+1):
                result = i+2

    return result

#%%

solution([])
solution([1])
solution([2])
solution([1,2])
solution([1,3])
solution([2,3])

solution([2, 3, 6, 4, 1])
solution([2, 3, 6, 4, 5])
solution([2, 3, 1, 4, 5])

#%%