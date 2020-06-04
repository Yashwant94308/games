import pygame
import sys
from bullet import Bullet
from human import Human
from time import sleep


def key_down(event, eg_setting, screen, virus, bullets, humans, sb, stats):
    if event.key == pygame.K_RIGHT:
        virus.virus_move_right = True
    elif event.key == pygame.K_LEFT:
        virus.virus_move_left = True
    elif event.key == pygame.K_UP:
        virus.virus_move_up = True
    elif event.key == pygame.K_DOWN:
        virus.virus_move_down = True
    elif event.key == pygame.K_p:
        start_game(eg_setting, screen, humans, virus, sb, stats, bullets)

    elif event.key == pygame.K_q:
        bullets.fire_humans_flag = False
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(eg_setting, screen, virus, bullets)


def key_up(event, virus):
    if event.key == pygame.K_RIGHT:
        virus.virus_move_right = False
    elif event.key == pygame.K_LEFT:
        virus.virus_move_left = False
    elif event.key == pygame.K_UP:
        virus.virus_move_up = False
    elif event.key == pygame.K_DOWN:
        virus.virus_move_down = False


def check_event(eg_settings, screen, virus, bullets, humans, buttons, stats, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event, eg_settings, screen, virus, bullets, humans, sb, stats)
        elif event.type == pygame.KEYUP:
            key_up(event, virus)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_y, mouse_x, buttons, stats, eg_settings, screen, humans, virus, sb, bullets)


def check_play_button(mouse_y, mouse_x, buttons, stats, eg_settings, screen, humans, virus, sb, bullets):
    mouse_clicked = buttons.rect.collidepoint(mouse_x, mouse_y)
    if mouse_clicked and not stats.active_game:
        start_game(eg_settings, screen, humans, virus, sb, stats, bullets)


def start_game(eg_settings, screen, humans, virus, sb, stats, bullets):
    pygame.mouse.set_visible(False)
    humans.empty()
    bullets.empty()
    eg_settings.dynamic_speed()
    stats.reset_stat()
    stats.active_game = True
    fire_humans(eg_settings, screen, humans, virus)

    sb.prep_score()
    sb.prep_level()
    sb.prep_virus()


def update_screen(eg_settings, screen, virus, bullets, humans, buttons, stats, sb):
    screen.fill(eg_settings.bg_color)

    """making bullet"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    virus.blitme()

    for human in humans.sprites():
        human.draw_human()
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.active_game:
        buttons.draw_button()

    pygame.display.flip()


def update_bullet(screen, bullets, humans, eg_setting, virus, stats, sb):
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)

    check_bullet_human_collision(bullets, humans, eg_setting, screen, virus, stats, sb)


def check_bullet_human_collision(bullets, humans, eg_setting, screen, virus, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, humans, True, True)
    if collisions:
        if len(humans) == 0:
            bullets.empty()
            eg_setting.increase_speed()
            fire_humans(eg_setting, screen, humans, virus)
        for human in collisions.values():
            stats.score += (eg_setting.hit_score * len(human))
            sb.prep_score()
        check_high_score(sb, stats)


def fire_bullet(eg_settings, screen, virus, bullets):
    """create new bullet and add"""
    new_bullet = Bullet(eg_settings, screen, virus)
    bullets.add(new_bullet)


def virus_gone(stats, humans, bullets, virus, eg_settings, screen, sb):
    if stats.virus_left > 0:
        stats.virus_left -= 1

        bullets.empty()
        humans.empty()
        virus.center_virus()
        sb.prep_virus()
        sb.prep_level()
        fire_humans(eg_settings, screen, humans, virus)
        sleep(1.0)
    else:
        stats.active_game = False
        stats.play_again_flag = -1

        pygame.mouse.set_visible(True)


def update_human(humans, virus, stats, bullets, eg_settings, screen, sb):
    humans.update()
    if pygame.sprite.spritecollideany(virus, humans):
        virus_gone(stats, humans, bullets, virus, eg_settings, screen, sb)
    check_left(stats, humans, bullets, virus, eg_settings, screen, sb)
    check_level(stats, sb)


def check_left(stats, humans, bullets, virus, eg_settings, screen, sb):
    for human in humans.sprites():

        if human.rect.left <= 0:
            virus_gone(stats, humans, bullets, virus, eg_settings, screen, sb)
            break


def fire_humans(eg_settings, screen, humans, virus):
    """create new bullet and add"""
    new_human = Human(eg_settings, screen, virus)
    humans.add(new_human)


def check_high_score(sb, stats):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_level(stats, sb):
    if stats.score == (900 * stats.level):
        stats.level += 1
        sb.prep_level()
