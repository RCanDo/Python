# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 28 09:41:37 2017

28. Object Oriented Programming
===============================

## •

Example 1: a class to deal with time
------------------------------------
"""

## this is oop_time_class.py
class Time:

    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def print24h(self):
        print("{:2d}:{:2d}".format(self.hour, self.min))

    def print12h(self):
        if self.hour < 12:
            ampm = "am"
        else:
            ampm = "pm"

        print("{:2d}:{:2d} {}".format(self.hour % 12, self.min, ampm))

if __name__ == "__main__":
    t = Time(15, 45)

    print("print as 24h: ")
    t.print24h()
    print("print as 12h: ")
    t.print12h()

    print("The time is %d hours and %d minutes." % (t.hour, t.min))
