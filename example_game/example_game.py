from pygame.sprite import Group
import pygame
from settings import Settings
from virus import Virus
import game_function as gf
from stats import Stats
from play_button import Button
from score_board import Score_Board


def run_game():
    eg_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((eg_settings.screen_width, eg_settings.screen_height))

    virus = Virus(eg_settings, screen)
    pygame.display.set_caption("virus human")
    humans = Group()
    bullets = Group()
    stats = Stats(eg_settings)
    buttons = Button(eg_settings, screen, stats, virus, bullets, gf)
    sb = Score_Board(eg_settings, screen, stats)

    while True:
        gf.check_event(eg_settings, screen, virus, bullets, humans, buttons, stats, sb)

        if stats.active_game:
            virus.update()

            gf.update_bullet(screen, bullets, humans, eg_settings, virus, stats, sb)
            gf.update_human(humans, virus, stats, bullets, eg_settings, screen, sb)
            if virus.flag:
                gf.fire_humans(eg_settings, screen, humans, virus)

        gf.update_screen(eg_settings, screen, virus, bullets, humans, buttons, stats, sb)


run_game()
