import pygame


ANCHO = 800
ALTO = 600


class Pong:
    def __init__(self) -> None:
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        
    def jugar(self):    # contiene el bucle principal
        salir = False
        while not salir:
            # bucle principal (o main loop)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True


            # renderizar nuestros objetos

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    print('Has llamado a pong.py directamente desde la línea de comandos')
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)