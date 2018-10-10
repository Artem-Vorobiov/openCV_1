import numpy as np
import cv2
import matplotlib.pyplot as plt

# Примеры из видео!
# img1 = cv2.imread('opencv-feature-matching-template.jpg',0)
# img2 = cv2.imread('opencv-feature-matching-image.jpg',0)

# Мои собственные примеры
# Важный момент - Обе картинки должны быть с похожим Размером изображения
img1 = cv2.imread('1.png',0)
img2 = cv2.imread('22.png',0)

# This is the detector we're going to use for the features.
orb = cv2.ORB_create()
# print('\n orb', orb)				# <ORB 0x105f7fd30>
# print('\n TYPE', type(orb))		# <class 'cv2.ORB'>

# Here, we find the key points and their descriptors with the orb detector
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# print('\n kp1', kp1)			#	[<KeyPoint 0x119c8bf60>, ...  <KeyPoint 0x119d315d0>]
# print('\n des1', des1)		#	[[ 37 169 136 ... 234  94 224] ... [251 128 174 ... 172 124  82]]
# print('\n TYPE', type(kp1))	#	<class 'list'>

# This is our BFMatcher object.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# print('\n bf', bf)			# <BFMatcher 0x119c7fef0>
# print('\n TYPE', type(bf))	# <class 'cv2.BFMatcher'>

# Here we create matches of the descriptors, then we sort them based on their distances.
matches = bf.match(des1,des2)
# print('\n matches', matches)	# [<DMatch 0x119c7aed0>, ... <DMatch 0x119d2dc50>]
# print('\n bf', type(matches))	# <class 'list'>
matches = sorted(matches, key = lambda x:x.distance)

# Here, we've drawn the first 10 matches
# (img1, keypoints1, img2, keypoints2, matches1to2[, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]]) → outImg
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
# print('\n img3', img3)			# Array 0 - 255
# print('\n TYPE', type(img3))	# <class 'numpy.ndarray'>
plt.imshow(img3)
plt.show()