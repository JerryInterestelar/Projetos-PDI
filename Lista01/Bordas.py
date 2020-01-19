import cv2 as cv
import numpy as np

#cv.BORDER_CONSTANT cv.BORDER_REFLECT cv.BORDER_REFLECT_101 cv.BORDER_REPLICATE cv.BORDER_WRAP

imgS = cv.imread('teste.png')
gImg = cv.cvtColor(imgS, cv.COLOR_BGRA2GRAY)
n, m = gImg.shape

addB = 1
bImg = cv.copyMakeBorder(gImg, addB, addB, addB, addB,cv.BORDER_REFLECT)
n, m = bImg.shape

cv.imshow('www', bImg)
cv.waitKey(0)
cv.destroyAllWindows()
