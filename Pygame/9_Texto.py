import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Texto")

miFuente = pygame.font.Font(None, 30)
miTexto = miFuente.render("Prueba Fuente", 0, (200, 60, 80), (200, 200, 120))

miFuenteSistema = pygame.font.SysFont("Arial", 30)
miTextoDos = miFuenteSistema.render("Prueba Fuente 2", 0, (200, 60, 80), (200, 200, 120))
while True:
    ventana.blit(miTexto, (100, 180))
    ventana.blit(miTextoDos, (100, 280))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


