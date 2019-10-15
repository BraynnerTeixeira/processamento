#Detecção de Placas

import numpy as np
import tkinter
import cv2



#Carregando a imagem originl
img = cv2.imread('D:\\Processamento de Imagens\\Reconhecimento de Placa\\imagens\\1.png')
#img = img[::10,::10]


#================================== Pré Processamento ==================================
#Colocando em tons de Cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#cv2.imshow("Tom de Cinza", cinza)

#Aplicando o blur 
blur =  cv2.GaussianBlur(cinza, (7, 7), 0)
#cv2.imshow("Blur", blur)

# Aplicando o filtro laplaciano
lap = cv2.Laplacian(blur, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
#cv2.imshow("Filtro Laplaciano", lap)

#Filtro Canny
canny1 = cv2.Canny(blur, 20, 120)
#cv2.imshow("Liminar MAis baixo", lap)
canny2 = cv2.Canny(blur, 70, 200)
#cv2.imshow("Liminar Mais Alto", lap)

#Aplicando o Filtro Sobel
sobelX = cv2.Sobel(cinza, cv2.CV_64F, 1, 0) 
sobelY = cv2.Sobel(cinza, cv2.CV_64F, 0, 1) 
sobelX = np.uint8(np.absolute(sobelX)) 
sobelY = np.uint8(np.absolute(sobelY)) 
sobel = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel", sobel)
cv2.waitKey(0)
