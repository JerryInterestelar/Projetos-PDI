import cv2

img = cv2.imread("imagens\imgTeste03.png", 0)
y, x = img.shape

#Code
grafico_vetor = []

for i in range(0, 256):
   grafico_vetor.append(0)

for j in range(0, y-1):
   for i in range(0, x-1):
      grafico_vetor[img[j][i]] += 1


print(grafico_vetor)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
