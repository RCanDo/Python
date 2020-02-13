# -*- coding: utf-8 -*-
# this is oop_time_class_2.py
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 28 15:50:50 2017

28. Object Oriented Programming
===============================

## •

Inheritance example Geometry
----------------------------
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        Point.__init__(self, x, y)
        self.radius = radius

    def circum(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

class Cylinder(Circle):
    def __init__(self, x=0, y=0, radius=1, height=1):
        Circle.__init__(self, x, y, radius)
        self.height = height

    def area(self):
        return 2*Circle.area(self) + self.circum() * self.height

    def volume(self):
        return 2*Circle.area(self) * self.height


if __name__ == "__main__":
    d = Circle(x=0, y=0, radius=1)
    print("Circle circumference: ", d.circum())
    print("Circle area: ", d.area())
    print([name for name in dir(d) if name[:2] != "__"])

    c = Cylinder(x=0, y=0, radius=1, height=2)
    print("Cylinder area: ", c.area())
    print("Cylinder volume: ", c.volulme())
    print([name for name in dir(c) if name[:2] != "__"])



