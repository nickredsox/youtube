import cv2

def getXY(evt, x,y, flags, userdata ):
    if evt == cv2.EVENT_LBUTTONDOWN:
     #   print("X: " + str(x) + " Y: " + str(y))
        value = im[y,x]
       # print("B: " + str(value[0]) + " G: " + str(value[1]) + 
      #      " R: " + str(value[2]))
        circles.append([x,y])
    if evt == cv2.EVENT_RBUTTONDOWN:
        global redraw_image
        # Check mouseclick (x, y) against all circles
        # If there is a match , delete that particular circle

        radius = 10
        for index, circle in enumerate(circles):
            if (x < circle[0] + radius and
                x > circle[0] - radius and
                y < circle[1] + radius and
                y > circle[1] - radius):
                    del circles[index]
                    redraw_image = True
                    break


        #circles.clear()
        
redraw_image = False
im = cv2.imread('color_bars.png')
im1 = im.copy()
window_title = "Color Bars"
circles = []

while True:
   # print(circles)
    for circle in circles:
        cv2.circle(im1, (circle[0], circle[1]), 10, (255,0,0),2)

    if len(circles) == 0 or redraw_image is True:
        im1 = im.copy()
        redraw_image = False

    #cv2.circle(im, (x,y), 10, (255,0,0), 2)
    cv2.imshow(window_title, im1)
    cv2.setMouseCallback(window_title, getXY, "Hello")
    k = cv2.waitKey(10)

    if k == ord('q') & 0xFF:
        break