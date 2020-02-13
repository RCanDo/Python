# -*- coding: utf-8 -*-
# this is oop_time_class_2.py
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 28 09:41:37 2017

28. Object Oriented Programming
===============================

## •

Example 2: a class to deal with time with _get_ and _set_ methods
-----------------------------------------------------------------
"""

class Time:

    def __init__(self, hour, min):
        self.setHour(hour)
        self.setMin(min)

    def setHour(self, hour):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    def setMin(self, min):
        if 0 <= min <= 59:
            self.min = min
        else:
            raise ValueError("Invalid min value: %d" % min)

    def getHour(self):
        return self.hour

    def getMin(self):
        return self.min

    def print24h(self):
        print("{:2d}:{:2d}".format(self.getHour(), self.getMin()))

    def print12h(self):
        if self.getHour() < 12:
            ampm = "am"
        else:
            ampm = "pm"

        print("{:2d}:{:2d} {}".format(self.getHour() % 12, self.getMin(), ampm))

    ## overloading

    def __str__(self):
        return "[ %2d:%2d ]" % (self.hour, self.min)   ## use set, get ?

    def __repr__(self):
        return "Time(%2d, %2d)" % (self.hour, self.min)

    def minutes(self):
        return self.hour * 60 + self.min

    def __gt__(self, other):
        if self.minutes() > other.minutes():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.minutes() < other.minutes():
            return True
        else:
            return False


class TimeUK(Time):     ## inherits from Time

    def __str__(self):
        if self.getHour() < 12:
            ampm = "am"
        else:
            ampm = "pm"

        return "[ {:2d}:{:2d} {} ]".format(self.getHour() % 12, self.getMin(), ampm)


if __name__ == "__main__":

    t1 = Time(15, 45)
    t2 = Time(10, 55)

    print("String representation of the object t1: %s" % t1)
    print("Representation of object = %r" % t1)
    print("compare t1 and t2: "),

    if t1 > t2:
        print("t1 is greater than t2")


    t3 = TimeUK(15, 45)
    print("TimeUK object = %s" % t3)
    t4 = Time(16, 15)
    print("Time object = %s" % t4)
    print("compare t3 and t4: ")
    if t3 > t4:
        print("t3 is greater than t4")
    else:
        print("t3 is not greater than t4")

