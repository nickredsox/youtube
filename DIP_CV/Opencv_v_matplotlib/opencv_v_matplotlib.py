import cv2
from matplotlib import pyplot as plt


im_cv2 = cv2.imread('brickley.jpg')
im_mat = plt.imread('brickley.jpg')

print(type(im_cv2))
print(type(im_mat))

fig, ax = plt.subplots(1,2)
#Opencv imports as BGR
#Matplotlib imports as RGB

im_mat2BGR = cv2.cvtColor(im_mat, cv2.COLOR_RGB2BGR)
im_cv2RGB = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2RGB)

cv2.imshow("Brickley",im_mat2BGR)
ax[0].imshow(im_cv2RGB)
ax[1].imshow(im_cv2)

plt.show()
cv2.waitKey(0)