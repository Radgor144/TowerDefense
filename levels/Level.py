import pygame
from enemies.Orc import Orc
from enemies.Wolf import Wolf


class Level:
    def __init__(self, level_data, enemy_group, mapa):
        self.enemy_group = enemy_group
        self.mapa = mapa

        self.amount_of_orcs = level_data.get("amount_of_orcs", 0)
        self.amount_of_wolfs = level_data.get("amount_of_wolfs", 0)

        self.orc_spawn_interval = level_data.get("orc_spawn_interval", 500)
        self.wolf_spawn_interval = level_data.get("wolf_spawn_interval", 300)

        self.orc_spawned = 0
        self.wolf_spawned = 0

        self.mob_spawn_timer = 0  # Timer for next enemy spawn

        # load images
        self.orc_image = pygame.image.load("enemies/assets/orc/orc1.png").convert_alpha()
        self.wolf_image = pygame.image.load("enemies/assets/wolf/wolf1.png").convert_alpha()

    def update(self, current_time):
        # Spawn orcs
        if self.orc_spawned < self.amount_of_orcs and current_time - self.mob_spawn_timer >= self.orc_spawn_interval:
            new_orc = Orc(self.mapa.waypoints, self.orc_image)
            self.enemy_group.add(new_orc)
            self.orc_spawned += 1
            self.mob_spawn_timer = current_time

        # Spawn wolfs
        elif self.orc_spawned >= self.amount_of_orcs and self.wolf_spawned < self.amount_of_wolfs and current_time - self.mob_spawn_timer >= self.wolf_spawn_interval:
            new_wolf = Wolf(self.mapa.waypoints, self.wolf_image)
            self.enemy_group.add(new_wolf)
            self.wolf_spawned += 1
            self.mob_spawn_timer = current_time

    def is_level_finished(self):
        return len(
            self.enemy_group) == 0 and self.orc_spawned >= self.amount_of_orcs and self.wolf_spawned >= self.amount_of_wolfs
