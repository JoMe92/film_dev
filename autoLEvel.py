# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:59:57 2020

@author: jonas
"""
import cv2
import numpy as np

def find_base(neg, print_progress=False):
    white_sample = [0, 0]
    previous_max = 0
    for y in range(neg.shape[1]):
        if print_progress:
            progress = y/neg.shape[1] * 100
            if progress.is_integer():
                print()
        for x in range(neg.shape[0]):
            local_max = 0
            for chan in range(neg.shape[2]):
                local_max += neg.item(x, y, chan)
            if local_max > previous_max:
                previous_max = local_max
                white_sample = [x, y]
    return [ neg.item(white_sample[0], white_sample[1], chan)
        for chan in range(neg.shape[2]) ]

def invert(neg, base, print_progress=False):
   
    # remove orange mask
    b,g,r = cv2.split(neg)
    b = b * (255 / base[0])
    g = g * (255 / base[1])
    r = r * (255 / base[2])
    res = cv2.merge((b,g,r))

    # invert
    res = 255 - res
  
    res = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX)
    return res

fileName = 'D:/Bilder/Negativ/2020-11-21/img14.tif'
fileOut = 'D:/Bilder/Negativ/2020-11-21/img14_test.tif'
img = cv2.imread(fileName)
base = find_base(img)

img_inv = invert(img,base)
img_Final = img_inv.astype(np.uint8)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img_Final)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(fileOut,img_Final)