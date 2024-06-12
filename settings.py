class Settings:
    """Una clase que guarda toda la configuración de Alien Invasion"""

    def __init__(self):
        """Inicia la configuración del juego"""
        # Configuración del juego
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (82, 85, 116)

        # Configuración de la nave
        self.ship_speed = 3.0

        # Configuración de los disparos
        self.bullet_speed = 3.5
        self.bullets_allowed = 5