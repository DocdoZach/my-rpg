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

# Sprite group
sprite_group = pygame.sprite.Group()

# Game window
screen = create_screen(800, 640, "My RPG")

# Tile background
tile_types = [
    TileType("grass", False, "media/sprites/grass_tile.png"),
    TileType("dirt", False, "media/sprites/dirt_tile.png"),
    TileType("water", True, "media/sprites/water_tile.png")
]
map = Map(tile_types, 32, "maps/world.map")

# Sprites
Sprite(80, 60, "media/sprites/tree.png")
Sprite(70, 460, "media/sprites/tree.png")
Sprite(200, 320, "media/sprites/tree.png")
Sprite(400, 500, "media/sprites/tree.png")
Sprite(300, 80, "media/sprites/tree.png")
Sprite(720, 160, "media/sprites/dead_tree.png")
Sprite(720, 350, "media/sprites/dead_tree.png")

# Player
player = Player(400, 320, "media/sprites/doc.png")

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
    screen.fill((127, 127, 127))
    map.draw(screen)
    for i in sprites:
        i.draw(screen)

    pygame.display.flip()

pygame.quit()