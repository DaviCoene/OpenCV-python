import numpy as np
import cv2
import random


def function(event, x ,y,flags,  param):
    global b, r, g, drawing, Radius, raio
    global A, B, C,D
    if event==cv2.EVENT_FLAG_LBUTTON:
        drawing = True 
        
        
    if drawing:
        A = x
        B = y
        blue = b
        green = g
        red = r
        raio = Radius
        
        retagulo_fake.append((A,B, blue, green,red, raio))
    
    if event==cv2.EVENT_FLAG_MBUTTON:
        drawing = False
    
        
b = 0
g = 0
r = 0
Radius = 10
def circle(A,B,blue,green,red, raio):
    cv2.circle(img, (A,B), raio, (blue,green,red), -1)


retagulo_fake = []

cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)


while True:    
    img = np.full((2048,2048, 3), (255,255,255), np.uint8)
    for (A,B,blue,green,red, raio) in retagulo_fake:
        circle(A,B,blue,green,red, raio)
    Testo4 = "Espessura: " + str(Radius)
    testo5 = "b = To increase blue, r = to increase Red, g to increase = green "
    testo6 = "Space to clean all"
    testo7 = "z = to increase radius, x = to decrease radius"
    testo8 = "1 = black, 2 = to white, 3 = to yellow, 4 = red"
    testo10 = "5 = green 6 = blue, 7 gray"
    testo9 = "0 = to undo p = rubber"
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    linha = cv2.LINE_AA
    cv2.putText(img, Testo4, (100,100), fonte, 1.5, (0,0,0),4,linha)
    cv2.putText(img, testo5, (1100,50), fonte, 0.5, (0,0,0),2,linha)
    cv2.putText(img, testo6, (1100,75), fonte, 0.5, (0,0,0),2,linha)
    cv2.putText(img, testo7, (1100,100), fonte, 0.5, (0,0,0),2,linha)
    cv2.putText(img, testo8, (1100,125), fonte, 0.5, (0,0,0),2,linha)
    cv2.putText(img, testo10, (1100,150), fonte, 0.5, (0,0,0),2,linha)
    cv2.putText(img, testo9, (1100,175), fonte, 0.5, (0,0,0),2,linha)
    cv2.circle(img, (1800, 100), 40, (0,0,0), -1)
    cv2.circle(img, (1800, 100), 30, (b,g,r), -1)
    
    

    key = cv2.waitKey(1) & 0xFF  
    if key == 98:  
        b = min(255, b + 10) 
        if b > 250:
            b = 0
    if key == 103:  
        g = min(255, g + 10)  
        if g > 250:
            g = 0
    if key == 122:  
        Radius = Radius + 5  

    if key == 120:  
        if Radius != 0:
            Radius = Radius - 5 
        
    if key == 114:  
        r = min(255, r + 10)  
        if r > 250:
            r = 0
    if key == 49:  
        r = 0
        g = 0
        b = 0
        Radius = 10
    if key == 50:  
        r = 255
        g = 255
        b = 255
    
    if key == 51:  
        r = 255
        g = 255
        b = 0
        
    if key == 52:
        r = 255
        g = 0   
        b = 0   

    if key == 53:   
        r = 0   
        g = 255   
        b = 0   
    
    if key == 54:   
        r = 0   
        g = 0   
        b = 255   
    
    if key == 55:   
        r = 100   
        g = 100   
        b = 100   
        
    if key == 112:     
        r = 255   
        g = 255   
        b = 255    
        Radius = 250    
    if key == 48:    
        if len(retagulo_fake) != 0:    
            retagulo_fake.pop()      
            retagulo_fake.pop()            
            retagulo_fake.pop()              
    if key == 32:  
        retagulo_fake.clear()
    if key == 27:  # Esc
        break
    
    if key == 83:
        cv2.imwrite(f"paint1{str(b)}.jpg", img) #to save
        


    cv2.imshow("janela", img)

cv2.destroyAllWindows()