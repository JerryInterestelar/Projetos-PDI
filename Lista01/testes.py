import cv2 as cv
import scipy.ndimage as snd

img = cv.imread('imagens/pessoa.jpg', 0)


cv.imshow('pessoa', img)
cv.imshow('pessoaModificada', snd.gaussian_filter(img, 1))
cv.imshow('pessoaModificada2', snd.gaussian_filter(img, 1))

cv.waitKey(0)
cv.destroyAllWindows()