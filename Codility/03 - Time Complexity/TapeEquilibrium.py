#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Tape Equilibrium
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    A non-empty array A consisting of N integers is given.
    Array A represents numbers on a tape.
    Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
    A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
    The difference between the two parts is the value of:
    |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
    In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
    For example, consider array A such that:
      A[0] = 3
      A[1] = 1
      A[2] = 2
      A[3] = 4
      A[4] = 3
    We can split this tape in four places:
    P = 1, difference = |3 − 10| = 7
    P = 2, difference = |4 − 9| = 5
    P = 3, difference = |6 − 7| = 1
    P = 4, difference = |10 − 3| = 7
    Write a function `def solution(A)` that, given a non-empty array A of N integers,
    returns the minimal difference that can be achieved.
    For example, given:
      A[0] = 3
      A[1] = 1
      A[2] = 2
      A[3] = 4
      A[4] = 3
    the function should return 1, as explained above.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [2..100,000];
    each element of array A is an integer within the range [−1,000..1,000].

sources:
    - title: Tape Equilibrium (Codility excericise)
      link: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: TapeEquilibrium.py
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
    diff = A[0] - sum(A[1:])
    result = abs(diff)
    for i in range(1, len(A)-1):
        diff = diff + 2*A[i]
        if abs(diff) < result:
            result = abs(diff)
        if result == 0:
            break
    return result


#%%
solution([3, 5])

#%%
import numpy as np
A = np.random.choice(range(-10, 10), 10, replace=True)
A

solution(A)

#%%
for i in range(1, len(A)-1):
    l, r = sum(A[:i]), sum(A[i:])
    print("|{} - {}| = {}".format(l, r, abs(l-r)))

#%%