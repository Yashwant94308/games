import pygame
from pygame.sprite import Sprite
import random


class Human(Sprite):
    def __init__(self, eg_settings, screen, virus):
        super(Human, self).__init__()
        self.screen = screen
        self.virus = virus
        self.screen_rect = screen.get_rect()
        self.eg_settings = eg_settings
        self.human_image = pygame.image.load("human.bmp")
        self.rect = self.human_image.get_rect()
        self.rect.centery = random.randint(28, 580)
        self.rect.right = self.screen_rect.right
        self.speed_factor = self.eg_settings.human_speed_factor

        """adjusting decimal value of bullet"""
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.speed_factor

        self.rect.x = self.x
        if self.rect.x == random.randint(950, 1080):
            self.virus.flag = True
        else:
            self.virus.flag = False

    def draw_human(self):
        self.screen.blit(self.human_image, self.rect)
