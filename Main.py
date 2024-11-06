import pygame
from Menu import Menu
from Juego import Juego

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Evitar Enemigos")

    menu = Menu()
    jugando = True

    # Bucle del programa
    while jugando:
        menu.esperar_inicio(pantalla)  # Mostrar y esperar en el menú de inicio

        # Si el jugador selecciona "Iniciar Juego", arrancamos el juego
        juego = Juego(pantalla)
        juego.iniciar()

        # Al terminar el juego (por perder o salir), mostrar el menú otra vez
        # o detener el bucle si selecciona salir en el menú
        if menu.estado_menu == "salir":
            jugando = False

    pygame.quit()

if __name__ == "__main__":
    main()
