import pygame

class Contador:
    def __init__(self):
        self.eliminados = 0

    def incrementar(self):
        """Incrementa el contador de enemigos eliminados."""
        self.eliminados += 1

    def mostrar(self, pantalla):
        """Muestra el contador en pantalla."""
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(f"Eliminados: {self.eliminados}", True, (255, 255, 255))
        pantalla.blit(texto, (10, 10))
