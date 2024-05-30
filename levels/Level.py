import pygame
from enemies.Orc import Orc
from enemies.Wolf import Wolf

class Level:
    def __init__(self, level_data, enemy_group, mapa):
        self.enemy_group = enemy_group
        self.mapa = mapa

        self.orc_spawn_data = level_data.get("orc_spawn_data", [])
        self.wolf_spawn_data = level_data.get("wolf_spawn_data", [])

        # Dodanie zmiennych do śledzenia zespawnowanych przeciwników dla każdego typu i trasy
        self.orc_spawned_on_route1 = 0
        self.orc_spawned_on_route2 = 0
        self.orc_spawned_on_route3 = 0

        self.wolf_spawned_on_route1 = 0
        self.wolf_spawned_on_route2 = 0
        self.wolf_spawned_on_route3 = 0

        # Dodanie zmiennych timera spawnu dla każdej trasy i każdego typu przeciwnika
        self.orc_spawn_timer_on_route1 = 0
        self.orc_spawn_timer_on_route2 = 0
        self.orc_spawn_timer_on_route3 = 0

        self.wolf_spawn_timer_on_route1 = 0
        self.wolf_spawn_timer_on_route2 = 0
        self.wolf_spawn_timer_on_route3 = 0

        # Load images
        self.orc_image = pygame.image.load("enemies/assets/orc/orc1.png").convert_alpha()
        self.wolf_image = pygame.image.load("enemies/assets/wolf/wolf1.png").convert_alpha()

    def update(self, current_time):
        for spawn_data in self.orc_spawn_data:
            amount, route = spawn_data

            # Wybierz odpowiednie zmienne do śledzenia ilości zespawnowanych przeciwników i timera spawnu
            spawn_var_name = f"orc_spawned_on_{route['route_name']}"    # dynamiczna zmiana nazwy zmiennej
            timer_var_name = f"orc_spawn_timer_on_{route['route_name']}"

            if getattr(self, spawn_var_name) < amount:
                if current_time - getattr(self, timer_var_name) >= route["spawn_interval"]:
                    waypoints = getattr(self.mapa, route["route_name"])
                    new_orc = Orc(waypoints, self.orc_image)
                    self.enemy_group.add(new_orc)
                    setattr(self, spawn_var_name, getattr(self, spawn_var_name) + 1)
                    setattr(self, timer_var_name, current_time)

        for spawn_data in self.wolf_spawn_data:
            amount, route = spawn_data

            # Analogicznie do orków, ale dla wilków
            spawn_var_name = f"wolf_spawned_on_{route['route_name']}"
            timer_var_name = f"wolf_spawn_timer_on_{route['route_name']}"

            if getattr(self, spawn_var_name) < amount:
                if current_time - getattr(self, timer_var_name) >= route["spawn_interval"]:
                    waypoints = getattr(self.mapa, route["route_name"])
                    new_wolf = Wolf(waypoints, self.wolf_image)
                    self.enemy_group.add(new_wolf)
                    setattr(self, spawn_var_name, getattr(self, spawn_var_name) + 1)
                    setattr(self, timer_var_name, current_time)

    def is_level_finished(self):
        return len(self.enemy_group) == 0
