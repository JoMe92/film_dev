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
import src.core as co
from numba import jit


def img16to8(img):
    """convert a 16 bit img to 8-bit image

    Parameter
    ------------
    img : np.array uint-16
        16-bit image 
    
    Return
    -------
    img_8 : np.array uint-8
        8 - bit image file

    """
    img_8 = (img/65535) * 255
    return img_8.astype('uint8')

def imshow(img):
    """show th image in external window

    Parameter
    ------------
    img : 
        8-bit or 16-bit image 

    """
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
    """invert the image

    Parameter
    ------------
    img : 8-bit or 16-bit image 

    Return
    ------------
    img_inv : 8-bit or 16-bit image 

    """
    if img.dtype == "uint8":
        print('the 8 bit image is inverted')
        img_inv = (255-img)
        return imagem
    elif img.dtype == 'uint16':
        img_inv = (65535 - img)
        print('the 16 bit image is inverted')
        return img_inv
    else:
        print("Error: the image has the wrong data type it must be either 8 bit or 16 bit")
    
    


def hist(img):
    """plot the histogram of the image

    Parameter
    ------------
    img : 8-bit or 16-bit image 

    Return
    ------------

    """

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
    """downscale the image with a percentage value

    Parameter
    ------------
    img : 

    scale_percent : int
        percent value 0% - 100 %

    Return
    ------------
    return img_smal:
        scaled down version of the image
    """
    # scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img_smal = cv2.resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img_smal


def auto_level(img, print_progress=False):
    """Automatically adjust the brightness values of the image.

    Parameter
    ------------
    img : 

    print_progress : bool

    Return
    ------------
    res : img
        auto level image as uint 8 or uint 16
    """

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


def apply_lut(img, table):
    """application of a look-up table to a image

    Parameter
    ------------
    img : 

    table : 

    Return
    ------------
    res : img
        image on which the lut was applied 
    """


    # Todo with numpay !!!
    i = 0
    j = 0
    
    image = img
    
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
    """change the gamma value of the image via a lut

    Parameter
    ------------
    img : 

    gamma : int

    Return
    ------------
    res : img
        image on which the gamma was applied 
    """

    # todo for 8 bit and 16 bit
    #uild a lookup table mapping the pixel values [0, 65535] to
    #heir adjusted gamma values
    table = np.array([((i / 65535.0) ** gamma) * 65535 
                      for i in np.arange(0, 65536)]).astype("uint16")
    # apply gamma correction using the lookup table
    img = apply_lut(table,image)
    
    return  img

def load_images_from_folder(folder): 
    """load all images of a given folder into a list

    Parameter
    ------------
    folder : str
        path to the folder

    Return
    ------------
    images : img
        a list containing the image data
    
     img_name : str
        a list containing the image file name
    """


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
