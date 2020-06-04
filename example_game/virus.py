import pygame
from pygame.sprite import Sprite


class Virus(Sprite):
    def __init__(self, eg_settings, screen):
        super(Virus, self).__init__()
        self.eg_settings = eg_settings
        self.screen = screen
        self.screen_Rect = self.screen.get_rect()
        self.image = pygame.image.load("covid.bmp")
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_Rect.centery

        self.virus_center = float(self.rect.centerx)
        self.flag = False
        self.virus_move_up = False
        self.virus_move_down = False
        self.virus_move_left = False
        self.virus_move_right = False

    def update(self):
        if self.virus_move_right and self.rect.right <= (self.eg_settings.screen_width/2):
            self.virus_center += self.eg_settings.virus_speed_factor
        if self.virus_move_left and self.rect.left >= 0:
            self.virus_center -= self.eg_settings.virus_speed_factor
        if self.virus_move_up and self.rect.top >= self.screen_Rect.top:
            self.rect.bottom -= self.eg_settings.virus_speed_factor
        if self.virus_move_down and self.rect.bottom <= self.screen_Rect.bottom:
            self.rect.bottom += self.eg_settings.virus_speed_factor
        self.rect.centerx = self.virus_center
        self.rect.bottom = self.rect.bottom

    def center_virus(self):
        self.rect.centery = self.screen_Rect.centery
        self.virus_center = 36

    def blitme(self):
        """updating screen with image"""
        self.screen.blit(self.image, self.rect)
