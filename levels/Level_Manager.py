
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
                "orc_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 400}),
                                   (0, {"route_name": "route2", "spawn_interval": 400}),
                                   (0, {"route_name": "route3", "spawn_interval": 400})],
            },
            {   # 2 poziom
                "orc_spawn_data": [(3, {"route_name": "route1", "spawn_interval": 400}),
                                   (3, {"route_name": "route2", "spawn_interval": 400}),
                                   (0, {"route_name": "route3", "spawn_interval": 400})],

                "wolf_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                    (1, {"route_name": "route2", "spawn_interval": 200}),
                                    (0, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 3 poziom
                "orc_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 400}),
                                   (4, {"route_name": "route2", "spawn_interval": 400}),
                                   (4, {"route_name": "route3", "spawn_interval": 400})],

                "wolf_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                    (1, {"route_name": "route2", "spawn_interval": 200}),
                                    (1, {"route_name": "route3", "spawn_interval": 200})],

                "dirt_golem_spawn_data": [(0, {"route_name": "route1", "spawn_interval": 200}),
                                          (1, {"route_name": "route2", "spawn_interval": 200}),
                                          (0, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 4 poziom
                "orc_spawn_data": [(7, {"route_name": "route1", "spawn_interval": 400}),
                                   (5, {"route_name": "route2", "spawn_interval": 400}),
                                   (7, {"route_name": "route3", "spawn_interval": 400})],

                "wolf_spawn_data": [(0, {"route_name": "route1", "spawn_interval": 200}),
                                    (2, {"route_name": "route2", "spawn_interval": 200}),
                                    (4, {"route_name": "route3", "spawn_interval": 200})],

                "dirt_golem_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                          (1, {"route_name": "route2", "spawn_interval": 200}),
                                          (1, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 5 poziom
                "orc_spawn_data": [(0, {"route_name": "route1", "spawn_interval": 400}),
                                   (0, {"route_name": "route2", "spawn_interval": 400}),
                                   (0, {"route_name": "route3", "spawn_interval": 400})],

                "wolf_spawn_data": [(6, {"route_name": "route1", "spawn_interval": 200}),
                                    (5, {"route_name": "route2", "spawn_interval": 200}),
                                    (7, {"route_name": "route3", "spawn_interval": 200})],

                "dirt_golem_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                          (2, {"route_name": "route2", "spawn_interval": 200}),
                                          (3, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 6 poziom
                "orc_spawn_data": [(10, {"route_name": "route1", "spawn_interval": 300}),
                                   (10, {"route_name": "route2", "spawn_interval": 300}),
                                   (10, {"route_name": "route3", "spawn_interval": 300})],

                "wolf_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 150}),
                                    (2, {"route_name": "route2", "spawn_interval": 150}),
                                    (7, {"route_name": "route3", "spawn_interval": 150})],

                "dirt_golem_spawn_data": [(2, {"route_name": "route1", "spawn_interval": 200}),
                                          (2, {"route_name": "route2", "spawn_interval": 200}),
                                          (3, {"route_name": "route3", "spawn_interval": 200})],

                "minotaur_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                        (0, {"route_name": "route2", "spawn_interval": 200}),
                                        (0, {"route_name": "route3", "spawn_interval": 200})],
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
            if self.current_level_index == len(self.levels) and len(self.enemy_group) == 0:
                self.victory = True
