#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Odd Occurrences In Array
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: [counter, list, array]
description: |
    A non-empty array A consisting of N integers is given.
    The array contains an odd number of elements,
    and each element of the array can be paired with another element that has the same value,
    except for one element that is left unpaired.
    For example, in array A such that:
      A[0] = 9  A[1] = 3  A[2] = 9
      A[3] = 3  A[4] = 9  A[5] = 7
      A[6] = 9
    the elements at indexes 0 and 2 have value 9,
    the elements at indexes 1 and 3 have value 3,
    the elements at indexes 4 and 6 have value 9,
    the element at index 5 has value 7 and is unpaired.
    Write a function  `def solution(A)`  that,
    given an array A consisting of N integers fulfilling the above conditions,
    returns the value of the unpaired element.
    For example, given array A such that:
      A[0] = 9  A[1] = 3  A[2] = 9
      A[3] = 3  A[4] = 9  A[5] = 7
      A[6] = 9
    the function should return 7, as explained in the example above.

    Write an efficient algorithm for the following assumptions:
    N is an odd integer within the range [1..1,000,000];
    each element of array A is an integer within the range [1..1,000,000,000];
    all but one of the values in A occur an even number of times.  !!!
remarks:
    - easy
sources:
    - title: Odd Occurrences In Array (Codility excericise)
      link: https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
    - link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: OddOccurrencesInArray.py
    path: .../ROBOCZY/Python/Codility
    date: 2021-09-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp@int.pl
"""

#%% basics !!!
#%% values counter of list
def counter(A: list) -> dict:
    dic = dict()
    for i in range(len(A)):
        item = A[i]
        if item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1
    return dic

def solution(A: list) -> int:
    dic = counter(A)
    result = [v for v, c in dic.items() if c==1][0]
    return result

#%%
def solution_0(A: list) -> int:
    result = None
    for v in set(A):
        if A.count(v) == 1:   # assumed that there's always at least 1 such element
                # this is source of inefficiency: count runs through whole list for each element !
                # HOWEVER this is fastest solution !!! see the bottom of file
            result = v
            break
    return result

#%%
def solution_cr(A: list) -> int:
    from collections import Counter
    c = Counter(A)
    result = [v for v, c in c.items() if c==1][0]
    return result

#%%
def solution_np(A: list) -> int:
    import numpy as np
    arr = np.array(A)
    v, c = np.unique(A, return_counts=True)
    result = [v for v, c in zip(v, c) if c==1][0]  # assumed that there's always at least 1 such element
    return result

#%%
def solution_pd(A: list) -> int:
    import pandas as pd
    ss = pd.Series(A)
    vc = ss.value_counts()
    result = vc[vc==1].index[0]  # assumed that there's always at least 1 such element
    return result

#%%
def solution_sort(A: list) -> int:
    # 100% in Codility; complexity O(N) or O(N*log(N))
    A = sorted(A)
    result = None
    for k in range(int((len(A)-1)/2)):  # len(A) is assumed to be odd !
        if A[2*k] != A[2*k+1]:
            result = A[2*k]
            break
    result = A[-1] if result is None else result
    return result


#%%
#%%
solution([1, 2, 1, 3, 4, 2, 3])
solution([1, 2, 1, 3, 4, 2, 3, 3, 3, 1])

solution_0([1, 2, 1, 3, 4, 2, 3])
solution_0([1, 2, 1, 3, 4, 2, 3, 3, 3, 1])

solution_np([1, 2, 1, 3, 4, 2, 3])
solution_np([1, 2, 1, 3, 4, 2, 3, 3, 3, 1])

solution_pd([1, 2, 1, 3, 4, 2, 3])
solution_pd([1, 2, 1, 3, 4, 2, 3, 3, 3, 1])

solution_cr([1, 2, 1, 3, 4, 2, 3])
solution_cr([1, 2, 1, 3, 4, 2, 3, 3, 3, 1])

solution_sort([1, 2, 1, 3, 4, 2, 3])
solution_sort([1, 2, 1, 3, 4, 2, 3, 3, 3])  # we assume only doubles and one single (as in description)

#%%
#%% generating testing case

import numpy as np
def generate_test(max_val = 100, size = 10, singular_0 = True):
    lst = np.random.choice( range(1, max_val), size=size, replace = False).tolist()
    singular = 0 if singular_0 else max_val + 1
    lst = lst * 2 + [singular]
    np.random.shuffle(lst)
    return lst

#%%
from collections import Counter
Counter(generate_test(100, 20))
Counter(generate_test(100, 90))

Counter(generate_test(100, 20, False))
Counter(generate_test(100, 90, False))

#%%
A = generate_test(100, 90)
Counter(A)

%timeit solution(A)
# 38.9 µs ± 2.31 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 66% in Codility

%timeit solution_0(A)
# 4.81 µs ± 26.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# 55% in Codility

%timeit solution_cr(A)
# 13.7 µs ± 542 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# 66% in Codility

%timeit solution_np(A)
# 68.6 µs ± 2.84 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# - in Codility -- no module named numpy

%timeit solution_pd(A)
# 548 µs ± 6.05 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# - in Codility -- no module named pandas

#  A = generate_test(max_val, size, False)
%timeit solution_sort(A)
# 6.63 µs ± 36 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)    -- 0 is singular
# 18.8 µs ± 584 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)   -- 101 is singular: A = generate_test(max_val, size, False)
# 100% in Codility; complexity O(N) or O(N*log(N))   !!!

#%%
"""
solution_0() is very fast
yet it is scored 55% in Codility because of
number of timeouts and time complexity O(n**2)
SO HOW TO MAKE IT FASTER !!!
"""
#%%
size = int(1e6)    # max = 1e6
max_val = int(1e9)    # max = 1e9
A = generate_test(max_val, size)


%timeit solution(A)
# 934 ms ± 10.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit solution_0(A)
# 303 ms ± 1.17 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit solution_cr(A)
# 603 ms ± 5.64 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit solution_np(A)
# 1.05 s ± 21.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit solution_pd(A)
# 820 ms ± 7.51 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#  A = generate_test(max_val, size, False)
%timeit solution_sort(A)
# 791 ms ± 40.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)         -- 0 is singular
# 1.01 s ± 16.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)         -- 1e9 + 1 is singular:  A = generate_test(max_val, size, False)

#%%