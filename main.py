'''
The Hologram - An RPG made for CS class
Zach N
'''

import pygame
from sprite import loaded_images
import keyinput
from items import *
from sprite import sprites, Sprite
from player import Player
from tilemap import *
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
    TileType("grass", False, "media/sprites/tiles/grass_tile.png"),
    TileType("dirt", False, "media/sprites/tiles/dirt_tile.png"),
    TileType("water", True, "media/sprites/tiles/water_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png"),
    TileType("dark_grass", False, "media/sprites/tiles/dark_grass_tile.png")
]
map = Map(tile_types, 32, "maps/tilemap.json")

# Trees
def make_tree(x, y):
    Entity(Sprite("media/sprites/tree.png"), Body(44, 96, 40, 64), x=x, y=y)

make_tree(716, 916)
make_tree(784, 660)
make_tree(616, 604)
make_tree(700, 584)
make_tree(576, 860)

# Player
doc = Entity(Player(1, [[sword, 1], [potion, 2]]), Sprite("media/sprites/player/doc.png"), Body(8, 48, 28, 28), x=872, y=1440)
previous_key = ""

# Game clock
clock = pygame.time.Clock()

# Game loop
run = True
while run:

    # Game clock frequency (60Hz)
    clock.tick(60)

    # Event handler (quit game, keys pressed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            keyinput.keys_down.add(event.key)

            # Open inventory
            if event.key == pygame.K_z:
                doc.get(Player).open_inventory()

            # Open stats
            if event.key == pygame.K_x:
                doc.get(Player).open_stats()

            # Walk up sprite
            if event.key == pygame.K_w:
                doc.get(Sprite).reload("media/sprites/player/doc_back.png")
                previous_key = "w"

            # Walk down sprite
            if event.key == pygame.K_s:
                doc.get(Sprite).reload("media/sprites/player/doc.png")
                previous_key = "s"

            # Walk down sprite
            if event.key == pygame.K_a:
                doc.get(Sprite).reload("media/sprites/player/doc_left.png")
                previous_key = "a"

            # Walk right sprite
            if event.key == pygame.K_d:
                doc.get(Sprite).reload("media/sprites/player/doc_right.png")
                previous_key = "d"

            # Debug testing:

            # Level up
            if event.key == pygame.K_RIGHTBRACKET:
                doc.get(Player).level += 1
                print(f"Levelled up to level {doc.get(Player).level}")

            # Level down
            if event.key == pygame.K_LEFTBRACKET:
                if doc.get(Player).level != 1:
                    doc.get(Player).level -= 1
                    print(f"Levelled down to level {doc.get(Player).level}")

            # Lose 3 HP
            if event.key == pygame.K_p:
                doc.get(Player).current_hp -= 3
                print("Lost 3 HP")

        elif event.type == pygame.KEYUP:
            keyinput.keys_down.remove(event.key)

    # Update objects/sprites
    for i in active_objects:
        i.update()
    sprite_group.update()

    # Draw sprites
    screen.fill((16, 16, 16))
    map.draw(screen)
    sprites.sort(key=lambda sprite: sprite.entity.y+sprite.image.get_height())
    for i in sprites:
        i.draw(screen)
    pygame.display.flip()

pygame.quit()