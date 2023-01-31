#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Thresholding 03
type: tutorial
keywords: [images]
description: |
    Simple thresholding, adaptive thresholding and Otsu's thresholding:
    cv.threshold() and cv.adaptiveThreshold().
    see also thresholding-01.py
remarks:
sources:
    - title: Image Thresholding
      link: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    - title: help on cv.threshold()
      link: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
    - title: help on cv.adaptiveThreshold()
      link: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3
    - title: AdaptiveThresholdTypes
      link: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gaa42a3e6ef26247da787bf34030ed772c
file:
    date: 2022-07-04
    author:
        - nick: arek
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
#%%
img = cv.imread(PICTURES+FILE, 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img,  thresh1,  thresh2,  thresh3,  thresh4,  thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#%%
#%% Adaptive Thresholding
"""
In the previous section, we used one global value as a threshold.
But this might not be good in all cases,
e.g. if an image has different lighting conditions in different areas.
In that case, adaptive thresholding can help.
Here, the algorithm determines the threshold for a pixel based on a small region around it.
So we get different thresholds for different regions of the same image which gives better results
for images with varying illumination.

in comparison with the parameters of cv.threshold(),
the method cv.adaptiveThreshold takes additional three input parameters.

cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]	) -> dst

1. adaptiveMethod  decides how the threshold value is calculated:

    cv.ADAPTIVE_THRESH_MEAN_C:
        The threshold value is the mean of the neighbourhood area minus the constant C.
    cv.ADAPTIVE_THRESH_GAUSSIAN_C:
        The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

2. blockSize  determines the size of the neighbourhood area and
3. C  is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.

Returns:
    only thresholded image

The code below compares global thresholding and adaptive thresholding for an image with varying illumination:
"""
img = cv.imread('sudoku.png', 0)
img = cv.medianBlur(img, 5)         # ?

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
            cv.THRESH_BINARY, 11, 2)

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv.THRESH_BINARY, 11, 2)

titles = ['Original Image',  'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding',  'Adaptive Gaussian Thresholding']

images = [img,  th1,  th2,  th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#%%
#%% Otsu's Binarization
"""
In global thresholding, we used an arbitrary chosen value as a threshold.
In contrast, Otsu's method avoids having to choose a value and determines it automatically.

Consider an image with only two distinct image values (bimodal image),
where the histogram would only consist of two peaks.
A good threshold would be in the middle of those two values.

Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

In order to do so, the cv.threshold() function is used,
where cv.THRESH_OTSU is passed as an extra flag.
The threshold value can be chosen arbitrary.
The algorithm then finds the optimal threshold value which is returned as the first output.

Check out the example below.
The input image is a noisy image.
In the first case, global thresholding with a value of 127 is applied.
In the second case, Otsu's thresholding is applied directly.
In the third case, the image is first filtered with a 5x5 gaussian kernel to remove the noise,
then Otsu thresholding is applied.
See how noise filtering improves the result.
"""

img = cv.imread('noisy2.png', 0)
# global thresholding
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Otsu's thresholding
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img,  0,  th1,
          img,  0,  th2,
          blur,  0,  th3]

titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]),  plt.xticks([]),  plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3+1].ravel(), 256)
    plt.title(titles[i*3+1]),  plt.xticks([]),  plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]),  plt.xticks([]),  plt.yticks([])

plt.show()


#%%
