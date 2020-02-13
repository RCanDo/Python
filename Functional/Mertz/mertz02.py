#! python3
# -*- coding: utf-8 -*-
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: Multipe Dispatch
subtitle:
version: 1.0
type: examples and explanations
keywords: [multipe dispatch]
description: |
remarks:
    - _
sources:
    - title: Functional Programming in Python
      chapter: Multiple Dispatch
      pages: 19-24
      link: "D:/bib/Python/Functional/Mertz - Functional Progrmming In Python (49).pdf"
      date: 2015-05-27
      authors:
          - fullname: David Mertz
      usage: examples and explanations
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: mertz02.py
    path: D:/ROBOCZY/Python/Functional/Mertz/
    date: 2019-07-10
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl
"""

#%%

cd D://ROBOCZY/Python/Functional/Mertz
pwd
ls

#%% Multipe Dispatch
#%%
"""
Let's implement simple game of rock/paper/scissors
"""

#%% way 1 -- purely imeprative = many branches
"""
long code with many repetitions prone to mistakes
"""


class Thing(object): pass
class Rock(Thing): pass
class Paper(Thing): pass
class Scissors(Thing): pass


def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None
        if isinstance(y, Paper):
            return y
        if isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown Second Thing")
    if isinstance(x, Paper):
        if isinstance(y, Rock):
            return x
        if isinstance(y, Paper):
            return None
        if isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown Second Thing")
    if isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        if isinstance(y, Paper):
            return x
        if isinstance(y, Scissors):
            return None
        else:
            raise TypeError("Unknown Second Thing")
    else:
        raise TypeError("Unknown First Thing")

rock, paper, scissors = Rock(), Paper(), Scissors()

#%%
beats(rock, paper)
beats(rock, scissors)
beats(rock, rock)
beats(paper, rock)
beats(paper, 3)

#%% way 2 -- Delegating to the Object
"""
As a second try we might try to eliminate some of the fragile repitition
with Python’s “duck typing”—that is, maybe we can have different
things share a common method that is called as needed:
"""

class DuckRock(Rock):
    def beats(self, other):
        if isinstance(other, Rock):
            return None
        elif isinstance(other, Paper):
            return other
        elif isinstance(other, Scissors):
            return self
        else:
            raise TypeError("Unknown Second Thing")

class DuckPaper(Paper):
    def beats(self, other):
        if isinstance(other, Rock):
            return self
        elif isinstance(other, Paper):
            return None
        elif isinstance(other, Scissors):
            return other
        else:
            raise TypeError("Unknown Second Thing")

class DuckScissors(Scissors):
    def beats(self, other):
        if isinstance(other, Rock):
            return other
        elif isinstance(other, Paper):
            return self
        elif isinstance(other, Scissors):
            return None
        else:
            raise TypeError("Unknown Second Thing")


def duck_beats(x, y):
    if hasattr(x, "beats"):
        return x.beats(y)
    else:
        raise TypeError("Unknown First Thing")

rock, paper, scissors = DuckRock(), DuckPaper(), DuckScissors()


#%%

duck_beats(rock, paper)
duck_beats(rock, scissors)
duck_beats(rock, rock)
duck_beats(paper, rock)
duck_beats(paper, 3)

#%% way 3 - Pattern Matching
"""
As a final try, we can express all the logic more directly using multiple dispatch.
This should be more readable, albeit there are still a number of cases to define:
"""

from multipledispatch import dispatch

@dispatch(Rock, Rock)
def md_beats(x, y): return None

@dispatch(Rock, Paper)
def md_beats(x, y): return y

@dispatch(Rock, Scissors)
def md_beats(x, y): return x

@dispatch(Paper, Rock)
def md_beats(x, y): return x

@dispatch(Paper, Paper)
def md_beats(x, y): return None

@dispatch(Paper, Scissors)
def md_beats(x, y): return y

@dispatch(Scissors, Rock)
def md_beats(x, y): return y

@dispatch(Scissors, Paper)
def md_beats(x, y): return x

@dispatch(Scissors, Scissors)
def md_beats(x, y): return None

@dispatch(object, object)
def md_beats(x, y):
    if not isinstance(x, (Rock, Paper, Scissors)):
        raise TypeError("Unknown First Thing")
    else:
        raise TypeError("Unknown Second Thing")

#%%

md_beats(rock, paper)
md_beats(rock, scissors)
md_beats(rock, rock)
md_beats(rock, 3)

#%% Predicate-based dispatch
#   ...


