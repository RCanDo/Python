-*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:31:21 2021

@author: staar

title: Python advanced features
subtitle: Classes/Objects
"""

#%% basic terminology
"""
class:
class variable:
data member:  class variable or instance variable
function overloading:
instance variable:
inheritance:
instance:
intantiation:
method:
object: instance of a structure defined by (its) class = data members + methods
operator overloading:
"""

#%% example
class Employee(object):
    """Class for employers.
    name:   employee name
    salary: employee salary
    EmpCount: class variable - nr of employees
    """

    EmpCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EmpCount += 1

    def display(self):
        print("name: {}".format(self.name))
        print(f"salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print("Total employee %d" % cls.EmpCount)


#%%
emp1 = Employee("A", 100)
emp2 = Employee("B", 120)

emp1.display()
emp2.display()

Employee.display_count()

#%% attributes
emp1.name
emp1.salary

emp1.age = 46
emp1.age
del emp1.age
emp1.age  #! AttributeError: 'Employee' object has no attribute 'age'

#%% one may use also:
getattr(emp1, "name")   # "A"
hasattr(emp1, "name")   # True
setattr(emp1, "name", "Val")
getattr(emp1, "name")   # "Val"
delattr(emp1, "name")
getattr(emp1, "name")   #! AttributeError: 'Employee' object has no attribute 'name'
hasattr(emp1, "name")   # False

#%% built-in class attributes
# see also  .../Python/Objects/class_own_fields.py

# dir(class) = magics + hidden + methods (no attributes!)
dir(Employee)
dir(emp2)        # dir(instance) = dir(class) + attributes

vars(emp2)       # only attributes
vars(Employee)   #?!!!  mappingproxy({'__module__': '__main__', ...,'__weakref__': <attribute '__weakref__' of 'Employee' objects>})

emp2.__dict__      # == vars(emp2)
Employee.__dict__  # == vars(Employee)

emp2.__doc__   # 'Class for employers.\n    name:   employee name\n    salary: employee salary\n    EmpCount: class variable - nr of employees\n    '
help(emp2)
help(Employee)
emp2??

emp2.__name__  #! AttributeError: 'Employee' object has no attribute '__name__'

emp2.__module__  # '__main__'
emp2.__bases__   #! AttributeError: 'Employee' object has no attribute '__bases__'

#%%
emp2.__repr__()
emp2.__str__()

#%% Garbage collector

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print("{} destroyed".format(class_name))

pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1))
print(id(pt2))
print(id(pt3))

del pt1
pt2

del pt2
pt3

del pt3

# nothing happens, like __del__() method doesn't work ???

#%% Inheritance


#%% Overriding methods


#%% Base overloading methods


#%% Overloading operators


#%% Data hiding


#%%