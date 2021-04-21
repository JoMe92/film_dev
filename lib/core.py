# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:05:56 2020

@author: jonas
"""
import cv2
import numpy as np
import os
from os import scandir 
from os import listdir
from matplotlib import pyplot as plt
import core as co
from numba import jit


def img16to8(img):
    """
    convert a 16 bit img to uint8
    """
   img_8 = (img/65535) * 255
   return img_8.astype('uint8')

def imshow(img):
    if img.dtype == "uint8":
        print('the 8 bit image is showen')
        co.scale_percent(img,33)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 0#
    elif img.dtype == 'uint16':
        print('the 16 bit image is showen as 8 bit')
        img = co.img16to8(img)
        co.scale_percent(img,33)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 0
    else:
        print("Error: the image has the wrong data type it must be either 8 bit or 16 bit")
    
def invert(img):
    
    if img.dtype == "uint8":
        print('the 8 bit image is inverted')
        imagem = (255-img)
        return imagem
    elif img.dtype == 'uint16':
        imagem = (65535 - img)
        print('the 16 bit image is inverted')
        return imagem
    else:
        print("Error: the image has the wrong data type it must be either 8 bit or 16 bit")
    
    


def hist(img):
    color = ('b','g','r')
    if img.dtype == "uint8":
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
            plt.show()
        return 0
    elif img.dtype == 'uint16':
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[65535],[0,65535])
            plt.plot(histr,color = col)
            plt.xlim([0,65535])
            plt.show()
        return 0
    else:
        print("Error: the image has the wrong data type it must be either 8 bit or 16 bit")

def scale_percent(img,scale_percent):
    # scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img_smal = cv2.resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img_smal


def auto_level(img, print_progress=False):
    if img.dtype == "uint8":
        print("Error")
        return 0
    elif img.dtype == 'uint16':
        
        # neg = co.scale_percent(img,80)
        neg = img
        print('Auto Level the image')
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
                    
        base = [ neg.item(white_sample[0], white_sample[1], chan)
            for chan in range(neg.shape[2]) ]
        
        b,g,r = cv2.split(img)
        b = b * (65535 / base[0])
        g = g * (65535 / base[1])
        r = r * (65535 / base[2])
        res = cv2.merge((b,g,r))
        return res.astype("uint16")
    else:
        print("Error dtype")
        return 0
    
@jit(nopython=True)
def apply_lut(table,image):
    # Todo with numpay !!!
    i = 0
    j = 0
    img = image

    for i in np.arange(0, image.shape[0]-1, 1):
        
        for j in np.arange(0, image.shape[1]-1, 1 ):
            index = image[i,j]
            value = table[index] 
            img[i, j] = value
            j = j + 1
        i = i + 1

    return img

# Gamma Corecten with Lut
def adjust_gamma(image, gamma=1.0):
    # todo for 8 bit and 16 bit
    #uild a lookup table mapping the pixel values [0, 65535] to
    #heir adjusted gamma values
    table = np.array([((i / 65535.0) ** gamma) * 65535 
                      for i in np.arange(0, 65536)]).astype("uint16")
    # apply gamma correction using the lookup table
    img = apply_lut(table,image)
    
    return  img

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
             img = cv2.imread(os.path.join(folder,filename)) 
             # ret, images = cv2.imreadmulti(os.path.join(folder,filename), [-1], cv2.IMREAD_UNCHANGED)
             # img = images[1]
             
        if '.tiff' in filename: 
             print("Load Tiff Files")
             img = cv2.imread(os.path.join(folder,filename)) 
             
        if '.dng' in filename: 
            print("Load DNG Files")
            raw_neg = rawpy.imread(os.path.join(folder,filename))
            lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)
            r,g,b = cv2.split(lin16bit)
            img = cv2.merge((b,g,r))
            # img = imag1es[1]
            
        if '.RAF' in filename: 
            print("Load RAF Files")
            raw_neg = rawpy.imread(os.path.join(folder,filename))
            lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)
            r,g,b = cv2.split(lin16bit)
            img = cv2.merge((b,g,r))
            
        if img is not None: 
            images.append(img) 
            img_name.append(filename)
            
    return images, img_name
