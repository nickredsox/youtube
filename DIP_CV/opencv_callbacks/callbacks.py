import cv2

def getXY(evt, x,y, flags, userdata ):
	if evt == cv2.EVENT_LBUTTONDOWN:
		print("X: " + str(x) + " Y: " + str(y))
		value = im[y,x]
		print("B: " + str(value[0]) + " G: " + str(value[1]) + 
			" R: " + str(value[2])) 



im = cv2.imread('color_bars.png')
window_title = "Color Bars"


cv2.imshow(window_title, im)
cv2.setMouseCallback(window_title, getXY, "Hello")
cv2.waitKey(0)
