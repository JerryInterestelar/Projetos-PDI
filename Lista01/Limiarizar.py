import cv2

img = cv2.imread('imagens\imgTeste03.png.png') #Lê a imagem

imgG = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY) #copia da imagem em escala de cinza
img1 = img  #Copia da Imagem padrão
y, x = imgG.shape   #Dimensões da imagem
#y --pos[0]
#x --pos[1]

avgIn = 120 #Valor de intesidade Analizado

for j in range(0, y-1):
    for i in range(0, x-1):
        if imgG[j][i] >= avgIn:
            imgG[j][i] = 255    #Se a intensidade naquele pixel for maior que "avgIn", o valor sera modificado para branco
        else:
            imgG[j][i] = 0  #Se a intensidade naquele pixel for maior que "avgIn", o valor sera modificado para branco

cv2.imshow('Padraozinha', img1)
cv2.imshow('limiarizada', imgG)
cv2.waitKey(0)
cv2.destroyAllWindows()
