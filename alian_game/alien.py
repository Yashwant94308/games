import pygame
from pygame.sprite import Sprite

"""making of single alien fleet"""


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """loading the image of alien"""
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        """situating alien to top lef corner"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """alien exact position in decimal"""
        self.x = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien right and down"""
        self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)

    def blitme(self):
        # drawing alien at current location.
        self.screen.blit(self.image, self.rect)
