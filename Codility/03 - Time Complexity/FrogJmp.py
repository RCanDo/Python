#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Frog Jmp
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: [modulo]
description: |
    A small frog wants to get to the other side of the road.
    The frog is currently located at position X and wants to get to a position greater than or equal to Y.
    The small frog always jumps a fixed distance, D.
    Count the minimal number of jumps that the small frog must perform to reach its target.
    Write a function  `def solution(X, Y, D)`  that, given three integers X, Y and D,
    returns the minimal number of jumps from position X to a position equal to or greater than Y.
    For example, given:
      X = 10
      Y = 85
      D = 30
    the function should return 3, because the frog will be positioned as follows:
    after the first jump, at position 10 + 30 = 40
    after the second jump, at position 10 + 30 + 30 = 70
    after the third jump, at position 10 + 30 + 30 + 30 = 100
    Write an efficient algorithm for the following assumptions:
    X, Y and D are integers within the range [1..1,000,000,000];
    X ≤ Y.
remarks:
    - easy
sources:
    - title: Frog Jmp (Codility excericise)
      link: https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: FrogJmp.py
    path: .../ROBOCZY/Python/Codility
    date: 2021-09-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp@int.pl
"""

#%%
def solution(X, Y, D):
    span = (Y - X)
    mod = span % D
    result = (span // D) + (mod > 0)
    return result

#%%
solution(10, 85, 30)
solution(10, 185, 34)

#%%