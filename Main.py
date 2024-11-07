import pygame
from Menu import Menu
from Juego import Juego

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Evitar Enemigos")

    while True:
        # Crear menú y esperar hasta que el jugador elija iniciar
        menu = Menu()
        menu.esperar_inicio(pantalla)  # Mostrar y esperar en el menú de inicio

        # Obtener dificultad seleccionada y crear el juego con esa dificultad
        dificultad = menu.obtener_dificultad()
        juego = Juego(pantalla, dificultad)  # Pasar la dificultad al juego
        juego.iniciar()

        # Si el juego se termina, mostrar el menú de fin
        if not juego.en_juego:
            menu.mostrar_menu_fin(pantalla)

if __name__ == "__main__":
    main()
