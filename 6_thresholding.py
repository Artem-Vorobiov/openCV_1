import cv2
import numpy as np

# 	ИДЕЯ ----- есть картинка, в плохом качестве, плохо видно детали. Пропускаю через фильтр и видно отлично!


img = cv2.imread('bookpage.jpg')
# img = cv2.imread('inn.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# cv2.imshow('original',img)
# cv2.imshow('threshold',threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#				=======.      MAIN.      =======

# th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 10)

# print('\n th: \n', th)					# массив с цифрасм 0-255
# print('\n type(th): \n', type(th)) 		# <class 'numpy.ndarray'>
# cv2.imshow('original',img)
# cv2.imshow('Adaptive threshold',th)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# retval2,threshold2 = cv2.threshold(grayscaled,115,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imshow('original',img)
# cv2.imshow('Otsu threshold',threshold2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()