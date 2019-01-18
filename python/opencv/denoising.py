
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('testraw.png')
# for a in range(1,10):
	# img = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()

cv.imshow("testwindow",dst)
#cv.imwrite("testraw000.png", dst)

cv.waitKey(0)
cv.destroyAllWindows()
