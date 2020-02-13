# -*- coding: utf-8 -*-
# this is solo_class_game.py
"""
title: Solo Learn Python
subtitle:
author: kasprark
date: Sat Feb  3 14:02:20 2018

xx. Object Oriented Programming
===============================

## •

Class Methods
------
"""

%reset

pwd
cd C:/Users/akasprzy/OneDrive - HERE Global B.V-/arek/ROBOCZY/Python/help/solo
ls

dir()

import importlib ## may come in handy

#%%

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        return "({:9.3f}, {:9.3f})".format(self.width, self.height)

    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(klasa, side_length):
        return klasa(side_length, side_length)

#%%   
    
oblong = Rectangle(2,4)
oblong
    
square = Rectangle.new_square(5)
print(square.calculate_area())
    