from matplotlib import pyplot as plt
import numpy as np
import cv2
import time

#Section 1 - Setup
im = plt.imread('rainbow.jpg')
fig, ax = plt.subplots(1,2)

(row, col, chan) = im.shape
gray_scale = np.zeros((row, col, 1))

#Section 2 - Grayscale

#R * 0.299 + G * 0.587 + B * 0.144

t_start = time.time()

# For Loop method uncomment
# for r in range(row):
#     for c in range(col):
#         R = im[r,c,0]
#         G = im[r,c,1]
#         B = im[r,c,2]

#         new_val = 0.299*R + 0.587*G + 0.114*B
#         gray_scale[r,c] = new_val


#Vectorized Method uncomment to use
#gray_scale = 0.299* im[:,:,0] + 0.587 * im[:,:,1] + 0.114* im[:,:,2]

#OpenCV 
gray_scale = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

t_stop = time.time()

elapsed_time = t_stop-t_start
print("It took " + str(elapsed_time) + " seconds")

#Section 3 - Displaying Images
ax[0].imshow(im)
ax[0].axis('off')
ax[0].set_title('RGB')

ax[1].imshow(gray_scale, cmap = 'gray')
ax[1].axis('off')
ax[1].set_title('Gray')

plt.show()



