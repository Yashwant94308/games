import pygame
from pygame.sprite import Sprite

"""class to manage bullet fire from ship"""


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """creating bullet object"""
        super(Bullet, self).__init__()
        self.screen = screen

        """creating bullet rect object at a position"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        """bullet position in decimal value"""
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    """updating bullet position"""

    def update(self):
        self.y -= self.speed_factor
        """ updating bullet position"""
        self.rect.y = self.y

    """creating bullet"""

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
