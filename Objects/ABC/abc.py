#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Abstract Base Classes
subtitle:
version: 1.0
type: review
keywords: [ABC, Abstract Base Class, abstract method]
description: |
remarks:
todo:
sources:
    - title: Python Module Of The Week
      chapter: abc — Abstract Base Classes
      link: https://pymotw.com/3/abc/
      date: 2019
      authors:
          - fullname: Doug Hellmann
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: abc.py
    path: D:/ROBOCZY/Python/help/Objects/ABC/
    date: 2020-02-05
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
cd D:/ROBOCZY/Python/Objects/ABC/

#%%
import abc

#%%
class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output.
        """

# PluginBase

#%%  registering a concrete class
"""
There are two ways to indicate that a concrete class implements an abstract API:
1. either explicitly register the class  (rare, shown just below)
2. or create a new subclass directly from the abstract base. (common as more intuitive)

Ad.1.
Use the register() class method as a decorator on a concrete class to add it explicitly
when the class provides the required API,
but is not part of the inheritance tree of the abstract base class.  [! use case !]
"""

class LocalBaseClass:
    pass

@PluginBase.register                                 # to inforce interface
class RegisteredImplementation(LocalBaseClass):      # to inherit sth.

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

#%%
issubclass(RegisteredImplementation, PluginBase)      # True
isinstance(RegisteredImplementation(), PluginBase)    # True

#%% Implementation Through Subclassing
"""
Ad.2.
Subclassing directly from the base avoids the need to register the class explicitly.
"""

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

#%%
issubclass(SubclassImplementation, PluginBase)      # True
isinstance(SubclassImplementation(), PluginBase)    # True

#%%
for sc in PluginBase.__subclasses__():
    print(sc.__name__)

# SubclassImplementation  but NO RegisteredImplementation !

#%% Helper Base Class
"""
"Forgetting" to set the metaclass properly means
the concrete implementations do not have  their APIs enforced.
To make it easier to set up the abstract class properly,
a base class is provided that sets the metaclass automatically.
"""

class PluginBase(abc.ABC):

    @abc.abstractclassmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

#%%
issubclass(SubclassImplementation, PluginBase)      # True
isinstance(SubclassImplementation(), PluginBase)    # True

#%%
...


#%%


#%%

