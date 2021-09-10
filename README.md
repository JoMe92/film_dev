# Film_Developing
The range of commercially available software for editing input film material is very limited.  In addition, the solutions offered on the market do not make it clear which process steps are carried out. For example, film profiles such as Kodak gold, Fuji 200, etc. are stored, but it is not clear how the image data is processed. Therefore, the goal of this project is to save the image data in a "raw" format and to process the images in software solutions such as Lightromm or Capture one. Therefore a program has to be developed that allows to read and process the image data. The difficulty also lies in the fact that there are a variety of methods for the digitization of ngeatives. The project will focus on the Pulstake 8000 scanner and data obtained with a Fuji XE-3.
## main Task:
- Reading unprocessed 16-bit or 8-bit image Data 
- applay all nesserery processing steps to get an positiv image
- do some basic image processing 

## How to use 

The initial image is the scan of a negative image. The image should be processed as little as possible. In Silverfast the image should be scanned as a 48 bit raw image to get an unprocessed negative image.
![Text](img_neg.jpg)

The r-g-b sensitivity of the film depends on the used film stock, these chanels must be aligned.
img_lev = src.core.auto_level(img_neg) 
adjust the color channels of the image

![Text](img_lev.jpg)


The negative image can then be inverted to obtain a positive image.


![Text](img_pos.jpg)