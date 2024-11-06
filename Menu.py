import pygame

class Menu:
    def __init__(self):
        """Inicializa el menú con las opciones disponibles."""
        self.estado_menu = "inicio"  # Puede ser "inicio", "pausa", "dificultad", "color", "fin"
        self.opciones = {
            "inicio": ["Iniciar Juego", "Seleccionar Dificultad", "Salir"],
            "pausa": ["Continuar", "Reiniciar", "Salir"],
            "dificultad": ["Fácil", "Medio", "Difícil"],
            "color": ["Cambiar Color del Jugador", "Cambiar Color de los Enemigos"],
            "fin": ["Reiniciar Juego", "Salir"]
        }
        self.seleccion_actual = 0

    def mostrar(self, pantalla):
        """Muestra el menú actual en la pantalla solo si está en un estado válido."""
        if self.estado_menu not in self.opciones:
            return  # No mostramos el menú si está en un estado no válido

        pantalla.fill((0, 0, 0))  # Fondo negro
        fuente = pygame.font.Font(None, 50)

        # Título del menú
        titulo = fuente.render(f"Menú de {self.estado_menu.capitalize()}", True, (255, 255, 255))
        pantalla.blit(titulo, (200, 50))

        # Opciones del menú actual
        for i, opcion in enumerate(self.opciones[self.estado_menu]):
            color = (255, 0, 0) if i == self.seleccion_actual else (255, 255, 255)
            texto = fuente.render(opcion, True, color)
            pantalla.blit(texto, (250, 150 + i * 50))

    def manejar_eventos(self, evento):
        """Maneja la navegación del menú según las teclas presionadas."""
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                # Mueve la selección hacia abajo
                self.seleccion_actual = (self.seleccion_actual + 1) % len(self.opciones[self.estado_menu])
            elif evento.key == pygame.K_UP:
                # Mueve la selección hacia arriba
                self.seleccion_actual = (self.seleccion_actual - 1) % len(self.opciones[self.estado_menu])
            elif evento.key == pygame.K_RETURN:
                # Selecciona la opción actual
                self.seleccionar_opcion()

    def seleccionar_opcion(self):
        """Ejecuta la acción correspondiente a la opción seleccionada."""
        if self.estado_menu == "inicio":
            if self.seleccion_actual == 0:  # Iniciar Juego
                return  # Salimos de `esperar_inicio` para iniciar el juego
            elif self.seleccion_actual == 1:  # Seleccionar Dificultad
                self.estado_menu = "dificultad"
            elif self.seleccion_actual == 2:  # Salir
                self.estado_menu = "salir"

        elif self.estado_menu == "pausa":
            if self.seleccion_actual == 0:  # Continuar
                self.estado_menu = "inicio"
            elif self.seleccion_actual == 1:  # Reiniciar
                self.estado_menu = "inicio"
            elif self.seleccion_actual == 2:  # Salir
                self.estado_menu = "salir"

        elif self.estado_menu == "fin":
            if self.seleccion_actual == 0:  # Reiniciar Juego
                self.estado_menu = "inicio"
            elif self.seleccion_actual == 1:  # Salir
                self.estado_menu = "salir"

    def esperar_inicio(self, pantalla):
        """Controla el menú de inicio, esperando que el jugador seleccione una opción."""
        en_menu = True
        while en_menu:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Navegación del menú
                self.manejar_eventos(evento)

            # Dibujar el menú en pantalla
            self.mostrar(pantalla)
            pygame.display.flip()

            # Salir del bucle si el jugador elige "Iniciar Juego"
            if self.estado_menu == "inicio" and self.seleccion_actual == 0:
                en_menu = False
            elif self.estado_menu == "inicio" and self.seleccion_actual == 2:
                self.estado_menu = "salir"
                en_menu = False

    def mostrar_menu_pausa(self, pantalla):
        """Muestra y controla el menú de pausa."""
        self.estado_menu = "pausa"
        self.seleccion_actual = 0
        en_menu_pausa = True
        while en_menu_pausa:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Manejo de eventos en el menú de pausa
                self.manejar_eventos(evento)

            # Dibujar el menú de pausa en pantalla
            self.mostrar(pantalla)
            pygame.display.flip()

            # Si el jugador elige "Continuar" o "Salir", salir del menú de pausa
            if self.estado_menu == "inicio" or self.estado_menu == "salir":
                en_menu_pausa = False

    def mostrar_menu_fin(self, pantalla):
        """Muestra el menú al final del juego cuando el jugador pierde."""
        self.estado_menu = "fin"
        self.seleccion_actual = 0
        en_menu_fin = True
        while en_menu_fin:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Manejo de eventos en el menú de fin de juego
                self.manejar_eventos(evento)

            # Dibujar el menú de fin en pantalla
            self.mostrar(pantalla)
            pygame.display.flip()

            # Si el jugador elige "Reiniciar Juego" o "Salir", salir del menú de fin
            if self.estado_menu == "inicio" or self.estado_menu == "salir":
                en_menu_fin = False
