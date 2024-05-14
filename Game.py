import pygame
from mapa import Mapa
from turret import Turret
from towerUpgradeMenu import TowerUpgradeMenu
from level1 import Level1
from archer import Archer
from player import Player
import json

FPS = 60
ROWS = 23
COLS = 40
TILE_SIZE = 32

SCREEN_WIDTH = TILE_SIZE * COLS
SCREEN_HEIGHT = TILE_SIZE * ROWS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

def draw_turret_range(archer, surface):
    """
    Wyświetla zasięg wieży na ekranie, jeśli wieża jest zaznaczona.

    Parameters:
        archer (Archer): Obiekt archera, dla którego rysowany jest zasięg.
        surface (pygame.Surface): Powierzchnia, na której ma być wyświetlony zasięg.
    """
    if archer.selected:
        surface.blit(archer.range_image, archer.range_rect)


# load images
orc = pygame.image.load("assets/enemy/2/D_walk/orc1.png").convert_alpha()
map_image = pygame.image.load("assets/map/mapa1.png").convert_alpha()
turret_image_lvl0 = pygame.image.load("assets/towers/toBuild.png").convert_alpha()
turret_image_lvl1 = pygame.image.load("assets/towers/archerTower.png").convert_alpha()
turret_image_lvl2 = pygame.image.load("assets/towers/archerTower2.png").convert_alpha()
archer_image = pygame.image.load("assets/archers/archer.png").convert_alpha()

upgrade_button = pygame.image.load("assets/content/UI/Button_Hover.png").convert_alpha()
coin_image = pygame.image.load("assets/content/UI/coin_32px.png").convert_alpha()
player_heart_image = pygame.image.load("assets/content/UI/player_heart_32px.png").convert_alpha()

player = Player(coin_image, player_heart_image)

# load json data for level
with open("assets/map/trasa1..tmj") as file:
    map_data = json.load(file)

# create map
mapa = Mapa(map_data, map_image)
mapa.proccess_data()

# create groups
enemy_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()
archer_group = pygame.sprite.Group()

# create levels
level1 = Level1(orc, enemy_group, mapa)

# load turret positions
with open("turretPosition.txt", "r") as file:
    turret_position = file.read().split("\n")
    for pos in turret_position:
        x, y = map(int, pos.split(' '))
        turret = Turret(turret_image_lvl0)
        turret.rect.topleft = (x, y)
        turret_group.add(turret)

tower_upgrade_menu = TowerUpgradeMenu(upgrade_button)

# Dictionary to store archers for each turret
turret_archer_dict = {}

# game loop
window_open = True
while window_open:

    screen.fill("grey100")

    # draw level
    mapa.draw(screen)

    # draw coin
    player.draw(screen)

    # draw enemy path
    pygame.draw.lines(screen, "grey0", False, mapa.waypoints)

    # update groups
    enemy_group.update(player)
    archer_group.update(enemy_group)

    # draw groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    for archer in archer_group:
        archer.draw(screen)  # Rysuje archerów
        draw_turret_range(archer, screen)  # Rysuje zasięg dla archerów, jeśli są zaznaczone

    # W głównej pętli gry, po zaktualizowaniu sprite'ów:
    level1.update(pygame.time.get_ticks())

    # Sprawdź, czy poziom został zakończony
    if level1.is_level_finished():
        # Tu możesz dodać kod, który obsługuje zakończenie poziomu, np. przejście do następnego poziomu
        pass

    for enemy in enemy_group:
        # Narysuj pasek HP nad jednostką
        pygame.draw.rect(screen, (0, 255, 0), enemy.hp_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        if event.type == pygame.MOUSEMOTION:
            # Sprawdzamy, czy myszka jest nad wieżą i ustawiamy flagę selected
            for archer in archer_group:
                if archer.rect.collidepoint(event.pos):
                    archer.selected = True
                else:
                    archer.selected = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for turret in turret_group:
                if turret.rect.collidepoint(event.pos):
                    # Jeśli kliknięto na wieżę, otwórz menu ulepszeń
                    tower_upgrade_menu.show_menu(screen, turret.rect.topleft)
                    turret_position = turret.rect.topleft
                    break
            else:
                # Ukryj menu ulepszeń, jeśli kliknięto gdzieś indziej
                tower_upgrade_menu.hide_menu()

            if tower_upgrade_menu.button_rect.collidepoint(event.pos):
                for turret in turret_group:
                    if turret.rect.topleft == turret_position:
                        # Jeśli kliknięto na przycisk ulepszenia, aktualizuj wieżę
                        if turret.image == turret_image_lvl0 and player.gold >= 100:
                            player.gold -= 100
                            turret.image = turret_image_lvl1  # Zaktualizuj obrazek wieży do lvl1
                            archer = Archer(archer_image, turret.rect, (5, 30))
                            archer_group.add(archer)
                            turret_archer_dict[turret] = archer  # Store archer reference for turret
                        elif turret.image == turret_image_lvl1 and player.gold >= 250:
                            player.gold -= 250
                            # Remove previous archer
                            if turret in turret_archer_dict:
                                archer_group.remove(turret_archer_dict[turret])
                            turret.image = turret_image_lvl2  # Zaktualizuj obrazek wieży do lvl2
                            archer = Archer(archer_image, turret.rect, (5, 20))
                            archer_group.add(archer)
                            turret_archer_dict[turret] = archer  # Store archer reference for turret
                        break

        if event.type == pygame.QUIT:
            window_open = False

    # Aktualizuj menu
    tower_upgrade_menu.update(screen)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
