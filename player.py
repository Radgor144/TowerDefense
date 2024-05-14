import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, coin_image, heart_image):
        super().__init__()
        self.gold = 300
        self.coin_image = coin_image
        self.coin_rect = self.coin_image.get_rect()

        # Hp
        self.health_points = 5
        self.heart_image = heart_image
        self.heart_rect = self.heart_image.get_rect

    def draw(self, screen):
        # Pozycja monety w lewym górnym rogu ekranu
        coin_position = (10, 10)
        heart_position = (1100, 10)

        # Pozycja liczby pieniędzy obok monety
        text_position = (coin_position[0] + self.coin_rect.width + 5, coin_position[1])

        # Rysowanie ikony monety na ekranie
        screen.blit(self.coin_image, coin_position)

        x = 0
        for i in range(self.health_points):
            screen.blit(self.heart_image, (1120 + x, 10))
            x += 30

        # Rysowanie liczby pieniędzy obok monety
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(self.gold), True, (255, 255, 255))
        text_position = (coin_position[0] + self.coin_rect.width + 5, coin_position[1] + 5)
        screen.blit(text_surface, text_position)

