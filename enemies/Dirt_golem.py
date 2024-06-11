import pygame

from .Enemy import Enemy


class Dirt_golem(Enemy):

    def __init__(self, waypoints, image):
        super().__init__(waypoints, image)
        self.speed = 0.7
        self.gold_for_kill = 100

        # zdrowie jednostki
        self.health_point = 1000  # zdrowie jednostki
        self.max_health = self.health_point  # maksymalna wartość punktów zdrowia