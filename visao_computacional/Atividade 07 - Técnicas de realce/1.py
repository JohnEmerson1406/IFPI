import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('entrada.jpg')

imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

negative = cv.bitwise_not(imgGray)

contrast = cv.equalizeHist(imgGray)

# image = imgGray

# for y in range(0, image.shape[0]):
#   for x in range(0, image.shape[1]):
#     image[y, x] = (255, 0, 0)


cv.imshow('Original', img)
cv.imshow('Gray', imgGray)
cv.imshow('Negative', negative)
cv.imshow('contrast', contrast)


cv.waitKey()

# plt.subplot(121), plt.imshow(img), plt.title('original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title('blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()
