import cv2

#Load image
im = cv2.imread("images/dog.jpg")

#Display image
cv2.imshow("Dog image", im)
cv2.waitKey(0)