import cv2
import numpy as np

# Load two images
img1 = cv2.imread('Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape		# Разложили на массив данных картинку 2
roi = img1[0:rows, 0:cols]			# Выбрали область пикселей на картинке 1

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)	# изменили цвет 2 картинки

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)	# ПОРОГ ???!!!
	
mask_inv = cv2.bitwise_not(mask)	# МАСКА ???!!!

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)	# Затемняем область под лого

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)	# Берем лого

dst = cv2.add(img1_bg,img2_fg)	#	Добавляем лого к существующей картинке
img1[0:rows, 0:cols ] = dst 	# 	Присваем этой области - картинку
 
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()