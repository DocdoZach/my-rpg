'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame
import input
from sprite import sprites
from sprite import Sprite
from player import Player
from camera import create_screen

pygame.init()

# Sprite group
sprite_group = pygame.sprite.Group()

# Game window
screen = create_screen(800, 600, "My RPG")

# Repeating tile background (wip)
screen.fill((255, 255, 255))
for i in range(0, 800, 32):
    for j in range(0, 600, 32):
        pygame.image.load("media/sprites/grass_tile.png")
        tile = Sprite(i, j, "media/sprites/grass_tile.png")

# Player
player = Player(400, 300, "media/sprites/doc.png")

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
    for i in sprites:
        i.draw(screen)

    pygame.display.flip()

pygame.quit()