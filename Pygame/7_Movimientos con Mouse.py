import pygame, sys
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("THE GAME")

Mi_imagen = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Benja/videos/CONTENIDO AUDIOVISUAL/"
                              "LOGOS/185px-Netflix_2015_N_logo.svg.png")
# Dónde va la imagen
PosX, PosY = 0, 0
velocidad = 2

Blanco = (255, 255, 255)
derecha = True


while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen, (PosX, PosY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                PosX -= velocidad
            elif evento.key == K_RIGHT:
                PosX += velocidad
        elif evento.type == pygame.KEYUP:
            if evento.key == K_LEFT:
                print("Tecla izquierda liberada")
            elif evento.key == K_RIGHT:
                print("Tecla derecha liberada")
    PosX, PosY = pygame.mouse.get_pos()
    PosX -= 100
    PosY -= 150
    print(pygame.mouse.get_pos()) # Regresa una tupla con los valores de la posición del mouse
    pygame.display.update()
