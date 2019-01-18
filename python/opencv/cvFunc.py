
import numpy as np
import cv2 as cv

def shrink(image,w_rate,h_rate,skMode=0):
	height, width = image.shape[:2]
	#print(image.shape[:2])
	size = (int(width*0.5), int(height*0.5))
	shrink_NEAREST = cv.resize(image, size, interpolation=cv.INTER_NEAREST)
	return shrink_NEAREST
# shrink_LINEAR = cv.resize(image, size, interpolation=cv.INTER_LINEAR)
# shrink_AREA = cv.resize(image, size, interpolation=cv.INTER_AREA)
# shrink_CUBIC = cv.resize(image, size, interpolation=cv.INTER_CUBIC)
# shrink_LANCZOS4 = cv.resize(image, size, interpolation=cv.INTER_LANCZOS4)

def prtImgPrpt(image):
	print(image.shape)
	print(image.size)
	print(image.dtype)


