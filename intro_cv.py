import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1 converting
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE) # Can use IMREAD_COLOR; IMREAD_UNCHANGED; 
# 2 pop up
cv2.imshow('image',img)
# 3 Set up Key for exit
cv2.waitKey(0)
# 4 Exit functions
cv2.destroyAllWindows()