import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Clase para controlar las balas disparadas por las naves"""

    def __init__(self, ai_game):
        """Crea el objeto bala en la posición de la nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la bala y obtiene sus dimensiones
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda la posición de la bala como float
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""
        # Actualiza la posición exacta de la bala
        self.y -= self.settings.bullet_speed
        # Actualiza la posición del rectángulo
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla"""
        self.screen.blit(self.image, self.rect)