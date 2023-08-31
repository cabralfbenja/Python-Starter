import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400, 500))
pygame.display.set_caption("THE GAME")

# Círculos
#                dónde    color             centro radio
pygame.draw.circle(ventana, (0, 140, 140), (300, 90), 20)

# Rectangulos
#                dónde    color           inicio,ancho,largo
pygame.draw.rect(ventana, (0, 140, 0), (0, 0, 200, 80))

# Polígonos
#                   dónde    color           inicio,ancho,largo
pygame.draw.polygon(ventana, (240, 40, 40), ((140, 0), (291, 106), (237, 277), (56, 277), (0, 106))) #Pentágono

# La ventana se muestra con un loop infinito
while True:
    for evento in pygame.event.get():
        # Ponemos  un evento para que salga con QUIT
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
