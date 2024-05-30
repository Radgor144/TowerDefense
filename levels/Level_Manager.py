from levels.Level import Level


class LevelManager:
    def __init__(self, enemy_group, mapa):
        self.enemy_group = enemy_group
        self.mapa = mapa
        self.current_level_index = 0
        self.levels = []
        self.load_levels()

    def load_levels(self):
        level_configs = [
            {
                "orc_spawn_data": [(3, {"route_name": "route1", "spawn_interval": 500}),
                                   (3, {"route_name": "route2", "spawn_interval": 500}),
                                   (3, {"route_name": "route3", "spawn_interval": 500})],
                "wolf_spawn_data": [(5, {"route_name": "route2", "spawn_interval": 400}),
                                    (2, {"route_name": "route3", "spawn_interval": 400})],
            },
            {
                "orc_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 500}),
                                   (4, {"route_name": "route2", "spawn_interval": 500}),
                                   (4, {"route_name": "route3", "spawn_interval": 500})],
                "wolf_spawn_data": [(2, {"route_name": "route2", "spawn_interval": 500}),
                                    (2, {"route_name": "route3", "spawn_interval": 500})],
            },
            # Dodaj więcej poziomów według potrzeb
        ]
        for config in level_configs:
            self.levels.append(Level(config, self.enemy_group, self.mapa))

    def start_next_level(self):
        if self.current_level_index < len(self.levels):
            self.current_level = self.levels[self.current_level_index]
            self.current_level_index += 1
        else:
            self.current_level = None  # No more levels

    def update(self, current_time):
        if self.current_level:
            self.current_level.update(current_time)

    def is_level_finished(self):
        if self.current_level:
            return self.current_level.is_level_finished()
        return True