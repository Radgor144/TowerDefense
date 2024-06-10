import pygame

from .Enemy import Enemy


class Orc(Enemy):

    def __init__(self, waypoints, image):
        super().__init__(waypoints, image)
        self.speed = 2
        self.gold_for_kill = 25

        # zdrowie jednostki
        self.health_point = 100  # zdrowie jednostki
        self.max_health = 100  # maksymalna wartość punktów zdrowia