#Detecção de Placas
import numpy as np
import cv2

print("chegou aqui")
def procurar(contornos,imagem):
    for c in contornos:
        # perimetro do contorno, verifica se o contorno é fechado
        perimetro = cv2.arcLength(c, True)
        if perimetro > 200 and perimetro < 2000:
           #aproxima os contornos da forma correspondente
           approx = cv2.approxPolyDP(c, 0.03 * perimetro, True)
           #verifica se é um quadrado ou retangulo de acordo com a qtd de vertices
           if len(approx) == 4:
             #Contorna a placa atraves dos contornos encontrados
             (x, y, lar, alt) = cv2.boundingRect(c)
             cv2.rectangle(imagem, (x, y), (x + lar, y + alt), (0, 255, 0), 2)
             #segmenta a placa da imagem
             roi = imagem[(y+15):y+alt, x:x+lar]
             #salva a imagem segmentada
             cv2.imwrite('D:\\Processamento de Imagens\\Reconhecimento de Placa\\saida\\te.jpg', roi)
             cv2.imshow("Placa Resgatada", roi)
    return imagem


    # Carregando a imagem originl
img = cv2.imread('D:\\Processamento de Imagens\\Reconhecimento de Placa\\imagens\\11.png')

    # area de localização
area = img[100: , 80:1200]
 
    # escala de cinza
img_result = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
 
    # limiarização
img, img_result = cv2.threshold(img_result, 90, 255, cv2.THRESH_BINARY)
 
    # desfoque
img_result = cv2.GaussianBlur(img_result, (7, 7), 0)
 
    # lista os contornos
contornos,img = cv2.findContours(img_result, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
#cv2.imshow('FRAME', img_result)
procurar(contornos, area)                 
cv2.imshow("Final", area)
cv2.waitKey(0)              
