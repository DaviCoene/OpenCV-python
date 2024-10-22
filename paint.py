import numpy as np
import cv2
import random


def function(event, x ,y,flags,  param):
    global b, r, g, drawing, Radius, raio
    global A, B, C,D, f
    if event==cv2.EVENT_FLAG_LBUTTON:
        drawing = True 
        
    if drawing:
        refazer.clear()
        f= True
        A = x
        B = y
        blue = b
        green = g
        red = r
        raio = Radius
        
        retagulo_fake.append((A,B, blue, green,red, raio))
    
    if event==cv2.EVENT_FLAG_MBUTTON:
        drawing = False
        
    if event == cv2.EVENT_RBUTTONDOWN:  # Conta-gotas ao clicar com botão direito
        # Verifica se as coordenadas estão dentro da imagem
        if x >= 0 and x < img.shape[1] and y >= 0 and y < img.shape[0]:
            cor_pixel = img[y, x]  # Captura a cor do pixel na posição (x, y)
            b, g, r = int(cor_pixel[0]), int(cor_pixel[1]), int(cor_pixel[2])

record = False 
f= True
b = 0
g = 0
r = 0
Radius = 10
def circle(A,B,blue,green,red, raio):
    cv2.circle(img, (A,B), raio, (blue,green,red), -1)


retagulo_fake = []
refazer = []

cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output = cv2.VideoWriter(f"paint{str(random.randint(0,1000))}.mp4", fourcc, 160, (1920,1080))

while True:
    img = np.full((1080,1920, 3), (255,255,255), np.uint8)
    testo90 = " 'n'2x to start "
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    linha = cv2.LINE_AA
    cv2.putText(img, testo90, (500,1000,), fonte, 5, (0,0,0),4,linha)
    key = cv2.waitKey(1) & 0xFF  
    if key == 110:
        break  
    cv2.imshow("janela", img)
while True:    
    img = np.full((1080,1920, 3), (255,255,255), np.uint8)
    for (A,B,blue,green,red, raio) in retagulo_fake:
        circle(A,B,blue,green,red, raio)
    
    
    if record == True:
        output.write(img)
        cv2.circle(img, (1800, 500), 30, (0,0,255), -1)
        Testo4 = "Espessura: " + str(Radius)
        testo5 = "b = To increase blue, r = to increase Red, g to increase = green "
        testo6 = "Space to clean all"
        testo7 = "z = to increase radius, x = to decrease radius"
        testo8 = "1 = black, 2 = to white, 3 = to yellow, 4 = red"
        testo10 = "5 = green 6 = blue, 7 gray"
        testo9 = "0 = to undo p = eraser, Shift + S to save"
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
        
    if key == 110:
        record = True
    if key ==  111:
        record = False
        output.release()
    if key == 112:     
        r = 255   
        g = 255   
        b = 255    
        Radius = 250    
    if key == 48:    
        if len(retagulo_fake) != 0:
            refazer.append(retagulo_fake[-1])
            retagulo_fake.pop()      
            refazer.append(retagulo_fake[-1])
            retagulo_fake.pop()            
            refazer.append(retagulo_fake[-1])
            retagulo_fake.pop()   
           
              
    if key == 57:
        if f == True:
            refazer.reverse()     
            f = False
        if len(refazer) != 0:
            retagulo_fake.append(refazer[0])
            del refazer[0]
            retagulo_fake.append(refazer[0])
            del refazer[0]
            retagulo_fake.append(refazer[0])
            del refazer[0]
    if key == 32:  
        retagulo_fake.clear()
    if key == 27:  # Esc
        break
    
    if key == 83:
        cv2.imwrite(f"paint1{str(random.randint(0,1000))}.jpg", img) #to save
        


    cv2.imshow("janela", img)
output.release()
cv2.destroyAllWindows()