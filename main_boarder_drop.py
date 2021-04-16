# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:53:34 2020

@author: Jonas Meier
"""

import os
import re     #this library is used so that I can use the "search" function
import sys
import boader
import cv2


try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")


img = cv2.imread(droppedFile);
img_boarder = boader.boarder(img)

cv2.imwrite(droppedFile,img_boarder)
