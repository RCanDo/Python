#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Count Div
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    Write a function `def solution(A, B, K)` that, given three integers A, B and K,
    returns the number of integers within the range [A..B] that are divisible by K, i.e.:
    { i : A ≤ i ≤ B, i mod K = 0 }
    For example, for A = 6, B = 11 and K = 2, your function should return 3,
    because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
    Write an efficient algorithm for the following assumptions:
    A and B are integers within the range [0..2,000,000,000];
    K is an integer within the range [1..2,000,000,000];
    A ≤ B.
difficulty:
    - easy
sources:
    - title: Count Div (Codility excericise)
      link: https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: CountDiv.py
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
# 100%; O(1)
def solution(A, B, K):

    div, mod = divmod(A, K)

    A1 = (div + (mod > 0)) * K

    print(list(range(A1, B + 1, K)))

    result = len(range(A1, B + 1, K))           #!!! this is O(1) !!!  WOW !!!

    return result

#%%
# 100%; O(1)
def solution(A, B, K):

    AdivK, AmodK = divmod(A, K)

    A1 = (AdivK + (AmodK > 0)) * K

    B1 = (B // K) * K

    result = (B1 - A1) // K + 1

    return result

#%%
solution(0, 0, 2)       # 1  [0]
solution(0, 10, 3)      # 4  [0, 3, 6, 9]
solution(6, 11, 2)      # 3  [6, 8, 10]
solution(7, 21, 3)      # 5  [9, 12, 15, 18, 21]
solution(15, 30, 5)     # 4  [15, 20, 25, 30]
solution(17, 31, 5)     # 3  [20, 25, 30]

#%%


#%%


#%%