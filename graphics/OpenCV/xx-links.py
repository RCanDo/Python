#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Links to more CV tuts
type: tutorial
keywords: [images]
description: |
remarks:
sources:
    - title: 04 Performance Measurement and Improvement Techniques
      link: https://docs.opencv.org/4.x/dc/d71/tutorial_py_optimization.html
      description: |
    - title:
      link:
      description: |

file:
    date: 2022-06-30
    author:
        - nick: arek
"""

#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PICTURES = "../../../../Data/pictures/"

#%%
"""
4 Performance Measurement and Improvement Techniques
https://docs.opencv.org/4.x/dc/d71/tutorial_py_optimization.html
"""

img1 = cv.imread(PICTURES + 'messi1.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
t
# Result I got is 0.521107655 seconds

# check if optimization is enabled
cv.useOptimized()  # True
%timeit res = cv.medianBlur(img,49)
# 10 loops, best of 3: 34.9 ms per loop
# Disable it
cv.setUseOptimized(False)
cv.useOptimized()  # False
%timeit res = cv.medianBlur(img,49)
# 10 loops, best of 3: 64.1 ms per loop

#%%
"""
title:
link:
description: |
"""



#%%



#%%



#%%
