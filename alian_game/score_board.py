import pygame.font
from pygame.sprite import Group
from ship import Ship


class Score_Board:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        """font setting for score board"""
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48, True)
        """high score"""

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """Turn the score into a rendered image."""
        self.rounded_score = int(round(self.stats.score))
        score_str = "{:,}".format(self.rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.rounded_high_score = int(round(self.stats.high_score))
        high_score_str = "{:,}".format(self.rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.ai_settings.bg_color)
        # Display the high score at the top center of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)
        # Display the level at the below of the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        self.ship = Group()
        print(self.stats.ship_left)

        for ship_number in range(self.stats.ship_left):
            """creating ship"""
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ship.add(ship)

    def show_score(self):
        """showing the score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ship.draw(self.screen)

