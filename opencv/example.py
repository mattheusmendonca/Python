import numpy as np
#o np é o apelido que criamos para carregar modulos do numpy
import cv2

obj_img = cv2.imread('amor.jpeg', cv2.IMREAD_COLOR)

#variavel = cv2.ler imagem do endereço passado como parametro
#cv2.namedWindow('cleiton')
#cv2.imshow('cleiton', img)
#cv2.waitKey()

from matplotlib import pyplot as plt
#a partir da biblioteca para criação de graficos importe um modulo presente
#nessa biblioteca que baseado em MATLAB, que é um software baseado para o cálculo de matrizes
#plt, é o apelido que usamos para carregar modulos pyplot
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
#a imagem vai receber dentro no cv.2, a alteração de cor para a cor normal
plt.imshow(obj_img)
#aqui você vai construir a imagem para aparecer na janela gráfica
plt.show()
#aqui ele vai reproduzir a janela
