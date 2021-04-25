# -*- coding: utf-8 -*-
"""carplatedetection.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_5hN49pE9UhUB-AuyHnHWJm8Sq3DTtRt
"""

from google.colab import files
file=files.upload()

from google.colab import files
file=files.upload()

import numpy as np
import cv2 
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

plate_classifier=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

img = cv2.imread('plate.png')
def display(img):
    fig=plt.figure(figsize=(10,8))
    ax=fig.add_subplot(111)
    new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)

display(img)

def detect_plate(img):
    plate_img=img.copy()
    plate_rects=plate_classifier.detectMultiScale(plate_img,1.1,1)
    for (x,y,w,h) in plate_rects:
        cv2.rectangle(plate_img,
                     (x,y),
                     (x+w,y+h),
                     (255,255,0),
                     4)
    return plate_img

result=detect_plate(img)
display(result)