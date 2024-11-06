import pygame
import random

class Jugador:
    def __init__(self):
        self.color = (0, 255, 0)
        self.posicion = pygame.Rect(400, 300, 50, 50)
        self.velocidad = 5

    def manejar_eventos(self, evento):
        """Maneja eventos específicos del jugador."""
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:
                self.cambiar_color()

    def cambiar_color(self):
        """Cambia el color del jugador."""
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def actualizar(self):
        """Actualiza la posición del jugador."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.posicion.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.posicion.x += self.velocidad
        if keys[pygame.K_UP]:
            self.posicion.y -= self.velocidad
        if keys[pygame.K_DOWN]:
            self.posicion.y += self.velocidad

    def dibujar(self, pantalla):
        """Dibuja el jugador en pantalla."""
        pygame.draw.rect(pantalla, self.color, self.posicion)
