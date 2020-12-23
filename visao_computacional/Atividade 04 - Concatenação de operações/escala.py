import numpy as np
import cv2 as cv

img = cv.imread('entrada.jpg')

res = cv.resize(img, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)

cv.imshow('img', res)
cv.waitKey(0)
cv.destroyAllWindows()
