import cv2
import numpy
from matplotlib import pyplot as plt
 
img = cv2.imread("11.jpg")
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
