"""
The Hologram - An RPG made for CS class
Zach N
"""

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

# Player
doc = Entity(Player(1, [sword, potion]),
             Sprite("media/sprites/player/doc.png"),
             Body(12, 72, 24, 8),
             x=480, y=768)

# Boss
aesor = Entity(Enemy(1),
               Sprite("media/sprites/aesor.png"),
               Body(12, 72, 24, 8),
               x=0, y=0)
aesor.get(Sprite).show = False
physics.bodies.remove(aesor.get(Body))

# Map exit checks
def map_exits():
    global spoke_to_resident, spoke_to_allium, spoke_to_friend

    # beach <-> river
    if maplist.worldmap == maplist.beach_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("Beach -> River")
        maplist.switch_map(maplist.river_map)
        doc.y = 1520
    if maplist.worldmap == maplist.river_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("River -> Beach")
        maplist.switch_map(maplist.beach_map)
        doc.y = 0

    # Enter/exit house SE
    if maplist.worldmap == maplist.river_map and doc.x in range(1084, 1108+1, 4) and doc.y == 856:
        print("River -> House SE")
        maplist.switch_map(maplist.houseSE_map)
        doc.x = 376
        doc.y = 528
        spoke_to_resident = False
    if maplist.worldmap == maplist.houseSE_map and doc.x in range(340, 412+1, 4) and doc.y == 560:
        print("House SE -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 1096
        doc.y = 864
        spoke_to_resident = False

    # Enter/exit house SW
    if maplist.worldmap == maplist.river_map and doc.x in range(348, 372+1, 4) and doc.y == 440:
        print("River -> House SW")
        maplist.switch_map(maplist.houseSW_map)
        doc.x = 376
        doc.y = 528
        spoke_to_allium = False
    if maplist.worldmap == maplist.houseSW_map and doc.x in range(340, 412+1, 4) and doc.y == 560:
        print("House SW -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 360
        doc.y = 448
        spoke_to_allium = False

    # Enter/exit house NW
    if maplist.worldmap == maplist.river_map and doc.x in range(540, 564+1, 4) and doc.y == 200:
        print("River -> House NW")
        maplist.switch_map(maplist.houseNW_map)
        doc.x = 376
        doc.y = 528
    if maplist.worldmap == maplist.houseNW_map and doc.x in range(340, 412+1, 4) and doc.y == 560:
        print("House NW -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 552
        doc.y = 208

    # Enter/exit house NE
    if maplist.worldmap == maplist.river_map and doc.x in range(1404, 1428+1, 4) and doc.y == 456:
        print("River -> House NE")
        maplist.switch_map(maplist.houseNE_map)
        doc.x = 376
        doc.y = 528
    if maplist.worldmap == maplist.houseNE_map and doc.x in range(340, 412+1, 4) and doc.y == 560:
        print("House NE -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 1416
        doc.y = 464

    # river <-> patch
    if maplist.worldmap == maplist.river_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("River -> Patch")
        maplist.switch_map(maplist.patch_map)
        doc.y = 1520
    if maplist.worldmap == maplist.patch_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Patch -> River")
        maplist.switch_map(maplist.river_map)
        doc.y = 0

    # river <-> ruins
    if maplist.worldmap == maplist.river_map and doc.x == -12 and doc.y in range(0, 1600+1, 4):
        print("River -> Ruins")
        maplist.switch_map(maplist.ruins_map)
        doc.x = 1552
    if maplist.worldmap == maplist.ruins_map and doc.x == 1564 and doc.y in range(0, 1600+1, 4):
        print("Ruins -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 0

    # beach <-> west beach
    if maplist.worldmap == maplist.beach_map and doc.x == -12 and doc.y in range(0, 1600+1, 4):
        print("Beach -> West Beach")
        maplist.switch_map(maplist.west_beach_map)
        doc.x = 1552
    if maplist.worldmap == maplist.west_beach_map and doc.x == 1564 and doc.y in range(0, 1600+1, 4):
        print("West Beach -> Beach")
        maplist.switch_map(maplist.beach_map)
        doc.x = 0

    # ruins <-> west beach
    if maplist.worldmap == maplist.ruins_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Ruins -> West Beach")
        maplist.switch_map(maplist.west_beach_map)
        doc.y = 0
    if maplist.worldmap == maplist.west_beach_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("West Beach -> Ruins")
        maplist.switch_map(maplist.ruins_map)
        doc.y = 1520

    # patch <-> castle_gate
    if maplist.worldmap == maplist.patch_map and doc.x == -12 and doc.y in range(0, 1600+1, 4):
        print("Patch -> Castle Gate")
        maplist.switch_map(maplist.castle_gate_map)
        doc.x = 1552
    if maplist.worldmap == maplist.castle_gate_map and doc.x == 1564 and doc.y in range(0, 1600+1, 4):
        print("Castle Gate -> Patch")
        maplist.switch_map(maplist.patch_map)
        doc.x = 0

    # ruins <-> castle_gate
    if maplist.worldmap == maplist.ruins_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("Ruins -> Castle Gate")
        maplist.switch_map(maplist.castle_gate_map)
        doc.y = 1520
    if maplist.worldmap == maplist.castle_gate_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Castle Gate -> Ruins")
        maplist.switch_map(maplist.ruins_map)
        doc.y = 0

    # beach <-> east beach
    if maplist.worldmap == maplist.beach_map and doc.x == 1564 and doc.y in range(0, 1600+1, 4):
        print("Beach -> East Beach")
        maplist.switch_map(maplist.east_beach_map)
        doc.x = 0
    if maplist.worldmap == maplist.east_beach_map and doc.x == -12 and doc.y in range(0, 1600+1, 4):
        print("East Beach -> Beach")
        maplist.switch_map(maplist.beach_map)
        doc.x = 1552

    # east beach <-> delta
    if maplist.worldmap == maplist.east_beach_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("East Beach -> Delta")
        maplist.switch_map(maplist.delta_map)
        doc.y = 1520
    if maplist.worldmap == maplist.delta_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Delta -> East Beach")
        maplist.switch_map(maplist.east_beach_map)
        doc.y = 0

    # river <-> delta
    if maplist.worldmap == maplist.river_map and doc.x == 1564 and doc.y in range(0, 1600 + 1, 4):
        print("River -> Delta")
        maplist.switch_map(maplist.delta_map)
        doc.x = 0
    if maplist.worldmap == maplist.delta_map and doc.x == -12 and doc.y in range(0, 1600 + 1, 4):
        print("Delta -> River")
        maplist.switch_map(maplist.river_map)
        doc.x = 1552

    # delta <-> lake
    if maplist.worldmap == maplist.delta_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("Delta -> Lake")
        maplist.switch_map(maplist.lake_map)
        doc.y = 1520
        spoke_to_friend = False
    if maplist.worldmap == maplist.lake_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("lake -> Delta")
        maplist.switch_map(maplist.delta_map)
        doc.y = 0
        spoke_to_friend = False

    # patch <-> lake
    if maplist.worldmap == maplist.patch_map and doc.x == 1564 and doc.y in range(0, 1600 + 1, 4):
        print("Patch -> Lake")
        maplist.switch_map(maplist.lake_map)
        doc.x = 0
        spoke_to_friend = False
    if maplist.worldmap == maplist.lake_map and doc.x == -12 and doc.y in range(0, 1600 + 1, 4):
        print("Lake -> Patch")
        maplist.switch_map(maplist.patch_map)
        doc.x = 1552
        spoke_to_friend = False

    # east beach <-> easter beach
    if maplist.worldmap == maplist.east_beach_map and doc.x == 1564 and doc.y in range(0, 1600 + 1, 4):
        print("East Beach -> Easter Beach")
        maplist.switch_map(maplist.easter_beach_map)
        doc.x = 0
    if maplist.worldmap == maplist.easter_beach_map and doc.x == -12 and doc.y in range(0, 1600 + 1, 4):
        print("Easter Beach -> East Beach")
        maplist.switch_map(maplist.east_beach_map)
        doc.x = 1552

    # easter beach <-> tower
    if maplist.worldmap == maplist.easter_beach_map and doc.x in range(0, 1600+1, 4) and doc.y == -44:
        print("Easter Beach -> Tower")
        maplist.switch_map(maplist.tower_map)
        doc.y = 1520
        spoke_to_friend = False
    if maplist.worldmap == maplist.tower_map and doc.x in range(0, 1600+1, 4) and doc.y == 1556:
        print("Tower -> Easter Beach")
        maplist.switch_map(maplist.easter_beach_map)
        doc.y = 0
        spoke_to_friend = False

    # delta <-> tower
    if maplist.worldmap == maplist.delta_map and doc.x == 1564 and doc.y in range(0, 1600 + 1, 4):
        print("Delta -> Tower")
        maplist.switch_map(maplist.tower_map)
        doc.x = 0
    if maplist.worldmap == maplist.tower_map and doc.x == -12 and doc.y in range(0, 1600 + 1, 4):
        print("Tower -> Delta")
        maplist.switch_map(maplist.delta_map)
        doc.x = 1552

spoke_to_resident = False
spoke_to_allium = False
spoke_to_friend = False

# Object interaction checks
def object_interactions():
    global spoke_to_resident, spoke_to_allium, spoke_to_friend

    # House SE chair
    if maplist.worldmap == maplist.houseSE_map and doc.x in range(228, 244+1, 4) and doc.y == 232:
        doc.get(Sprite).delete()
        doc.get(Sprite).__init__("media/sprites/player/doc.png")

    # House SE NPC
    if not spoke_to_resident:
        if maplist.worldmap == maplist.houseSE_map and doc.x in range(404, 444+1, 4) and doc.y == 280:
            print("Resident: Hey Doc! Find anything cool lately?")
            spoke_to_resident = True

    # House SW chair
    if maplist.worldmap == maplist.houseSW_map and doc.x in range(588, 604+1, 4) and doc.y == 192:
        doc.get(Sprite).delete()
        doc.get(Sprite).__init__("media/sprites/player/doc.png")

    # House SW Allium
    if not spoke_to_allium:
        if maplist.worldmap == maplist.houseSW_map and doc.x in range(380, 420+1, 4) and doc.y == 328:
            print("ALLIUM: Hello, Doc. I'm looking after a friend's place. He's near the lake if you're looking for him.")
            spoke_to_allium = True

    # Lake friend
    if not spoke_to_friend:
        if maplist.worldmap == maplist.lake_map and doc.x == 556 and doc.y == 1220:
            print("ALLIUM's Friend: Psst, buddy, over here. I'm the tree. Here's an acorn!")
            doc.get(Player).inventory.append(acorn)
            spoke_to_friend = True

# Audio
song = pygame.mixer.Sound("media/audio/music/hologram.mp3")
pygame.mixer.Sound.set_volume(song, 0.5)

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

                # Exit game
                if event.key == pygame.K_ESCAPE:
                    is_running = False

                # Open inventory
                if event.key == pygame.K_z:
                    doc.get(Player).open_inventory()

                # Open stats
                if event.key == pygame.K_x:
                    doc.get(Player).open_stats()

                # Debug testing:

                # Create Battle object
                if event.key == pygame.K_b:
                    battle.current_battle = Battle(doc, aesor, song)
                    doc.get(Sprite).delete()
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

                # Change move speed
                if event.key == pygame.K_y:
                    doc.get(Player).move_speed = float(input("What is the new move speed?: "))

        elif event.type == pygame.KEYUP:
            keyinput.keys_down.remove(event.key)

    # Update objects/sprites
    for i in active_objects:
        i.update()
    sprite_group.update()

    # Check for map exits
    map_exits()

    # Check for object interactions
    object_interactions()

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
        battle.current_battle.check_end()
    if battle.in_battle:
        battle.current_battle.use_stare()
        battle.current_battle.check_end()

pygame.quit()