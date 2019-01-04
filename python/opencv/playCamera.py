
import numpy as np
import cv2 as cv
#cap = cv.VideoCapture(0)
cap = cv.VideoCapture('rtsp://192.168.0.60:43794/profile1')
#ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
#ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
#print(ret)
cv.namedWindow('frame', cv.WINDOW_NORMAL)	#you can resize window

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',frame)
    if (cv.waitKey(1) == ord('q') or cv.waitKey(1) == 27) :
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()