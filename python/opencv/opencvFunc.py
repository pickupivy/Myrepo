
import numpy as np
import cv2 as cv

class Window():
	
	def __init__(self, winName, imgName):
		self.winName=winName
		self.imgName=imgName
		

	


drawing = False # true if mouse is pressed
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def print_opencv_events():
	events = [i for i in dir(cv) if 'EVENT' in i]
	for item in events:
		print( item )

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(g_img,(x,y),10,(255,0,0),-1)

# mouse callback function
def draw_circle2(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(g_img,(ix,iy),(x,y),(0,255,0),1)
            else:
                cv.circle(g_img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(g_img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv.circle(g_img,(x,y),5,(0,0,255),-1)

#print_opencv_events()

# Create a black image, a window and bind the function to window
g_img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle2)
#(Name of the window, Callback function for mouse events)

while(1):
    cv.imshow('image',g_img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()

