#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Max Product Of Three
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    A non-empty array A consisting of N integers is given.
    The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
    For example, array A such that:
      A[0] = -3
      A[1] = 1
      A[2] = 2
      A[3] = -2
      A[4] = 5
      A[5] = 6
    contains the following example triplets:
    (0, 1, 2), product is −3 * 1 * 2 = −6
    (1, 2, 4), product is 1 * 2 * 5 = 10
    (2, 4, 5), product is 2 * 5 * 6 = 60
    Your goal is to find the maximal product of any triplet.
    Write a function: `def solution(A)` that, given a non-empty array A,
    returns the value of the maximal product of any triplet.
    For example, given array A such that:
      A[0] = -3
      A[1] = 1
      A[2] = 2
      A[3] = -2
      A[4] = 5
      A[5] = 6
    the function should return 60, as the product of triplet (2, 4, 5) is maximal.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [3..100,000];
    each element of array A is an integer within the range [−1,000..1,000].
remarks:
    - easy ??? rather medium! lots of cases to consider;
    - assume that sorting algorithm is given (built-in sorted() in Python)
sources:
    - title: Max Product Of Three (Codility excericise)
      link: https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: MaxProductOfThree.py
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
# 100% in Codility; O(N * log(N))
def solution(A: list) -> int:

    if len(A) == 3:
        result = A[0] * A[1] * A[2]

    else:
        B = [x for x in A if x <= 0]
        A = [x for x in A if x > 0]

        if len(A) == 0:
            B = sorted(B, reverse=True)
            result = B[0] * B[1] * B[2]

        elif len(A) == 1:
            B = sorted(B)
            result = A[0] * B[0] * B[1]

        elif len(B) > 1:
            B = sorted(B)
            b = B[0] * B[1]

            A = sorted(A, reverse=True)

            if len(A) > 2:
                result = max(A[0] * A[1] * A[2], A[0] * b)
            else:
                result = A[0] * b

        else:
            A = sorted(A, reverse=True)
            result = A[0] * A[1] * A[2]

    return result

#%%
solution([4, 5, 1, 0])

#%%