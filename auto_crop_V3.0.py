# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:33:59 2021

@author: Jonas Meier
"""


# %matplotlib inline
import cv2
import numpy as np
import matplotlib.pyplot as plt
import rawpy
import core as co 
import imutils

raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (20).dng")
lin16bit = raw_neg.postprocess(gamma=(1, 1),no_auto_bright=True, output_bps=16, user_flip = 3)
raw = lin16bit
raw = co.invert(lin16bit)
raw = co.adjust_gamma(raw,2.4)

#read in the pinwheel image
img = co.img16to8(raw[:,:,0])





#%%
ratio = img.shape[0] / 300.0
orig = img.copy()
image = imutils.resize(img, height = 300)
# convert the image to grayscale, blur it, and find edges
# in the image
image = cv2.medianBlur(image, 5)
# image = cv2.GaussianBlur(image,(3,7),0)

image = cv2.adaptiveThreshold(image,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,55,16)




gray = image
gray = cv2.bilateralFilter(gray, 21, 11, 11)
edged = cv2.Canny(gray, 4, 255)

cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

# loop over our contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    print(len(approx))

    if len(approx) > 15:
        screenCnt = approx
        print("found something")
        screenCnt = approx
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
        cv2.imshow("Game Boy Screen", image)
        cv2.waitKey(0)
        break
        
        



plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edged,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()





#%%
# Median filter clears small details
# img = cv2.medianBlur(img, 75)
# img = cv2.GaussianBlur(img,(11,11),0)

# img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,45,3)

# # ret,img = cv2.threshold(img,235,255,cv2.THRESH_BINARY)


# # img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 0, 0])
# # plt.imshow(edges_img)




# edges_img = cv2.Canny(img,200,255)
# # cv2.imwrite("img_test01.jpg",img)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges_img,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

# # Getting contours  

# cnts = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
# screenCnt = None
# # loop over our contours
# for c in cnts:
# 	# approximate the contour
# 	peri = cv2.arcLength(c, True)
# 	approx = cv2.approxPolyDP(c, 0.015 * peri, True)
# 	# if our approximated contour has four points, then
# 	# we can assume that we have found our screen
# 	if len(approx) == 4:
# 		screenCnt = approx
# 		break