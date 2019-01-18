
import numpy as np
import cv2 as cv

class Window():
	
	def __init__(self, winName, imgName, isCircle):
		self.winName=winName
		self.imgName=imgName
		self.drawing=False	# true if mouse is pressed
		self.isCircle=isCircle	#if True, draw circle; else, draw rectangle
		self.ix=-1
		self.iy=-1
		self.setCalBckFunc()
		#self.print_opencv_events()
	
	# mouse callback function
	def drawCircle(self,event,x,y,flags,param):
		if event == cv.EVENT_LBUTTONDBLCLK:
			cv.circle(self.imgName,(x,y),10,(255,0,0),-1)
	
	# mouse callback function	
	def drawCircle2(self,event,x,y,flags,param):
		if event == cv.EVENT_LBUTTONDOWN:
			self.drawing = True
			self.ix,self.iy = x,y
		elif event == cv.EVENT_MOUSEMOVE:
			if self.drawing == True:
				if self.isCircle == True:
					cv.circle(self.imgName,(x,y),5,(0,0,255),-1)	#BGR		
				else:
					cv.rectangle(self.imgName,(self.ix,self.iy),(x,y),(0,255,0),1)	#BGR
		elif event == cv.EVENT_LBUTTONUP:
			self.drawing = False
			if self.isCircle == True:
				cv.circle(self.imgName,(x,y),5,(0,0,255),-1)	#BGR	
			else:
				cv.rectangle(self.imgName,(self.ix,self.iy),(x,y),(0,255,0),1)	#BGR
	
	def setCalBckFunc(self):	
		cv.setMouseCallback(self.winName,self.drawCircle2)
		#(Name of the window, Callback function for mouse events)
		
	def print_opencv_events(self):
		events = [i for i in dir(cv) if 'EVENT' in i]
		for item in events:
			print( item )

#drawing = False # true if mouse is pressed
#mode = False # if True, draw rectangle. Press 'm' to toggle to curve
#ix,iy = -1,-1

# mouse callback function
# def draw_circle(event,x,y,flags,param):
    # if event == cv.EVENT_LBUTTONDBLCLK:
        # cv.circle(g_img,(x,y),10,(255,0,0),-1)

# mouse callback function
# def draw_circle2(event,x,y,flags,param):
    # global ix,iy,drawing,mode
    # if event == cv.EVENT_LBUTTONDOWN:
        # drawing = True
        # ix,iy = x,y
    # elif event == cv.EVENT_MOUSEMOVE:
        # if drawing == True:
            # if mode == True:
                # cv.rectangle(g_img,(ix,iy),(x,y),(0,255,0),1)
            # else:
                # cv.circle(g_img,(x,y),5,(0,0,255),-1)
    # elif event == cv.EVENT_LBUTTONUP:
        # drawing = False
        # if mode == True:
            # cv.rectangle(g_img,(ix,iy),(x,y),(0,255,0),1)
        # else:
            # cv.circle(g_img,(x,y),5,(0,0,255),-1)

# Create a black image, a window and bind the function to window
g_img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
#cv.setMouseCallback('image',draw_circle2)

win1=Window('image',g_img,False)

while(1):
    cv.imshow('image',g_img)
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()

