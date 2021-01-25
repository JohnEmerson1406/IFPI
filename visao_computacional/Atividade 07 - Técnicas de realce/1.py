import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math


#------------------- IMAGEM ORIGINAL -------------------
img = cv.imread('entrada.jpg')


#------------------- IMAGEM EM TONS DE CINZA -------------------
imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)


#------------------- NEGATIVO DA IMAGEM -------------------

# negative = cv.bitwise_not(imgGray)
# negative = -imgGray

negative = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
for y in range(0, negative.shape[0]):
  for x in range(0, negative.shape[1]):
    negative[y, x] = 255 - negative[y, x]


#------------------- NORMALIZAÇÃO DO CONTRASTE -------------------

contrast = cv.equalizeHist(imgGray)

# contrast = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# a = 0
# b = 255
# c = 100
# d = 200
# for y in range(0, contrast.shape[0]):
#   for x in range(0, contrast.shape[1]):
#     contrast[y, x] = (contrast[y, x] - a) * ((d-c)/(b-a)) + c


#------------------- CORREÇÃO GAMA -------------------

gamma = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
c = 3
y_value = 0.8
for y in range(0, gamma.shape[0]):
  for x in range(0, gamma.shape[1]):
    gamma[y, x] = c * gamma[y, x] ** y_value


#------------------- REALCE LOGARÍTIMICO-------------------

realce = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
for y in range(0, realce.shape[0]):
  for x in range(0, realce.shape[1]):
    realce[y, x] = (255/(math.log(255, 10))) * (math.log(realce[y, x] + 1, 10))

cv.imshow('Original', img)
cv.imshow('Gray', imgGray)
cv.imshow('Negative', negative)
cv.imshow('contrast', contrast)
cv.imshow('gamma', gamma)
cv.imshow('realce', realce)

cv.waitKey()
