class Game_Stats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        """ending the game"""
        self.game_active = False
        self.high_score = 0
        """ play again flag"""
        self.play_again_flag = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
