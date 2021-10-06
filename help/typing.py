#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: typing
subtitle: Support for type hints
version: 1.0
type: tutorial
keywords: [typin, type hint]
description: |
    Support for type hints
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: typing
      link: https://docs.python.org/3/library/typing.html
      usage: |

file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: typing.py
    path: E:/ROBOCZY/Python/datetime
    date: 2021-09-29
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/Pandas/User Guide/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

#%%
#%%  Type aliases
"""
A type alias is defined by assigning the type to the alias.
In this example, Vector and list[float] will be treated as interchangeable synonyms:
"""
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])

#%% Type aliases are useful for simplifying complex type signatures. For example:

from collections.abc import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.

def broadcast_message(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
    ...

# Note that None as a type hint is a special case and is replaced by type(None).

#%%
#%%  NewType
"""
Use the NewType() helper function to create distinct types:
"""
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
type(some_id)       # int   ???

"""
The static type checker will treat the new type as if it were a subclass of the original type.
This is useful in helping catch logical errors:
"""
def get_user_name(user_id: UserId) -> str:
    print(user_id)

# typechecks
user_a = get_user_name(UserId(42351))

# does not typecheck; an int is not a UserId
user_b = get_user_name(-1)

"""
You may still perform all int operations on a variable of type UserId,
but the result will always be of type int.
This lets you pass in a UserId wherever an int might be expected,
but will prevent you from accidentally creating a UserId in an invalid way:
"""
# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
type(output)

"""
Note that these checks are enforced only by the static type checker.
At runtime, the statement Derived = NewType('Derived', Base) will make Derived a function
that immediately returns whatever parameter you pass it.
That means the expression Derived(some_value) does not create a new class
or introduce any overhead beyond that of a regular function call.

More precisely, the expression some_value is Derived(some_value) is always true at runtime.

This also means that it is not possible to create a subtype of Derived
since it is an identity function at runtime, not an actual type:
"""
from typing import NewType

UserId = NewType('UserId', int)

# Fails at runtime and does not typecheck
class AdminUserId(UserId): pass

# However, it is possible to create a NewType() based on a ‘derived’ NewType:

from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)

# and typechecking for ProUserId will work as expected.
# See PEP 484 for more details.

"""Note

Recall that the use of a type alias declares two types to be equivalent to one another. Doing Alias = Original will make the static type checker treat Alias as being exactly equivalent to Original in all cases. This is useful when you want to simplify complex type signatures.

In contrast, NewType declares one type to be a subtype of another. Doing Derived = NewType('Derived', Original) will make the static type checker treat Derived as a subclass of Original, which means a value of type Original cannot be used in places where a value of type Derived is expected. This is useful when you want to prevent logic errors with minimal runtime cost.

New in version 3.5.2.
"""

