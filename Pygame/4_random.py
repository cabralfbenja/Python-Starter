import pygame, sys
from pygame.locals import *
from  random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("THE GAME")

Mi_imagen = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Benja/capo.png")
# Dónde va la imagen
PosX, PosY = randint(0, 500), randint(0, 50)

ventana.blit(Mi_imagen, (PosX, PosY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
