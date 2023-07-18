#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 12:58:41 2023

https://www.pythontutorial.net/python-oop/python-mixin/

"""
# %%
"""
What is a mixin in Python

A mixin is a class that provides method implementations for reuse by multiple related child classes.
However, the inheritance is not implying an is-a relationship.

A mixin doesn’t define a new type.
Therefore, it is not intended for direction instantiation.

A mixin bundles a set of methods for reuse.
Each mixin should have a single specific behavior, implementing closely related methods.

Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.

Since Python doesn’t define a formal way to define mixin classes,
it’s a good practice to name mixin classes with the suffix Mixin.

A mixin class is like an interface in Java and C# with implementation.
And it’s like a trait in PHP.
"""

# %%
from pprint import pprint


class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes):
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class Person:
    def __init__(self, name):
        self.name = name


class Employee(DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


# %%

e = Employee(
    name='John',
    skills=['Python Programming', 'Project Management'],
    dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']}
)

pprint(e.to_dict())
e.to_dict()

type(e)
isinstance(e, DictMixin)
issubclass(Employee, DictMixin)

# %%
dm = DictMixin()
type(dm)


# %%