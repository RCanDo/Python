#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Trackbar as the Color Palette
type: tutorial
keywords: [images]
description: |
    Learn to bind trackbar to OpenCV windows
    You will learn these functions: cv.getTrackbarPos(), cv.createTrackbar() etc.
remarks:
    - see the second source for using trackbars for thresholding
sources:
    - title: Trackbar as the Color Palette
      link: https://docs.opencv.org/4.x/d9/dc8/tutorial_py_trackbar.html
    - title: Image Thresholding
      link: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
file:
    date: 2022-07-03
    author:
        - nick: arek
"""

#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('~/Roboczy/Python/graphics/OpenCV')
PICTURES = "../../../../Data/pictures/"

from rcando import ak

#%% Goal
"""
Here we will create a simple application which shows the color you specify.
You have a window which shows the color and three trackbars to specify each of B,G,R colors.
You slide the trackbar and correspondingly window color changes.
By default, initial color will be set to Black.

For cv.createTrackbar() function:

    createTrackbar(trackbarName, windowName, value, count, onChange) -> None

1. argument is the trackbar name,
2. is the window name to which it is attached,
3. is the default value,    !!!
4. is the maximum value and
5. is the callback function which is executed every time trackbar value changes.

The callback function always has a default argument which is the trackbar position.
In our case, function does nothing, so we simply pass.

Another important application of trackbar is to use it as a button or switch.
OpenCV, by default, doesn't have button functionality.
So you can use trackbar to get such functionality.
In our application,
we have created one switch in which application works only if switch is ON,
otherwise screen is always black.

HENCE:
    1. trackbars operates only on integer values [0, count]
       (what is not stated explicitely)
"""
#%%
import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Create a black image,  a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
## createTrackbar(trackbarName, windowName, value, count, onChange) -> None
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch_name = '0 : OFF \n1 : ON'
cv.createTrackbar(switch_name, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch_name, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()


#%%
