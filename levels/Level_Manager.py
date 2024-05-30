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
            {"amount_of_orcs": 5, "amount_of_wolfs": 2, "orc_spawn_interval": 500, "wolf_spawn_interval": 300},
            {"amount_of_orcs": 10, "amount_of_wolfs": 5, "orc_spawn_interval": 450, "wolf_spawn_interval": 250},
            # Add more levels as needed
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
            if self.is_level_finished():
                print("koniec lvl")


    def is_level_finished(self):
        if self.current_level:
            return self.current_level.is_level_finished()
        return True  # If there are no more levels, consider it finished
