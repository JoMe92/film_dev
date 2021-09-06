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
from os import scandir
from numba import jit



# path = "D:/OneDrive/12Programming/FilmDevelopment/img14.tif"
# path = "F:/01Img/2021/00Export/2021-01-30--6x6-Negativ"
# path = "F:/01Img/Analog-Photography/2021-01-27"
path = "F:/01Img/Analog-Photography/2021-02-18-Agfa400-Schlosspark"

folder = path




def load_images_from_folder(folder): 
    images = [] 
    img_name = []
    
    
    for entry in scandir(folder):
        if entry.is_dir():
            # do code or skip
            print("dir")
            continue
        filename  =  entry.name
      
        if '.tif' in filename: 
             print("Load Tif Files")
             img = cv2.imread(os.path.join(folder,filename),-1) 
             # ret, images = cv2.imreadmulti(os.path.join(folder,filename), [-1], cv2.IMREAD_UNCHANGED)
             # img = images[1]
             
        if '.tiff' in filename: 
             print("Load Tiff Files")
             img = cv2.imread(os.path.join(folder,filename)) 
             
        if '.dng' in filename: 
            print("Load DNG Files")
            raw_neg = rawpy.imread(os.path.join(folder,filename))
            # lin16bit = raw_neg.postprocess(gamma=(2.222, 15),no_auto_bright=True, output_bps=16)
            lin16bit = raw_neg.postprocess(gamma=(1,1), output_bps=16, user_flip = 3, no_auto_bright = True) 
            # r,g,b = cv2.split(lin16bit)
            # img = cv2.merge((b,g,r))
            # img = imag1es[1]
            img = lin16bit
            
        if '.RAF' in filename: 
            print("Load RAF Files")
            raw_neg = rawpy.imread(os.path.join(folder,filename))
            lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)
            # r,g,b = cv2.split(lin16bit)
            # img = cv2.merge((b,g,r))
            img = lin16bit
            
        if img is not None: 
            images.append(img) 
            img_name.append(filename)
            
    return images, img_name

# images, img_name = load_images_from_folder(path)
#%%
# raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (2).dng")

# # Read Metadata
# WB = raw_neg.camera_white_level_per_channel 
# wb2 = raw_neg.camera_whitebalance
# cstring = raw_neg.color_desc
# cm = raw_neg.color_matrix
# img_raw = raw_neg.raw_image
# rgb_xyz = raw_neg.rgb_xyz_matrix
# curve = raw_neg.tone_curve



# lin16bit = raw_neg.postprocess(gamma=(1, 1),no_auto_bright=True, output_bps=16, user_flip = 3)
# Teszt = raw_neg.postprocess(output_bps=16)

# img = co.invert(img_raw)
# img = co.adjust_gamma(img,2.4)

# # co.imshow(img)            
# cv2.imwrite("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00_lin16.tiff",img)



# raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (2).dng")
# img_raw = raw_neg.raw_image

# img = co.invert(img_raw)

# img = co.adjust_gamma(img, 2.4)
# # co.imshow(img)   
# cv2.imwrite("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00_Gamma_24.tiff",img)

#%% histogramm 


# raw_neg = rawpy.imread("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (10).dng")

# # lin16bit = raw_neg.postprocess(gamma=(2.222, 15),no_auto_bright=True, output_bps=16)
# lin16bit = raw_neg.postprocess(gamma=(1,1), output_bps=16, user_flip = 3, no_auto_bright = True) 
 
# img = lin16bit
# img = co.invert(img)
# img = co.adjust_gamma(img, 2.4)
# img8 = co.img16to8(img)


# #create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(1,1))
# cl1 = clahe.apply(img8)
# cl1 = cv2.merge((cl1,cl1,cl1))

# cv2.imwrite("F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Test_100_100.jpg",cl1)


#%%

#

images, img_name = load_images_from_folder(path)
#
directory = path + "/Develop"



if not os.path.exists(directory):
    os.makedirs(directory)
    
j = 1
for i in images:
    img_name =  "/Img_" + str(j).zfill(2) + "_Dev_gamma" + ".tiff"
    img_name_jpg =  "/Img_" + str(j).zfill(2) + "_Dev_gamma" + ".jpg"
    path_save = directory + img_name
    path_save_jpg = directory + img_name_jpg
    
    print("processimg img: " + img_name)
    str(j).zfill(2)
    
    img = i
    
    # img = co.auto_level(img)

    
    if os.path.isfile(path_save):
        print ("Err File already exist: " + img_name )
    else:
        print ("File not exist save img: " + img_name)
        # img = co.auto_level(img)
        # img = i
        img = i[:,:,0]
        
        # img =  (16383 - img)
        
        img = co.invert(img)
        
        print("gamma correction")
        img = co.adjust_gamma(img, 2.4)
        img_16bit = cv2.merge((img,img,img))
        
        img8 = co.img16to8(img)
        equ = cv2.equalizeHist(img8)
        

        
        img_final = cv2.merge((equ,equ,equ))
        
        cv2.imwrite(path_save, img_16bit)
        
        cv2.imwrite(path_save_jpg, img_final)
    

    j = j + 1
# co.imshow(img)

# cv2.imwrite("Test02.tiff", img)
