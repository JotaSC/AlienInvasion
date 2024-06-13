import sys
import pygame
import time

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # Flag para poder detener el juego una vez ha habido GAME OVER
        self.game_active = True

    def run_game(self):
        """Empieza el main loop para el juego"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
        elif event.key == pygame.K_LEFT:
            # Mueve la nave hacia la izquieda
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a los eventos de dejar de pulsar"""
        if event.key == pygame.K_RIGHT:
            # Deja de mover la nave hacia la derecha
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            # Deja de mover la nave hacia la izquieda
            self.ship.moving_left = False

    def _update_bullets(self):
        """Actualiza la posición de las balas y deshace las balas perdidas"""
        # Actualiza la posición de las balas.
        self.bullets.update()

        # Revisa si alguna bala ha colisionado con un alien.
        # Si lo ha hecho, elimina la bala y el alien.
        self._check_bullet_alien_collisions()

        # Deshacerse de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if not self.aliens:
            # Destruye las balas existentes y crea una nueva flota
            self.bullets.empty()
            self._create_fleet()

    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas"""
        if len(self.bullets) < self. settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Crea la flota de aliens"""
        # Crea un alien y sigue añadiendo aliens mientras haya espacio
        # El espacio entre alien y alien es 0.3 alien (altura y anchura)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x , current_y = 1 * alien_width, 0.25 * alien_height 
        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - 1.28 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1.28 * alien_width
            
            # Acaba la fila, resetear la X y aumentar la Y.
            current_x = 1 * alien_width
            current_y += 1.1 * alien_height
    
    def _check_fleet_edges(self):
        """Responde apropiadamente si un alien toca el borde de la pantalla"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja la flota entera una altura y cambia su dirección movimiento"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, position_x, position_y):
        """Crea un alien y lo coloca en su posición"""
        new_alien = Alien(self)
        new_alien.x = position_x
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Actualiza la posición de todos los aliens de la flota"""
        self._check_fleet_edges()
        self.aliens.update()

        # Revisa si ha habido una colisión alien-nave
        for alien in self.aliens:
            if alien.rect.bottom >= (
                self.settings.screen_height - self.ship.rect.height):
                    self._ship_hit()
                    break

    def _ship_hit(self):
        """Interactúa cuando un alien llega a la altura de la nave"""
        if self.stats.ships_left > 0:
            # Decrementa las vidas de la nave
            self.stats.ships_left -= 1
            # Muestra cómo los aliens han llegado a la altura de la nave
            self._update_screen()
            # Espera 1s
            time.sleep(1)

            # Deshacerse de las balas y aliens
            self.bullets.empty()
            self.aliens.empty()

            # Crear una nueva flota y volver a centrar la nave
            self._create_fleet()
            self.ship.center_ship()

            # Elimina los eventos de teclado (evitar disparos falsos tras morir)
            pygame.event.clear()
            self.ship.restart_movements_flags()
        else:
            self.game_active = False

    def _update_screen(self):
        """Actualiza la imagen en pantalla y visualiza la nueva imagen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Haz una instancia del juego y ejecútala.
    ai = AlienInvasion()
    ai.run_game()