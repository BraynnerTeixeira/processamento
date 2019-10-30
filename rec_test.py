#Detecção de Placas
import numpy as np
import tkinter
import cv2


print("chegou aqui")
def procurar(contornos,imagem):
    for c in contornos:
        # perimetro do contorno, verifica se o contorno é fechado
        perimetro = cv2.arcLength(c, True)
        if perimetro > 200 and perimetro < 600:
           #aproxima os contornos da forma correspondente
           approx = cv2.approxPolyDP(c, 0.03 * perimetro, True)
           #verifica se é um quadrado ou retangulo de acordo com a qtd de vertices
           if len(approx) == 4:
             #Contorna a placa atraves dos contornos encontrados
             #cv2.drawContours(imagem, [c], -1, (0, 255, 0), 2)
             (x, y, lar, alt) = cv2.boundingRect(c)
             cv2.rectangle(imagem, (x, y), (x + lar, y + alt), (0, 255, 0), 2)
             #segmenta a placa da imagem
             roi = imagem[(y+15):y+alt, x:x+lar]
             #salva a imagem segmentada em "C:/Tesseract-OCR/saidas/"
             cv2.imwrite('D:\\Processamento de Imagens\\Reconhecimento de Placa\\saida\\te.jpg', roi)
    return imagem


#Carregando a imagem originl
img = cv2.imread('D:\\Processamento de Imagens\\Reconhecimento de Placa\\imagens\\1.png')

#area de localização
area = img[100: , 80:1200]
 
    # escala de cinza
img_result = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
 
    # limiarização
ret, img_result = cv2.threshold(img_result, 90, 255, cv2.THRESH_BINARY)
 
    # desfoque
img_result = cv2.GaussianBlur(img_result, (5, 5), 0)
 
    # lista os contornos
img, contornos = cv2.findContours(img_result, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

 
cv2.imshow('FRAME', img_result)
#procurar(contornos, area)                 
cv2.imshow("Final", area)
cv2.waitKey(0)              
