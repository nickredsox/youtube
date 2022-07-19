from matplotlib import pyplot as plt

fig, ax = plt.subplots(1,2)   # row columns

im1 = plt.imread('galaxy_cluster.jpg')
im2 = plt.imread('fingerprint.jpg')

pixels = im1[163,396,:] #x,    y
print(pixels)

s1 = im1.shape
s2 = im2.shape

print(s1)
print(s2)


ax[0].imshow(im1, cmap = 'gray')
ax[0].axis('off')
ax[0].set_title('Galaxy')

ax[1].imshow(im2)
ax[1].axis('off')
ax[1].set_title('Fingerprint')

plt.show()