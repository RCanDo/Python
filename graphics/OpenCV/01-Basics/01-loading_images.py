#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Loading files
type: tutorial
keywords: [images]
description: |
remarks:
    - run it as a stand-alone program -- better NOT!
sources:
    - title: Getting Started with Images
      link: https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html
    - title: Getting Started with Images
      link: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
file:
    date: 2022-06-30
    author:
        - nick: arek
          email: arkadiusz.kasprzyk@quantup.pl
"""
#%%
import sys
import cv2 as cv

# os.chdir('~/Roboczy/Python/graphics/OpenCV')
PICTURES = "../../../../Data/pictures/"

from rcando import ak

#%%
cvdir = dir(cv)
len(cvdir)  # 2570

#%%
#img = cv.imread( cv.samples.findFile("starry_night.jpg") ) #! error: OpenCV(4.5.5)
    #! /io/opencv/modules/core/src/utils/samples.cpp:64:
    #! error: (-2:Unspecified error) OpenCV samples: Can't find required data file: starry_night.jpg in function 'findFile'
    #! ???

img = cv.imread(PICTURES + "messi1.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

# uncomment it to run the script as a stand-alone program -- better NOT!
# k = cv.waitKey(0)
# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)

#%%
"""
The second argument to cv.imread() is optional
and specifies the format in which we want the image. This may be:
    IMREAD_COLOR loads the image in the BGR 8-bit format.                   #!!!   B G R  format  !!!
        This is the default that is used here.
    IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
    IMREAD_GRAYSCALE loads the image as an intensity one
"""

#%% !!!
"""
cv.destroyWindow("name")
cv.destroyAllWindows()
"""

#%%
cv.imwrite("messi2.png", img)

#%%
"""
There is a special case where you can already create a window and load image to it later.
!!!  In that case, you can specify whether window is resizable or not.  !!!
It is done with the function cv2.namedWindow().
By default, the flag is
 cv2.WINDOW_AUTOSIZE.
But if you specify flag to be
 cv2.WINDOW_NORMAL,
you can resize window.
It will be helpful when image is too large in dimension and adding track bar to windows.
"""

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)

"""
iprint(filter_re("^WINDOW", cvdir), pref="cv.")
cv.WINDOW_NORMAL        = 0  Allows to manually change window size
cv.WINDOW_AUTOSIZE      = 1  (Default) – Automatically sets the window size
cv.WINDOW_FULLSCREEN    = 1  Changes the window size to fullscreen
cv.WINDOW_FREERATIO     = 256
cv.WINDOW_GUI_EXPANDED  = 0
cv.WINDOW_GUI_NORMAL    = 16
cv.WINDOW_KEEPRATIO     = 0
cv.WINDOW_OPENGL        = 4096
"""

#%% Using Matplotlib
"""
Matplotlib is a plotting library for Python which gives you wide variety of plotting methods.
You will see them in coming articles.
Here, you will learn how to display image with Matplotlib.
You can zoom images, save it etc using Matplotlib.
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(PICTURES + 'messi1.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.tight_layout()
plt.show()

""" Warning
Color image loaded by OpenCV is in BGR mode.
But Matplotlib displays in RGB mode.
So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.
"""
img = cv2.imread(PICTURES + 'messi1.jpg')
plt.imshow(img)
plt.imshow(img[:,:,[2,1,0]])  # that's OK


#%%

"""
#
imread(filename[, flags]) -> retval
...
flags  Flag that can take values of cv::ImreadModes (? not for Python)

#
imwrite(filename, img[, params]) -> retval
...
params  Format-specific parameters encoded as pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ... .)
see cv::ImwriteFlags

#
iprint(filter_re("^IM", cvdir), pref="cv.")

additional flags for imread & imwrite
cv.IMREAD_ANYCOLOR
cv.IMREAD_ANYDEPTH
cv.IMREAD_COLOR                 = 1  Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv.IMREAD_GRAYSCALE             = 0  Loads image in grayscale mode
cv.IMREAD_IGNORE_ORIENTATION
cv.IMREAD_LOAD_GDAL
cv.IMREAD_REDUCED_COLOR_2
cv.IMREAD_REDUCED_COLOR_4
cv.IMREAD_REDUCED_COLOR_8
cv.IMREAD_REDUCED_GRAYSCALE_2
cv.IMREAD_REDUCED_GRAYSCALE_4
cv.IMREAD_REDUCED_GRAYSCALE_8
cv.IMREAD_UNCHANGED             = -1  Loads image as such including alpha channel
cv.IMWRITE_EXR_COMPRESSION
cv.IMWRITE_EXR_COMPRESSION_B44
cv.IMWRITE_EXR_COMPRESSION_B44A
cv.IMWRITE_EXR_COMPRESSION_DWAA
cv.IMWRITE_EXR_COMPRESSION_DWAB
cv.IMWRITE_EXR_COMPRESSION_NO
cv.IMWRITE_EXR_COMPRESSION_PIZ
cv.IMWRITE_EXR_COMPRESSION_PXR24
cv.IMWRITE_EXR_COMPRESSION_RLE
cv.IMWRITE_EXR_COMPRESSION_ZIP
cv.IMWRITE_EXR_COMPRESSION_ZIPS
cv.IMWRITE_EXR_TYPE
cv.IMWRITE_EXR_TYPE_FLOAT
cv.IMWRITE_EXR_TYPE_HALF
cv.IMWRITE_JPEG2000_COMPRESSION_X1000
cv.IMWRITE_JPEG_CHROMA_QUALITY
cv.IMWRITE_JPEG_LUMA_QUALITY
cv.IMWRITE_JPEG_OPTIMIZE
cv.IMWRITE_JPEG_PROGRESSIVE
cv.IMWRITE_JPEG_QUALITY
cv.IMWRITE_JPEG_RST_INTERVAL
cv.IMWRITE_PAM_FORMAT_BLACKANDWHITE
cv.IMWRITE_PAM_FORMAT_GRAYSCALE
cv.IMWRITE_PAM_FORMAT_GRAYSCALE_ALPHA
cv.IMWRITE_PAM_FORMAT_NULL
cv.IMWRITE_PAM_FORMAT_RGB
cv.IMWRITE_PAM_FORMAT_RGB_ALPHA
cv.IMWRITE_PAM_TUPLETYPE
cv.IMWRITE_PNG_BILEVEL
cv.IMWRITE_PNG_COMPRESSION
cv.IMWRITE_PNG_STRATEGY
cv.IMWRITE_PNG_STRATEGY_DEFAULT
cv.IMWRITE_PNG_STRATEGY_FILTERED
cv.IMWRITE_PNG_STRATEGY_FIXED
cv.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY
cv.IMWRITE_PNG_STRATEGY_RLE
cv.IMWRITE_PXM_BINARY
cv.IMWRITE_TIFF_COMPRESSION
cv.IMWRITE_TIFF_RESUNIT
cv.IMWRITE_TIFF_XDPI
cv.IMWRITE_TIFF_YDPI
cv.IMWRITE_WEBP_QUALITY

"""
