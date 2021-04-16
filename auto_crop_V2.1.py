# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:17:41 2021

@author: Jonas Meier https://stackoverflow.com/questions/54937062/opencv-python-find-contours-based-on-edges-problem
"""


import cv2

import numpy as np
import core as co
import rawpy
# import numpy as np
import imutils


raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (2).dng")
lin16bit = raw_neg.postprocess(gamma=(1, 1),no_auto_bright=True, output_bps=16, user_flip = 3)

raw = co.invert(lin16bit)
raw = co.adjust_gamma(raw,2.4)

img8 = co.img16to8(raw)
equ = cv2.equalizeHist(img8)

cv2.GaussianBlur(equ, (3,3), 0, equ)
orig = img8
img = equ


#%%


# import cv2

# Read the image file
image = img
# Resize the image - change width to 500
image = co.scale_percent(image,10)

gray = image

# RGB to Gray scale conversion
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("1 - Grayscale Conversion", gray)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# Find Edges of the grayscale image
edged = cv2.Canny(gray, 245, 255)

# Find contours based on Edges
cnts, hier = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
# we currently have no Number plate contour
NumberPlateCnt = None

# loop over our contours to find the best possible approximate contour of number plate
count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:  # Select the contour with 4 corners
            NumberPlateCnt = approx #This is our approx Number Plate Contour
            break

# Drawing the selected contour on the original image
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow("Final Image With Number Plate Detected", image)


cv2.waitKey(0) #Wait for user input before closing the images displayed