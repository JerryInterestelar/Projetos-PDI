import cv2
import matplotlib.pyplot as plt

def makeHist(img): #recebe um objeto imagem em grayScale lido pela openCV (Mat) e retorna um vetor
    y, x = img.shape
    # Code
    grafico_vetor = []
    for i in range(0, 256):
        grafico_vetor.append(0)

    for j in range(0, y - 1):
        for i in range(0, x - 1):
            grafico_vetor[img[j][i]] += 1

    return grafico_vetor

def plotVector(vector, nome):
    plt.plot(vector)
    plt.ylabel('pixes')
    plt.xlabel('Escalas de cinza')
    plt.title(nome)
    plt.show()

if __name__ == '__main__':
    img = cv2.imread("imagens\imgTeste03.png", 0)
    histograma = makeHist(img)

    #print(histograma)

    cv2.imshow("img", img)
    plotVector(histograma, "imagem")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
