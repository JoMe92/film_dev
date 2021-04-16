# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:17:41 2021

@author: Jonas Meier https://stackoverflow.com/questions/6555629/algorithm-to-detect-corners-of-paper-sheet-in-photo
"""


import cv2

import numpy as np
import core as co
import rawpy

def get_new(old):
    new = np.ones(old.shape, np.uint8)
    cv2.bitwise_not(new,new)
    return new
# these constants are carefully picked
MORPH = 9
CANNY = 84
HOUGH = 25


raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (2).dng")
lin16bit = raw_neg.postprocess(gamma=(1, 1),no_auto_bright=True, output_bps=16, user_flip = 3)

raw = co.invert(lin16bit)
raw = co.adjust_gamma(raw,2.4)

img8 = co.img16to8(raw)
equ = cv2.equalizeHist(img8)

cv2.GaussianBlur(equ, (3,3), 0, equ)
orig = img8
img = equ

# this is to recognize white on white
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(MORPH,MORPH))
dilated = cv2.dilate(img, kernel)

edges = cv2.Canny(dilated, 0, CANNY, apertureSize=3)

lines = cv2.HoughLinesP(edges, 1,  3.14/180, HOUGH)
for line in lines[0]:
     cv2.line(edges, (line[0], line[1]), (line[2], line[3]),
                     (255,0,0), 2, 8)
     
     
     
# finding contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = filter(lambda cont: cv2.arcLength(cont, False) > 100, contours)
contours = filter(lambda cont: cv2.contourArea(cont) > 10000, contours)

# simplify contours down to polygons
rects = []
for cont in contours:
    rect = cv2.approxPolyDP(cont, 40, True).copy().reshape(-1, 2)
    rects.append(rect)

# that's basically it
cv2.drawContours(orig, rects,-1,(0,255,0),1)

# show only contours
new = get_new(img)
cv2.drawContours(new, rects,-1,(0,255,0),1)
cv2.GaussianBlur(new, (9,9), 0, new)
new = cv2.Canny(new, 0, CANNY, apertureSize=3)

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', orig)
cv2.waitKey(0)
cv2.imshow('result', dilated)
cv2.waitKey(0)
cv2.imshow('result', edges)
cv2.waitKey(0)
cv2.imshow('result', new)
cv2.waitKey(0)

cv2.destroyAllWindows()