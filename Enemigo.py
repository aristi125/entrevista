import pygame
import random
import math
from Disparo import Disparo

class Enemigo:
    def __init__(self):
        self.color = (255, 0, 0)
        self.posicion = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 40, 40)
        self.velocidad = random.randint(1, 3)

    def actualizar(self, jugador):
        """Actualiza la posición del enemigo acercándose al jugador."""
        if self.posicion.x < jugador.posicion.x:
            self.posicion.x += self.velocidad
        elif self.posicion.x > jugador.posicion.x:
            self.posicion.x -= self.velocidad
        if self.posicion.y < jugador.posicion.y:
            self.posicion.y += self.velocidad
        elif self.posicion.y > jugador.posicion.y:
            self.posicion.y -= self.velocidad

    def colisiona(self, jugador):
        """Verifica si el enemigo ha colisionado con el jugador."""
        return self.posicion.colliderect(jugador.posicion)

    def disparar_bala(self, jugador):
        """Genera una bala que se dirige hacia el jugador."""
        dx = jugador.posicion.centerx - self.posicion.centerx
        dy = jugador.posicion.centery - self.posicion.centery
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        direccion = (dx / distancia, dy / distancia)  # Dirección normalizada
        return Disparo(self.posicion.centerx, self.posicion.centery, direccion)

    def dibujar(self, pantalla):
        """Dibuja el enemigo en pantalla."""
        pygame.draw.rect(pantalla, self.color, self.posicion)
