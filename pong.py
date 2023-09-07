# from typing import Any
from random import randint
import pygame

ANCHO = 1280
ALTO = 720

C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

ANCHO_PALA = 10
ALTO_PALA = 50
MARGEN = 20
TAM_PELOTA = 10

VEL_MAX = 10
VEL_JUGADOR = 5

ARRIBA = True
ABAJO = False

FPS = 35
TAM_LETRA = 100


class Pelota(pygame.Rect):
    def __init__(self):
        super(Pelota, self).__init__((ANCHO-TAM_PELOTA)/2,
                                     (ALTO-TAM_PELOTA)/2, TAM_PELOTA, TAM_PELOTA)
        self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX, VEL_MAX)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y + self.velocidad_y

        if self.y <= 0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.y >= ALTO-TAM_PELOTA:
            self.y = ALTO-TAM_PELOTA
            self.velocidad_y = -self.velocidad_y

    def comprobar_punto(self):
        # Comprobar si la pelota ha salido por los laterales

        # Si sale por la izquierda suma a jugador 2
        if self.right <= 0:
            print("Punto para J2")
            self.center = (ANCHO/2, ALTO/2)
            self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
            self.velocidad_x = randint(-VEL_MAX, -1)
            return 2
        # Si sale por la derecha  suma a jugador 1
        if self.left >= ANCHO:
            print("Punto para J1")
            self.center = (ANCHO/2, ALTO/2)
            self.velocidad_y = randint(-VEL_MAX, VEL_MAX)
            self.velocidad_x = randint(1, VEL_MAX)
            return 1
        return 0


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Jugador, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self, direccion):
        if direccion == ARRIBA:
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= VEL_JUGADOR
        if direccion == ABAJO:
            if self.y >= ALTO - ALTO_PALA:
                self.y = ALTO - ALTO_PALA
            else:
                self.y += VEL_JUGADOR


class Marcador:
    def __init__(self):
        self.reset()
        self.tipografia = pygame.font.SysFont('candara', TAM_LETRA)

    def incrementar(self, jugador):
        self.puntos[jugador-1] += 1

    def reset(self):
        self.puntos = [0, 0]

    def pintame(self, pantalla):

        # puntuacion = str(self.puntos[0])
        # texto = self.tipografia.render(puntuacion, True, C_OBJETOS)
        # pos_x = ANCHO/4
        # pos_y = MARGEN
        # pantalla.blit(texto, (pos_x, pos_y))
        i = 1
        for punto in self.puntos:
            puntuacion = str(punto)
            texto = self.tipografia.render(puntuacion, True, C_OBJETOS)
            pos_x = i * ANCHO/4
            pos_y = MARGEN
            pantalla.blit(texto, (pos_x, pos_y))
            i += 2

    def comprobar_ganador(self):
        pass

        """
    NEcesita:
    - Atributo Guardar la puntuación J1
    - Atributo Guardar la puntuación J2
    - Metodo ponerse a cero
    - Metodo mostrarse en pantalla"""


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.nombre_ventana = pygame.display.set_caption("Manu's Pong")
        # self.cargar_icono = pygame.image.load("icono.png")
        # self.icono = pygame.display.set_icon(self.cargar_icono)
        self.reloj = pygame.time.Clock()

        self.pelota = Pelota()

        self.jugador1 = Jugador(MARGEN, (ALTO-ALTO_PALA)/2)
        self.jugador2 = Jugador(ANCHO - MARGEN, (ALTO-ALTO_PALA)/2)
        self.marcador = Marcador()

    def jugar(self):
        # contiene el bucle principal
        pos_alto_inicial = ALTO/2 - ALTO_PALA/2
        salir = False

        while not salir:
            # bucle principal (o main loop)
            # Boque 1 Captura de eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

            self.comprobar_teclas()

            # BLoque 2 Renderizar nuestros objetos
            self.pantalla.fill(C_FONDO)
            # pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO)))
            self.pintar_red()

            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)

            self.pintar_pelota()
            hay_punto = self.pelota.comprobar_punto()
            if hay_punto > 0:
                self.marcador.incrementar(hay_punto)
                hay_ganador = self.marcador.comprobar_ganador()

            self.marcador.pintame(self.pantalla)

            # Bloque 3: mostrar los cambios en la pantalla
            pygame.display.flip()
            self.reloj.tick(FPS)
        pygame.quit()

    def comprobar_teclas(self):
        estado_teclas = pygame.key.get_pressed()
        if estado_teclas[pygame.K_q]:
            self.jugador1.mover(ARRIBA)
        if estado_teclas[pygame.K_a]:
            self.jugador1.mover(ABAJO)
        if estado_teclas[pygame.K_UP]:
            self.jugador2.mover(ARRIBA)
        if estado_teclas[pygame.K_DOWN]:
            self.jugador2.mover(ABAJO)

    def pintar_pelota(self):
        self.pelota.mover()
        if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self.jugador2):
            self.pelota.velocidad_x = -self.pelota.velocidad_x
        self.pelota.pintame(self.pantalla)

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
