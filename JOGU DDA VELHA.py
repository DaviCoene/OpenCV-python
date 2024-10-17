import numpy as np
import cv2


count = 0
b = 0
g = 0
r = 255

A, B = 0, 0  
retagulo_fake = []
X_true = []

def function(event, x, y, flags, param):
    global b, r, g, count, A, B
    if event == cv2.EVENT_LBUTTONDOWN:
        count += 1
        if count % 2 != 0:  # Ímpar
            if x <= 170 and y <= 170:
                A, B = 85, 85
            elif x <= 170 and 170 < y <= 340:
                A, B = 85, 255
            elif x <= 170 and 340 < y <= 512:
                A, B = 85, 425
            elif 170 < x <= 340 and y <= 170:
                A, B = 255, 85
            elif 170 < x <= 340 and 170 < y <= 340:
                A, B = 255, 255
            elif 170 < x <= 340 and 340 < y <= 512:
                A, B = 255, 425
            elif 340 < x <= 512 and y <= 170:
                A, B = 425, 85
            elif 340 < x <= 512 and 170 < y <= 340:
                A, B = 425, 255
            elif 340 < x <= 512 and 340 < y <= 512:
                A, B = 425, 425
            X_true.append((A, B))
        else:  # Par
            if x <= 170 and y <= 170:
                A, B = 85, 85
            elif x <= 170 and 170 < y <= 340:
                A, B = 85, 255
            elif x <= 170 and 340 < y <= 512:
                A, B = 85, 425
            elif 170 < x <= 340 and y <= 170:
                A, B = 255, 85
            elif 170 < x <= 340 and 170 < y <= 340:
                A, B = 255, 255
            elif 170 < x <= 340 and 340 < y <= 512:
                A, B = 255, 425
            elif 340 < x <= 512 and y <= 170:
                A, B = 425, 85
            elif 340 < x <= 512 and 170 < y <= 340:
                A, B = 425, 255
            elif 340 < x <= 512 and 340 < y <= 512:
                A, B = 425, 425
            retagulo_fake.append((A, B))


def circle(A, B):
    cv2.circle(img, (A, B), 50, (b, g, r), -1)

def EXYS(A, B):
    cv2.line(img, (-50 + A, -50 + B), (50 + A, 50 + B), (255, 0, 255), 5)
    cv2.line(img, (50 + A, -50 + B), (-50 + A, 50 + B), (255, 0, 255), 5)


cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)

while True:
    img = np.full((512, 512, 3), (0, 0, 0), np.uint8)

    
    cv2.line(img, (170, 0), (170, 512), (255, 0, 255), 5)
    cv2.line(img, (340, 0), (340, 512), (255, 0, 255), 5)
    cv2.line(img, (0, 170), (512, 170), (255, 0, 255), 5)
    cv2.line(img, (0, 340), (512, 340), (255, 0, 255), 5)

    
    for (A, B) in retagulo_fake:
        circle(A, B)

    for (A, B) in X_true:
        EXYS(A, B)

   
    key = cv2.waitKey(10) & 0xFF
    if key == 98:  # 'b' para mudar o azul
        b = (b + 10) % 256
    if key == 103:  # 'g' para mudar o verde
        g = (g + 10) % 256
    if key == 114:  # 'r' para mudar o vermelho
        r = (r + 10) % 256
    if key == 27:  # Esc para sair
        break

    cv2.imshow("janela", img)

cv2.destroyAllWindows()
