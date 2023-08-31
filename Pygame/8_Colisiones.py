import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((700, 500))
pygame.display.set_caption("THE GAME")

rectangulo_2 = pygame.Rect(300, 300, 100, 50)

PosX, PosY = 200, 100
velocidad = 1

Blanco = (255, 255, 255)
derecha = True

rectangulo = pygame.Rect(0, 0, 100, 50)

while True:
    ventana.fill(Blanco)
    pygame.draw.rect(ventana, (180, 70, 70), rectangulo)
    pygame.draw.rect(ventana, (70, 180, 70), rectangulo_2)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

    if rectangulo.colliderect(rectangulo_2):
        velocidad = 0

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if derecha:
        if PosX < 600:
            PosX += velocidad
            rectangulo_2.left = PosX
        else:
            derecha = False
    else:
        if PosX > 1:
            PosX -= velocidad
            rectangulo_2.left = PosX
        else:
            derecha = True
    pygame.display.update()
