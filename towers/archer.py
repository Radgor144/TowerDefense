import math
import pygame


class Archer(pygame.sprite.Sprite):
    def __init__(self, image, tower_rect, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        x, y = position
        self.rect.centerx = tower_rect.centerx - x
        self.rect.bottom = tower_rect.top + y

        self.position = self.rect.center

        self.range = 150
        self.cooldown = 800
        self.damage = 35
        self.last_shot = pygame.time.get_ticks()
        self.selected = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    def update(self, enemy_group):
        if pygame.time.get_ticks() - self.last_shot > self.cooldown:
            # find the first target in range and attack it
            for enemy in enemy_group:
                distance = math.hypot(self.position[0] - enemy.rect.center[0], self.position[1] - enemy.rect.center[1])
                if distance <= self.range:
                    # print("atak")
                    enemy.health_point -= self.damage
                    self.last_shot = pygame.time.get_ticks()  # Zaktualizuj czas ostatniego strzału
                    break
        # draw distance
        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.range_image, "grey20", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center[0], self.rect.center[1] + 10
