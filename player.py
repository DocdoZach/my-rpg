import pygame
from sprite import Sprite
from input import is_key_pressed

class Player(Sprite):
    def __init__(self, x, y, image_file):
        super().__init__(x, y, image_file)
        self.move_speed = 8
    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.move_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.move_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.move_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.move_speed