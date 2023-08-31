import pygame, sys
from pygame.locals import *

# COLORES
Color = pygame.Color(0, 140, 60)

pygame.init()
ventana = pygame.display.set_mode((400, 500))
pygame.display.set_caption("THE GAME")

# Para dibujar cualquier figura geométrica pygame.draw
#                dónde    color  inicio     final    ancho
pygame.draw.line(ventana, Color, (60, 80), (160, 100), 8)

# Para verificar el color
print(Color.r)
print(Color.b)
print(Color.g)

# La ventana se muestra con un loop infinito
while True:
    for evento in pygame.event.get():
        # Ponemos  un evento para que salga con QUIT
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
