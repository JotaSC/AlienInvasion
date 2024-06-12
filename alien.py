import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase para representar un alien de la flota"""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posición"""
        super().__init__()
        self.screen = ai_game.screen
        # Carga la imagen del alien y establece su rectángulo
        self.image = pygame.image.load('images/greenAlien.bmp')
        self.rect = self.image.get_rect()

        # Cada alien se establece arriba a la izquierda de la pantalla.
        self.rect.x = 0.25 * self.rect.width
        self.rect.y = 0.25 *self.rect.height 

        # Guarda la posición exacta de x del alien.
        self.x = float(self.rect.x)

