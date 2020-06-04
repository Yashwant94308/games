import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        # moving to the right
        ship.moving_right = True
    # moving to left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        """creating new bullets function"""
        fire_bullets(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # after releasing right arrow ship stop
        ship.moving_right = False
    # after releasing left arrow ship stop
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_event(ai_settings, screen, ship, sb, bullets, stats, play_button, aliens):
    # RUNNING EVENT LOOP FOR CONTROL GAME USING KEYBOARD
    for event in pygame.event.get():
        # IF STATEMENT FOR USING KEYBOARD
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            """clicking on play button"""

            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    mouse_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if mouse_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """hiding the mouse cursor"""
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    # Reset the scoreboard images.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ship()

    bullets.empty()
    aliens.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # it updates the screen
    # filling screen with color
    screen.fill(ai_settings.bg_color)

    """redraw the bullet"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # make most recently draw visible
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_aliens_collision(aliens, bullets, ai_settings, screen, ship, stats, sb)


def check_bullet_aliens_collision(aliens, bullets, ai_settings, screen, ship, stats, sb):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.

    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += (ai_settings.alien_score * len(aliens)  )
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        """all aliens has destroyed then creating new"""
        bullets.empty()
        ship.center_ship()
        ai_settings.increase_speed()
        """increase level"""
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edge(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets):
    """Respond to ship being hit by alien."""

    if stats.ship_left > 0:
        # Decrement ships_left.
        stats.ship_left -= 1
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        sb.prep_ship()
        """ create new fleet and center of ship"""
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause the game
        sleep(0.5)
    else:
        stats.play_again_flag = -1
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_alien_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        """checking alien hitting bottom"""
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets):
    """
     Check if the fleet is at an edge,
     and then update the positions of all aliens in the fleet.
     """
    check_fleet_edge(ai_settings, aliens)
    """updating the positions of all aliens of the fleet"""
    aliens.update()

    """alien ship collision"""
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
    """alien hitting bottom"""
    check_alien_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) <= ai_settings.bullets_allowed:
        """creating new bullet"""
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    """ number of aliens can feet on screen"""
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_aliens(ai_settings, screen, alien_number, number_rows, aliens):
    """creating aliens and placing in row"""
    alien = Alien(ai_settings, screen)
    """positioning the aliens in x and y plane"""
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # creating full aliens
    """finding number of aliens and width of screen"""
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    """number of rows"""
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)
    """creating 1st row of aliens"""
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            """ call of function of creating row of aliens"""
            create_aliens(ai_settings, screen, alien_number, row_number, aliens)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
