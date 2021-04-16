# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:05:41 2021

@author: Jonas Meier

Automaticly crop Images scaned with pulstak 

"""
import cv2
import numpy as np
import rawpy
import core as co


path = 'F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (8).dng'
raw_neg = rawpy.imread(path)

lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)

img = lin16bit
img = co.invert(img)
img = co.adjust_gamma(img, 2.4)

co.imshow(img)

gray = co.img16to8(img)

gray = cv2.bilateralFilter(gray, 10, 25, 25)
# gray = cv2.equalizeHist(gray)
# clahe = cv2.createCLAHE(clipLimit=5, tileGridSize=(7,7))
# gray = clahe.apply(gray)

_, ignoreMask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

co.imshow(ignoreMask)

kernel = np.ones((10,10),np.uint8)
ignoreMask = cv2.dilate(ignoreMask, kernel, iterations = 5)


img = cv2.imread("lenna.png")

# crop_img = img[y:y+h, x:x+w]




#%% # Select boarder by click
import pygame, sys
from PIL import Image
import cv2
import numpy as np
import rawpy
import core as co
pygame.init()


def displayImage(screen, px, topleft, prior):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width =  pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn't moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    # return current box extents
    return (x, y, width, height)


def setup(img):
    px = pygame.image.frombuffer(img.tostring(), img.shape[1::-1], "RGB")
    # px = pygame.image.load(path)
    screen = pygame.display.set_mode( px.get_rect()[2:] )
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px

def mainLoop(screen, px):
    topleft = bottomright = prior = None
    n=0
    while n!=1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    n=1
        if topleft:
            prior = displayImage(screen, px, topleft, prior)
    return ( topleft + bottomright )



path = 'F:/01Img/Analog-Photography/2021-01-15-Agfa100-Muenchen/Img00 (8).dng'
raw_neg = rawpy.imread(path)

lin16bit = raw_neg.postprocess(gamma=(1,1),no_auto_bright=True, output_bps=16)

img = lin16bit
img = co.invert(img)
img = co.adjust_gamma(img, 2.4)
img_16 = img

img = co.img16to8(img)
img = cv2.merge((img,img,img))


screen, px = setup(img)
left, upper, right, lower = mainLoop(screen, px)

# ensure output rect always has positive width, height
if right < left:
    left, right = right, left
if lower < upper:
    lower, upper = upper, lower
    


img_16_crop = img_16[upper:lower, left:right, :]
co.imshow(img_16_crop)


