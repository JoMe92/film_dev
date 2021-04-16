# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:20:39 2020

@author: Jonas Meier
"""

import numpy as np
from numpy.fft import fft2, ifft2
import cv2 as cv
import matplotlib.pyplot as plt




# =============================================================================
# plot
# =============================================================================
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
    
# def wiener_filter(img, kernel, K = 10):
img = cv.imread("lena.tiff")
fft = fft2(img)

plt.imshow(np.abs(fft))

ImComp(img,fft)


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("lena.tiff")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
f = np.fft.fft2(img[:,:,0])
fshift = np.fft.fftshift(f) # shigt the 0 in the center of the img
magnitude_spectrum = 20*np.log(np.abs(fshift)) # However, there is a reason for taking the logarithm. The values of the spectrum vary over a great range. So, often you only see a single peak (or in 2D a bright spot) at the center. The logarithm compresses the range of values - larger peaks are scaled down more than smaller peaks. This is useful for visualization because it allows you to see details at all amplitudes.
ImComp(img,magnitude_spectrum)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
