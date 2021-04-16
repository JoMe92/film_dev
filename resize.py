# -*- coding: utf-8 -*-
import cv2 

path = "D:/Bilder/Negativ/2020-11-21/img14.tif"
img = cv2.imread(path,-1)

def resize(img,scale_percent):
    # scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img_smal = cv2.resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img_smal

