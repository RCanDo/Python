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
    - title: 03 Arithmetic Operations on Images
      link: https://docs.opencv.org/4.x/d0/d86/tutorial_py_image_arithmetics.html
      description: |
          - image addition/blending
          - bitwise operations (e.g masking!)
file:
    date: 2022-07-02
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

#%%
#%%
""" 03 Arithmetic Operations on Images
https://docs.opencv.org/4.x/d0/d86/tutorial_py_image_arithmetics.html

1. image addition/blending
"""
cv.add(im1, im2)

cv.addWeighted(im1, a, im2, b, g)    # a*im1 + b*im2 + g  where  a in [0, 1], b = 1 - a;

#%%
"""
2. Bitwise Operations

This includes the bitwise AND, OR, NOT, and XOR operations.
They will be highly useful while extracting any part of the image
(as we will see in coming chapters),
defining and working with non-rectangular ROI's, and etc.

Ex.
I want to put the OpenCV logo above an image.
If I add two images, it will change the color.
If I blend them, I get a transparent effect.
But I want it to be opaque.
If it was a rectangular region,
I could use ROI as we did in the last chapter.
But the OpenCV logo is a not a rectangular shape.
So you can do it with bitwise operations as shown below:
"""
# Load two images
img1 = cv.imread(PICTURES + 'messi1.jpg')
cv.imshow("messi", img1)
img2 = cv.imread(PICTURES + 'opencv-logo-small.png')
cv.imshow("logo", img2)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
cv.imshow("roi", roi)

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)     # cv.COLOR_BGR2GRAY == 6
cv.imshow("logo_gray", img2gray)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)   # cv.THRESH_BINARY == 0
ret     # 10.
mask    # array(...)
np.unique(mask)     # 0, 255
cv.imshow("logo_mask", mask)

mask_inv = cv.bitwise_not(mask)
cv.imshow("logo_mask_inv", mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
cv.imshow("background", img1_bg)
""" help(cv.bitwise_and)
bitwise_and(src1, src2, dst, mask) -> dst
src1  first input array or a scalar.
src2  second input array or a scalar.
dst   output array that has the same size and type as the input arrays.
mask  optional operation mask, 8-bit single channel array, that
    specifies elements of the output array to be changed
    hmm...
    what is 0 in the mask will TURN BLACK !!!
    what is 255 in the mask will get get value  src1 & src2  (i.e. bit-wise conjunction)
       if src1 == src2 we get then just the same element
...
src1, src2  must have the same nr of channels (if they are both matrices)
each channel is processed independently
...
"""
# notice it's not straightforward to run cv.bitwise_and(.) simpler way
img1_bg_2 = cv.bitwise_and(roi, mask_inv)   #! dimesions do not agree...
# so we first need to add dim to mask_inv
mask_inv_3 = np.tile(mask_inv[:,:,np.newaxis], (1,1,3))
# or
mask_inv_3 = np.r_['2,3,0', mask_inv, mask_inv, mask_inv]
img1_bg_2 = cv.bitwise_and(roi, mask_inv_3)
cv.imshow("", img1_bg_2)
# ok

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask = mask)
cv.imshow("logo_foreground", img2_fg)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
cv.imshow("roi_with_logo", dst)

img1[0:rows, 0:cols] = dst
cv.imshow('result', img1)

# cv.waitKey(0)
# cv.destroyAllWindows()
