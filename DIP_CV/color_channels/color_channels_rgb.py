from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots(2,2)

im = plt.imread('frog.jpg')
s  = im.shape

color_red   = np.zeros(s, dtype = np.uint8)
color_green = np.zeros(s, dtype = np.uint8)
color_blue  = np.zeros((s[0],s[1]), dtype = np.uint8)

im_red   = im[:,:,0] 
im_green = im[:,:,1]
im_blue  = im[:,:,2]
print(im_red.shape)

color_red[:,:,0]   = im_red
color_green[:,:,1] = im_green
blue = np.dstack((color_blue, color_blue, im_blue))

ax[0,0].imshow(im)
ax[0,0].axis('off')
ax[0,0].set_title('RGB')

ax[0,1].imshow(color_red, cmap = 'gray')
ax[0,1].axis('off')
ax[0,1].set_title('Red Channel')

ax[1,0].imshow(color_green, cmap = 'gray')
ax[1,0].axis('off')
ax[1,0].set_title('Green Channel')

ax[1,1].imshow(blue, cmap = 'gray')
ax[1,1].axis('off')
ax[1,1].set_title('Blue Channel')

plt.show()