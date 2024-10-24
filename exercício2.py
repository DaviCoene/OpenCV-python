import numpy as np
import cv2

img = cv2.imread('arrozz.jpg')

lower = (195,195,195)
upper = (255,255,255)

blur = cv2.GaussianBlur(img, (7,7), 0)

mask = cv2.inRange(blur, lower, upper)

imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cv2.imshow("Imagem original", imagem_cinza)
_, imagem_binaria = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagem originala", imagem_binaria)
Count = 0

contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(img, (x -10, y -10), (x + w +10,10+ y + h ), (0, 255, 0), 2)
    Count = Count + 1


print(Count)
testo9 = f"Count = {str(Count)}" 
fonte = cv2.FONT_HERSHEY_SIMPLEX
linha = cv2.LINE_AA
cv2.putText(img, testo9, (50,50), fonte, 1.5, (0,255,0),4,linha)
cv2.imshow('Grãos com Retângulos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()

