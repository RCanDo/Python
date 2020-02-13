# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Tue Dec 12 13:52:36 2017

9. Modules
==========
"""

%reset
dir()

ls
cd C:/PROJECTS/Python/tuts/PFCSAE
ls

import module1 as m

m.somefun()
m.somefun

cd ~
import module1

%reset
dir()
ls
import module1 as m
dir()

from module1 import somefun
dir()
somefun
somefun()
