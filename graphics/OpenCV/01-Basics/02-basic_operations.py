#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Basic Operations on Images
type: tutorial
keywords: [images]
description: |
    - Access pixel values and modify them
    - Access image properties
    - Set a Region of Interest (ROI)
    - Split and merge images
    Almost all the operations in this section are mainly related to Numpy rather than OpenCV.
    A good knowledge of Numpy is required to write better optimized code with OpenCV.
remarks:
sources:
    - title: Basic Operations on Images
      link: https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html
    - title:
      link:
file:
    date: 2022-06-30
    author:
        - nick: arek
"""
#%%
import numpy as np
import cv2 as cv

# os.chdir('~/Roboczy/Python/graphics/OpenCV')
PICTURES = "../../../../Data/pictures/"

from rcando import ak

#%%
img = cv.imread( PICTURES + "messi1.jpg" )
cv.imshow('messi', img)

type(img) # numpy.ndarray
img.shape # (280, 450, 3)
img.dtype # dtype('uint8')
img.size  # img.size

#%%
px = img[100, 100]
px      # BGR intensity
# array([57, 63, 68], dtype=uint8)

# pixel value can be changed
img[100,100] = [255,255,255]
img[100,100]    # [255 255 255]
cv.imshow('messi', img)

#%% Better pixel accessing and editing method :
# accessing RED value
img.item(10,10,2)   # 59
# modifying RED value
img.itemset((10,10,2), 100)
img.item(10,10,2)   # 100

#%% ROI -- Region Of Image (or Interest)
ball = img[230:280, 270:320]
cv.imshow("", ball)
ball.shape

img[200:250, 100:150] = ball

#%% Splitting and Merging Image Channels

b,g,r = cv.split(img)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# or
b = img[:,:,0]
cv.imshow("blue", b)

#
img_rev = cv.merge((r,g,b))
cv.imshow("rev", img_rev)

#  Suppose you want to set all the red pixels to zero - you do not need to split the channels first.
# Numpy indexing is faster:
img_rev[:,:,2] = 0
cv.imshow("rg", img_rev)

#!!! cv.split() is a costly operation (in terms of time). So use it only if necessary.
#    Otherwise go for Numpy indexing.  !!!

#%% Making Borders for Images (Padding)
"""
If you want to create a border around an image, something like a photo frame,
you can use cv.copyMakeBorder().
But it has more applications for convolution operation, zero padding etc.
This function takes following arguments:

    src - input image
    top, bottom, left, right - border width in number of pixels in corresponding directions
    borderType - Flag defining what kind of border to be added. It can be following types:
        cv.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
        cv.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
        cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
        cv.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
        cv.BORDER_WRAP - Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
    value - Color of border if border type is cv.BORDER_CONSTANT

Below is a sample code demonstrating all these border types for better understanding:
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread(PICTURES + 'opencv-logo-small.png')    # find other exmpl !!

BLUE = [255,0,0]  # it's BLUE for  cv2.imshow()  BUT it's RED for  matplotlib
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

#%%




#%%



#%%
