import cv2
import numpy as np

# 	ИДЕЯ ---->>>> есть 2 картинки, мы накладываем одну картинку на другую

# Load two images
img1 = cv2.imread('Matplotlib.png')		# Считывание фото, формат  <class 'numpy.ndarray'>
img2 = cv2.imread('mainlogo.png')		# Имеет вид масства с ячейками 0-255


# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape		# rows 126, cols 126, channels 3
print('\n ROWS: \n', rows)			
print('\n COLS: \n', cols)
print('\n Channels: \n', channels)
# print('\n img2: \n', img2)
print('\n type(img2): \n', type(img2)) 				#	 <class 'numpy.ndarray'>
print('\n img2.shape: \n', img2.shape)				# 	 (126, 126, 3)
print('\n type(img2.shape): \n', type(img2.shape))	#	 <class 'tuple'>



roi = img1[0:rows, 0:cols]			# Выбрали область пикселей на картинке 1
print('\n roi: \n', roi)
print('\n type(roi): \n', type(roi)) 				# 	 <class 'numpy.ndarray'>

#		EXPERIMENT
roi100 = img1[100:104, 100:104]						#	[[[3x4],[3x4],[3x4],[3x4]]]
print('\n roi100: \n', roi100)
print('\n type(roi100): \n', type(roi100)) 



# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)	# 	изменили цвет 2 картинки. Заменили цифры в массиве
print('\n img2gray: \n', img2gray)					#	массив
print('\n type(img2gray): \n', type(img2gray)) 		#	<class 'numpy.ndarray'>


# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)	# фильтр, заменяет цифры в массиве
#  А имеено аолгоритм проходится по цифрам в массиве и подбирает оптимальное соотношение
print('\n ret: \n', ret)							#	 220.0
print('\n type(ret): \n', type(ret)) 				# 	<class 'float'>
print('\n mask: \n', mask)							#	 массив
print('\n type(mask): \n', type(mask)) 				# 	<class 'numpy.ndarray'>
	
#	Inverts every bit of an array
mask_inv = cv2.bitwise_not(mask)					#   работает с массивом цифр(пиксели)
print('\n mask_inv: \n', mask_inv)					#	 массив
print('\n type(mask_inv): \n', type(mask_inv)) 		# 	class 'numpy.ndarray'>


# Now black-out the area of logo in ROI
# 	Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)	# Затемняем область под лого
print('\n img1_bg: \n', img1_bg)					#	 массив
print('\n type(img1_bg): \n', type(img1_bg)) 		# 	class 'numpy.ndarray'>
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)	# Берем лого

# 	Calculates the per-element sum of two arrays or an array and a scalar.
dst = cv2.add(img1_bg,img2_fg)						#	Добавляем лого к существующей картинке
print('\n img1_bg: \n', img1_bg)					#	 массив
print('\n type(img1_bg): \n', type(img1_bg)) 		# 	class 'numpy.ndarray'>

img1[0:rows, 0:cols ] = dst 						# 	Присваем этой области - картинку


# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()