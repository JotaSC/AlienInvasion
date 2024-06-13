import pygame

class Ship:
    """La clase que manejará a la nave"""

    def __init__(self, ai_game):
        """Crea la nave y establece su posición inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga el barco y obtiene sus dimensiones
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.center_ship()

        # Flag de movimiento; empieza con una nave que no se mueve
        self.restart_movements_flags()

    def update(self):
        """Actualiza la posición de la nave según la flag de movimiento"""
        # Actualiza la posición x de la nave, no la del rectángulo.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza la posición x del rectángulo a partir de la de la nave.
        self.rect.x = self.x

    def center_ship(self):
        """Coloca el barco en el centro-abajo de la pantalla"""
        self.rect.midbottom = self.screen_rect.midbottom
        # Guarda un float para la posición horizontal exacta de la nave
        self.x = float(self.rect.x)

    def restart_movements_flags(self):
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Dibuja la nave en su posición actual"""
        self.screen.blit(self.image, self.rect)