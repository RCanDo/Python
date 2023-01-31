#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begins with ---

title: Thresholding 02
type: tutorial
keywords: [images]
description: |
    Perform basic thresholding operations using OpenCV cv::inRange function.
    Detect an object based on the range of pixel values in the HSV colorspace.
remarks:
sources:
    - title: Thresholding Operations using inRange
      link: https://docs.opencv.org/4.5.5/da/d97/tutorial_threshold_inRange.html
    - title: help on cv.inRange()
      link: https://docs.opencv.org/4.5.5/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981
    - title: help on cv.cvtColor()
      link: https://docs.opencv.org/4.5.5/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab
    - title: ColorConversionCodes
      link: https://docs.opencv.org/4.5.5/d8/d01/group__imgproc__color__conversions.html#ga4e0972be5de079fed4e3a10e24ef5ef0
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
FILE = "dzieciol.jpg"

from rcando import ak

#%%
import argparse

WINDOW_CAPTURE_NAME = 'Video Capture'
WINDOW_DETECTION_NAME = 'Object Detection'

MAX_VALUE = 255
MAX_VALUE_H = 360//2

LOW_H = 0
LOW_S = 0
LOW_V = 0

HIGH_H = MAX_VALUE_H
HIGH_S = MAX_VALUE
HIGH_V = MAX_VALUE

LOW_H_NAME = 'Low H'
LOW_S_NAME = 'Low S'
LOW_V_NAME = 'Low V'

HIGH_H_NAME = 'High H'
HIGH_S_NAME = 'High S'
HIGH_V_NAME = 'High V'


def on_LOW_H_thresh_trackbar(val):
    global LOW_H
    global HIGH_H
    LOW_H = val
    LOW_H = min(HIGH_H-1, LOW_H)
    cv.setTrackbarPos(LOW_H_NAME, WINDOW_DETECTION_NAME, LOW_H)

def on_HIGH_H_thresh_trackbar(val):
    global LOW_H
    global HIGH_H
    HIGH_H = val
    HIGH_H = max(HIGH_H, LOW_H+1)
    cv.setTrackbarPos(HIGH_H_NAME, WINDOW_DETECTION_NAME, HIGH_H)

def on_LOW_S_thresh_trackbar(val):
    global LOW_S
    global HIGH_S
    LOW_S = val
    LOW_S = min(HIGH_S-1, LOW_S)
    cv.setTrackbarPos(LOW_S_NAME, WINDOW_DETECTION_NAME, LOW_S)

def on_HIGH_S_thresh_trackbar(val):
    global LOW_S
    global HIGH_S
    HIGH_S = val
    HIGH_S = max(HIGH_S, LOW_S+1)
    cv.setTrackbarPos(HIGH_S_NAME, WINDOW_DETECTION_NAME, HIGH_S)

def on_LOW_V_thresh_trackbar(val):
    global LOW_V
    global HIGH_V
    LOW_V = val
    LOW_V = min(HIGH_V-1, LOW_V)
    cv.setTrackbarPos(LOW_V_NAME, WINDOW_DETECTION_NAME, LOW_V)

def on_HIGH_V_thresh_trackbar(val):
    global LOW_V
    global HIGH_V
    HIGH_V = val
    HIGH_V = max(HIGH_V, LOW_V+1)
    cv.setTrackbarPos(HIGH_V_NAME, WINDOW_DETECTION_NAME, HIGH_V)


parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
#parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)  #oryg from site
parser.add_argument('--input', help='Path to input image.', default=PICTURES+FILE)
args = parser.parse_args()

#cap = cv.VideoCapture(args.camera)  #oryg from site
frame = cv.imread(cv.samples.findFile(args.input))


cv.namedWindow(WINDOW_CAPTURE_NAME)
cv.namedWindow(WINDOW_DETECTION_NAME)


cv.createTrackbar(LOW_H_NAME,  WINDOW_DETECTION_NAME , LOW_H,  MAX_VALUE_H, on_LOW_H_thresh_trackbar)
cv.createTrackbar(HIGH_H_NAME, WINDOW_DETECTION_NAME , HIGH_H, MAX_VALUE_H, on_HIGH_H_thresh_trackbar)
cv.createTrackbar(LOW_S_NAME,  WINDOW_DETECTION_NAME , LOW_S,  MAX_VALUE, on_LOW_S_thresh_trackbar)
cv.createTrackbar(HIGH_S_NAME, WINDOW_DETECTION_NAME , HIGH_S, MAX_VALUE, on_HIGH_S_thresh_trackbar)
cv.createTrackbar(LOW_V_NAME,  WINDOW_DETECTION_NAME , LOW_V,  MAX_VALUE, on_LOW_V_thresh_trackbar)
cv.createTrackbar(HIGH_V_NAME, WINDOW_DETECTION_NAME , HIGH_V, MAX_VALUE, on_HIGH_V_thresh_trackbar)


while True:

    #ret, frame = cap.read()  #oryg from site
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (LOW_H, LOW_S, LOW_V), (HIGH_H, HIGH_S, HIGH_V))

    cv.imshow(WINDOW_CAPTURE_NAME, frame)
    cv.imshow(WINDOW_DETECTION_NAME, frame_threshold)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

#%%
