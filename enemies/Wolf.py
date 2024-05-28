from .Enemy import Enemy


class Wolf(Enemy):

    def __init__(self, waypoints, image):
        super().__init__(waypoints, image)
        self.speed = 3
        self.gold_for_kill = 75

        # zdrowie jednostki
        self.health_point = 50  # zdrowie jednostki
        self.max_health = 50  # maksymalna wartość punktów zdrowia