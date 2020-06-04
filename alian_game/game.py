import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gamefunction as gf
from game_stats import Game_Stats
from button import Button
from score_board import Score_Board


def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    """groups of aliens"""
    aliens = Group()
    """creating fleet of aliens"""
    gf.create_fleet(ai_settings, screen, ship, aliens)
    """groups of bullets"""
    bullets = Group()

    pygame.display.set_caption("GAMES OF ALIEN")
    # Create an instance to store game statistics.
    stats = Game_Stats(ai_settings)

    play_button = Button(ai_settings, screen, stats, ship, bullets, gf)

    sb = Score_Board(ai_settings, screen, stats)

    # RUNNING MAIN LOOP
    while True:
        # RUNNING EVENT LOOP FOR CONTROL GAME USING KEYBOARD
        gf.check_event(ai_settings, screen, ship, sb, bullets, stats, play_button, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
