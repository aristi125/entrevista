import pygame

class Disparo:
    def __init__(self, x, y, direccion):
        self.posicion = pygame.Rect(x, y, 10, 10)  # Tamaño de la bala
        self.velocidad = 7
        self.direccion = direccion  # Dirección de la bala, por ejemplo (1, 0) para derecha

    def mover(self):
        """Mueve la bala en la dirección especificada."""
        self.posicion.x += self.velocidad * self.direccion[0]
        self.posicion.y += self.velocidad * self.direccion[1]

    def dibujar(self, pantalla):
        """Dibuja la bala en pantalla."""
        pygame.draw.rect(pantalla, (255, 255, 0), self.posicion)  # Bala amarilla
