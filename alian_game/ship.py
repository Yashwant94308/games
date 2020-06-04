import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ai_settings):

        super(Ship, self).__init__()
        """for ship adjustment on screen"""
        self.screen = screen

        # load image and make its rect
        self.image = pygame.image.load('gameimage\ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # adjusting ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.ai_settings = ai_settings

        # store decimal value to for ship center
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):

        # continuous movement
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >= 0:
            self.center -= self.ai_settings.ship_speed_factor

        """updating rect value to centerx"""
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def blitme(self):
        # drawing ship at current location.
        self.screen.blit(self.image, self.rect)
