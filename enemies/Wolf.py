from .Enemy import Enemy


class Wolf(Enemy):

    def __init__(self, waypoints, image):
        super().__init__(waypoints, image)
        self.speed = 3
        self.gold_for_kill = 35

        # zdrowie jednostki
        self.health_point = 100  # zdrowie jednostki
        self.max_health = self.health_point  # maksymalna wartość punktów zdrowia