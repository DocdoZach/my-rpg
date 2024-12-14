import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera
from entity import active_objects
from physics import Body

class Player:
    def __init__(self):
        active_objects.append(self)
        self.move_speed = 8

    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        if is_key_pressed(pygame.K_w):
            self.entity.y -= self.move_speed

        if is_key_pressed(pygame.K_s):
            self.entity.y += self.move_speed

        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_a):
            self.entity.x -= self.move_speed

        if is_key_pressed(pygame.K_d):
            self.entity.x += self.move_speed

        if not body.is_position_valid():
            self.entity.x = previous_x

        camera.x = self.entity.x - camera.width / 2 + sprite.image.get_width()/2
        camera.y = self.entity.y - camera.height / 2 + sprite.image.get_height()/2