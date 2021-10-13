import cv2
from matplotlib import pyplot as plt
from src import core
img = cv2.imread(r'C:\Users\jonas\Development\film_dev\files\img_pos.jpg',0)
  
# alternative way to find histogram of an image
plt.hist(img.ravel(),256,[0,256])
plt.show()

img_level = core.level_img(img,10,240)

# alternative way to find histogram of an image
plt.hist(img_level.ravel(),256,[0,256])
plt.show()