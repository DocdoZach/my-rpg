'''
The Hologram - An RPG made for CS class
Zach N
'''

import pygame
import input
from sprite import sprites, Sprite
from player import Player
from tilemap import TileType, Map
from camera import create_screen
from entity import Entity, active_objects
from physics import Body

pygame.init()
pygame.mixer.init()

# Sprite group
sprite_group = pygame.sprite.Group()

# Game window
screen = create_screen(800, 640, "THE HOLOGR△M")

# Audio
song = pygame.mixer.Sound("media/audio/music/hologram.mp3")
pygame.mixer.Sound.set_volume(song, 0.5)
#pygame.mixer.Sound.play(song)

# Tile background
tile_types = [
    None,
    TileType("grass", False, "media/sprites/grass_tile.png"),
    TileType("dirt", False, "media/sprites/dirt_tile.png"),
    TileType("water", True, "media/sprites/water_tile.png"),
    TileType("wood", False, "media/sprites/wood_tile.png")
]
map = Map(tile_types, 32, "maps/tilemap.json")

# Trees
def make_tree(x, y):
    Entity(Sprite("media/sprites/tree.png"), Body(20, 64, 40, 64), x=x, y=y)

make_tree(512, 740-128)
make_tree(620, 740-128)
make_tree(740, 780-128)
make_tree(700, 1080-128)

# Player
player = Entity(Player(), Sprite("media/sprites/doc.png"), Body(8, 48, 28, 28), x=872, y=1440)

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
    for i in active_objects:
        i.update()
    sprite_group.update()

    # Draw
    screen.fill((16, 16, 16))
    map.draw(screen)
    sprites.sort(key=lambda sprite: sprite.entity.y+sprite.image.get_height())
    for i in sprites:
        i.draw(screen)

    pygame.display.flip()

pygame.quit()