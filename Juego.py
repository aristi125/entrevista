import pygame
from Contador import Contador
from Disparo import Disparo
from Enemigo import Enemigo
from Jugador import Jugador
from Menu import Menu

class Juego:
    def __init__(self, pantalla):
        """Inicializa el juego y todos los elementos necesarios."""
        self.pantalla = pantalla
        self.jugador = Jugador()
        self.enemigos = [Enemigo() for _ in range(5)]
        self.balas = []  # Lista para almacenar las balas activas
        self.menu = Menu()
        self.contador = Contador()

        self.dificultad = 1  # Nivel inicial
        self.en_juego = False
        self.reloj = pygame.time.Clock()

    def iniciar(self):
        """Inicia el bucle principal del juego."""
        self.en_juego = True
        while self.en_juego:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(30)

    def manejar_eventos(self):
        """Maneja todos los eventos de entrada."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.en_juego = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    # Mostrar el menú de pausa
                    self.menu.mostrar_menu_pausa(self.pantalla)
                    # Salir del juego si el jugador selecciona salir en el menú de pausa
                    if self.menu.estado_menu == "salir":
                        self.en_juego = False
                elif evento.key == pygame.K_SPACE:
                    # Disparar una bala
                    self.disparar_bala()

                # Manejo de eventos del jugador
                self.jugador.manejar_eventos(evento)

    def disparar_bala(self):
        """Crea una bala en la posición del jugador y la añade a la lista de balas."""
        direccion = (1, 0)  # Por ejemplo, disparo a la derecha
        nueva_bala = Disparo(self.jugador.posicion.centerx, self.jugador.posicion.centery, direccion)
        self.balas.append(nueva_bala)

    def actualizar(self):
        """Actualiza el estado del juego, incluyendo balas y enemigos."""
        self.jugador.actualizar()

        # Actualizar posición de cada bala
        for bala in self.balas:
            bala.mover()

        # Verificar colisiones de balas con enemigos
        self.verificar_colisiones()

        # Actualizar enemigos y verificar si colisionan con el jugador
        for enemigo in self.enemigos:
            enemigo.actualizar(self.jugador)
            if enemigo.colisiona(self.jugador):
                # Fin del juego si el jugador es atacado
                self.en_juego = False
                # Mostrar menú de fin de juego
                self.menu.mostrar_menu_fin(self.pantalla)
                # Salir del juego si el jugador selecciona salir en el menú de fin
                if self.menu.estado_menu == "salir":
                    pygame.quit()
                    quit()

        # Aumentar dificultad gradualmente si todos los enemigos fueron eliminados
        if len(self.enemigos) == 0 and self.dificultad < 3:
            self.dificultad += 1
            self.enemigos = [Enemigo() for _ in range(5 * self.dificultad)]

        # Eliminar balas que salen de la pantalla
        self.balas = [bala for bala in self.balas if 0 <= bala.posicion.x <= 800 and 0 <= bala.posicion.y <= 600]

    def verificar_colisiones(self):
        """Verifica colisiones entre las balas y los enemigos."""
        enemigos_restantes = []
        for enemigo in self.enemigos:
            colision = False
            for bala in self.balas:
                if bala.posicion.colliderect(enemigo.posicion):
                    colision = True
                    self.contador.incrementar()  # Aumentar contador si un enemigo es eliminado
                    self.balas.remove(bala)  # Eliminar la bala que golpeó al enemigo
                    break
            if not colision:
                enemigos_restantes.append(enemigo)

        # Actualizamos la lista de enemigos eliminando aquellos que fueron alcanzados por balas
        self.enemigos = enemigos_restantes

    def dibujar(self):
        """Dibuja todos los elementos en pantalla."""
        self.pantalla.fill((0, 0, 0))
        self.jugador.dibujar(self.pantalla)

        # Dibujar enemigos
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)

        # Dibujar balas
        for bala in self.balas:
            bala.dibujar(self.pantalla)

        # Mostrar el contador de enemigos eliminados
        self.contador.mostrar(self.pantalla)
        pygame.display.flip()

    def terminar(self):
        """Finaliza el juego."""
        pygame.quit()
