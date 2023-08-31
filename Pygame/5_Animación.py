import pygame, sys
from pygame.locals import *
from  random import randint

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("THE GAME")

Mi_imagen = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Benja/videos/CONTENIDO AUDIOVISUAL/"
                              "LOGOS/185px-Netflix_2015_N_logo.svg.png")
# Dónde va la imagen
PosX, PosY = 0, randint(0, 50)
velocidad = 5

Blanco = (255, 255, 255)
derecha = True


while True:
    ventana.fill(Blanco)
    # Para actualizar la imagen, la ponemos en el while
    ventana.blit(Mi_imagen, (PosX, PosY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if derecha:
        if PosX < 600:
            PosX += velocidad
        else:
            derecha = False
    else:
        if PosX > 1:
            PosX -= velocidad
        else:
            derecha = True
    pygame.display.update()
