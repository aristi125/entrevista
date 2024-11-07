import pygame

class Contador:
    def __init__(self):
        self.eliminados = 0
        self.nivel = 1  # Nivel inicial

    def incrementar(self):
        """Incrementa el contador de enemigos eliminados."""
        self.eliminados += 1

    def actualizar_nivel(self, nivel):
        """Actualiza el nivel en el contador."""
        self.nivel = nivel

    def mostrar(self, pantalla):
        """Muestra el contador y el nivel actual en pantalla."""
        fuente = pygame.font.Font(None, 36)
        texto_eliminados = fuente.render(f"Eliminados: {self.eliminados}", True, (255, 255, 255))
        texto_nivel = fuente.render(f"Nivel: {self.nivel}", True, (255, 255, 255))

        pantalla.blit(texto_eliminados, (10, 10))
        pantalla.blit(texto_nivel, (10, 50))
