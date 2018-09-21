import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print('\n cap: \n', cap)                  #     <VideoCapture 0x104117eb0>
print('\n type(cap): \n', type(cap))      #     <class 'cv2.VideoCapture'>

while(1):
    _, frame = cap.read()
    # print('\n frame: \n', frame)                    #     массив 0 - 255
    # print('\n type(frame): \n', type(frame))        #     <class 'numpy.ndarray'>
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # print('\n hsv: \n', hsv)                        #     массив 0-255
    # print('\n type(hsv): \n', type(hsv))            #      <class 'numpy.ndarray'>
    
    lower_red = np.array([30,150,50])                 #     from green
    upper_red = np.array([255,255,180])               #     to yellow
    # print('\n lower_red: \n', lower_red)                  # массив с цифрасм 0-255
    # print('\n type(lower_red): \n', type(lower_red))      # <class 'numpy.ndarray'>
    
    #   cv2.inRange()   --   Checks if array elements lie between the elements of two other arrays.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    print('\n mask: \n', mask)                        #     массив 0-255
    print('\n type(mask): \n', type(mask))            #     <class 'numpy.ndarray'>
    #   cv2.bitwise_and --   Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar. 
    res = cv2.bitwise_and(frame,frame, mask= mask)
    print('\n res: \n', res)                          #     массив 0-255
    print('\n type(res): \n', type(res))              #     <class 'numpy.ndarray'>   

    cv2.imshow('frame',frame)                       #     Original
    cv2.imshow('mask',mask)                         #     BLACK AND WHITE
    cv2.imshow('res',res)                           #     GREEN AND RED
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

#   There are built in methods to OpenCV to convert BGR to HSV. 
#.  If you wanted to pick just a single color, then the BGR to HSV would be great to use.
dark_red  = np.uint8([[[12,22,121]]])
dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)