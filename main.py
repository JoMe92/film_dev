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

# path = "D:/OneDrive/12Programming/FilmDevelopment/img14.tif"
# path = "D:/OneDrive/12Programming/FilmDevelopment/*.tiff"
path = "F:/01Img/2021/00Export/2021-01-20-2010-05-26-Skatepark-Negativ/"
       # "F:/01Img/2021/00Export/2021-01-20-2010-05-26-Skatepark-Negativ/*.tif"

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



# ret, images = cv2.imreadmulti(path, [-1], cv2.IMREAD_UNCHANGED)
# im1 = images[0]
# im2 = images[1]
# im3 = images[2]
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
