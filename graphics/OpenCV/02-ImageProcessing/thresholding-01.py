#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Thresholding 01
type: tutorial
keywords: [images]
description: |
    Perform basic thresholding operations using OpenCV function cv.threshold().
    see also thresholding-03.py for GAUSSIAN and OTSU thresholding;
remarks:
sources:
    - title: Basic Thresholding Operations
      link: https://docs.opencv.org/4.5.5/db/d8e/tutorial_threshold.html
    - title: help on cv.threshold()
      link: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
file:
    date: 2022-07-02
    author:
        - nick: arek
"""

#%%
"""
cv.threshold(	src, thresh, maxval, type[, dst]	) -> 	retval, dst
- src	input array (multiple-channel, 8-bit or 32-bit floating point).
- thresh	threshold value.
- maxval	maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
- type	thresholding type (see ThresholdTypes):
    cv.THRESH_BINARY
    cv.THRESH_BINARY_INV
    cv.THRESH_TRUNC
    cv.THRESH_TOZERO
    cv.THRESH_TOZERO_INV
    Also, the special values THRESH_OTSU or THRESH_TRIANGLE may be combined with one of the above values.
    In these cases, the function determines the optimal threshold value
    using the Otsu's or Triangle algorithm and uses it instead of the specified thresh.
Returns:
- retval  the computed threshold value if Otsu's or Triangle methods used.
- dst	output array of the same size and type and the same number of channels as src.
"""

#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('~/Roboczy/Python/graphics/OpenCV')
PICTURES = "../../../../Data/pictures/"
FILE = "kora.jpg"

from rcando import ak

#%%
from __future__ import print_function
import argparse

WINDOW_NAME = 'Threshold Demo'

MAX_VALUE = 255
MAX_TYPE = 4
MAX_BINARY_VALUE = 255

## this is for standalone module (may be convenient but needs copying the script to separate file)
parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default=PICTURES+FILE)
args = parser.parse_args()

src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)      # Convert the image to Gray

trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'

def Threshold_Demo(val):
    #0: Binary
    #1: Binary Inverted
    #2: Threshold Truncated
    #3: Threshold to Zero
    #4: Threshold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, WINDOW_NAME)
    threshold_value = cv.getTrackbarPos(trackbar_value, WINDOW_NAME)

    _, dst = cv.threshold(src_gray, threshold_value, MAX_BINARY_VALUE, threshold_type)
    """

    """
    cv.imshow(WINDOW_NAME, dst)

cv.namedWindow(WINDOW_NAME)
cv.createTrackbar(trackbar_type, WINDOW_NAME, 3, MAX_TYPE, Threshold_Demo)
cv.createTrackbar(trackbar_value, WINDOW_NAME, 0, MAX_VALUE, Threshold_Demo)

Threshold_Demo(0)
cv.waitKey()    # Wait until user finishes program

#%%
