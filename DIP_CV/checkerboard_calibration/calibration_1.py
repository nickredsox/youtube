import cv2
import os
import numpy as np
import glob

# make a connection with the webcam and display
# capture images using a mouse callback and save them
# do the calibration and undistort and display the image. Static and video

def make_webcam_connection(capture_device):
    cap = cv2.VideoCapture(capture_device)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    return cap

def save_images(evt, x, y, flags, userdata):
    if evt == cv2.EVENT_LBUTTONDOWN:
        frame, num_image_counter = userdata
        print(num_image_counter[0])
        os.makedirs("./images1", exist_ok = True)
        cv2.imwrite("./images1/" + str(num_image_counter[0]) + ".jpg", frame)
        num_image_counter[0] += 1


def capture_images(cap, window_title, num_images):
    num_images_taken = [0]
    while num_images_taken[0] < num_images:
        ret, frame = cap.read()
        cv2.imshow(window_title, frame)
        cv2.setMouseCallback(window_title, save_images, [frame, num_images_taken])
        if cv2.waitKey(1) == ord('q'):
            break

def perform_calibration(cap):
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    rows = 7
    cols = 10

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((rows*cols,3), np.float32)
    objp[:,:2] = np.mgrid[0:cols,0:rows].T.reshape(-1,2)
     
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
     
    images = glob.glob('images/*.png')
    
    image_num = 0
    for image in images:
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (rows,cols), None)
     
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
     
            corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)
     
            # Draw and display the corners
            cv2.drawChessboardCorners(img, (rows,cols), corners2, ret)
            cv2.imshow('img', img)
            cv2.imwrite("checkerboards/" + str(image_num) + ".jpg", img)
            cv2.waitKey(500)
        image_num += 1

    #Calibration !!
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    img = cv2.imread("images/1.png")
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)

    while True:
        #img = cv2.imread("images1/1.jpg")
        ret, img = cap.read()
       # h, w = img.shape[:2]
        
        #Undistort
        #dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
        cv2.imshow("Undistorted image", dst)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == "__main__":

    capture_device = 2
    window_title = "Image"

    #Typically be between 15-30 images for calibration
    num_images = 5

    cap = make_webcam_connection(capture_device)
    #capture_images(cap, window_title, num_images)
    perform_calibration(cap)