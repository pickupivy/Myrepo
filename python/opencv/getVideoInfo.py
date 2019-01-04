
import cv2

cap=cv2.VideoCapture("bb.mkv")

if cap.isOpened():
	width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("width="+str(width)+", height="+str(height))