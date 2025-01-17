'''
The Hologram - An RPG made for CS class
Zach N
'''

import pygame

import battle
from sprite import loaded_images
import keyinput
from itemlist import *
import maplist
from sprite import sprites, Sprite
from player import Player
from tilemap import *
from camera import create_screen
from entity import Entity, active_objects, Enemy
from physics import Body
from battle import Battle

pygame.init()

# Sprite group
sprite_group = pygame.sprite.Group()

# Game window
screen = create_screen(800, 640, "THE HOLOGR△M")

# Map exit checks
def map_exits():

    # ID 1 -> 2
    if maplist.worldmap == maplist.beach_map and doc.x in range(0, 960+1, 4) and doc.y == -44:
        print("Beach -> River")
        maplist.switch_map(maplist.river_map)
        doc.x += 640
        doc.y = 1520

    # ID 2 -> 1
    if maplist.worldmap == maplist.river_map and doc.x in range(640, 1600+1, 4) and doc.y == 1556:
        print("River -> Beach")
        maplist.switch_map(maplist.beach_map)
        doc.x -= 640
        doc.y = 0

    # Enter house SE
    if maplist.worldmap == maplist.river_map and doc.x in range(1084, 1108+1, 4) and doc.y == 856:
        print("River -> House SE")
        maplist.switch_map(maplist.houseSE_map)
        doc.x = 376
        doc.y = 528

    # Exit house SE
    if maplist.worldmap == maplist.houseSE_map and doc.x in range(344, 408+1, 4) and doc.y == 560:
        print("House SE -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 1096
        doc.y = 864

    # Enter house SW
    if maplist.worldmap == maplist.river_map and doc.x in range(348, 372+1, 4) and doc.y == 440:
        print("River -> House SW")
        maplist.switch_map(maplist.houseSW_map)
        doc.x = 376
        doc.y = 528

    # Exit house SW
    if maplist.worldmap == maplist.houseSW_map and doc.x in range(344, 408+1, 4) and doc.y == 560:
        print("House SW -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 360
        doc.y = 448

    # Enter house NW
    if maplist.worldmap == maplist.river_map and doc.x in range(540, 564+1, 4) and doc.y == 200:
        print("River -> House NW")
        maplist.switch_map(maplist.houseNW_map)
        doc.x = 376
        doc.y = 528

    # Exit house NW
    if maplist.worldmap == maplist.houseNW_map and doc.x in range(344, 408+1, 4) and doc.y == 560:
        print("House NW -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 552
        doc.y = 208

    # Enter house NE
    if maplist.worldmap == maplist.river_map and doc.x in range(1404, 1428+1, 4) and doc.y == 456:
        print("River -> House NE")
        maplist.switch_map(maplist.houseNE_map)
        doc.x = 376
        doc.y = 528

    # Exit house NE
    if maplist.worldmap == maplist.houseNE_map and doc.x in range(344, 408+1, 4) and doc.y == 560:
        print("House NE -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 1416
        doc.y = 464

    # ID 2 -> 3
    if maplist.worldmap == maplist.river_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("River -> Patch")
        maplist.switch_map(maplist.patch_map)
        doc.y = 1520

    # ID 3 -> 2
    if maplist.worldmap == maplist.patch_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Patch -> River")
        maplist.switch_map(maplist.river_map)
        doc.y = 0

# Audio
song = pygame.mixer.Sound("media/audio/music/hologram.mp3")
pygame.mixer.Sound.set_volume(song, 0.5)


# Player
doc = Entity(Player(1, [[sword, 1], [potion, 2]]),
             Sprite("media/sprites/player/doc.png"),
             Body(12, 72, 24, 8),
             x=480, y=768)

# Boss
aesor = Entity(Enemy(1),
               Sprite("media/sprites/aesor.png"),
               Body(0, 0, 64, 96),
               x=0, y=0)
aesor.get(Sprite).show = False
physics.bodies.remove(aesor.get(Body))

# Game clock
clock = pygame.time.Clock()

# Game loop
is_running = True
while is_running:

    # Game clock frequency (60Hz)
    clock.tick(60)

    # Event handler (quit game, keys pressed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            keyinput.keys_down.add(event.key)
            if not battle.in_battle:

                # Open inventory
                if event.key == pygame.K_z:
                    doc.get(Player).open_inventory()

                # Open stats
                if event.key == pygame.K_x:
                    doc.get(Player).open_stats()

                # Debug testing:

                # Create Battle object
                if event.key == pygame.K_b:
                    battle.current_battle = Battle(doc, aesor, None)
                    doc.get(Sprite).__init__("media/sprites/player/doc_back.png")

                # Print Doc's coordinates
                if event.key == pygame.K_e:
                    print(f"x, y: {doc.x}, {doc.y}")

                # Level up
                if event.key == pygame.K_RIGHTBRACKET:
                    doc.get(Player).level += 1
                    print(f"Leveled up to level {doc.get(Player).level}")

                # Level down
                if event.key == pygame.K_LEFTBRACKET:
                    if doc.get(Player).level != 1:
                        doc.get(Player).level -= 1
                        print(f"Leveled down to level {doc.get(Player).level}")

                # Lose 3 HP
                if event.key == pygame.K_p:
                    doc.get(Player).current_hp -= 3
                    print("Lost 3 HP")

                # Toggle on music
                if event.key == pygame.K_n:
                    pygame.mixer.Sound.play(song)

                # Toggle off music
                if event.key == pygame.K_m:
                    pygame.mixer.stop()

        elif event.type == pygame.KEYUP:
            keyinput.keys_down.remove(event.key)

    # Update objects/sprites
    for i in active_objects:
        i.update()
    sprite_group.update()

    # Check for map exits
    map_exits()

    # Draw sprites
    screen.fill((16, 16, 16))
    maplist.worldmap.draw(screen)
    sprites.sort(key=lambda sprite: sprite.entity.y+sprite.image.get_height())
    for i in sprites:
        if i.is_bg:
            sprites.remove(i)
            sprites.insert(0, i)
    for i in sprites:
        i.draw(screen)
    pygame.display.flip()

    # Battle mode
    if battle.in_battle:
        battle.current_battle.your_turn()

pygame.quit()