import numpy as np
import cv2

while(1):

	img = cv2.imread('opencv-corner-detection-sample.jpg')
# Converts an image from one color space to another
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)

# Determines strong corners on an image.
# cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) → corners
	corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
	corners = np.int0(corners)
	# print('\n corners', corners)			#  [[[ 92 166]] ...  [[203 288]]]]
	# print('\n TYPE', type(corners))		#  <class 'numpy.ndarray'>

	for corner in corners:
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.ravel(x)) ---> [1 2 3 4 5 6]
	    x,y = corner.ravel()
	    # print('\n x', x)			#	101
	    # print('\n y', y)			#	156
	    # print('\n type', type(x))	#	<class 'numpy.int64'>
# cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) → None
	    cv2.circle(img,(x,y),3,255,-1)
	    
	cv2.imshow('Corner',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()