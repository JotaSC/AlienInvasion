import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase para representar un alien de la flota"""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posición"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la imagen del alien y establece su rectángulo
        self.image = pygame.image.load('images/greenAlien.bmp')
        self.rect = self.image.get_rect()

        # Cada alien se establece arriba a la izquierda de la pantalla.
        self.rect.x = 0.3 * self.rect.width
        self.rect.y = 0.3 * self.rect.height 

        # Guarda la posición exacta de x del alien.
        self.x = float(self.rect.x)

    def update(self):
        """Mueve el alien hacia la derecha"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Devuelve True si el alien ha tocado el borde de la pantalla"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
