# import the necessary packages
import numpy as np
import argparse
import cv2
import core

# load the image and convert it to grayscale
path = "D:/Bilder/Negativ/2020-11-21/img14.tif"
image = cv2.imread(path)
# image = cv2.imread(args["image"])
# orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Robust", gray)
core.imshow(gray)

# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
# display the results of the naive attempt
core.imshow(image)
# apply a Gaussian blur to the image then find the brightest
# region

gray = cv2.GaussianBlur(gray,(273,273),0)
core.imshow(gray)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
# image = orig.copy()
test = cv2.circle(image, maxLoc, 1, (255, 0, 0), 2)
# display the results of our newly improved method
core.imshow(test)
