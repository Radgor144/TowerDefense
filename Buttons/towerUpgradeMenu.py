import pygame

MENU_HEIGHT = 100
MENU_WIDTH = 100


class TowerUpgradeMenu:
    def __init__(self):
        self.upgrade_button_image = pygame.image.load("assets/content/UI/Button_Hover.png").convert_alpha()
        self.menu_surface = pygame.Surface((0, 0))
        self.menu_rect = pygame.Rect(0, 0, 64, 64)  # Prostokąt menu
        self.button_rect = self.menu_rect
        self.is_menu_shown = False
        self.cost = 100
        self.cost_rect = self.menu_rect

    def show_menu(self, surface, turret_position, upgrade_cost):
        # Ustaw pozycję menu
        x, y = turret_position
        self.menu_rect.topleft = (x, y - 100)
        self.cost = upgrade_cost
        self.is_menu_shown = True
        self.update(surface)

    def hide_menu(self):
        self.is_menu_shown = False

    def update(self, surface):
        # Sprawdź, czy menu powinno być wyświetlane
        if self.is_menu_shown:
            surface.blit(self.menu_surface, self.menu_rect)
            # Umieść przycisk na środku menu
            self.button_rect = self.menu_rect
            surface.blit(self.upgrade_button_image, self.button_rect)

            font = pygame.font.Font(None, 28)
            text_surface = font.render(str(self.cost), True, (255, 255, 255))
            text_position = (self.menu_rect.x + 15, self.menu_rect.y + 15)
            surface.blit(text_surface, text_position)

