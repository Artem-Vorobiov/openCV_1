import cv2
import numpy as np

# 1. Загружаем исходную картинку
# 2. Изменяем цветовую схему
# 3. Загружаем шаблон
# 4. Определили Форму массива Шаблона
# 5. Используя функцию cv2.matchTemplate() сравниваемк картинку и шаблом, на выходе получаем массив -1 до 1
# 6. Ставим порог 0.8, все что больше искомый объект
# 7. Проходимся по всем объектам и обводим их прямоугольником

# print('\n img_rgb', img_rgb)
# print('\n TYPE', type(img_rgb))
A = [0,1,2,3,4,5]
for a in A[::-1]:
	print(a)		# Backwards = 5,4,3,2,1,0

while(1):

# Use the function cv2.imread() to read an image.
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

	img_rgb = cv2.imread('1.png')
	# print('\n img_rgb', img_rgb)								#	0 - 255		
	# print('\n TYPE', type(img_rgb))							#	<class 'numpy.ndarray'>

# Converts an image from one color space to another
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Loads image in grayscale mode
	template = cv2.imread('2.png',0)
	# print('\n template', template)		#	Все 255
	# print('\n TYPE', type(template))		#	<class 'numpy.ndarray'>

# We load the template and note the dimensions.
	w, h = template.shape[::-1]
	# print('\n w', w)					#	164
	# print('\n TYPE', type(w))			#	<class 'int'>
	# print('\n h', h)					#	138
	# print('\n TYPE', type(h))			#	<class 'int'>

# Compares a template against overlapped image regions.
# cv2.matchTemplate(image, templ, method[, result]) → result
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	# print('\n res', res)					#	массив от -1 до 1
	# print('\n TYPE', type(res))			#	<class 'numpy.ndarray'>

	threshold = 0.8
# Return elements, either from x or y, depending on condition.
# Здесь имеем массив с элементами(включает их месторасположение) совпавшими на картинке
	loc = np.where( res >= threshold)
	# print('\n loc', loc)					#	 loc (array([149, 149, 149, ..., 399, 399, 399]), array([1115, 1116, 1117, ..., 2329, 2330, 2331]))
	# print('\n TYPE', type(loc))			#	 TYPE <class 'tuple'>

# cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None

	for pt in zip(*loc[::-1]):
		print('\n pt', pt)				#	(1115, 149), (1116, 149)...(2330, 399), (2331, 399)
		print('\n TYPE', type(pt))		#	<class 'tuple'>
# pt это первая точка для прамоугольника, прибавляем к ней значения w,h и получаем вторую точку pt2
# В следующей строке мы создали прямоугольник который обводит искомый предмет !
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

	cv2.imshow('Detected',img_rgb)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()