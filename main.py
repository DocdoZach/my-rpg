'''
The Hologram - An RPG made for CS class
Zach N
'''

import pygame
from sprite import loaded_images
import keyinput
from itemlist import *
from maplist import *
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
worldmap = river_map

# Trees
def make_sprite(kind, x, y):
    if kind == "tree":
        return Entity(Sprite("media/sprites/tree.png"), Body(40, 96, 44, 64), x=x, y=y)
    if kind == "house":
        return Entity(Sprite("media/sprites/house.png"), Body(28, 92, 164, 132), x=x, y=y)
    if kind == "well":
        return Entity(Sprite("media/sprites/well.png"), Body(28, 92, 164, 132), x=x, y=y)

make_sprite("tree", 364, 616)
make_sprite("tree", 480, 848)
make_sprite("tree", 300, 1112)
make_sprite("tree", 716, 916)
make_sprite("tree", 232, 440)
make_sprite("tree", 1180, 816)
make_sprite("tree", 636, 512)
make_sprite("tree", 892, 376)
house1 = make_sprite("house", 1008, 704)
house2 = make_sprite("house", 272, 288)
make_sprite("well", 784, 432)

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
    if worldmap == river_map and doc.x == 1096 and doc.y == 860:
        print("Doc enters house 1")
        worldmap = house_map
        doc.x = 352
        doc.y = 528

    # Draw sprites
    screen.fill((16, 16, 16))
    worldmap.draw(screen)
    sprites.sort(key=lambda sprite: sprite.entity.y+sprite.image.get_height())
    for i in sprites:
        i.draw(screen)
    pygame.display.flip()

pygame.quit()