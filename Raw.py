# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:22:13 2020

@author: Jonas Meier
"""

import rawpy
import core as co
from matplotlib.pyplot import imshow

path = "F:/01Img/Analog-Photography/2020/2020-01-01 Fuji Superia Xtra 400 - jan -märz 2020/Img22.dng"
path = "F:/01Img/2019/02_Februar/2019-02-16/IMG_5122.CR2"

raw_neg = rawpy.imread(path)


# rgb_base_linear = raw_neg.postprocess(output_color=rawpy.ColorSpace.raw, gamma=(1, 1),
#                                        user_wb=[1.0, 1.0, 1.0, 1.0], no_auto_bright=True)
# imshow(rgb_base_linear)


# 16 bit linear

# lin16bit = raw_neg.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=16)
lin16bit = raw_neg.postprocess(no_auto_bright=True, output_bps=16)
# Some Parameters
colorMatrix = raw_neg.color_matrix
rgb_xyz_matrix = raw_neg.rgb_xyz_matrix
camera_whitebalance = raw_neg.camera_whitebalance
color_desc = raw_neg.color_desc
raw_image = raw_neg.raw_image
raw_type = raw_neg.raw_type
tone_curve = raw_neg.tone_curve




def img16to8(img):
   img_8 = (img/65535) * 255
   
   return img_8.astype('uint8')



# Leveld = co.auto_level(lin16bit)
# positiv = co.invert(Leveld)
poisitiv8 = img16to8(positiv)

imshow(poisitiv8)
