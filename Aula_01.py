import cv2
import numpy as np
# imagem_original = cv2.imread("img\yodinha.jpg")
# imagem_neutra = cv2.imread("img\yodinha.jpg",0)
# imagem_transparente = cv2.imread("img\yodinha.jpg",-1)

# cv2.imshow("Yodinha colorido", imagem_original)
# cv2.imshow("Yodinha desbotado", imagem_neutra)
# cv2.imshow("Yodinha tranparente", imagem_transparente)


# imagem_original2 = cv2.imread("img\rainha.png")
# imagem_neutra2 = cv2.imread("img\rainha.png",0)
# imagem_transparente2 = cv2.imread("img\rainha.png",-1)

# cv2.imshow("Yodinha colorido", imagem_original2)
# cv2.imshow("Yodinha desbotado", imagem_neutra2)
# cv2.imshow("Yodinha tranparente", imagem_transparente2)

# ----------------------------------
# img = cv2.imread("img\yodinha.jpg")
# print('Tamanho original', img.shape)

# img2 = cv2.imread("img\yodinha.jpg",0)
# print('Tamanho original', img.shape)

# img_cut = img[0:300, 150:350]
# print('Tamanho Cortada', img_cut.shape)

# cv2.imshow("ç", img2)
# cv2.imshow("", img_cut)

# while True:
#         if cv2.waitKey(0) == 120:
#             break
#         if chr(cv2.waitKey(0)) == "x":
#             break

# cv2.destroyAllWindows()
# print(x, chr(x))
#----------------------------------
while True:
    img = np.zeros((512,512,3), np.uint8)

    #Horizontal line
    # s (xi, yi), (xf,yf), (cor), (tamanho)
    cv2.line(img, (150, 0), (150,512), (255,0,255), 5)
    cv2.line(img, (350, 0), (350,512), (255,0,255), 5)

    cv2.line(img, (0, 150), (512,150), (255,0,255), 5)
    cv2.line(img, (0, 350), (512,350), (255,0,255), 5)



    cv2.imwrite("jogo da velha.jpg", img)

    cv2.rectangle(img, (200, 200), (300,300), (0,0,255), -1)

    cv2.circle(img,(75,75), 50, (0,0,255), -1)

    Testo = "COR"
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    linha = cv2.LINE_AA
    cv2.putText(img, Testo, (50,100), fonte, 1.5, (255,0,0),4,linha)

    cv2.imshow("teste", img)
    
    img2 = np.zeros((512,512,3), np.uint8)
    img3 = np.zeros((5096,5096,3), np.uint8)

    cv2.imshow("teste", img2)
    cv2.imshow("teste", img3)
    cv2.waitKey(5)

    cv2.destroyAllWindows()