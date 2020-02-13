#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Subclassing built-in types
subtitle:
version: 1.0
type: tutorial
keywords: [kw1,...]
description: |
remarks:
todo:
sources:
    - title: Expert Python Programming
      chapter: 03 - Syntax Best Practices
      pages: 78-
      link: d:/bib/Python/expertpythonprogramming.pdf
      date: 2016
      authors:
          - fullname: Michał Jaworski
          - fullname: Tarek Ziadé
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-subclassing_built-in_types.py
    path: D:/ROBOCZY/Python/help/ExpertPython/03-SyntaxBestPractices/
    date: 2019-12-15
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%

cd D:/ROBOCZY/Python/help/ExpertPython/0x-chapter

#%%
"""
Built-in types cover most use cases
When you are about to create a new class that acts like a sequence or
a mapping, think about its features and look over the existing built-in
types. The `collections` module extends basic built-in types with many
useful containers. You will end up using one of them most of the time.
"""

#%% Ex. 1

class DistinctError(ValueError):
    """Raised when duplicate value is added to a distinctdict."""

class distinctdict(dict):
    """Dictionary that does not accept duplicate values."""
    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value) or
                key not in self
            ):
                raise DistinctError("This value already exists for different key")

        super().__setitem__(key, value)

#%%
type(distinctdict)   # type
distinctdict.__bases__   # (dict,)

myd = distinctdict()
type(myd)   # __main__.distinctdict

myd
print(myd)  # {}

myd['key'] = 'value'
myd           # {'key': 'value'}
myd['other_key'] = 'value'   # DistinctError: This value already exists for different key
myd['other_key'] = 'value2'
myd

myd['key'] = 'x'
myd

#%% Ex. 2
class Folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self, nesting=0):
        offset = "  " * nesting
        print(f'{offset}{self.name}/')

        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print(f'{offset}  {element}')

#%%
tree = Folder('project')
tree
tree.dir()

tree.append('README.md')
tree
tree.dir()

src = Folder('src')
src.append('script.py')
src
src.dir()

tree.append(src)
tree
tree.dir()

#%%
