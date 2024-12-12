import pygame
import math
from sprite import Sprite
from input import is_key_pressed
from camera import camera

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

        camera.x = self.x - camera.width / 2 + self.image.get_width()/2
        camera.y = self.y - camera.height / 2 + self.image.get_height()/2