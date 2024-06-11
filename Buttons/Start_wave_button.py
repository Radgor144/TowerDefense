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

        mobs_to_check = ["orc", "wolf", "minotaur", "dirt_golem"]  # Lista mobów do sprawdzenia

        for i in range(1, 4):  # Iteracja po trasach
            for mob in mobs_to_check:  # Iteracja po mobach
                spawn_data = config.get(f"{mob}_spawn_data", [])
                if any(amount > 0 for amount, route in spawn_data if route['route_name'] == f"route{i}"):
                    setattr(self, f"is_button_shown{i}", True)  # Ustawienie flagi pokazania przycisku dla danej trasy

        self.show_button(screen)

