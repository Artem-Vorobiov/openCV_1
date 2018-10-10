import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()                           #   массив 0 - 255  <class 'numpy.ndarray'>
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    #   Переводим из BGR в HSV
    
    lower_red = np.array([30,150,50])               #   Green
    upper_red = np.array([255,255,180])             #   Yellow
    
    mask = cv2.inRange(hsv, lower_red, upper_red)   #     <class 'numpy.ndarray'> 
    res = cv2.bitwise_and(frame,frame, mask= mask)  #     <class 'numpy.ndarray'>

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    # print('\n laplacian: \n', laplacian)                  #     массив не редко встречаются отрицательные значения
    # print('\n type(laplacian): \n', type(laplacian))      #     <class 'numpy.ndarray'>

    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    print('\n sobelx: \n', sobelx)                          #     массив не редко встречаются отрицательные значения
    print('\n type(sobelx): \n', type(sobelx))              #     <class 'numpy.ndarray'>
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)      

    cv2.imshow('Original',frame)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('laplacian',laplacian)
    # cv2.imshow('sobelx',sobelx)
    # cv2.imshow('sobely',sobely)

    edges = cv2.Canny(frame,100,200)
    # print('\n edges: \n', edges)                    #     массив 
    # print('\n type(edges): \n', type(edges))        #     <class 'numpy.ndarray'>
    
    cv2.imshow('Edges',edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()