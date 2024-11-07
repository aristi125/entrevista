import pygame
import random
from Contador import Contador
from Enemigo import Enemigo
from Jugador import Jugador
from Menu import Menu
from Disparo import Disparo

class Juego:
    def __init__(self, pantalla, dificultad):
        """Inicializa el juego con la dificultad especificada."""
        self.pantalla = pantalla
        self.dificultad = dificultad  # Asigna la dificultad seleccionada
        self.en_juego = True
        self.jugador = Jugador()
        self.enemigos = self.generar_enemigos_por_dificultad()
        self.balas = []  # Lista para almacenar las balas activas del jugador
        self.balas_enemigas = []  # Lista para almacenar las balas activas de los enemigos
        self.menu = Menu()
        self.contador = Contador()
        self.reloj = pygame.time.Clock()

    def generar_enemigos_por_dificultad(self):
        """Genera enemigos según el nivel de dificultad."""
        if self.dificultad == 1:
            return [self.generar_enemigo_alejado() for _ in range(5)]
        elif self.dificultad == 2:
            return [self.generar_enemigo_alejado() for _ in range(10)]
        elif self.dificultad == 3:
            return [self.generar_enemigo_alejado() for _ in range(15)]

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
                    if self.menu.estado_menu == "inicio":
                        self.en_juego = False
                elif evento.key == pygame.K_SPACE:
                    # Disparar una bala
                    self.disparar_bala()

                # Manejo de eventos del jugador
                self.jugador.manejar_eventos(evento)

    def disparar_bala(self):
        """Crea una bala en la posición del jugador y la añade a la lista de balas."""
        direccion = (1, 0)  # Ejemplo: disparo a la derecha
        nueva_bala = Disparo(self.jugador.posicion.centerx, self.jugador.posicion.centery, direccion)
        self.balas.append(nueva_bala)

    def actualizar(self):
        """Actualiza el estado del juego, incluyendo balas y enemigos."""
        self.jugador.actualizar()

        # Actualizar balas del jugador
        for bala in self.balas:
            bala.mover()

        # Actualizar balas enemigas
        for bala_enemiga in self.balas_enemigas:
            bala_enemiga.mover()

        # Verificar colisiones
        self.verificar_colisiones()
        self.verificar_colisiones_entre_balas()
        self.verificar_colisiones_balas_enemigas()

        # Actualizar enemigos y hacer que disparen
        for enemigo in self.enemigos:
            enemigo.actualizar(self.jugador)
            if self.dificultad >= 2 and random.randint(1, 100) < 3:  # Probabilidad de disparo en niveles avanzados
                nueva_bala_enemiga = enemigo.disparar_bala(self.jugador)
                self.balas_enemigas.append(nueva_bala_enemiga)

            if enemigo.colisiona(self.jugador):
                # Fin del juego si el jugador es atacado
                self.en_juego = False
                self.menu.mostrar_menu_fin(self.pantalla)

    def verificar_colisiones(self):
        """Verifica colisiones entre las balas del jugador y los enemigos."""
        enemigos_restantes = []
        for enemigo in self.enemigos:
            colision = False
            for bala in self.balas:
                if bala.posicion.colliderect(enemigo.posicion):
                    colision = True
                    self.contador.incrementar()
                    self.balas.remove(bala)
                    break
            if not colision:
                enemigos_restantes.append(enemigo)

        # Actualizamos la lista de enemigos eliminando aquellos que fueron alcanzados por balas
        self.enemigos = enemigos_restantes

    def verificar_colisiones_balas_enemigas(self):
        """Verifica si alguna bala enemiga colisiona con el jugador."""
        for bala_enemiga in self.balas_enemigas:
            if bala_enemiga.posicion.colliderect(self.jugador.posicion):
                # Fin del juego si el jugador es alcanzado
                self.en_juego = False
                self.menu.mostrar_menu_fin(self.pantalla)

    def verificar_colisiones_entre_balas(self):
        """Verifica colisiones entre las balas del jugador y las balas enemigas."""
        balas_jugador_restantes = []
        balas_enemigas_restantes = []

        for bala in self.balas:
            colision = False
            for bala_enemiga in self.balas_enemigas:
                if bala.posicion.colliderect(bala_enemiga.posicion):
                    colision = True
                    self.balas_enemigas.remove(bala_enemiga)
                    break
            if not colision:
                balas_jugador_restantes.append(bala)

        self.balas = balas_jugador_restantes

    def generar_enemigo_alejado(self):
        """Genera un enemigo en una posición alejada del jugador."""
        distancia_minima = 200
        enemigo = Enemigo()

        # Generar posición hasta que esté lejos del jugador
        while True:
            enemigo.posicion.x = random.randint(0, 750)
            enemigo.posicion.y = random.randint(0, 550)
            distancia = ((enemigo.posicion.x - self.jugador.posicion.x) ** 2 +
                         (enemigo.posicion.y - self.jugador.posicion.y) ** 2) ** 0.5
            if distancia >= distancia_minima:
                break

        return enemigo

    def dibujar(self):
        """Dibuja todos los elementos en pantalla."""
        self.pantalla.fill((0, 0, 0))
        self.jugador.dibujar(self.pantalla)

        # Dibujar enemigos
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)

        # Dibujar balas del jugador
        for bala in self.balas:
            bala.dibujar(self.pantalla)

        # Dibujar balas enemigas
        for bala_enemiga in self.balas_enemigas:
            bala_enemiga.dibujar(self.pantalla)

        # Mostrar el contador de enemigos eliminados
        self.contador.mostrar(self.pantalla)
        pygame.display.flip()

    def terminar(self):
        """Finaliza el juego."""
        pygame.quit()
