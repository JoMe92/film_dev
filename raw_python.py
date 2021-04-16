# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:30:09 2020

Based on The PAper Raw Python
@author: jonas
"""
import rawpy
import core as co
import numpy as np
import cv2
from matplotlib.pyplot import imshow

path = "F:/01Img/2019/02_Februar/2019-02-16/IMG_5122.CR2"
# path = "D:/OneDrive/Bilder/HuaweiP20/2020-03-20/IMG_20200320_122022.dng"
# load the raw file
raw_neg = rawpy.imread(path)

#%% some data
lin16bit = raw_neg.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=16)
colorMatrix = raw_neg.color_matrix
rgb_xyz_matrix = raw_neg.rgb_xyz_matrix
camera_whitebalance = raw_neg.camera_whitebalance
color_desc = raw_neg.color_desc
raw_image = raw_neg.raw_image
raw_type = raw_neg.raw_type
tone_curve = raw_neg.tone_curve

co.imshow(lin16bit)
co.imshow(raw_image)
#%% # Whitebalance the img
uint14_max = 2**14 - 1#
raw_image = np.clip(raw_image, 0, uint14_max)# c l i p to range
raw_image = raw_image.astype(float)

raw_image[0::2,0::2 ] *= camera_whitebalance[0] # s c a l e r eds
raw_image[1::2,1::2 ] *= camera_whitebalance[2] # s c a l e blue s
raw_image = np.clip(raw_image ,0 , uint14_max )# c l i p to range



# Demosaic Img
#%%
def downsample (m):
    r = m[0::2, 0::2]
    g = np.clip(m[0::2,1::2] // 2 + m[ 1::2, 0::2] // 2 , 0, 2**14 - 1)
    b = m[1::2,1::2]
    print("downscale done")
    # return np.stack((r,g,b), axis=0).transpose()
    # return np.stack ( [ b , g , r ] )
    return cv2.merge([r,b,g])

img = downsample (raw_image ) # d i s p l a y a b l e rgb image

img = img.astype("uint16")

co.imshow(img)
# co.imshow(img)
# img = co.img16to8(img)
