from Enemy import Enemy
class Level1:

    def __init__(self, orc_image, enemy_group, mapa):
        self.amount_of_orcs = 5
        self.orc_spawn_interval = 500 #Interwał pojawiania się nowych orków w sekundach
        self.orc_spawn_timer = 0  # Licznik czasu do następnego pojawienia się orka
        self.orc_spawned = 0  # Licznik orków, które już się pojawiły
        self.orc_image = orc_image
        self.enemy_group = enemy_group
        self.mapa = mapa

    def update(self, current_time):
        # Sprawdź, czy czas na stworzenie nowego orka
        if self.orc_spawned < self.amount_of_orcs and current_time - self.orc_spawn_timer >= self.orc_spawn_interval:
            # Stwórz nowego orka
            new_orc = Enemy(self.mapa.waypoints, self.orc_image)
            self.enemy_group.add(new_orc)

            # Zaktualizuj liczniki i timer
            self.orc_spawned += 1
            self.orc_spawn_timer = current_time

    def is_level_finished(self):
        # Sprawdź, czy wszyscy orkowie zostali zniszczeni
        return len(self.enemy_group) == 0 and self.orc_spawned >= self.amount_of_orcs

