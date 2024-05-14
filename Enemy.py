import pygame
from pygame.math import Vector2
import math
class Enemy(pygame.sprite.Sprite):

    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Pasek zdrowia
        self.health_point = 100  # zdrowie jednostki
        self.max_health = 100  # maksymalna wartość punktów zdrowia
        self.hp_rect = pygame.Rect(0, 0, 20, 5)  # początkowe ustawienia prostokąta paska HP

        # Timer do odliczania czasu do odjęcia punktów zdrowia
        self.health_timer = pygame.time.get_ticks()
        self.health_interval = 50  # Czas w milisekundach między odjęciami punktów zdrowia

    def update(self):
        self.move()
        self.rotate()
        self.hp_position()  # Aktualizuj pozycję paska HP

        # Aktualizuj pasek HP
        self.update_health_bar()

        # Odjęcie punktów zdrowia co pewien czas
        now = pygame.time.get_ticks()
        if now - self.health_timer > self.health_interval:
            self.health_timer = now
            self.health_point -= 1
            if self.health_point <= 0:
                self.kill()  # Jeśli zdrowie spadnie do zera lub mniej, usuń jednostkę

    def hp_position(self):
        x, y = self.rect.center
        self.hp_rect.topleft = (x - 10, y - 20)  # Aktualizuj pozycję paska HP

    def update_health_bar(self):
        # Oblicz szerokość paska HP proporcjonalnie do aktualnego zdrowia
        health_width = int((self.health_point / self.max_health) * 20)
        self.hp_rect.width = max(health_width, 0)  # Szerokość paska HP nie może być mniejsza niż 0

    def move(self):
        # define target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position
        else:
            # enemy has reached the end of the path
            self.kill()

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
