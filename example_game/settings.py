class Settings:
    def __init__(self):
        """screen settings"""

        self.bg_color = (250, 230, 230)
        self.screen_width = 1200
        self.screen_height = 600

        """bullet settings"""
        self.virus_limit = 3

        self.bullet_allowed = 30
        self.speed_up = .03
        self.dynamic_speed()



    def dynamic_speed(self):
        """humans settings"""
        self.human_speed_factor = .25
        self.bullet_speed_factor = 2
        self.hit_score = 50
        self.virus_speed_factor = 1.

    def increase_speed(self):
        self.human_speed_factor += self.speed_up
        self.bullet_speed_factor += self.speed_up
        self.virus_speed_factor += self.speed_up


