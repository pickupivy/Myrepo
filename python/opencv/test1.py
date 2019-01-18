
import numpy as np
import cv2 as cv
from cvFunc import *

# img=cv.imread('cut.png')
# prtImgPrpt(img)
# for pixel in img[0:4, 0:1]:
	# print(pixel)

# ball = img[380:440, 330:390]
# img[273:333, 100:160] = ball

# cv.imshow('ha', img)
# k=cv.waitKey(0)

# img1 = cv.imread('cut.png')
# prtImgPrpt(img1)
# img2 = cv.imread('cut2.png')
# prtImgPrpt(img2)
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow('dst',dst)

img=cv.imread("testraw.png")
dst=shrink(img)
cv.imshow("1", img)
cv.imshow("2", dst)
#cv.imwrite("testraw0.png", img)

cv.waitKey(0)
cv.destroyAllWindows()
