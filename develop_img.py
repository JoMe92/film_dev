import cv2
import numpy as np
import test
import src.core
import src.noise




img_neg = cv2.imread(r"C:\Users\jonas\Development\film_dev\img14.tif",-1) # load a 16-bit negative image
img_neg = src.core.scale_percent(img_neg,20) # downscale to 50% of the image size
img_lev = src.core.auto_level(img_neg) # Auto adjust the r,g,b chanell of the image to match the collor chanels
img_pos = src.core.invert(img_lev) # invert the leveled image
# img_gamma = src.core.gamma(img_pos,3)

# save the image as 8 bit jpg file
cv2.imwrite("files\\img_neg.jpg", src.core.img16to8(img_neg))
cv2.imwrite("files\\img_lev.jpg", src.core.img16to8(img_lev))
cv2.imwrite("files\\img_pos.jpg", src.core.img16to8(img_pos))
# cv2.imwrite("img_gamma.jpg", src.core.img16to8(img_gamma))
print("end")


img_nois = src.noise.noisy("gauss", src.core.img16to8(img_pos))
cv2.imwrite("files\\img_noise.jpg", img_nois)