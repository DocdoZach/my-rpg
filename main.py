'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((388, 280, 12, 20))

run = True
while run:

    pygame.draw.rect(screen, (0, 0, 255), player)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()