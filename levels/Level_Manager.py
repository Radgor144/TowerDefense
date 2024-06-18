
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
            {   # 2 poziom
                "orc_spawn_data": [(3, {"route_name": "route1", "spawn_interval": 600}),
                                   (3, {"route_name": "route2", "spawn_interval": 600}),
                                   (0, {"route_name": "route3", "spawn_interval": 600})],

                "wolf_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 200}),
                                    (1, {"route_name": "route2", "spawn_interval": 200}),
                                    (2, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 3 poziom
                "orc_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 650}),
                                   (4, {"route_name": "route2", "spawn_interval": 650}),
                                   (4, {"route_name": "route3", "spawn_interval": 650})],

                "wolf_spawn_data": [(2, {"route_name": "route1", "spawn_interval": 200}),
                                    (1, {"route_name": "route2", "spawn_interval": 200}),
                                    (2, {"route_name": "route3", "spawn_interval": 200})],

                "dirt_golem_spawn_data": [(0, {"route_name": "route1", "spawn_interval": 200}),
                                          (1, {"route_name": "route2", "spawn_interval": 200}),
                                          (0, {"route_name": "route3", "spawn_interval": 200})],
            },
            {  # 4 poziom
                "orc_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 450}),
                                   (4, {"route_name": "route2", "spawn_interval": 500}),
                                   (4, {"route_name": "route3", "spawn_interval": 450})],

                "wolf_spawn_data": [(0, {"route_name": "route1", "spawn_interval": 300}),
                                    (3, {"route_name": "route2", "spawn_interval": 300}),
                                    (4, {"route_name": "route3", "spawn_interval": 300})],

                "dirt_golem_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 400}),
                                          (1, {"route_name": "route2", "spawn_interval": 400}),
                                          (1, {"route_name": "route3", "spawn_interval": 400})],
            },
            {  # 5 poziom
                "wolf_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 300}),
                                    (5, {"route_name": "route2", "spawn_interval": 300}),
                                    (5, {"route_name": "route3", "spawn_interval": 300})],

                "dirt_golem_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 500}),
                                          (2, {"route_name": "route2", "spawn_interval": 500}),
                                          (3, {"route_name": "route3", "spawn_interval": 700})],
            },
            {  # 6 poziom
                "orc_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 400}),
                                   (4, {"route_name": "route2", "spawn_interval": 400}),
                                   (4, {"route_name": "route3", "spawn_interval": 400})],

                "wolf_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 400}),
                                    (2, {"route_name": "route2", "spawn_interval": 400}),
                                    (3, {"route_name": "route3", "spawn_interval": 400})],

                "dirt_golem_spawn_data": [(2, {"route_name": "route1", "spawn_interval": 400}),
                                          (1, {"route_name": "route2", "spawn_interval": 400}),
                                          (2, {"route_name": "route3", "spawn_interval": 400})],
            },
            {  # 7 poziom
                "orc_spawn_data": [(4, {"route_name": "route1", "spawn_interval": 500}),
                                   (3, {"route_name": "route2", "spawn_interval": 600}),
                                   (5, {"route_name": "route3", "spawn_interval": 500})],

                "wolf_spawn_data": [(3, {"route_name": "route1", "spawn_interval": 400}),
                                    (3, {"route_name": "route2", "spawn_interval": 400}),
                                    (3, {"route_name": "route3", "spawn_interval": 400})],

                "dirt_golem_spawn_data": [(2, {"route_name": "route1", "spawn_interval": 700}),
                                          (2, {"route_name": "route2", "spawn_interval": 700}),
                                          (2, {"route_name": "route3", "spawn_interval": 700})],
            },
            {  # 8 poziom
                "wolf_spawn_data": [(10, {"route_name": "route1", "spawn_interval": 300}),
                                    (5, {"route_name": "route2", "spawn_interval": 330}),
                                    (8, {"route_name": "route3", "spawn_interval": 400})],
            },
            {  # 9 poziom
                "orc_spawn_data": [(8, {"route_name": "route1", "spawn_interval": 2500}),
                                   (8, {"route_name": "route2", "spawn_interval": 3200}),
                                   (8, {"route_name": "route3", "spawn_interval": 1500})],

                "dirt_golem_spawn_data": [(3, {"route_name": "route1", "spawn_interval": 5000}),
                                          (3, {"route_name": "route2", "spawn_interval": 5000}),
                                          (3, {"route_name": "route3", "spawn_interval": 5000})],
            },
            {  # 10 poziom
                "orc_spawn_data": [(10, {"route_name": "route1", "spawn_interval": 3500}),
                                   (10, {"route_name": "route2", "spawn_interval": 3700}),
                                   (10, {"route_name": "route3", "spawn_interval": 3900})],

                "wolf_spawn_data": [(10, {"route_name": "route1", "spawn_interval": 2700}),
                                    (10, {"route_name": "route2", "spawn_interval": 3000}),
                                    (10, {"route_name": "route3", "spawn_interval": 2500})],

                "dirt_golem_spawn_data": [(5, {"route_name": "route1", "spawn_interval": 5000}),
                                          (5, {"route_name": "route2", "spawn_interval": 5000}),
                                          (5, {"route_name": "route3", "spawn_interval": 5000})],

                "minotaur_spawn_data": [(1, {"route_name": "route1", "spawn_interval": 20000}),
                                        (0, {"route_name": "route2", "spawn_interval": 200}),
                                        (0, {"route_name": "route3", "spawn_interval": 200})],
            },

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
