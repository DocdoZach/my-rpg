'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame
import input
from sprite import sprites, Sprite
from player import Player
from tilemap import TileType, Map
from camera import create_screen

pygame.init()
pygame.mixer.init()

# Sprite group
sprite_group = pygame.sprite.Group()

# Game window
screen = create_screen(800, 640, "My RPG")

# Audio
song = pygame.mixer.Sound("media/audio/music/hologram.mp3")
pygame.mixer.Sound.set_volume(song, 0.5)
#pygame.mixer.Sound.play(song)

# Tile background
tile_types = {
    1: TileType("grass", False, "media/sprites/grass_tile.png"),
    2: TileType("dirt", False, "media/sprites/dirt_tile.png"),
    3: TileType("water", True, "media/sprites/water_tile.png"),
    4: TileType("wood", False, "media/sprites/wood_tile.png")
}
map = Map(tile_types, 32, "maps/tilemap.json")

# Sprites
Sprite(512, 740-128, "media/sprites/tree.png")
Sprite(620, 740-128, "media/sprites/tree.png")
Sprite(740, 780-128, "media/sprites/tree.png")
Sprite(700, 1080-128, "media/sprites/tree.png")
# Player
player = Player(872, 1440, "media/sprites/doc.png")

# Clock
clock = pygame.time.Clock()

# Game loop
run = True

while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    # Update
    player.update()
    sprite_group.update()

    # Draw
    screen.fill((16, 16, 16))
    map.draw(screen)
    for i in sprites:
        i.draw(screen)

    pygame.display.flip()

pygame.quit()