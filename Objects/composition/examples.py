#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: composition examples
sources:
    - title: example of Composition in Python
      link: https://www.pythonprogramming.in/give-an-example-of-composition-in-python.html
file:
    name: examples.py
    data: 2022-07-19
    authors:
        - nick: rcando
          email: rcando@int.pl
"""

#%% example of Composition in Python
#  https://www.pythonprogramming.in/give-an-example-of-composition-in-python.html

class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return (self.pay*12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())


#%%



#%%



#%%
