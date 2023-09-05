# from typing import Any
from random import randint
import pygame


ANCHO = 1200
ALTO = 850

C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

ANCHO_PALA = 10
ALTO_PALA = 50
MARGEN = 20
TAM_PELOTA = 10

VEL_MAX = 3


class Pelota:
    def __init__(self):
        self.rectangulo = pygame.Rect(
            (ANCHO-TAM_PELOTA)/2, (ALTO-TAM_PELOTA)/2, TAM_PELOTA, TAM_PELOTA)
        self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX, VEL_MAX)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self.rectangulo)

    def mover(self):
        self.rectangulo.x = self.rectangulo.x + self.velocidad_x
        self.rectangulo.y = self.rectangulo.y + self.velocidad_y

        if self.rectangulo.y <= 0:
            self.rectangulo.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.rectangulo.y >= ALTO-TAM_PELOTA:
            self.rectangulo.y = ALTO-TAM_PELOTA
            self.velocidad_y = -self.velocidad_y

    def comprobar_punto(self):
        # Comprobar si la pelota ha salido por los laterales
        # Si sale por la derecha  suma a jugador 1
        # Si sale por la izquierda suma a jugador 2
        pass


class Jugador:
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(
            x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self.rectangulo)


class Pong:
    def __init__(self) -> None:
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN, (ALTO-ALTO_PALA)/2)
        self.jugador2 = Jugador(ANCHO - MARGEN, (ALTO-ALTO_PALA)/2)

    def jugar(self):
        # contiene el bucle principal
        pos_alto_inicial = ALTO/2 - ALTO_PALA/2
        salir = False

        while not salir:
            # bucle principal (o main loop)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
            # renderizar nuestros objetos
            # PANTALLA
            pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO)))

            self.pintar_red()
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)

            self.pelota.mover()
            self.pelota.pintame(self.pantalla)

            # pintar red

            # pintar marcador

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        tramo_pintado = 30
        tramo_vacio = 15
        ancho_red = 2
        posicion_x = (ANCHO)/2
        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(self.pantalla, C_OBJETOS,
                             (posicion_x, y,), (posicion_x, y + tramo_pintado), ancho_red)


if __name__ == '__main__':
    print('Has llamado a pong.py directamente desde la línea de comandos')
    print('Tamaño de la pantalla', ANCHO, 'x', ALTO)
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)
