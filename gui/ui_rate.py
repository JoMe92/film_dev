# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rateDQqDLN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog
# from PySide2.QtGui import (QImage, QPixmap)
from PySide2.QtWidgets import *

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QImage)


import cv2, imutils




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(719, 1114)
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionOpen_Image = QAction(MainWindow)
        self.actionOpen_Image.setObjectName(u"actionOpen_Image")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../files/img_neg.jpg"))

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout_2.addWidget(self.pushButton_open)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_2.addWidget(self.pushButton_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_8_convert = QPushButton(self.centralwidget)
        self.pushButton_8_convert.setObjectName(u"pushButton_8_convert")

        self.horizontalLayout.addWidget(self.pushButton_8_convert)

        self.pushButton_left = QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName(u"pushButton_left")

        self.horizontalLayout.addWidget(self.pushButton_left)

        self.pushButton_right = QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName(u"pushButton_right")

        self.horizontalLayout.addWidget(self.pushButton_right)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_8_convert.clicked.connect(self.label.clear)
        self.pushButton_right.clicked.connect(self.label.clear)
        self.pushButton_left.clicked.connect(self.label.clear)
        self.pushButton_open.clicked.connect(self.label.clear)
        self.pushButton_save.clicked.connect(self.label.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionOpen_Image.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.label.setText("")
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_8_convert.setText(QCoreApplication.translate("MainWindow", u"convert", None))
        self.pushButton_left.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.pushButton_right.setText(QCoreApplication.translate("MainWindow", u"-->", None))
    # retranslateUi


    def loadImage(self):
        """ load an image
        
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

    def setPhoto(self,image):
        """ This function will take image input and resize it 
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def update(self):
        """ This function will update the photo according to the 
            current values of blur and brightness and set it to photo label.
        """
        img = self.convert(self.image)
        self.setPhoto(img)

    def savePhoto(self):
        """ This function will save the image"""
        # here provide the output file name
        # lets say we want to save the output as a time stamp
        # uncomment the two lines below

        # import time
        # filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'

        # Or we can give any name such as output.jpg or output.png as well
        # filename = 'Snapshot.png'	

        # Or a much better option is to let user decide the location and the extension
            # using a file dialog.

        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]

        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',self.filename)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyshine photo editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


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
            
    def convert(self, image):
        ''' concert the image'''
        img_lev = auto_level(image) # Auto adjust the r,g,b chanell of the image to match the collor chanels
        img_pos = invert(img_lev) # invert the leveled image
        return image