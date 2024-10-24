import numpy as np
import cv2
import datetime


lower_verde = (50, 200, 50)   
upper_verde = (170, 255, 170)  

lower_vermelho = (50, 50, 200)   
upper_vermelho = (170, 170, 255) 

lower_amarelo = (50, 200, 200)   
upper_amarelo = (170, 255, 255) 

cap = cv2.VideoCapture("traffic_light.mp4")


if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()


fourcc = cv2.VideoWriter_fourcc(*'MP4V')


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"traffic_{timestamp}.mp4"
output = cv2.VideoWriter(output_filename, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))
Count_amarelo = 0
Count_vermelho = 0
Count_verde = 0
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break


    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask_verde = cv2.inRange(hsv_frame, lower_verde, upper_verde)

    kernel = np.ones((1, 1), np.uint8)  
    aberto_verde = cv2.morphologyEx(mask_verde, cv2.MORPH_OPEN, kernel, iterations=2)
    dilatado_verde = cv2.dilate(aberto_verde, kernel, iterations=1)  


    roi_mask_verde = np.zeros_like(mask_verde)  
    roi_mask_verde[125:550, 600:695] = 255  

    
    dilatado_verde_roi = cv2.bitwise_and(dilatado_verde, roi_mask_verde)


    contornos_verde, _ = cv2.findContours(dilatado_verde_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contorno in contornos_verde:
        if cv2.contourArea(contorno) > 100:  
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            testo9 = f"verde" 
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            linha = cv2.LINE_AA
            cv2.putText(frame, testo9, (x,y), fonte, 0.5, (0,255,0),2,linha)
            
    testo99 = f"{str(Count_verde)}"        
    cv2.putText(frame, testo99, (900,400), fonte, 0.5, (0,255,0),2,linha)
    if len(contornos_verde) > 0 and Count_amarelo == 0:
        Count_verde = Count_verde + 3

    # ----------------------------------------------------------
    
    mask_vermelho = cv2.inRange(frame, lower_vermelho, upper_vermelho)

    kernel = np.ones((1, 1), np.uint8)  
    aberto_vermelho = cv2.morphologyEx(mask_vermelho, cv2.MORPH_OPEN, kernel, iterations=2)
    dilatado_vermelho = cv2.dilate(aberto_vermelho, kernel, iterations=1)  


    roi_mask_vermelho = np.zeros_like(mask_vermelho)  
    roi_mask_vermelho[125:550, 600:695] = 255  

    
    dilatado_vermelho_roi = cv2.bitwise_and(dilatado_vermelho, roi_mask_vermelho)


    contornos_vermelho, _ = cv2.findContours(dilatado_vermelho_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contorno in contornos_vermelho:
        if cv2.contourArea(contorno) > 100:  
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            testo9 = f"vermelho" 
            
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            linha = cv2.LINE_AA
            cv2.putText(frame, testo9, (x,y), fonte, 0.5, (0,0,255),2,linha)
      
    testo91 = f"{str(Count_vermelho)}"        
    cv2.putText(frame, testo91, (750,100), fonte, 0.5, (0,0,255),2,linha)
    if len(contornos_vermelho) > 0 :
        Count_vermelho = Count_vermelho + 3 
            
    # ----------------------------------------------------------
    
    mask_amarelo = cv2.inRange(frame, lower_amarelo, upper_amarelo)

    kernel = np.ones((1, 1), np.uint8)  
    aberto_amarelo = cv2.morphologyEx(mask_amarelo, cv2.MORPH_OPEN, kernel, iterations=2)
    dilatado_amarelo = cv2.dilate(aberto_amarelo, kernel, iterations=1)  


    roi_mask_amarelo = np.zeros_like(mask_amarelo)  
    roi_mask_amarelo[125:550, 600:695] = 255  

    
    dilatado_amarelo_roi = cv2.bitwise_and(dilatado_amarelo, roi_mask_amarelo)


    contornos_amarelo, _ = cv2.findContours(dilatado_amarelo_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contorno in contornos_amarelo:
        if cv2.contourArea(contorno) > 100:  
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            testo9 = f"Amarelo" 
            
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            linha = cv2.LINE_AA
            cv2.putText(frame, testo9, (x,y), fonte, 0.5, (0,255,255),2,linha)
    testo90 = f"{str(Count_amarelo)}"         
    cv2.putText(frame, testo90, (750,250), fonte, 0.5, (0,255,255),2,linha)          
    
    if len(contornos_amarelo) > 0 and Count_vermelho != 0:
        Count_amarelo = Count_amarelo + 3
            
    
    
    
    
    output.write(frame)

    # Mostra os frames
    cv2.imshow("Traffic Light", frame)
    cv2.imshow("Mask_verde", dilatado_verde_roi) 
    print(Count_verde)
 
# Exibe a máscara dilatada

    # Sai do loop ao pressionar a tecla 'ESC'
    if cv2.waitKey(10) == 27:
        break

# Libera os recursos
output.release()
cap.release()
cv2.destroyAllWindows()
