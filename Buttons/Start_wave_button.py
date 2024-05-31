import pygame


class Start_wave_button:

    def __init__(self):
        self.start_button_image = pygame.image.load("./assets/content/UI/sword.png").convert_alpha()
        self.red_button_image = pygame.image.load("./assets/content/UI/Button_Red.png").convert_alpha()
        self.red_button_rect1 = pygame.Rect(20, 270, 64, 64)
        self.button_rect1 = pygame.Rect(36, 279, 64, 64)

        self.red_button_rect2 = pygame.Rect(20, 490, 64, 64)
        self.button_rect2 = pygame.Rect(36, 500, 64, 64)

        self.red_button_rect3 = pygame.Rect(710, 30, 64, 64)
        self.button_rect3 = pygame.Rect(725, 40, 64, 64)

        self.is_button_shown1 = False
        self.is_button_shown2 = False
        self.is_button_shown3 = False

    def show_button(self, screen):
        if self.is_button_shown1:
            screen.blit(self.red_button_image, self.red_button_rect1)
            screen.blit(self.start_button_image, self.button_rect1)

        if self.is_button_shown2:
            screen.blit(self.red_button_image, self.red_button_rect2)
            screen.blit(self.start_button_image, self.button_rect2)

        if self.is_button_shown3:
            screen.blit(self.red_button_image, self.red_button_rect3)
            screen.blit(self.start_button_image, self.button_rect3)

    def hide_buttons(self):
        self.is_button_shown1 = False
        self.is_button_shown2 = False
        self.is_button_shown3 = False

    def update(self, screen, level_configs, current_level_index):
        config = level_configs[current_level_index]

        orc_spawn_data = config.get("orc_spawn_data", [])
        wolf_spawn_data = config.get("wolf_spawn_data", [])

        for spawn_data in orc_spawn_data:
            amount, route = spawn_data
            is_orc_coming = route['route_name']

            if is_orc_coming == "route1" and amount > 0:
                self.is_button_shown1 = True

            if is_orc_coming == "route2" and amount > 0:
                self.is_button_shown2 = True

            if is_orc_coming == "route3" and amount > 0:
                self.is_button_shown3 = True

        for spawn_data in wolf_spawn_data:
            amount, route = spawn_data
            is_wolf_coming = route['route_name']

            if is_wolf_coming == "route1" and amount > 0:
                self.is_button_shown1 = True

            if is_wolf_coming == "route2" and amount > 0:
                self.is_button_shown2 = True

            if is_wolf_coming == "route3" and amount > 0:
                self.is_button_shown3 = True

        self.show_button(screen)
