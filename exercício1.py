import numpy as np
import cv2


drawing = False 
finish = False
A, B, C, D = 0, 0, 0, 0  

def function(event, x, y, flags, param):
    global A, B, C, D, drawing
    if event == cv2.EVENT_LBUTTONDOWN:  
        drawing = True
        A, B = x, y  

    elif event == cv2.EVENT_MOUSEMOVE:  
        if drawing: 
            C, D = x, y  
    elif event == cv2.EVENT_LBUTTONUP:  
        drawing = False  
        finish = True
        C, D = x, y 


image = cv2.imread('img/yodinha.jpg')
cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)

while True:
    
    image_copy = image.copy()

    if drawing:  
        cv2.rectangle(image_copy, (A, B), (C, D), (0, 255, 0), 2)

    
    cv2.imshow("janela", image_copy)

    
    if not drawing and (C > A and D > B):
        imagem_cortada = image[B:D, A:C]
        while True:
            if cv2.waitKey(10) == 13:
                cv2.imshow("imagem cortada", imagem_cortada)
                break
            if drawing:
                break
            
       

    
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
