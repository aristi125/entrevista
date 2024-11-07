import pygame

class Disparo:
    def __init__(self, x, y, direccion, color=(255, 255, 0)):
        """Inicializa una bala con una posición, dirección y color."""
        self.posicion = pygame.Rect(x, y, 10, 10)  # Tamaño de la bala
        self.velocidad = 7
        self.direccion = direccion  # Dirección en formato (dx, dy)
        self.color = color  # Color de la bala

    def mover(self):
        """Mueve la bala en la dirección especificada."""
        self.posicion.x += self.velocidad * self.direccion[0]
        self.posicion.y += self.velocidad * self.direccion[1]

    def dibujar(self, pantalla):
        """Dibuja la bala en pantalla."""
        pygame.draw.rect(pantalla, self.color, self.posicion)  # Dibujar la bala con el color especificado
