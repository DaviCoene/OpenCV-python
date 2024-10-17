import numpy as np
import cv2
import random


def function(event, x ,y,flags,  param):
    global b, r, g
    if event==cv2.EVENT_LBUTTONDOWN:
        b = random.randint(0,255) 
        r = random.randint(0,255)
        g = random.randint(0,255)


b = 255
g = 255
r = 255

cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)
while True:
    img = np.full((512,2048, 3), (b,g,r), np.uint8)
    cv2.circle(img,(256,256), 75, (0,0,255), -1)
    cv2.imshow("janela", img)

    if cv2.waitKey(150) & 0xFF == 27:
        break

    cv2.waitKey(150)
cv2.destroyAllWindows()