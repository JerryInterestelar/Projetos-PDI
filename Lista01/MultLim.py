import cv2
import numpy as np
#nImg = np.array(img).copy()

def mLimPart(gLevels, img):
    nImg = np.array(img).copy()
    y, x = img.shape
    dIn = round(255 / gLevels)

    for j in range(0, y):
        for i in range(0, x):
            nImg[j][i] = 0

    for j in range(0, y):
        for i in range(0, x):
            cont = 1
            while (cont <= gLevels):
                if(img[j][i] <= cont*dIn):
                    nImg[j][i] += dIn
                    break
                else:
                    nImg[j][i] += dIn
                cont += 1
    return nImg

def mLimArb(img, *ints):
    #A funçao pode receber quantos parametros de intensidades forem necessários
    # a intensidade que, em um pixel especifico, for maior que o ULTIMO valor de intesidade adicionado na função terá como nova tonalidade o branco (255)
    nImg = np.array(img).copy()
    y, x = img.shape
    lInts = list(ints)
    lInts.sort()

    for j in range(0, y):
        for i in range(0, x):
            nImg[j][i] = 0

    for j in range(0, y):
        for i in range(0, x):
            for its in lInts:
                if(img[j][i] <= its):
                    nImg[j][i] += its
                    break
                else:
                    nImg[j][i] += its
                nImg[j][i] = 255
    return nImg

if __name__ == "__main__":
    img = cv2.imread('imagens\leaodiferente.jpg', 0)

    #mult2 = mLimPart(2, img)
    #mult3 = mLimPart(3, img)
    #mult4 = mLimPart(4, img)
    teste = mLimArb(img, 200, 150, 50)

    cv2.imshow('normalzinha', img)
    cv2.imshow('teste', teste)

    #cv2.imshow('limiarizada em 2 niveis', mult2)
    #cv2.imshow('MultLim: 3 niveis', mult3)
    #cv2.imshow('limiarizada em 4 niveis', mult4)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
