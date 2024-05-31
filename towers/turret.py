import pygame


class Turret(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, position, surface):
        x, y = map(int, position.split(' '))
        surface.blit(self.image, (x, y))

    def new_position(self, x, y):
        self.rect.x -= x
        self.rect.y -= y

