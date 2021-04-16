# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:29:00 2020

@author: Jonas Meier
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

def ImComp(img1,img2):
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(img1)
    ax.set_title('Before')
    # plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
    ax = fig.add_subplot(1, 2, 2)
    imgplot = plt.imshow(img2)
    # imgplot.set_clim(0.0, 0.7)
    ax.set_title('After')
    return 0

img = cv2.imread("lena.tiff")

# Convert the BRG image to RGB
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Convert the RGB image to HSV
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Convert to Gray
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# LAB image
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#%%

h,s,v = cv2.split(img_HSV)

L, a, b = cv2.split(lab_image)
# Generate Gaussian noise
gauss = np.random.normal(0,1,L.size)
gauss = gauss.reshape(L.shape[0],L.shape[1]).astype('uint8')
# Add the Gaussian noise to the image
img_gauss = cv2.add(L,gauss)

img_blur = cv2.merge([gauss, a, b])

img_blur_rgb = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

ImComp(img_blur_rgb, img)
# some img processing