-8`#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Max Counters
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    You are given M counters, initially set to 0, and you have two possible operations on them:
    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the current maximum value of any counter.
    A non-empty array A of N integers is given. This array represents consecutive operations:
    if A[K] = X, such that 1 ≤ X ≤ M, then operation K is increase(X),
    if A[K] = M + 1 then operation K is max counter.
    For example, given integer M = 5 and array A such that:
        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:
        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.
    Write a function `def solution(A)` that, given an integer M and a non-empty array A
    consisting of N integers, returns a sequence of integers representing the values of the counters.
    Result array should be returned as an array of integers.
    For example, given:
        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the function should return [3, 2, 2, 4, 2], as explained above.
    Write an efficient algorithm for the following assumptions:
    M and N are integers within the range [1..100,000];
    each element of array A is an integer within the range [1..M + 1].
difficulty:
    - medium
sources:
    - title: Max Counters (Codility excericise)
      link: https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
    - title: How to find all occurrences of an element in a list
      link: https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
      remarks:
          - see (1) in the code
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: MaxCounters.py
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
from typing import List
from collections import Counter

def split(lst: list, idx: List[int],
          by_value: bool = False,
          to_left: bool = None
          ) -> List[List]:
    """
    lst    list to be splitted according to values in idx
    idx    list of indices (integers) or value  (if by_value=True)
           according to which lst will be splitted
    by_value   if False (default) then `idx` is
           better not use: find indices externally with method appropriate to the data
           (see https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list)

    Split list `lst` into sublists at indices in `idx`.
    Values at indices are removed i.e. they DO NOT appear in any
    of the sublists on the left or on the right of the goven index.
    split([0, 3, 1, 2, 3, 1], [2, 5])  # -> [[0, 3], [2, 3], []]
    split([1, 0, 3], [])   # -> [[1, 0, 3]]
    split([1, 0, 3], [0])  # -> [[], [0, 3]]
    split([1, 0, 3], [1])  # -> [[1], [3]]
    split([1, 0, 3], [2])  # -> [[1, 0], []]
    """

    if by_value:
        idx = [i for i, v in enumerate(lst) if v==idx]   # (1)

    if len(idx) == 0:
        return [lst]

    idx = sorted(set(idx))          #!!!
    idx = [-1] + idx + [len(lst)]

    result = []
    for k in range(len(idx) - 1):

        SL = slice(idx[k]+1, idx[k+1])
        result += [lst[SL]]

    return result

#%%
# 100%; complexity O(N + M)
#
def solution(M: int, A: list) -> list:

    max_counters = [i for i, v in enumerate(A) if v == M+1]  # (1)

    sublists = split(A, max_counters)

    sum_maxs = sum((Counter(sub).most_common(1)[0][1] if len(sub) > 0 else 0)
              for sub in sublists[:-1])

    final = sublists[-1]
    final = Counter(final)

    result = [sum_maxs] * M

    for k in final.keys():
        result[k-1] += final[k]

    return result

#%%
solution(3, [])
solution(3, [2, 2, 2])
solution(1, [2, 2, 2])
solution(1, [1, 2, 1, 2, 1, 1, 2])

solution(3, [3, 4, 4, 1, 4, 4])
solution(4, [3, 4, 4, 1, 4, 4])
solution(5, [3, 4, 4, 1, 4, 4])

solution(5, [3, 4, 4, 6, 1, 4, 4])
solution(5, [3, 4, 4, 6, 1, 4, 4, 6])

#%%