class Settings:
    def __init__(self):
        """screen setting"""
        self.screen_width = 1350
        self.screen_height = 600
        self.bg_color = (255, 230, 230)

        """bullet settings"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        """alien setting"""
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.03
        self.score_up_scale = 1.03

        """ship setting"""
        self.ship_limit = 3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1

        """it will change the direction"""
        self.fleet_direction = 1
        """score"""
        self.alien_score = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.score_up_scale)
