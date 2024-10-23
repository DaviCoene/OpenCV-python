import numpy as np
import cv2

img = cv2.imread('img/sonic1.jpg')

lower = (200,0,0)
upper = (255,0,0)



cv2.imshow('imagem original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

