import pygame


class Start_wave_button:

    def __init__(self):
        self.start_button_image = pygame.image.load("./assets/content/UI/sword.png").convert_alpha()
        self.red_button_image = pygame.image.load("./assets/content/UI/Button_Red.png").convert_alpha()
        self.red_button_rect = pygame.Rect(20, 270, 64, 64)
        self.button_rect = pygame.Rect(36, 279, 64, 64)
        self.is_button_shown = True

    def show_button(self, screen):
        self.is_button_shown = True

        screen.blit(self.red_button_image, self.red_button_rect)
        screen.blit(self.start_button_image, self.button_rect)

    def hide_button(self):
        self.is_button_shown = False

    def update(self, screen):

        if self.is_button_shown:
            self.show_button(screen)


