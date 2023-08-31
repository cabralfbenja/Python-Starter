import pygame
import sys
from pygame.locals import *
from random import randint

ancho = 900
alto = 480
listaEnemigo = []

class naveEspacial(pygame.sprite.Sprite):
    """ Clase para las Naves
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/nave.jpg")
        self.ImagenExplosion = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/explosion.jpg")
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho / 2
        self.rect.centery = alto - 30

        self.listaDisparo = []
        self.Vida = True

        self.velocidad = 50
        self.sonidoDisparo = pygame.mixer.Sound("C:/Users/NOTEBOOK/Desktop/Pygame/FIUMBA.mp3")
        self.sonidoExplosion = pygame.mixer.Sound("C:/Users/NOTEBOOK/Desktop/Pygame/goku.mp3")

    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.Vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.left > 870:
                self.rect.left = 840

    def disparar(self, x, y):
        miProyectil = proyectil(x, y, "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/disparoa.jpg", True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
    def destruccion(self):
        self.sonidoExplosion.play()
        self.Vida = False
        self.velocidad = 0
        self.ImagenNave = self.ImagenExplosion


class proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        self.imagenProyectil = pygame.image.load(ruta)

        self.rect = self.imagenProyectil.get_rect()

        self.velocidadDisparo = 3

        self.rect.top = posy
        self.rect.left = posx

        self.disparoPersonaje = personaje

    def trayectoria(self):
        if self.disparoPersonaje:
            self.rect.top -= self.velocidadDisparo
        else:
            self.rect.top += self.velocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)


class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA = pygame.image.load(imagenUno)
        self.imagenB = pygame.image.load(imagenDos)
        self.listaImagenes = [self.imagenA, self.imagenB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenA.get_rect()

        self.listaDisparos = []
        self.velocidad = 10
        self.rect.top = posy
        self.rect.left = posx

        self.tiempoCambio = 1
        self.rangoDisparo = 5

        self.conquista = False

        self.derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top + 40

        self.limiteDerecha = posx + distancia
        self.limiteIzquierda = posx - distancia

    def dibujar(self, superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)

    def comportamiento(self, tiempo):
        if self.conquista == False:
            self.__movimientos()
            self.__ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen += 1
                self.tiempoCambio += 1

                if self.posImagen > len(self.listaImagenes) - 1:
                    self.posImagen = 0

    def __movimientos(self):
        if self.contador < 3:
            self.__movimientolateral()
        else:
            self.__descenso()

    def __descenso(self):
        if self.Maxdescenso == self.rect.top:
            self.contador = 0
            self.Maxdescenso = self.rect.top + 40
        else:
            self.rect.top += 1

    def __movimientolateral(self):
        if self.derecha:
            self.rect.left += self.velocidad
            if self.rect.left > self.limiteDerecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left -= self.velocidad
            if self.rect.left < self.limiteIzquierda:
                self.derecha = True

    def __ataque(self):
        if randint(0, 500) < self.rangoDisparo:
            self.__disparo()

    def __disparo(self):
        x, y = self.rect.center
        miProyectil = proyectil(x, y, "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/disparob.jpg", False)
        self.listaDisparos.append(miProyectil)

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparos:
            enemigo.listaDisparos.remove(disparo)
        enemigo.conquista = True

def cargarEnemigos():
    posx = 100
    for i in range(4):
        enemigo = Invasor(posx, 100, 40, "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/marcianoA.jpg",
                                    "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/MarcianoB.jpg")
        listaEnemigo.append(enemigo)
        posx += 200

    posx = 100
    for i in range(4):
        enemigo = Invasor(posx, 0, 40, "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/Marciano2A.jpg",
                                    "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/Marciano2B.jpg")
        listaEnemigo.append(enemigo)
        posx += 200

    posx = 100
    for i in range(4):
        enemigo = Invasor(posx, -100, 40, "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/Marciano3A.jpg",
                              "C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/Marciano3B.jpg")
        listaEnemigo.append(enemigo)
        posx += 200

def ganar(ventana):
    fuente = pygame.font.SysFont("Arial", 50, True)
    texto = fuente.render("GANASTE!!!!!", 0, (255, 255, 255))
    ventana.blit(texto, (350, 50))

def spaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Space Invaders")
    ImagenFondo = pygame.image.load("C:/Users/NOTEBOOK/Desktop/Pygame/Primer Juego/Fondo.jpg")
    pygame.mixer.music.load("C:/Users/NOTEBOOK/Desktop/Pygame/MUSICA.mp3")
    pygame.mixer.music.play(3)

    miFuente = pygame.font.SysFont("Arial", 30)
    Texto = miFuente.render("Fin del Juego", 0, (120, 100, 40))
    jugador = naveEspacial()
    cargarEnemigos()

    enJuego = True

    reloj = pygame.time.Clock()

    while True:

        reloj.tick(60)
        tiempo = round(pygame.time.get_ticks() / 1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key == pygame.K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        ventana.blit(ImagenFondo, (0, 0))

        jugador.dibujar(ventana)

        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)

                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)
        if len(listaEnemigo) > 0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)
                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego = False
                    detenerTodo()

                if len(enemigo.listaDisparos) > 0:
                    for x in enemigo.listaDisparos:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego = False
                            detenerTodo()

                        if x.rect.top > 900:
                            enemigo.listaDisparos.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparos.remove(x)
        elif len(listaEnemigo) == 0:
            ganar(ventana)
            enJuego = False

        if enJuego == False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto, (400, 200))
        pygame.display.update()

if __name__ == "__main__":
    spaceInvader()

