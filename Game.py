import pygame

from Buttons.Start_wave_button import Start_wave_button
from levels.Level_Manager import LevelManager
from mapa import Mapa
from towers.turret import Turret
from Buttons.towerUpgradeMenu import TowerUpgradeMenu
from towers.archer import Archer
from player import Player
import json

FPS = 60
ROWS = 23
COLS = 40
TILE_SIZE = 32

SCREEN_WIDTH = TILE_SIZE * COLS
SCREEN_HEIGHT = TILE_SIZE * ROWS

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()


def draw_turret_range(archer, surface):
    if archer.selected:
        surface.blit(archer.range_image, archer.range_rect)


def load_turret_positions():
    with open("turretPosition.txt", "r") as turret_pos_file:
        turret_position = turret_pos_file.read().split("\n")
        for pos in turret_position:
            x, y = map(int, pos.split(' '))
            turret = Turret(turret_image_lvl0)
            turret.rect.topleft = (x, y)
            turret_group.add(turret)


def start_wave(is_start):
    if is_start:
        enemy_group.draw(screen)
        for enemy in enemy_group:
            pygame.draw.rect(screen, (0, 255, 0), enemy.hp_rect)
        level_manager.update(pygame.time.get_ticks())


def upgrading_towers(event, turret_group):
    global turret_position
    for turret in turret_group:
        if turret.rect.collidepoint(event.pos):
            tower_upgrade_menu.show_menu(screen, turret.rect.topleft, turret.cost)
            turret_position = turret.rect.topleft
            break
    else:
        tower_upgrade_menu.hide_menu()

    if tower_upgrade_menu.button_rect.collidepoint(event.pos):
        for turret in turret_group:
            if turret.rect.topleft == turret_position:
                if turret.image == turret_image_lvl0 and player.gold >= 100:
                    upgrade_tower(turret, 100, 250, turret_image_lvl1, (5, 30), (0, 0), 0, 800, 5)
                elif turret.image == turret_image_lvl1 and player.gold >= 250:
                    upgrade_tower(turret, 250, 500, turret_image_lvl2, (5, 20), (0, 0), 25, 700, 5)
                elif turret.image == turret_image_lvl2 and player.gold >= 500:
                    upgrade_tower(turret, 500, 700, turret_image_lvl3, (5, 20), (0, 10), 50, 600, 5)
                elif turret.image == turret_image_lvl3 and player.gold >= 700:
                    upgrade_tower(turret, 700, 900, turret_image_lvl4, (5, 42), (0, 23), 75, 500, 5)
                elif turret.image == turret_image_lvl4 and player.gold >= 900:
                    upgrade_tower(turret, 900, 900, turret_image_lvl5, (5, 42), (0, 0), 100, 400, 5)
                break


def upgrade_tower(turret, cost, upgrade_cost, image, archer_pos, tower_pos, range, cooldown, damage):
    player.gold -= cost
    tower_upgrade_sound.play()
    if turret in turret_archer_dict:
        archer_group.remove(turret_archer_dict[turret])
    turret.image = image
    turret.new_position(*tower_pos)
    turret.cost = upgrade_cost
    archer = Archer(archer_image, turret.rect, archer_pos)
    archer.range += range
    archer.cooldown = cooldown
    archer.damage += damage
    archer_group.add(archer)
    turret_archer_dict[turret] = archer


def show_welcome_screen():
    start_button_image = pygame.image.load("assets/content/UI/Button_Hover_3Slides.png").convert_alpha()
    start_button_rect = start_button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    # Utworzenie przezroczystego Surface z trybem alfa
    transparent_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 128))  # Czarny z przezroczystością 50%

    while True:
        screen.fill((0, 0, 0))
        mapa.draw(screen)
        turret_group.draw(screen)
        screen.blit(transparent_surface, (0, 0))
        screen.blit(start_button_image, start_button_rect)

        font = pygame.font.Font(None, 28)
        text_surface = font.render(str("Rozpocznij grę"), True, (255, 255, 255))
        text_position = (start_button_rect.x + 25, start_button_rect.y + 15)
        screen.blit(text_surface, text_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button_rect.collidepoint(event.pos):
                    return  # Exit the welcome screen loop and start the game

        pygame.display.flip()
        clock.tick(FPS)


def show_game_over_screen():
    start_button_image = pygame.image.load("assets/content/UI/Button_Red_3Slides.png").convert_alpha()
    start_button_rect = start_button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    # Utworzenie przezroczystego Surface z trybem alfa
    transparent_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 128))  # Czarny z przezroczystością 50%

    while True:
        # Zaktualizuj ekran gry przed nałożeniem przezroczystego tła
        mapa.draw(screen)
        player.draw(screen)
        enemy_group.draw(screen)
        turret_group.draw(screen)
        for archer in archer_group:
            archer.draw(screen)
            draw_turret_range(archer, screen)

        screen.blit(transparent_surface, (0, 0))
        screen.blit(start_button_image, start_button_rect)

        font = pygame.font.Font(None, 28)
        text_surface = font.render("Przegrana", True, (255, 255, 255))
        text_position = (start_button_rect.x + 50, start_button_rect.y + 15)
        screen.blit(text_surface, text_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button_rect.collidepoint(event.pos):
                    return  # Exit the game over screen loop and restart the game

        pygame.display.flip()
        clock.tick(FPS)


def show_victory_screen():
    start_button_image = pygame.image.load("assets/content/UI/Ribbon_Blue_3Slides.png").convert_alpha()
    start_button_rect = start_button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    # Utworzenie przezroczystego Surface z trybem alfa
    transparent_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 128))  # Czarny z przezroczystością 50%

    while True:
        # Zaktualizuj ekran gry przed nałożeniem przezroczystego tła
        mapa.draw(screen)
        player.draw(screen)
        enemy_group.draw(screen)
        turret_group.draw(screen)
        for archer in archer_group:
            archer.draw(screen)
            draw_turret_range(archer, screen)

        screen.blit(transparent_surface, (0, 0))
        screen.blit(start_button_image, start_button_rect)

        font = pygame.font.Font(None, 28)
        text_surface = font.render("Wygrana", True, (255, 255, 255))
        text_position = (start_button_rect.x + 55, start_button_rect.y + 15)
        screen.blit(text_surface, text_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        clock.tick(FPS)


# load music
wave_incoming_sound = pygame.mixer.Sound("assets/music/Wave Incoming.mp3")
tower_upgrade_sound = pygame.mixer.Sound("assets/music/tower upgrade.mp3")
tower_upgrade_sound.set_volume(0.5)

# load images
map_image = pygame.image.load("assets/map/mapa1.png").convert_alpha()
turret_image_lvl0 = pygame.image.load("assets/towers/toBuild.png").convert_alpha()
turret_image_lvl1 = pygame.image.load("assets/towers/archerTower.png").convert_alpha()
turret_image_lvl2 = pygame.image.load("assets/towers/archerTower2.png").convert_alpha()
turret_image_lvl3 = pygame.image.load("assets/towers/archerTower3.png").convert_alpha()
turret_image_lvl4 = pygame.image.load("assets/towers/archerTower4.png").convert_alpha()
turret_image_lvl5 = pygame.image.load("assets/towers/archerTower5.png").convert_alpha()

archer_image = pygame.image.load("assets/archers/archer.png").convert_alpha()

coin_image = pygame.image.load("assets/content/UI/coin_32px.png").convert_alpha()
player_heart_image = pygame.image.load("assets/content/UI/player_heart_32px.png").convert_alpha()

player = Player(coin_image, player_heart_image)

with open("assets/map/trasa1..tmj") as file:
    map_data = json.load(file)

mapa = Mapa(map_data, map_image)
mapa.proccess_data()

enemy_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()
archer_group = pygame.sprite.Group()

load_turret_positions()

tower_upgrade_menu = TowerUpgradeMenu()

Start_wave_button = Start_wave_button()

# Dictionary to store archers for each turret
turret_archer_dict = {}

level_manager = LevelManager(enemy_group, mapa)

show_welcome_screen()

window_open = True
IsStart = False
while window_open:
    mapa.draw(screen)
    player.draw(screen)

    pygame.draw.lines(screen, "grey0", False, mapa.route1)
    pygame.draw.lines(screen, "grey0", False, mapa.route2)
    pygame.draw.lines(screen, "grey0", False, mapa.route3)

    if level_manager.current_level_index < len(level_manager.levels):
        Start_wave_button.update(screen, level_manager.level_configs, level_manager.current_level_index)

    enemy_group.update(player)
    archer_group.update(enemy_group)
    turret_group.draw(screen)

    start_wave(IsStart)

    for archer in archer_group:
        archer.draw(screen)
        draw_turret_range(archer, screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        if event.type == pygame.MOUSEMOTION:
            for archer in archer_group:
                if archer.rect.collidepoint(event.pos):
                    archer.selected = True
                else:
                    archer.selected = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            upgrading_towers(event, turret_group)

            if (Start_wave_button.red_button_rect1.collidepoint(event.pos) or
                    Start_wave_button.red_button_rect2.collidepoint(event.pos) or
                    Start_wave_button.red_button_rect3.collidepoint(event.pos)):
                IsStart = True
                Start_wave_button.hide_buttons()
                level_manager.start_next_level()
                wave_incoming_sound.play()

        if event.type == pygame.QUIT:
            window_open = False

    tower_upgrade_menu.update(screen)

    if player.health_points <= 0:
        show_game_over_screen()
        window_open = False

    if level_manager.victory:
        show_victory_screen()

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
