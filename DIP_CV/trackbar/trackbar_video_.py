import cv2
import numpy as np

window = 'Lilly'

thresh1 = 100
max_thresh1 = 255
thresh2 = 200
max_thresh2 = 255

def change_thresh1(val):
    global thresh1
    thresh1 = val

def change_thresh2(val):
    global thresh2 
    thresh2 = val

def perform_operation(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, int(thresh1), int(thresh2))
    cv2.imshow(window, canny)

cap = cv2.VideoCapture(1)

cv2.namedWindow(window)
cv2.createTrackbar("Thresh1", window, thresh1, max_thresh1, change_thresh1)
cv2.createTrackbar("Thresh2", window, thresh2, max_thresh2, change_thresh2)
#cv2.waitKey(0)

while True:
    ret, frame = cap.read()
    perform_operation(frame)
    

    if cv2.waitKey(1) == ord('q'):
        break

