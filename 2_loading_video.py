import numpy as np
import cv2


# This return video from webcam
cap = cv2.VideoCapture(0)

while(True):
	# Probably transform video to specific type of code
    ret, frame = cap.read()
    # Change color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the video
    cv2.imshow('frame',gray)
    # Statment for close the process
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stopping
cap.release()
# Closing
cv2.destroyAllWindows()