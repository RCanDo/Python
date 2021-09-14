#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Number Of Disc Intersections
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: [sort, overlapping pairs]
description: |
    We draw N discs on a plane. The discs are numbered from 0 to N − 1.
    An array A of N non-negative integers, specifying the radiuses of the discs, is given.
    The J-th disc is drawn with its center at (J, 0) and radius A[J].
    We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs
    have at least one common point (assuming that the discs contain their borders).
    The figure below shows discs drawn for N = 6 and A as follows:
      A[0] = 1
      A[1] = 5
      A[2] = 2
      A[3] = 1
      A[4] = 4
      A[5] = 0
    There are eleven (unordered) pairs of discs that intersect, namely:
    discs 1 and 4 intersect, and both intersect with all the other discs;
    disc 2 also intersects with discs 0 and 3.
    Write a function `def solution(A)` that,
    given an array A describing N discs as explained above,
    returns the number of (unordered) pairs of intersecting discs.
    The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
    Given array A shown above, the function should return 11, as explained above.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range [0..2,147,483,647].
remarks:
    - medium (O(n**2) is easy but to get below needs some idea)
sources:
    - title: NumberOfDiscIntersections (Codility excericise)
      link: https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: NumberOfDiscIntersections.py
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
# 56% in Codility; O(N**2); Task Score: 56%; Correctness: 100%; Performance: 12%
def solution_0(A: list) -> int:

    if len(A) < 2:
        return 0

    # else
    pairs = 0
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            pairs += (i - j <= A[i] + A[j])

    return pairs

#%%
# more Pythonic
# 56% in Codility; O(N**2); Task Score: 56%; Correctness: 100%; Performance: 12%
def solution_1(A: list) -> int:

    if len(A) < 2:
        return 0

    # else
    pairs = sum([sum([ i - j <= A[i] + A[j] for j in range(i)]) for i in range(len(A)-1, 0, -1)])

    return pairs

#%%
# 62% in Codility; O(N**2); Task Score: 62%; Correctness: 100%; Performance: 25%
def solution_2(A: list) -> int:

    if len(A) < 2:
        return 0

    # else
    pairs = 0
    for i in range(len(A)):
        pairs += min(A[i], len(A) - 1 - i)
        for j in range(A[i] + i + 1, len(A)):
            pairs += (j - i <= A[i] + A[j])

    return pairs

#%%
# 100% in Codility; O(N*log(N)) or O(N)
def solution(A: list) -> int:
    #  j - i <= A[i] + A[j]  <=>  j - A[j] <= A[i] + i ,   j > i

    if len(A) < 2:
        return 0

    # else
    N = len(A)
    J = [j - A[j] for j in range(N)]
    I = [A[i] + i for i in range(N)]

    J = sorted(J)
    I = sorted(I)

    pairs = int(N*(N-1)/2)
    K = 0

    for j in range(N):
        for i in range(K, N):
            if J[j] <= I[i]:
                K = i
                pairs -= K
                break

    #pairs -= int(N*(N+1)/2)

    pairs = -1 if pairs > int(1e7) else pairs  # nonsense!

    return pairs

#%%
solution([])
solution([1])
solution([1, 5])
solution([1, 5, 2])
solution([1, 5, 2, 1])
solution([1, 5, 2, 1, 4])
solution([1, 5, 2, 1, 4, 0])

#%%
solution([1, 1, 1])

A = [1, 5, 2]

#%%
arr = [[1, 2, 0],
       [0, 2, 3],
       [2, 0, 1]]

for i in range(3):
    print(f" {i}")
    for j in range(3):
        v = arr[i][j]
        print(arr[i][j])
        if v == 0:
            break

#%%

