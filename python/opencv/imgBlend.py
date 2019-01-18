
import numpy as np
import cv2 as cv

dst=[]
k=0

def slideBar(x):
	#r = cv.getTrackbarPos('bili','dstWd')
	t=x/100.0
	print(x, t, 1-t)
	dst[:] = cv.addWeighted(img1,t,img2,1-t,0)	#切片法修改数组
	#cv.imshow('dstWd',dst)

	
img1 = cv.imread('cut.png')
img2 = cv.imread('cut2.png')

cv.namedWindow('dstWd')
cv.createTrackbar('bili','dstWd',0,100,slideBar)

dst = cv.addWeighted(img1,0.1,img2,0.9,0)	#初始化值
#cv.imshow('dstWd',dst)

while(1):
	#dst = cv.addWeighted(img1,t,img2,k,0)
	cv.imshow('dstWd',dst)
	#print("changed")
	
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break

cv.destroyAllWindows()