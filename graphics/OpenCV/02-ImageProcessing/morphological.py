#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Morphological Transformations
type: tutorial
keywords: [kernel, erosion, dilation, closing, opening, top hat, blck hat]
description: |
    Morphological operations like Erosion, Dilation, Opening, Closing etc.
    Functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.
remarks:
sources:
    - title: Morphological Transformations
      link: https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
    - title: help on cv.getStructuringElement()
      link: https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc
file:
    date: 2022-07-05
    author:
        - nick: arek
"""


#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from rcando import ak

# os.chdir('~/Roboczy/Python/graphics/OpenCV')
PICTURES = "../../../../Data/pictures/"
FILE = "j.png"

#%%
img = cv.imread(PICTURES+FILE, 0)
cv.imshow("0", img)

#%% erosion
"""
A pixel in the original image (either 1 or 0) will be considered 1
only if all the pixels under the kernel is 1,
otherwise it is eroded (made to zero).
"""
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow("erosion", erosion)

#%% dilation
"""
It is just opposite of erosion.
Here, a pixel element is '1' if at least one pixel under the kernel is '1'.
"""
dilation = cv.dilate(img, kernel, iterations = 1)
cv.imshow("dilation", dilation)

#%% Opening
"""
Opening is just another name of erosion followed by dilation.
It is useful in removing noise, as we explained above.
Here we use the function, cv.morphologyEx()
"""
JS = "j_sparks.png"
js = cv.imread(PICTURES+JS, 0)
cv.imshow("sparks", img)

opening = cv.morphologyEx(js, cv.MORPH_OPEN, kernel)
cv.imshow("opening", opening)

#%% Closing
"""
Closing is reverse of Opening, Dilation followed by Erosion.
It is useful in closing small holes inside the foreground objects,
or small black points on the object.
"""
JD = "j_dirt.png"
jd = cv.imread(PICTURES+JD, 0)
cv.imshow("dirt", img)

closing = cv.morphologyEx(jd, cv.MORPH_CLOSE, kernel)
cv.imshow("closing", closing)

#%% Morphological Gradient
"""
It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.
"""
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow("gradient", gradient)

#%% Top Hat
"""
It is the difference between input image and Opening of the image.
Below example is done for a 9x9 kernel.
"""
kernel9 = np.ones((9, 9), np.uint8)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel9)
cv.imshow("tophat", tophat)

#%% Black Hat
"""
It is the difference between the closing of the input image and input image.
"""
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow("blackhat", blackhat)

#%%
#%% Structuring Element
"""
We manually created a structuring elements in the previous examples with help of Numpy.
It is rectangular shape.
But in some cases, you may need elliptical/circular shaped kernels.
So for this purpose, OpenCV has a function,
   cv.getStructuringElement().
You just pass the shape and size of the kernel, you get the desired kernel.
"""
# Rectangular Kernel
cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5,5))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
# array([[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0]], dtype=uint8)

""" there are no more shapes:
https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#gac2db39b56866583a95a5680313c314ad
"""

#%%
