# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:48:41 2020

@author: jonas
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import core as co
import os
import glob
import rawpy
import core

# path = "D:/OneDrive/12Programming/FilmDevelopment/img14.tif"
path = "D:/Bilder/Negativ/2010-01-05/*.dng"



def load_images_from_folder(folder): 
    images = [] 
    img_name = []
    for filename in glob.glob(path):
     img = cv2.imread(os.path.join(folder,filename)) 
     # ret, images = cv2.imreadmulti(os.path.join(folder,filename), [-1], cv2.IMREAD_UNCHANGED)
     img = images[1]
     
     if img is not None: 
      images.append(img) 
      img_name.append(filename)
    return images, img_name




# =============================================================================
# path = 'D:/Bilder/Negativ/2010-01-05/Img01.dng'
path = 'F:/01Img/Analog-Photography/2010-05-26-Skatepark/Pulstek/Img36.dng'
raw_neg = rawpy.imread(path)

lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)
r,g,b = cv2.split(lin16bit)
img = cv2.merge((b,g,r))

co.imshow(img)
img = co.auto_level(img)
img = co.invert(img)

cv2.imwrite("Test06.tiff", img)
# =============================================================================

#%%
# Load Fuji Image an convert it
path = "F:/01Img/Analog-Photography/2010-05-26-Skatepark/Fuji-Scan/Negativ/DSCF5677.RAF"

raw_neg = rawpy.imread(path)

lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)
r,g,b = cv2.split(lin16bit)
img = cv2.merge((b,g,r))


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
gray = cv2.equalizeHist(gray)

_, ignoreMask = cv2.threshold(gray, 65400, 65540, cv2.THRESH_BINARY)

_, binary = cv2.threshold(img, lowerThresh, 65540, cv2.THRESH_BINARY_INV) # THRESH_TOZERO_INV
# binary = cv2.bitwise_not(binary)

binary = cv2.bitwise_and(ignoreMask, binary)

# Prevent tiny outlier collections of pixels spoiling the rect fitting
kernel = np.ones((5,5),np.uint8)
binary = cv2.dilate(binary, kernel, iterations = 3)
binary = cv2.erode(binary, kernel, iterations = 3)


co.imshow(img)
img = co.auto_level(img)
img = co.invert(img)

cv2.imwrite("Test07.tiff", img)
#%%

path = 'F:/01Img/2021/00Export/Negativ-Analog-Test/DSCF5677.tif'
img = cv2.imread(path,-1)

co.imshow(img)
img = co.auto_level(img)
img = co.invert(img)

cv2.imwrite("Test07.tiff", img)



#%%

#
images, img_name = load_images_from_folder(path)

j = 0
for i in images:
 
    print(img_name[j])
    j = j + 1
    img = (images[j])
    img = co.auto_level(img)
    img = co.invert(img)
    
    cv2.imwrite("Test02.tiff", img)
# co.imshow(img)

# cv2.imwrite("Test02.tiff", img)
