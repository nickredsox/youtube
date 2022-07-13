from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,2)

im1 = plt.imread('galaxy_cluster.jpg')
im2 = plt.imread('fingerprint.jpg')

s1 = im1.shape
s2 = im2.shape

print(s1)
print(s2)

ax[0].imshow(im1)
ax[0].axis('off')
ax[0].set_title('Galaxy')

ax[1].imshow(im2, cmap = 'gray')
ax[1].axis('off')
ax[1].set_title('Fingerprint')



plt.show()


