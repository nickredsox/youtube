import cv2
import numpy as np

#brightness im + offset
#contrast   im*contrast
#im *contrast + brightness
im = cv2.imread('lilly.jpg')
im = np.float32(im/255)
window = 'Lilly'
contrast = 10
max_contrast = 100
brightness = 0
max_brightness = 100

def change_contrast(val):
	global contrast
	contrast = val/10
	perform_operation()

def change_brightness(val):
	global brightness 
	brightness = val/100
	perform_operation()

def perform_operation():
	im1 = im*contrast + brightness
	cv2.imshow(window, im1)

cv2.imshow(window, im)
cv2.createTrackbar("Contrast", window, contrast, max_contrast, change_contrast)
cv2.createTrackbar("Brightness", window, brightness, max_brightness, change_brightness)
cv2.waitKey(0)