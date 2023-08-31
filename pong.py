import pygame


ANCHO = 1200
ALTO = 900

C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

ANCHO_PALA = 10
ALTO_PALA = 50

MARGEN = 20

class Pong:
    def __init__(self) -> None:
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        
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

            pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO)))

            # pintar jugador 1 (izquierda)
            jugador1 = pygame.Rect(MARGEN, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador1)

            # pintar jugador 2 (derecha)
            jugador2 = pygame.Rect(ANCHO - MARGEN - ANCHO_PALA, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador2)

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    print('Has llamado a pong.py directamente desde la línea de comandos')
    print('Tamaño de la pantalla', ANCHO, 'x', ALTO)
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)