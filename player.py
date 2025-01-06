# This file contains the Player class. It is used as a component to an Entity object representing the player character. Movement, body and camera are set here.

import pygame
from sprite import Sprite
from keyinput import is_key_pressed
from camera import camera
from entity import active_objects
from physics import Body
import tilemap

class Player:
    def __init__(self, level, inventory):
        active_objects.append(self)
        self.move_speed = 8
        self.level = level
        self.inventory = inventory
        self.hp = 10 + self.level * 5

    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        # Toggle inventory
        if is_key_pressed(pygame.K_e):
            print("Inventory:")
            for item in self.inventory:
                print(item[0])

        # Player's stats
        self.hp = 10 + self.level * 5

        # Player's movement
        if is_key_pressed(pygame.K_LCTRL):
            self.move_speed = 12
        else:
            self.move_speed = 8

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

        target_camera_x = self.entity.x - camera.width / 2 + sprite.image.get_width()/2
        target_camera_y = self.entity.y - camera.height / 2 + sprite.image.get_height()/2

        if target_camera_x < 0:
            target_camera_x = 0
        elif target_camera_x > tilemap.worldmap.width * tilemap.worldmap.tile_size - camera.width:
            target_camera_x = tilemap.worldmap.width * tilemap.worldmap.tile_size - camera.width
        if target_camera_y < 0:
            target_camera_y = 0
        elif target_camera_y > tilemap.worldmap.height * tilemap.worldmap.tile_size - camera.height:
            target_camera_y = tilemap.worldmap.height * tilemap.worldmap.tile_size - camera.height

        camera.x = target_camera_x
        camera.y = target_camera_y