import cv2
import numpy as np

#	Я создал две переменные - массивы, затем внес эти переменные 
# 	в функцию cv2.imshow()  и мне программа отобразила эти массивы
# 	в виде ччерных кважратов. Размеры равны размерности массива



while(1):

	game = np.zeros((2, 3, 3), np.uint8)
	print(game)

	print('\n')
	print('\t NEXT:')
	game_data = np.zeros((200, 176, 3), np.uint8)
	print(game_data)

	cv2.imshow('Intel', game)
	cv2.imshow('GAME_DATA', game_data)
	cv2.waitKey(1)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()