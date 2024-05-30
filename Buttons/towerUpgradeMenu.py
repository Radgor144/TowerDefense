import pygame

MENU_HEIGHT = 100
MENU_WIDTH = 100


class TowerUpgradeMenu():
    def __init__(self):
        self.upgrade_button_image = pygame.image.load("assets/content/UI/Button_Hover.png").convert_alpha()
        self.menu_surface = pygame.Surface((0, 0))
        self.menu_rect = pygame.Rect(0, 0, 64, 64)  # Prostokąt menu
        self.button_rect = self.menu_rect
        self.is_menu_shown = False

    def show_menu(self, surface, turret_position):
        # Ustaw pozycję menu
        x, y = turret_position
        self.menu_rect.topleft = (x, y - 100)

        # Ustaw pozycję przycisku w menu
        self.button_rect = self.menu_rect  # Tu możesz dostosować pozycję przycisku, np. na środek menu

        self.is_menu_shown = True
        self.update(surface)

    def hide_menu(self):
        self.is_menu_shown = False

    def handle_click(self, click_pos):
        if self.menu_rect.collidepoint(click_pos):
            # Kliknięto w obszar menu, możesz obsłużyć to tutaj
            pass

    def update(self, surface):
        # Sprawdź, czy menu powinno być wyświetlane
        if self.is_menu_shown:
            surface.blit(self.menu_surface, self.menu_rect)
            # Umieść przycisk na środku menu
            self.button_rect = self.menu_rect
            surface.blit(self.upgrade_button_image, self.button_rect)

    def update_tower(self, surface, tower_position, turret_lvl):
        print("XXX")
        x, y = tower_position
        surface.blit(turret_lvl, (x, y))
