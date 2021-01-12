import cv2 as cv

img = cv.imread('entrada.jpg', 1)

channels = cv.split(img)

cv.imshow('RGB', img)
cv.imshow('Blue', channels[0])
cv.imshow('Green', channels[1])
cv.imshow('Red', channels[2])
cv.waitKey()
