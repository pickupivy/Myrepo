
import numpy as np
import cv2
cap = cv2.VideoCapture('bb.mkv')
#frame = cv2.imread("11.png")
count=0
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	#第一个参数ret的值为True或False，代表有没有读到图片
	#第二个参数是frame，是当前截取一帧的图片。
	#read()函数返回两个参数，所以才这么写。	
	if ret == True:
		cv2.imshow('frame', frame)
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#cv2.imshow('frame', gray)
		#cv2.waitKey(5)
	else:
		cap.release()	#窗口释放
		#cv2.waitKey(0)
		#count=count+1
		#print(str(count)+"\n")
		break
	#count=count+1
	#if count >= 300:
		#break
	if cv2.waitKey(5) == ord('q'):
		break

#cap.release()	
cv2.destroyAllWindows()
