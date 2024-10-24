import numpy as np
import cv2
import random


lower = (0, 200, 200)
upper = (80, 255, 255)

cap = cv2.VideoCapture("pacman.mp4")

Count = 0
oldX=0
x = 1000000
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output = cv2.VideoWriter(f"pacman{str(random.randint(0,1000))}.mp4", fourcc, 33, (480,360))
while cap.isOpened():
    ret, frame = cap.read()  
    
    
    if not ret:
        break  

    blur = cv2.GaussianBlur(frame, (1,1), 5)
    mask = cv2.inRange(blur, lower, upper)
    
    kernel = np.ones((1,1),np.uint8)
    
    aberto = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 2)
    

    imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    _, imagem_binaria = cv2.threshold(aberto, 127, 255, cv2.THRESH_BINARY)

    contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



    x, y, w, h = cv2.boundingRect(contornos[-1])
    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), (0, 255, 0), 2)

    testo9 = f"PACMAN" 
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    linha = cv2.LINE_AA
    cv2.putText(frame, testo9, (x + 10,y), fonte, 0.5, (0,255,0),2,linha)
    output.write(frame)
    cv2.imshow("pacman", frame)
    

    if cv2.waitKey(20) == 27:
        break

output.release()
cap.release()
cv2.destroyAllWindows()
