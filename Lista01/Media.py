import cv2 as cv
import numpy as np

imgS = cv.imread('imagens\imgTeste03.png')
imgG = cv.cvtColor(imgS, cv.COLOR_BGRA2GRAY)

n, m = imgG.shape

print(f'comprimento/ Quantidade de colunas: {m}, altura/ Quantidade de linhas: {n}')

cv.imshow('Imagen Normal', imgG)


for y in range(1, m - 1):
    for x in range(1, n - 1):
        nIn = 0
        fatorM = 0
        for i in range(-1, 2):
            for j in range(-1,2):
                nIn += imgG.item(x + i, y + j)
                fatorM += 1
        nIn /= fatorM
        imgG.itemset((x,y), nIn)

cv.imshow('Com Media', imgG)
cv.waitKey(0)
cv.destroyAllWindows()
