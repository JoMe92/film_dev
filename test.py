# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:38:39 2020

@author: jonas
"""

from PIL import Image
import numpy as np
import cv2 as cv

fileName = 'D:/Bilder/Negativ/2020-11-21/img14.tif'
fileOut = 'D:/Bilder/Negativ/2020-11-21/img14_test.tif'


# img = cv.imread(fileName)

# imgPil = Image.open(fileName) 


# imgCV = np.asarray(imgPil, np.uint8)
imgCV = cv.imread(fileName)
imgCV = (255-imgCV)

hsv = cv.cvtColor(imgCV, cv.COLOR_RGB2HSV)
h,s,v = cv.split(hsv)
ceil = np.percentile(v,95) # 5% of pixels will be white
floor = np.percentile(v,5) # 5% of pixels will be black
a = 255/(ceil-floor)
b = floor*255/(floor-ceil)
v = np.maximum(0,np.minimum(255,v*a+b)).astype(np.uint8)
hsv = cv.merge((h,s,v))
rgb = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
imgPil = Image.fromarray(rgb)
imgPil.save(fileOut)