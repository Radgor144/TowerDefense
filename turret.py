import pygame

class Turret(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, position, surface):
        x, y = map(int, position.split(' '))
        surface.blit(self.image, (x, y))