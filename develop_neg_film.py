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

from os import listdir
from os.path import isfile, join

path = "F:/01Img/Analog-Photography/2010-05-26-Skatepark/Python_test"
images, img_name = core.load_images_from_folder(path)
directory = path + "//DevelopTest02"

if not os.path.exists(directory):
    os.makedirs(directory)
    
j = 0
for i in images:
 
    print(img_name[j])
    img = (images[j])
    img = co.auto_level(img)
    img = co.invert(img)
    
    path_save = os.path.join(directory,img_name[j][:-4]+ "_Dev" + ".tiff")
    
    cv2.imwrite(path_save, img)
    j = j + 1
