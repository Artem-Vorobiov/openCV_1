import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')	# <class 'numpy.ndarray'>   0 - 255	
# print(img.shape[:2])				# (281, 500)
# print(type(img.shape[:2]))		# <class 'tuple'>
mask = np.zeros(img.shape[:2],np.uint8)
# print(mask)				#  Создан массив из 0
# print(type(mask))			# <class 'numpy.ndarray'>

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (161,79,150,150)

# img - Input image
# mask - It is a mask image where we specify which areas are background, foreground or probable background/foreground etc.
# rect - It is the coordinates of a rectangle which includes the foreground object in the format (x,y,w,h)
# bdgModel, fgdModel - These are arrays used by the algorithm internally. 
# iterCount - Number of iterations the algorithm should run.
# mode - It should be cv.GC_INIT_WITH_RECT or cv.GC_INIT_WITH_MASK or combined which decides whether we are drawing rectangle or final touchup strokes.
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# Часть архитектуры этого процесса
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()