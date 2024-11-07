import pygame

class Menu:
    def __init__(self):
        """Inicializa el menú con las opciones disponibles."""
        self.estado_menu = "inicio"  # Puede ser "inicio", "pausa", "dificultad", "fin", "victoria"
        self.opciones = {
            "inicio": ["Iniciar Juego", "Seleccionar Dificultad", "Salir"],
            "pausa": ["Continuar", "Reiniciar", "Salir"],
            "dificultad": ["Fácil", "Medio", "Difícil"],
            "fin": ["Reiniciar Juego", "Salir"],
            "victoria": ["Reiniciar Juego", "Salir"]  # Opciones para el menú de victoria
        }
        self.seleccion_actual = 0
        self.dificultad_seleccionada = 1  # Dificultad por defecto (1 = fácil)

    def mostrar(self, pantalla):
        """Muestra el menú actual en la pantalla solo si está en un estado válido."""
        if self.estado_menu not in self.opciones:
            return  # No mostramos el menú si está en un estado no válido

        pantalla.fill((0, 0, 0))  # Fondo negro
        fuente = pygame.font.Font(None, 50)

        # Título del menú
        titulo_texto = "Menú de " + self.estado_menu.capitalize() if self.estado_menu != "victoria" else "¡Victoria!"
        titulo = fuente.render(titulo_texto, True, (255, 255, 255))
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
                self.estado_menu = "jugando"  # Cambia el estado para iniciar el juego
            elif self.seleccion_actual == 1:  # Seleccionar Dificultad
                self.estado_menu = "dificultad"  # Cambia al menú de dificultad
            elif self.seleccion_actual == 2:  # Salir
                pygame.quit()
                quit()

        elif self.estado_menu == "dificultad":
            # Cambiar la dificultad según la selección
            if self.seleccion_actual == 0:
                self.dificultad_seleccionada = 1  # Fácil
            elif self.seleccion_actual == 1:
                self.dificultad_seleccionada = 2  # Medio
            elif self.seleccion_actual == 2:
                self.dificultad_seleccionada = 3  # Difícil
            self.estado_menu = "inicio"  # Volver al menú inicial después de seleccionar

        elif self.estado_menu == "pausa":
            if self.seleccion_actual == 0:  # Continuar
                self.estado_menu = "jugando"
            elif self.seleccion_actual == 1:  # Reiniciar
                self.estado_menu = "inicio"  # Volvemos al menú inicial
            elif self.seleccion_actual == 2:  # Salir
                pygame.quit()
                quit()

        elif self.estado_menu == "fin":
            if self.seleccion_actual == 0:  # Reiniciar Juego
                self.estado_menu = "inicio"  # Volver al menú inicial para reiniciar
            elif self.seleccion_actual == 1:  # Salir
                pygame.quit()
                quit()

        elif self.estado_menu == "victoria":
            if self.seleccion_actual == 0:  # Reiniciar Juego
                self.estado_menu = "inicio"  # Volver al menú inicial para reiniciar
            elif self.seleccion_actual == 1:  # Salir
                pygame.quit()
                quit()

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
            if self.estado_menu == "jugando":
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
            # Si el jugador elige "Continuar", salir del menú de pausa
            if self.estado_menu == "jugando":
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
            if self.estado_menu == "inicio":
                en_menu_fin = False

    def mostrar_menu_victoria(self, pantalla):
        """Muestra un menú de victoria cuando el jugador alcanza el nivel máximo."""
        self.estado_menu = "victoria"
        self.seleccion_actual = 0
        en_menu_victoria = True
        while en_menu_victoria:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Manejo de eventos en el menú de victoria
                self.manejar_eventos(evento)
            # Dibujar el menú de victoria en pantalla
            self.mostrar(pantalla)
            pygame.display.flip()
            # Salir del menú de victoria si elige "Reiniciar Juego" o "Salir"
            if self.estado_menu == "inicio":
                en_menu_victoria = False

    def obtener_dificultad(self):
        """Devuelve la dificultad seleccionada para ser usada en el juego."""
        return self.dificultad_seleccionada
