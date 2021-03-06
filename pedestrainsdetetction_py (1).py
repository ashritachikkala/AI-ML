# -*- coding: utf-8 -*-
"""pedestrainsdetetction.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bqfPcp3dGAGeKVXEQrMswCt_LkSs2IyS
"""

import cv2

from google.colab import files
file=files.upload()

from google.colab import files
file=files.upload()

body_classifier=cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap=cv2.VideoCapture('stock-footage-new-york-usa-people-and-cyclists-crossing-the-crossing-on-busy-street-in-new-york-city.mp4')

from google.colab.patches import cv2_imshow

while cap.isOpened():
    ret,frame=cap.read()
    bodies=body_classifier.detectMultiScale(frame,1.2,3)
    if ret ==True:
        for (x,y,w,h) in bodies:
            cv2.rectangle(frame,
                         (x,y),
                         (x+w,y+h),
                         (255,255,255),
                         5)
            cv2_imshow(frame)
    else :
        break
cap.release()
cv2.destroyAllWindows()