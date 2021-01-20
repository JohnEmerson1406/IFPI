import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('entrada.jpg')

imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

blur = cv.blur(imgGray, (5,5))
median = cv.medianBlur(imgGray, 5)
gaussian = cv.GaussianBlur(imgGray, (5,5), 0)

cv.imshow('Original', img)
cv.imshow('Gray', imgGray)
cv.imshow('Blurred', blur)
cv.imshow('Median', median)
cv.imshow('Gaussian', gaussian)
cv.waitKey()

# plt.subplot(121), plt.imshow(img), plt.title('original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title('blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()
