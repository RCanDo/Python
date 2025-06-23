#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 10:34:12 2025

@author: arek
"""
# %%
from typing import Generator

FILE = '/home/arek/Projects/Notes/chińskie przysłowia.txt'

with open(FILE) as f:
    lines = f.readlines()

lines
len(lines)

# %%
N = 3
B = 5

def gen_fun(lines: list[str], chunk_size: int = N, bach_size: int = B) -> Generator:
    """
    lines: list[str]
    chunk_size: int = N
    bach_size: int = B
    -> Generator
    """
    L = len(lines)
    start = 0
    batch = []
    b = 0
    while start < L:
        while b < batch_size:
            end = start + chunk_size
            batch.append(lines[start:end])
            b += 1
            start += chunk_size
        yield batch
        b = 0
        batch = []

# %%  v2
def gen_fun(lines: list[str], chunk_size: int = 3, batch_size: int = 5) -> Generator:
    """
    lines: list[str]
    chunk_size: int = N
    batch_size: int = B
    -> Generator
    """
    L = len(lines)
    used = 0
    batch = []
    b = 0
    while used < L:
        while b < batch_size:
            batch.append(lines[:chunk_size])
            lines = lines[chunk_size:]
            used += chunk_size
            b += 1
        yield batch
        b = 0
        batch = []

# %%
lgen = gen_fun(lines, N)
lgen
next(lgen)
{b: batch for b, batch in enumerate(lgen)}




