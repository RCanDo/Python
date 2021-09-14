#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Binary Gap
subtitle: Codility excericise
version: 1.0
type: task & solution
keywords: [binary, decimal]
description: |
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros
    that is __surrounded__ by ones at both ends in the binary representation of N.
    For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
    The number 529 has binary representation 1000010001 and contains two binary gaps:
    one of length 4 and one of length 3.
    The number 20 has binary representation 10100 and contains one binary gap of length 1.
    The number 15 has binary representation 1111 and has no binary gaps.
    The number 32 has binary representation 100000 and has no binary gaps.  !!!
    Write a function: `def solution(N)` that, given a positive integer N,
    returns the length of its longest binary gap.
    The function should return 0 if N doesn't contain a binary gap.
    For example, given N = 1041 the function should return 5,
    because N has binary representation 10000010001 and so its longest binary gap is of length 5.
    Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.  !!!
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..2,147,483,647].
remarks:
    - easy
sources:
    - title: Binary Gap (Codility excericise)
      link: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
    - link: https://stackoverflow.com/questions/699866/python-int-to-binary-string
    - link: https://stackoverflow.com/questions/13656343/python-binary-to-decimal-conversion
    - link: https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
      remark: |
         How to do it from first principles (without resorting to string representation) - IMPORTANT!
         See 1.2 and 2.2 in the code.
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: BinaryGap.py
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
from typing import Union, List

#%%
"""
1. decimal to binary
"""

#%%
"""
1.1 via built-ins
"""
def dec2bin_0(N: int) -> str:
    # reportedly slower (???)
    return format(N, 'b')

def dec2bin(N: int) -> str:
    return bin(N)[2:]

#%%
dec2bin_0(12345)
dec2bin(12345)

#%%
import numpy as np
arr = np.random.choice(int(1e9), int(1e3), replace=True)

%timeit [dec2bin_0(x) for x in arr]
# 448 µs ± 24.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit [dec2bin(x) for x in arr]
# 340 µs ± 10.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

# so yeah, _0 version, `format(N, 'b')`, is about 1/4 slower

#%%
"""
1.2 from first principles
"""
def decimalToBinary(N, res=None):
    """
    returns list of binary repr of N BUT in reversed order !!!
    """

    res = [] if res is None else res
    res.append(N % 2)

    if(N > 1):
        # divide with integral result
        # (discard remainder)
        res = decimalToBinary(N // 2, res)

    return res

def dec2bin_1(N: int, as_string: bool = False) -> Union[List, str]:
    """only to reverse"""
    res = decimalToBinary(N)[::-1]
    if as_string:
        res = "".join(str(x) for x in res)
    return res

#%%
decimalToBinary(1)
dec2bin_1(1)
decimalToBinary(2)
dec2bin_1(2)
decimalToBinary(3)
dec2bin_1(3)
decimalToBinary(4)
dec2bin_1(4)

decimalToBinary(63)
dec2bin_1(63)

decimalToBinary(64)
dec2bin_1(64)

decimalToBinary(12345)
dec2bin_1(12345)
dec2bin_1(12345, True)

decimalToBinary(12346)
dec2bin_1(12346)
dec2bin_1(12346, True)

#%%
"""
2. binary to decimal -- not for the task but important
"""
#%%
"""
2.1 via buit-in
"""
def bin2dec(ss: str):
    return int(ss, 2)

#%%
bin2dec(dec2bin(1234))

bin2dec('111111')

#%%
"""
2.2 from first principle
"""
def binaryToDecimal(B: Union[str, list]) -> int:
    """
    assume that:
    - in both formats only 0 1nd 1 may appear !!!
    - order of digits in list form of B is as in str i.e.
      from highest power to lowest (see (1) )
    """

    if isinstance(B, str):
        B = [int(d) for d in list(B)][::-1]   # (1)
    else:
        B = B[::-1]

    res = 0
    p = 1
    for d in B:
        if d:
            res += p
        p *= 2

    return res

#%%
binaryToDecimal('111')
binaryToDecimal([1, 1, 1])
binaryToDecimal('1111')
binaryToDecimal([1, 1, 1, 1])
binaryToDecimal('10000')
binaryToDecimal([1, 0, 0, 0, 0])
binaryToDecimal('11000000111010')
binaryToDecimal([1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0])

#%%
#%%
"""
3. final solution
"""
#%%
"""
3.1 via regexp
"""
import re

def binary_gap(N: int) -> int:

    # binary represenatation (str)
    B = bin(N)[2:]
    #print(B)

    res0 = re.findall(r'0+1', B)

    if len(res0) > 0:
        res = max(len(x)-1 for x in res0)
    else:
        res = 0

    return res

# 100% in Codility

#%%
binary_gap(63)     # 0   111111
binary_gap(12345)  # 6   11000000111001

binary_gap(32)
binary_gap(64)

#%%
"""
3.2 without regexp
"""

def binary_gap(N: int) -> int:

    # binary represenatation (str)
    B = bin(N)[2:]
    print(B)

    B = list(B)  # here one could use solution 1.2 i.e. decimalToBinary(N) which return list - order doesn't matter!

    counters = []
    counter = 0

    for k in range(len(B)):
        if B[k] == '0':
            counter += 1
        else:
            counters.append(counter)
            counter = 0

    counters = counters[:-1]
    if counters:
        res = max(counters)
    else:
        res = 0

    return res


#%%
binary_gap(63)
binary_gap(64)
binary_gap(12345)

#%%
#%%



#%%