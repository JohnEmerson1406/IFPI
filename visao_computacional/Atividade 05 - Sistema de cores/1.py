import cv2 as cv

img = cv.imread('entrada.jpg', 1)

imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
imgHSV = cv.cvtColor(img, cv.COLOR_RGB2HSV)

cv.imshow('RGB', img)
cv.imshow('GRAY', imgGray)
cv.imshow('HSV', imgHSV)
cv.waitKey()
