import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Texto")
aux = 1

miFuente = pygame.font.SysFont("Arial", 30)
while True:
    ventana.fill((255, 255, 255))
    Tiempo = pygame.time.get_ticks()/1000
    if aux == Tiempo:
        print(Tiempo)
        aux += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    contador = miFuente.render("Tiempo: "+ str(Tiempo), 0, (0, 0, 255))
    ventana.blit(contador, (0, 0))
    pygame.display.update()
