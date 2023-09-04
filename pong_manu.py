import pygame

ANCHO = 800
ALTO = 600

COLOR_OBJETOS = (255, 255, 255)
COLOR_FONDO = (100, 100, 100)

ANCHO_PALA = 20
ALTO_PALA = 60
MARGEN = 15


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        pos_alto_inicial = ALTO/2 - ALTO_PALA/2

        while not salir:
            # bucle principal
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

            # renderizar objetos (Pantalla)
            pygame.draw.rect(self.pantalla, COLOR_FONDO,
                             ((0, 0), (ANCHO, ALTO)))

            # pintar J1 (Izquierda)
            J1 = pygame.Rect(MARGEN, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, J1)
            # pintar J2 (Derecha)
            J2 = pygame.Rect(ANCHO-MARGEN-ANCHO_PALA,
                             pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, J2)
            # mostrar los cambios en pantalla
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)
