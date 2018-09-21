import cv2
import numpy as np

cap = cv2.VideoCapture(0)                           # <VideoCapture 0x104117eb0>    <class 'cv2.VideoCapture'>

while(1):

    _, frame = cap.read()                           #   массив 0 - 255  <class 'numpy.ndarray'>
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    #   Переводим из BGR в HSV
    
    lower_red = np.array([30,150,50])               #   Green
    upper_red = np.array([255,255,180])             #   Yellow
    
    mask = cv2.inRange(hsv, lower_red, upper_red)   #     <class 'numpy.ndarray'> 
    res = cv2.bitwise_and(frame,frame, mask= mask)  #     <class 'numpy.ndarray'> 

    kernel = np.ones((15,15),np.float32)/225
    # print('\n kernel: \n', kernel)                #     массив из 0.00444444
    # print('\n type(kernel): \n', type(kernel))    #     <class 'numpy.ndarray'>

    smoothed = cv2.filter2D(res,-1,kernel)
    # print('\n smoothed: \n', smoothed)             #     массив 
    # print('\n type(smoothed): \n', type(smoothed)) #     <class 'numpy.ndarray'>

    blur = cv2.GaussianBlur(res,(15,15),0)
    # print('\n blur: \n', blur)                     #     массив 
    # print('\n type(blur): \n', type(blur))         #     <class 'numpy.ndarray'>

    median = cv2.medianBlur(res,15)
    # print('\n median: \n', median)                 #     массив 
    # print('\n type(median): \n', type(median))     #     <class 'numpy.ndarray'>


    bilateral = cv2.bilateralFilter(res,15,75,75)
    # print('\n bilateral: \n', bilateral)             #     массив 
    # print('\n type(bilateral): \n', type(bilateral)) #     <class 'numpy.ndarray'>

    cv2.imshow('bilateral Blur',bilateral)
    cv2.imshow('Median Blur',median)
    cv2.imshow('Gaussian Blurring',blur)
    # cv2.imshow('Original',frame)
    # cv2.imshow('Averaging',smoothed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

# kernel = np.ones((15,15),np.float32)/225	#  Создан массив 15 на 15
# print('\n', kernel)