import cv2 as cv
import numpy as np
import math

def media(img, masc):
    nImg = np.array(img).copy()
    n, m = img.shape
    b, a = masc.shape
    b = round(b/2)-1
    a = round(a/2)-1
    sumMask = masc.sum()

    for y in range(b, m - b):
        for x in range(a, n - b):
            sum = 0
            for i in range(-b, b+1):
                for j in range(-a, a+1):
                    sum += nImg.item(x + i, y + j)*masc.item(i+a, j+b)
            sum /= sumMask
            nImg.itemset((x,y), sum)

    return nImg

def mediana(img, nTam):
    nImg = np.array(img).copy()
    n, m = img.shape
    index = (round(nTam/2))-1

    for y in range(index, m - index):
        for x in range(index, n - index):
            auxV = []
            for i in range(-index, index+1):
                for j in range(-index, index+1):
                    auxV.append(nImg.item(x+i, y+j))
            auxV.sort()
            midPoint = round((len(auxV))/2)
            nImg.itemset((x,y), auxV[midPoint])

    return nImg

def convolucao(img, masc):
    n, m = img.shape
    nImg = np.array(img).copy()
    b, a = masc.shape
    b = round(b / 2) - 1
    a = round(a / 2) - 1

    for y in range(b, m - b):
        for x in range(a, n - b):
            sum = 0
            for i in range(-b, b + 1):
                for j in range(-a, a + 1):
                    sum += img.item(x + i, y + j) * masc.item(i + a, j + b)
            if(sum > 255):
                sum = 255
            elif sum < 0:
                sum = 0

            nImg.itemset((x, y), sum)

    return nImg

def lapF (img):
    kernelLap = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    return convolucao(img, kernelLap)

def bDetecF (img, mascV, mascH):
    n, m = img.shape
    nImg = np.array(img).copy()

    for y in range(1, m - 1):
        for x in range(1, n - 1):
            sumV = 0
            sumH = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sumV += img.item(x + i, y + j) * mascV.item(i + 1, j + 1)
                    sumH += img.item(x + i, y + j) * mascH.item(i + 1, j + 1)
            if (sumV > 255):
                sumV = 255
            elif sumV < 0:
                sumV = 0
            if (sumH > 255):
                sumH = 255
            elif sumH < 0:
                sumH = 0

            fSum = round(math.sqrt((sumV*sumV)+(sumH*sumH)))
            nImg.itemset((x, y), fSum)

    return nImg

def prewF(img):
    kernelPrewV = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    kernelPrewH = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    return bDetecF(img, kernelPrewV, kernelPrewH)

def sobelF(img):
    kernelPrewV = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    kernelPrewH = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return bDetecF(img, kernelPrewV, kernelPrewH)

if __name__ == '__main__':
    img = cv.imread('imagens\pessoa.jpg', 0)

    teste1 = prewF(img)
    teste2 = sobelF(img)

    cv.imshow('normal', img)
    cv.imshow('prewwit', teste1)
    cv.imshow('sobel', teste2)


    cv.waitKey(0)
    cv.destroyAllWindows()
