import pygame
import os
import pytmx

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Wczytaj mapę .tmx
path = os.path.join(os.getcwd(), 'assets')
tmx_map = pytmx.TiledMap(os.path.join(path, "mapka.tmx"))

# define map
ROWS = tmx_map.height
COLS = tmx_map.width
TILE_SIZE = tmx_map.tilewidth


def draw_grid():
    # vertical lines
    for c in range(COLS + 1):
        pygame.draw.line(screen, (255, 255, 255), (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
    # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, (255, 255, 255), (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


window_open = True
while window_open:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        if event.type == pygame.QUIT:
            window_open = False

    screen.fill((0, 0, 0))  # Wyczyść ekran przed renderowaniem

    # Renderowanie warstw mapy
    for layer in tmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image_info = tmx_map.get_tile_image_by_gid(gid)
                if tile_image_info:
                    tile_image_path = tile_image_info[0]
                    tile_surface = pygame.image.load(
                        os.path.join(path, tile_image_path)).convert_alpha()  # Wczytaj kafelek jako powierzchnię
                    screen.blit(tile_surface, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

    draw_grid()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
