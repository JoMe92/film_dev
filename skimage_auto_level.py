# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:50:52 2020

@author: Jonas Meier
"""

from skimage import data
from skimage.morphology import disk, ball
from skimage.filters.rank import autolevel
import numpy as np
import rawpy
import core as co 
import cv2

path = "F:/01Img/2019/02_Februar/2019-02-16/IMG_5122.CR2"
# path = "D:/OneDrive/Bilder/HuaweiP20/2020-03-20/IMG_20200320_122022.dng"
# load the raw file
raw_neg = rawpy.imread(path)

lin16bit = raw_neg.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=16)


img = lin16bit
uint14_max = 2**14 - 1#
co.hist(img)

volume = np.random.randint(0, uint14_max, size=(10,10,10), dtype=np.uint16)


b,g,r = cv2.split(img)

auto = autolevel(b, disk(5))
co.hist(auto)

auto_vol = autolevel(volume, ball(5))
