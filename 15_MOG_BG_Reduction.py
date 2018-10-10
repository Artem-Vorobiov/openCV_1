#		MOG Background Reduction OpenCV Python Tutorial

#	In this OpenCV with Python tutorial, we're going to be covering
#	 how to reduce the background of images, by detecting motion

import numpy as np
import cv2

# cap = cv2.VideoCapture('people-walking.mp4')
cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break
    

cap.release()
cv2.destroyAllWindows()