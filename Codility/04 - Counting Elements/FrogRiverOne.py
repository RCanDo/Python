#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Frog River One
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: []
description: |
    A small frog wants to get to the other side of a river.
    The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1).
    Leaves fall from a tree onto the surface of the river.
    You are given an array A consisting of N integers representing the falling leaves.
    A[K] represents the position where one leaf falls at time K, measured in seconds.
    The goal is to find the earliest time when the frog can jump to the other side of the river.
    The frog can cross only when leaves appear at every position across the river from 1 to X
    (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves).
    You may assume that the speed of the current in the river is negligibly small,
    i.e. the leaves do not change their positions once they fall in the river.
    For example, you are given integer X = 5 and array A such that:
      A[0] = 1
      A[1] = 3
      A[2] = 1
      A[3] = 4
      A[4] = 2
      A[5] = 3
      A[6] = 5
      A[7] = 4
    In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
    Write a function `def solution(X, A)` that,
    given a non-empty array A consisting of N integers and integer X,
    returns the earliest time when the frog can jump to the other side of the river.
    If the frog is never able to jump to the other side of the river, the function should return −1.
    For example, given X = 5 and array A such that:
      A[0] = 1
      A[1] = 3
      A[2] = 1
      A[3] = 4
      A[4] = 2
      A[5] = 3
      A[6] = 5
      A[7] = 4
    the function should return 6, as explained above.
    Write an efficient algorithm for the following assumptions:
    N and X are integers within the range [1..100,000];
    each element of array A is an integer within the range [1..X].  #!!!
remarks:
    - easy
sources:
    - title: FrogRiverOne (Codility excericise)
      link: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: FrogRiverOne.py
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
# 81%; Task Score: 81%; Correctness: 100%; Performance: 60%; O(N)
def solution(X: int, A: list) -> int:

    if len(A) < X:
        return -1

    # else
    route = [False] * X

    for time in range(len(A)):
        route[A[time]-1] = True
        done = all(route)               #!!! slow !!!!
        if done:
            break

    if not done:
        time = -1

    return time

#%%
# 54%; Task Score: 100%; Correctness: 100%; Performance: 100%; O(N)
def solution(X: int, A: list) -> int:

    if len(A) < X:
        return -1

    # else
    route = [False] * X
    done = 0

    for time in range(len(A)):
        if not route[A[time]-1]:
            route[A[time]-1] = True
            done += 1
        if done == X:
            break

    if done < X:
        time = -1

    return time

#%%
# 54%; Task Score: 54%; Correctness: 100%; Performance: 0%; O(N**2)
def solution(X: int, A: list) -> int:

    if len(A) < X:
        return -1

    # else
    firsts = list(map( lambda x: A.index(x), A))
    time = max(firsts)

    if time + 1 < X:
        time = -1

    return time

#%%
A = [1, 3, 1, 4, 2, 3, 5, 4]
solution(5, A)

solution(2, [1, 1, 1, 1])


#%%