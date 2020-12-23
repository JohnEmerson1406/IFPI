import cv2 as cv

img = cv.imread('entrada.jpg')

horizontal_img = img.copy()
vertical_img = img.copy()
both_img = img.copy()

horizontal_img = cv.flip(img, 0)
vertical_img = cv.flip(img, 1)
both_img = cv.flip(img, -1)

cv.imshow('original', img)
cv.imshow('horizontal flip', horizontal_img)
cv.imshow('vertical flip', vertical_img)
cv.imshow('both flip', both_img)

cv.waitKey(0)

cv.destroyAllWindows()
