import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, eg_settings, screen, virus):
        super(Bullet, self).__init__()
        self.virus = virus
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.eg_settings = eg_settings
        self.bullet_image = pygame.image.load("bullet.bmp")
        self.rect = self.bullet_image.get_rect()
        self.rect.centery = self.virus.rect.centery
        self.rect.right = self.virus.rect.right
        self.speed_factor = self.eg_settings.bullet_speed_factor

        """adjusting decimal value of bullet"""
        self.x = float(self.rect.x)


    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.bullet_image, self.rect)
