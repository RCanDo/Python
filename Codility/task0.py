# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:25:21 2021

@author: staar
"""

#%%
#%%
def solution(N):
    """
    For N in (1, 500)
    Find smallest natural number greater then N
    whose sum of digits is twice the sum of digits of N.
    solution(14)   #-> 19
    solution(15)   #-> 39
    solution(10)   #-> 11
    solution(100000)  #-> 100001
    solution(99)   #-> 9999
    solution(123)  #-> 129
    solution(941)  #-> 1999
    """
    ...

    return result

#%%
solution(14)
solution(15)
solution(10)
solution(99)
solution(100000)
solution(123)
solution(941)


#%%
#%%

def solution(A):
    """
    For array A of integers in {1, ..., N} and of length N
    find number M = minimal number 'moves', i.e.
    of additions and/or subtractions of 1 from any of the number in A
    so that after all these moves A is a permutation of (1, ..., N).
    solution([1, 2, 1])  #-> [1, 2, 3] or [2, 3, 1],  M = 2
    solution([2, 1, 4, 4])  #-> [2, 1, 4, 3] or [2, 1, 3, 4],  M = 1
    solution([6, 2, 3, 5, 6, 3])  #-> [6, 2, 3, 5,  4, 1],  M = 4
    return -1 if M > 1e9
    """
    ...

    return moves

#%%
solution([1, 2, 1])
solution([2, 1, 4, 4])
solution([6, 2, 3, 5, 6, 3])

#%%
#%%

def solution(S):
    """
    Call the string 'balanced' when each letter appears in it in lower- and upper-case.
    Eg. "Aa", "Aaa", "AaBb", "bABaa" are all balanced while
    "A", "aa", "aAb", "aAbb", "bABaC" are not balanced.
    For any string find there the length of a _minimal_ balanced substring (continuous).
    Return -1 if there is no balanced substring.
    We assume string is non-empty.
    E.g.
    solution('a')    #-> -1
    solution('aA')   #-> 2
    solution('aAa')  #-> 2
    solution('azABaabza')  #-> 5  'ABaab'
    solution('TacoCat')    #-> -1
    solution('AcZCbaBz')   #-> 8   whole string only
    solution('akjbdgiubweirjnvpiqyebr')  #-> -1
    """
    ...

    return balanced


#%%
is_balanced('ABCdDacbbaaD')   # True
is_balanced('ABCDacbbaaD')    # False
is_balanced('ABaab')          # True

#%%
solution('a')
solution('aA')
solution('aAa')
solution('azABaabza')
solution('TacoCat')
solution('AcZCbaBz')
solution('akjbdgiubweirjnvpiqyebr')

#%%