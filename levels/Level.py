import pygame
from enemies.Orc import Orc
from enemies.Wolf import Wolf
from enemies.Minotaur import Minotaur
from enemies.Dirt_golem import Dirt_golem


class Level:
    def __init__(self, level_data, enemy_group, mapa):
        self.enemy_group = enemy_group
        self.mapa = mapa

        self.victory_wave_sound = pygame.mixer.Sound("assets/music/victory.mp3")
        self.victory_wave_sound.set_volume(0.1)

        self.spawn_data = {
            "orc": {
                "data": level_data.get("orc_spawn_data", []),
                "image": pygame.image.load("assets/orc/orc1.png").convert_alpha(),
                "class": Orc,
                "spawned": {"route1": 0, "route2": 0, "route3": 0},
                "timers": {"route1": 0, "route2": 0, "route3": 0},
            },
            "wolf": {
                "data": level_data.get("wolf_spawn_data", []),
                "image": pygame.image.load("assets/wolf/wolf1.png").convert_alpha(),
                "class": Wolf,
                "spawned": {"route1": 0, "route2": 0, "route3": 0},
                "timers": {"route1": 0, "route2": 0, "route3": 0},
            },
            "minotaur": {
                "data": level_data.get("minotaur_spawn_data", []),
                "image": pygame.image.load("assets/minotaur/minotaur2.png").convert_alpha(),
                "class": Minotaur,
                "spawned": {"route1": 0, "route2": 0, "route3": 0},
                "timers": {"route1": 0, "route2": 0, "route3": 0},
            },
            "dirt_golem": {
                "data": level_data.get("dirt_golem_spawn_data", []),
                "image": pygame.image.load("assets/dirt golem/dirt_golem.png").convert_alpha(),
                "class": Dirt_golem,
                "spawned": {"route1": 0, "route2": 0, "route3": 0},
                "timers": {"route1": 0, "route2": 0, "route3": 0},
            },
        }

        self.victory_played = False

    def update(self, current_time):
        for enemy_type, enemy_info in self.spawn_data.items():
            for amount, route in enemy_info["data"]:
                route_name = route["route_name"]
                spawn_var = enemy_info["spawned"]
                timer_var = enemy_info["timers"]

                if spawn_var[route_name] < amount:
                    if current_time - timer_var[route_name] >= route["spawn_interval"]:
                        waypoints = getattr(self.mapa, route_name)
                        new_enemy = enemy_info["class"](waypoints, enemy_info["image"])
                        self.enemy_group.add(new_enemy)
                        spawn_var[route_name] += 1
                        timer_var[route_name] = current_time

        if len(self.enemy_group) == 0 and not self.victory_played:
            self.victory_wave_sound.play()
            self.victory_played = True
