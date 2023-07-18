#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 09:43:53 2023

@author: arek

https://realpython.com/python-getter-setter/
"""
# %%
# employee.py

from datetime import date

class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = date.fromisoformat(value)


# %%
# point.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name: str):
        print("qq")
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        print("!!!")
        self.__dict__[f"_{name}"] = float(value)

# %%

point = Point(21, 42)

point.x     # 21.0
point.y     # 42.0

point.x = 84
point.x     # 84.0

dir(point)  # ['__class__', '__delattr__', ..., '_x', '_y']

# %%