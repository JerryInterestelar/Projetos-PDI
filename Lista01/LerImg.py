import cv2 as cv
import numpy as np

img = cv.imread('teste.png')
imgG = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
xi, yi = imgG.shape
mask = [[-10, -10, -10],
        [-10, -10, -10],
        [-10, -10, -10],
        ]

sumM = 4
lm = len(mask)
for i in range(0, lm):
    for j in range(0, lm):
        sumM += mask[i][j]

passos = int(lm/2)
print(sumM)

cv.imshow('teste', imgG)
0
for y in range(1, yi-lm):
    for x in range(1, xi-lm):
        nIntScl = 0
        for i in range(-passos, passos+1):
            for j in range(-passos, passos + 1):
                nIntScl += mask[i+1][j+1]*imgG.item(x+i, y+j)
        imgG.itemset((x,y), nIntScl/sumM)


#y --pos[0]
#x --pos[1]


cv.imshow('toda_fudida_sapoha', imgG)
cv.waitKey(0)
cv.destroyAllWindows()