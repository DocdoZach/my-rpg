# This file contains the code to create a game screen, and provides code used to set the player's camera.

import pygame

camera = pygame.Rect(0, 0, 0, 0)

def create_screen(width, height, title):
    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width, height), flags=pygame.SCALED, vsync=1)
    camera.width = width
    camera.height = height
    return screen