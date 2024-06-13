class GameStats:
    """Analiza las diferentes estadísticas de la partida"""

    def __init__(self, ai_game):
        """Inicializa las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Establece las estadísticas que cambiarán durante la partida"""
        self.ships_left = self.settings.ship_limit