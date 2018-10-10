import cv2
import numpy as np

cap = cv2.VideoCapture(0)            # <VideoCapture 0x104117eb0>    <class 'cv2.VideoCapture'>


#   1. Подписать недостающие функции
#   2. Доописать оставшиеся уроки
#


while(1):

    _, frame = cap.read()                               #   массив 0 - 255  <class 'numpy.ndarray'>
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)        #   Переводим из BGR в HSV
    
    lower_red = np.array([30,150,50])                   #   Green
    upper_red = np.array([255,255,180])                 #   Yellow
    
    #   cv2.inRange()   --   Checks if array elements lie between the elements of two other arrays.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #   cv2.bitwise_and --   Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar. 
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
    # print('\n kernel: \n', kernel)                    #     массив из едениц
    # print('\n type(kernel): \n', type(kernel))        #     <class 'numpy.ndarray'>

    #   cv2.erode().   --
    erosion = cv2.erode(mask,kernel,iterations = 1)
    # print('\n erosion: \n', erosion)                  #     массив из нулей. Дополняем нули
    # print('\n type(erosion): \n', type(erosion))      #     <class 'numpy.ndarray'>

    #   cv2.dilate()    --
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    # print('\n dilation: \n', dilation)                #     массив из нулей. Дополняем 255ки
    # print('\n type(dilation): \n', type(dilation))    #     <class 'numpy.ndarray'>

    #   v2.morphologyEx --
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # print('\n opening: \n', opening)                    #     массив 
    # print('\n type(opening): \n', type(opening))        #     <class 'numpy.ndarray'>

    #   cv2.morphologyEx --
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # print('\n closing: \n', closing)                    #     массив 
    # print('\n type(closing): \n', type(closing))        #     <class 'numpy.ndarray'>


    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)

    cv2.imshow('Mask',mask)
    # cv2.imshow('Original',frame)
    # cv2.imshow('Erosion',erosion)
    # cv2.imshow('Dilation',dilation)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()