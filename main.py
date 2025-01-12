'''
The Hologram - An RPG made for CS class
Zach N
'''

import pygame
from sprite import loaded_images
import keyinput
from itemlist import *
import maplist
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
maplist.worldmap = maplist.river_map

# Player
doc = Entity(Player(1, [[sword, 1], [potion, 2]]), Sprite("media/sprites/player/doc.png"), Body(8, 72, 28, 4), x=872, y=1316)
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
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                doc.get(Sprite).reload("media/sprites/player/doc_back.png")
                previous_key = "w"

            # Walk down sprite
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                doc.get(Sprite).reload("media/sprites/player/doc.png")
                previous_key = "s"

            # Walk down sprite
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                doc.get(Sprite).reload("media/sprites/player/doc_left.png")
                previous_key = "a"

            # Walk right sprite
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                doc.get(Sprite).reload("media/sprites/player/doc_right.png")
                previous_key = "d"

            # Debug testing:

            # Print Doc's coordinates
            if event.key == pygame.K_e:
                print(f"x, y: {doc.x}, {doc.y}")

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

    # Enter house 1
    if maplist.worldmap == maplist.river_map and doc.x in range(1084, 1108, 4) and doc.y == 856:
        print("Doc enters house 1")
        maplist.switch_map(maplist.house_map)
        doc.x = 376
        doc.y = 528

    # Exit house 1
    if maplist.worldmap == maplist.house_map and doc.x in range(344, 408, 4) and doc.y == 560:
        print("Doc exits house 1")
        maplist.switch_map(maplist.river_map)
        doc.x = 1096
        doc.y = 864

    # Draw sprites
    screen.fill((16, 16, 16))
    maplist.worldmap.draw(screen)
    sprites.sort(key=lambda sprite: sprite.entity.y+sprite.image.get_height())
    for i in sprites:
        i.draw(screen)
    pygame.display.flip()

pygame.quit()