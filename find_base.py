# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:59:57 2020

@author: jonas
"""
import cv2
import numpy as np
import core as co

def find_base(neg, print_progress=False):
    white_sample = [0, 0]
    previous_max = 0
    for y in range(neg.shape[1]): #Run through all columns of the array
        #     progress = y/neg.shape[1] * 100
        #     if progress.is_integer():
        #         print()
        for x in range(neg.shape[0]):#Run through all rows of the array
            local_max = 0
            for chan in range(neg.shape[2]): #Run through all rwos of the array
                local_max += neg.item(x, y, chan)
            if local_max > previous_max:
                previous_max = local_max
                white_sample = [x, y]
    return [ neg.item(white_sample[0], white_sample[1], chan)
        for chan in range(neg.shape[2]) ]

def invert(neg, base, print_progress=False):
   
    # remove orange mask
    b,g,r = cv2.split(neg)
    b = b * (65535 / base[0])
    g = g * (65535 / base[1])
    r = r * (65535 / base[2])
    res = cv2.merge((b,g,r))

    # invert
    res = 65535 - res
  
    res = cv2.normalize(res, None, 0, 65535, cv2.NORM_MINMAX)
    return res

fileName = 'F:/01Img/2021/00Export/2021-01-20-2010-05-26-Skatepark-Negativ/IMG-07.tif'
fileOut = fileName
image = cv2.imread(fileName,-1)


# img = co.scale_percent(image,10)
img = image
base = find_base(img)
# co.hist(img)

img_inv = invert(img,base)
# co.hist(img_inv.astype(np.uint16))
img_Final = img_inv.astype(np.uint16)

cv2.imwrite(fileOut,img_Final)

# co.imshow(img_Final)
