import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math


#------------------- IMAGEM ORIGINAL -------------------
img = cv.imread('alcohol-dehydrogenase.png')


#------------------- SEGMENTAÇÃO PELA COR -------------------

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # converte para HSV
blur = cv.medianBlur(hsv, 5) # aplica o filtro de mediana para remoção de ruídos
lower = np.array([0, 0, 90]) # valor limite de cor mínimo
upper = np.array([0, 255, 255]) # valor limite de cor máximo
mask = cv.inRange(blur, lower, upper) # define a máscara
seg = cv.bitwise_and(img, img, mask=mask) # aplica a máscara na imagem original


#------------------- SISTEMAS DE CORES -------------------

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # preto e branco (tons de cinza)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # sistema HSV
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB) # sistema L*a*b*


#------------------- FILTROS -------------------

blurred = cv.blur(img, (5,5))
median = cv.medianBlur(img, 5)
gaussian = cv.GaussianBlur(img, (5,5), 0)


#------------------- REALCE -------------------

realce = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
for y in range(0, realce.shape[0]):
  for x in range(0, realce.shape[1]):
    realce[y, x] = (255/(math.log(255, 10))) * (math.log(realce[y, x] + 1, 10)) # realce logarítmico


#------------------- RESULTADOS -------------------

cv.imshow('Original', img)
cv.imshow('Segmentacao', seg)
cv.imshow('tons de cinza', gray)
cv.imshow('HSV', hsv)
cv.imshow('L*a*b*', lab)
cv.imshow('blurred', blurred)
cv.imshow('median', median)
cv.imshow('gaussian', gaussian)
cv.imshow('realce', realce)

cv.waitKey()
