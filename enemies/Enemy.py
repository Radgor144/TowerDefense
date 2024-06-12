import pygame
from pygame.math import Vector2
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        #load music
        self.lose_hp_sound = pygame.mixer.Sound("assets/music/lose Hp.mp3")
        self.enemy_death_sound = pygame.mixer.Sound("assets/music/enemy Death.mp3")

        #modify music
        self.enemy_death_sound.set_volume(0.05)

        # Pasek zdrowia
        self.hp_rect = pygame.Rect(0, 0, 20, 5)  # początkowe ustawienia prostokąta paska HP

        # Timer do odliczania czasu do odjęcia punktów zdrowia
        # self.health_timer = pygame.time.get_ticks()
        # self.health_interval = 50  # Czas w milisekundach między odjęciami punktów zdrowia

    def update(self, player):
        self.move(player)
        self.rotate()
        self.hp_position()  # Aktualizuj pozycję paska HP


        # Aktualizuj pasek HP
        self.update_health_bar(player)

        # Odjęcie punktów zdrowia co pewien czas
        # now = pygame.time.get_ticks()
        # if now - self.health_timer > self.health_interval:
        #     self.health_timer = now
        #     self.health_point -= 1
        #     if self.health_point <= 0:
        #         self.kill()  # Jeśli zdrowie spadnie do zera lub mniej, usuń jednostkę

    def hp_position(self):
        x, y = self.rect.center
        self.hp_rect.topleft = (x - 10, y - 20)  # Aktualizuj pozycję paska HP

    def update_health_bar(self, player):
        from .Orc import Orc
        from .Wolf import Wolf
        from .Dirt_golem import Dirt_golem
        from .Minotaur import Minotaur
        # Oblicz szerokość paska HP proporcjonalnie do aktualnego zdrowia
        health_width = int((self.health_point / self.max_health) * 20)
        self.hp_rect.width = max(health_width, 0)  # Szerokość paska HP nie może być mniejsza niż 0
        if self.health_point <= 0:
            self.kill()
            self.enemy_death_sound.play()
            if isinstance(self, Orc):
                player.gold += self.gold_for_kill
            elif isinstance(self, Wolf):
                player.gold += self.gold_for_kill
            elif isinstance(self, Dirt_golem):
                player.gold += self.gold_for_kill
            elif isinstance(self, Minotaur):
                player.gold += self.gold_for_kill

    def move(self, player):
        from .Minotaur import Minotaur
        # define target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position
        else:
            if isinstance(self, Minotaur):
                player.health_points = 0
            else:
                # enemy has reached the end of the path
                self.kill()
                player.health_points -= 1
                player.gold -= 50
                self.lose_hp_sound.play()

        # calculate distance to target
        distance = self.movement.length()

        # check if remaining distance is greater than enemy speed
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            self.target_waypoint += 1
        self.rect.center = self.position

    def rotate(self):
        # calculate distance to next waypoint
        distance = self.target - self.position

        # use distance to calculate angle
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        # rotate image and update rectangle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
