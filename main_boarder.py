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
# wait for enter, otherwise we'll just close on exit

# path = input("Enter the name of your text file - please use / backslash when typing in directory path: ")

for file in os.listdir(path):
    if file.endswith(".jpg"):
        img_path = os.path.join(path, file)
        img = cv2.imread(img_path);
        img_boarder = boader.boarder(img)
        # img_boarder = cv2.resize(img_boarder, (1350, 1080))
        save_path = os.path.join(path, "WB_" + file)
        cv2.imwrite(save_path,img_boarder)
