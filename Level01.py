# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:45:41 2020
This is the code that I use. Levels are done, 1) on the brightness 
channel of the HSV image and, 2) according to the desired amount of
 blacks and whites pixels in the result.

The code can be modified to avoid to use pillow since openCV use 
numpy arrays as internal data. If doing so, be aware that openCV 
native colorspace is BGR. You will have to change the calls
 to cv.cvtColor() accordingly.
 
@author: https://stackoverflow.com/questions/3105603/doing-the-same-as-imagemagicks-level-in-python-pil
"""

from PIL import Image
import numpy as np
import cv2 
import core as co

path = "D:/OneDrive/12Programming/FilmDevelopment/img14.tif"
ret, images = cv2.imreadmulti(path, [-1], cv2.IMREAD_UNCHANGED)
im1 = images[0]
im2 = images[1]
im3 = images[2]

imgPil = Image.open(path) 
imgCV = np.asarray(imgPil, np.uint16)

# Achtung das ist ein nicht Linearer Operator!!!
#img_rgb = img_rgb.astype(np.float32) before using non-linear conversions helps, it reduced max abs diff to diff: 0.00011444092 and adding img_rgb = img_rgb / 255.0 helps 
#https://stackoverflow.com/questions/63688369/opencv-rbg-hsv-rgb-is-lossless
img_rgb = im2.astype(np.float32) 
img_rgb = img_rgb / 255.0 
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)


h,s,v = cv2.split(hsv)
ceil = np.percentile(v,95) # 5% of pixels will be white
floor = np.percentile(v,5) # 5% of pixels will be black
a = 255/(ceil-floor)
b = floor*255/(floor-ceil)
v = np.maximum(0,np.minimum(255,v*a+b)).astype(np.uint8)
hsv = cv2.merge((h,s,v))
rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

img_inv = co.invert(rgb.astype("uint8"))
co.imshow(img_inv)

co.hist(rgb)

