from matplotlib import pyplot as plt


fig, ax = plt.subplots(2,2)

im = plt.imread('frog.jpg')
print(im.shape)
im_red   = im[:,:,0] 
im_green = im[:,:,1]
im_blue  = im[:,:,2]
print(im_red.shape)

ax[0,0].imshow(im)
ax[0,0].axis('off')
ax[0,0].set_title('RGB')

ax[0,1].imshow(im_red, cmap = 'gray')
ax[0,1].axis('off')
ax[0,1].set_title('Red Channel')

ax[1,0].imshow(im_green, cmap = 'gray')
ax[1,0].axis('off')
ax[1,0].set_title('Green Channel')

ax[1,1].imshow(im_blue, cmap = 'gray')
ax[1,1].axis('off')
ax[1,1].set_title('Blue Channel')

plt.show()