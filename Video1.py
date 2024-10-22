import numpy as np
import cv2
import random


def function(event, x ,y,flags,  param):
    pass

b = 0
g = 0
r = 0
count = 0


fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("exercicio1.avi", fourcc, 30, (512, 512))

cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)

while True:
    img = np.full((512,512, 3), (b,g,r), np.uint8)
    count = count + 1
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    B = random.randint(20, 500)
    A = random.randint(20, 2000)
    RADIUS = random.randint(2, 150)
    R = random.randint(0, 255)
    G =random.randint(0, 255)
    B =random.randint(0, 255)
    if random.randint(0, 255) < 150:
        cv2.circle(img, (A,B), RADIUS, (B,G,R), -1)
    else:
        cv2.rectangle(img, (A , B ), (A + 30, B + 30), (B,G,R), -1)
    
    output.write(img)
    
    if cv2.waitKey(20) & 0xFF == 27 or count == 450:
        break
    
    cv2.imshow("janela", img)
    
output.release()
cv2.destroyAllWindows()