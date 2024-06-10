import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Clase general para controlar los 'game assets' y el comportamiento"""

    def __init__(self):
        """Inicia el juego y crea los recursos del juego"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Empieza el main loop para el juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde a los eventos ocurridos (ratón y teclado)"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a los eventos de pulsar"""
        if event.key == pygame.K_RIGHT:
            # Mueve la nave hacia la derecha
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # Mueve la nave hacia la izquieda
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a los eventos de dejar de pulsar"""
        if event.key == pygame.K_RIGHT:
            # Deja de mover la nave hacia la derecha
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            # Deja de mover la nave hacia la izquieda
            self.ship.moving_left = False

    def _update_screen(self):
        """Actualiza la imagen en pantalla y visualiza la nueva imagen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        pygame.display.flip()


if __name__ == '__main__':
    # Haz una instancia del juego y ejecútala.
    ai = AlienInvasion()
    ai.run_game()