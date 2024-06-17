
from levels.Level import Level


class LevelManager:
    def __init__(self, enemy_group, mapa):
        self.victory = False
        self.level_configs = None
        self.enemy_group = enemy_group
        self.mapa = mapa
        self.current_level_index = 0
        self.levels = []
        self.load_levels()

    def load_levels(self):
        self.level_configs = [
            {  # 1 poziom
                "orc_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 600}),
                                   (0, {"route_name": "route2", "spawn_interval": 600}),
                                   (0, {"route_name": "route3", "spawn_interval": 600})],
            },

            # Dodaj więcej poziomów według potrzeb
        ]

        for config in self.level_configs:
            self.levels.append(Level(config, self.enemy_group, self.mapa))

    def start_next_level(self):
        if self.current_level_index < len(self.levels):
            self.current_level = self.levels[self.current_level_index]
            self.current_level_index += 1

    def update(self, current_time):
        if self.current_level:
            self.current_level.update(current_time)
            # condition of victory in the game
            if self.current_level_index == len(self.levels) and len(self.enemy_group) == 0:
                self.victory = True
