#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: pymonad
version: 1.0
type: examples             # module, analysis, model, tutorial, help, example, ...
keywords: [functional, monads, curry, ...]
description: |
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: PyMonad
      link: https://jasondelaat.github.io/pymonad_docs/#orgd2c61ef
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    date: 2022-07-09
    authors:
        - nick: arek
          email:
              - akasp@int.pl
"""

#%%
from pymonad.tools import curry

#%%
@curry(2)
def add(x, y):
    return x + y

add(1, 2)       # 3
add_1 = add(1)  # <function pymonad.tools._curry_helper.<locals>._curry_internal(*arguments: List[Any])>
add_1(2)        # 3

#%%
