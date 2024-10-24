import numpy as np
import cv2

def function(event, x, y, flags, param):
    global scrolling_direction, Count
    
    if event == cv2.EVENT_MOUSEWHEEL:
        # A quantidade de rolagem para cima ou para baixo
        if flags > 0:
            scrolling_direction += 1  # Rolou para cima
            Count += 1
        else:
            scrolling_direction -= 1  # Rolou para baixo
            Count -= 1

# Inicializa variáveis globais
Count = 0
scrolling_direction = 0

# Cria a janela e configura o callback do mouse
cv2.namedWindow("janela")
cv2.setMouseCallback("janela", function)

# Carrega a imagem
img = cv2.imread("img/yodinha.jpg")

while True:    
    # Imprime a direção de rolagem e o contador
    print(scrolling_direction)
    print(Count)

    # Define o novo tamanho da imagem com um mínimo de 1x1
    largura = max(1, 462 + round((scrolling_direction * 25)*1.78))  # Multiplicando para um efeito mais perceptível
    altura = max(1, 260 + scrolling_direction * 25)

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(img, (largura, altura))

    # Exibe a imagem redimensionada
    cv2.imshow("janela", imagem_redimensionada)

    key = cv2.waitKey(100) & 0xFF
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()
