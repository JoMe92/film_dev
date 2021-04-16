# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:23:17 2020

@author: jonas
"""

import cv2

def boarder(img):
    # path_save = "D:/OneDrive/09 Instagramm/jonas.meier.photo/2020-12-27-Structure-of-Snow/2020-12-27/DSCF3890_wb.jpg"
    # img = cv2.imread("D:/OneDrive/09 Instagramm/jonas.meier.photo/2020-12-27-Structure-of-Snow/2020-12-27/DSCF3890.jpg")
    # img = cv2.imread("Img1x2.jpg")
    # img = cv2.imread("lena.tiff")
    x = img.shape[0]
    y = img.shape[1]
    white = [255,255,255]
    
    
    
    if (x/y < 1):
        
        if(x/y == 1/2):
            print("The img is a 2 by 1 img")      
        if(x/y == (2/3)):
           print("The img is a 3 by 2 img")
        else:
            print ("Its a Horizonatl Image"); 
            
        x_h = int(img.shape[1] * (5 / 4));
        
        top = (x_h - img.shape[0]) / 2; bottom = top;
        le = 0; ri = le;
    
        dst = cv2.copyMakeBorder(img, int(top), int(bottom), 0, 0, cv2.BORDER_CONSTANT);
       
        if (dst.shape[1]/dst.shape[0] != 0.8):
            print("err")
        else:
            print("The img is noh in a 4 by 5 format with boarder")
        
        return dst
          
    elif (x/y > 1): # Hochformat
        print(x/y)
        print ("Its a Vertical Image");
        x = img.shape[0] / 5 * 4;
        new_x = x - img.shape[1] / 2;
        top = ((x - img.shape[1]) / 2); bottom = top;
        le = (new_x); ri = le;
    
        dst = cv2.copyMakeBorder(img, 0, 0, int(top), int(bottom), cv2.BORDER_CONSTANT);
        return dst
        
    elif (x/y == 1):
        print(x/y)
        print("Its a squer img")
        # 3 by 2 aspact ratio
        x = img.shape[0] * (3/ 2);
        new_x = (x - img.shape[0]) / 2;
        top = 0; bottom = top;
        le = int(new_x); ri = le;
        dst = cv2.copyMakeBorder(img, top, bottom, le, ri, cv2.BORDER_CONSTANT, value = white);
      
    
        # y = dst.shape[1] * (5 / 4);
        # new_y = (y - dst.shape[1]) / 2;
        # top = abs(new_y); bottom = top;
        # le = 0; ri = le;
    
        # dst = cv2.copyMakeBorder(dst, int(top), int(bottom), le, ri, cv2.BORDER_CONSTANT, value = white);
        # cv2.imwrite(path_save ,dst)
        print ("Its a Horizonatl Image");
        x = dst.shape[0] / 5 * 4;
        new_x = (x - dst.shape[1]) / 2;
        top = abs((x - dst.shape[1]) / 2); bottom = top;
        le = (new_x); ri = le;
    
        dst = cv2.copyMakeBorder(dst, int(top), int(bottom), 0, 0, cv2.BORDER_CONSTANT, value = white);
        return dst
    
        
    
    else:
        print("Err")
            
            
    


