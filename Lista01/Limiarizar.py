import cv2

img = cv2.imread('imagens\imgTeste03.png.png')

imgG = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
img1 = img
y, x = imgG.shape
#y --pos[0]
#x --pos[1]

avgIn = 120

for j in range(0, y-1):
    for i in range(0, x-1):
        if imgG[j][i] >= avgIn:
            imgG[j][i] = 255
        else:
            imgG[j][i] = 0

cv2.imshow('Padraozinha', img1)
cv2.imshow('limiarizada', imgG)
cv2.waitKey(0)
cv2.destroyAllWindows()