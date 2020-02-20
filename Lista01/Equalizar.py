import cv2
import histograma as hst
import numpy as np

def equalizeH(img):
    nImg = np.array(img).copy()

    y, x = nImg.shape
    tam = nImg.size
    histograma = hst.makeHist(nImg)
    histogramaEqu = []

    for i in range(len(histograma)): #probabilidade de ocorrencia
        histograma[i] /= tam

    for i in range(len(histograma)): #cumulaçao das probabilidades
        histograma[i] += histograma[i-1]

    for i in range(len(histograma)): #Normalização
        histograma[i] *= 255

    for i in range(len(histograma)):
        histogramaEqu.append(round(histograma[i], 0))

    return histogramaEqu

def makeNewEqu(img):
    nImg = np.array(img).copy()
    hEqu = equalizeH(nImg)
    y, x = nImg.shape

    for j in range(0, y - 1):
        for i in range(0, x - 1):
            nImg[j][i] = hEqu[nImg[j][i]]
    return nImg

if __name__ == '__main__':
    imagem = cv2.imread("imagens\cegocioIrritante.jpg", 0)


    equalizada = makeNewEqu(imagem)
    cv2.imshow("imagem original", imagem)
    hst.plotVector(hst.makeHist(imagem), "imagem original")
    cv2.imshow("imagem equalizada", equalizada)
    hst.plotVector(hst.makeHist(equalizada), "imagem equalizada")


    cv2.waitKey(0)
    cv2.destroyAllWindows()
