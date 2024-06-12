import pygame

from .Enemy import Enemy


class Minotaur(Enemy):

    def __init__(self, waypoints, image):
        super().__init__(waypoints, image)
        self.speed = 0.4
        self.gold_for_kill = 10000

        # zdrowie jednostki
        self.health_point = 5000  # zdrowie jednostki
        self.max_health = self.health_point  # maksymalna wartość punktów zdrowia