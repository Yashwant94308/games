import pygame.font


class Button:
    def __init__(self, eg_settings, screen, stats, virus, bullets, gf):
        self.screen = screen
        self.stats = stats
        self.gf = gf
        self.virus = virus
        self.bullets = bullets
        self.eg_settings = eg_settings
        self.screen_rect = screen.get_rect()

        """making button"""
        self.width, self.height = 250, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48, True)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect_again = pygame.Rect(0, 0, self.width, self.height)

        """center the button on screen"""

        self.rect.center = self.screen_rect.center
        self.rect_again.center = self.screen_rect.center

        """message passing to prep_msg function"""
        self.prep_msg("Play")

    def prep_msg(self, msg):

        """making msg image to show on screen"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_again = self.font.render("Play-Again", True, self.text_color, self.button_color)
        self.over_image_again = self.font.render("Game-Over", True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_again_rect = self.msg_image_again.get_rect()

        self.msg_image_again_rect.center = self.rect.center
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        if self.stats.play_again_flag == 1:
            # Draw blank button and then draw message.
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        elif self.stats.play_again_flag == -1:
            # Draw blank button and then draw message.
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image_again, self.msg_image_again_rect)
