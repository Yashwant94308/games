import pygame.font
from pygame.sprite import Group
from virus import Virus


class Score_Board:
    def __init__(self, eg_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.eg_settings = eg_settings
        self.stats = stats
        """font setting for score board"""
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48, True)
        """high score"""
        self.prep_virus()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        self.rounded_score = int(round(self.stats.score))
        score_str = "{:,}".format(self.rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.eg_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.rounded_high_score = int(round(self.stats.high_score))
        high_score_str = "{:,}".format(self.rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.eg_settings.bg_color)
        # Display the high score at the top center of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.eg_settings.bg_color)
        # Display the level at the below of the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_virus(self):

        self.virus = Group()

        for virus_number in range(self.stats.virus_left):
            """creating virus"""
            virus = Virus(self.eg_settings, self.screen)
            virus.rect.x = (self.eg_settings.screen_width - 190) + virus_number * virus.rect.width
            virus.rect.y = (self.eg_settings.screen_height - 60)
            self.virus.add(virus)

    def show_score(self):
        """showing the score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.virus.draw(self.screen)

