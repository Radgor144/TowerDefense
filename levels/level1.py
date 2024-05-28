import pygame

from enemies.Enemy import Enemy
from enemies.Orc import Orc
from enemies.Wolf import Wolf


class Level1:

    def __init__(self, enemy_group, mapa):
        self.amount_of_orcs = 5
        self.amount_of_wolfs = 2

        self.orc_spawn_interval = 500 #Interwał pojawiania się nowych orków w sekundach
        self.orc_spawned = 0  # Licznik orków, które już się pojawiły

        self.mob_spawn_timer = 0  # Licznik czasu do następnego pojawienia się orka

        self.wolf_spawned = 0  # Licznik orków, które już się pojawiły
        self.wolf_spawn_interval = 300  # Interwał pojawiania się nowych wilkow w sekundach

        self.enemy_group = enemy_group
        self.mapa = mapa

        # load images
        self.orc_image = pygame.image.load("enemies/assets/orc/orc1.png").convert_alpha()
        self.wolf_image = pygame.image.load("enemies/assets/wolf/wolf1.png").convert_alpha()

    def update(self, current_time):
        # Sprawdź, czy czas na stworzenie nowego orka
        if self.orc_spawned < self.amount_of_orcs and current_time - self.mob_spawn_timer >= self.orc_spawn_interval:
            # Stwórz nowego orka
            new_orc = Orc(self.mapa.waypoints, self.orc_image)
            self.enemy_group.add(new_orc)

            # Zaktualizuj liczniki i timer
            self.orc_spawned += 1
            self.mob_spawn_timer = current_time

        if self.orc_spawned >= self.amount_of_orcs and self.wolf_spawned < self.amount_of_wolfs and current_time - self.mob_spawn_timer >= self.wolf_spawn_interval:
            # Stwórz nowego orka
            new_wolf = Wolf(self.mapa.waypoints, self.wolf_image)
            self.enemy_group.add(new_wolf)

            # Zaktualizuj liczniki i timer
            self.wolf_spawned += 1
            self.mob_spawn_timer = current_time

    def is_level_finished(self):
        # Sprawdź, czy wszyscy orkowie zostali zniszczeni
        return len(self.enemy_group) == 0 and self.orc_spawned >= self.amount_of_orcs

