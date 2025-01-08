# This file contains the Player class. It is used as a component to an Entity object representing the player character. Movement, body and camera are set here.

import pygame
from items import *
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
        self.max_hp = 10 + self.level * 5
        self.current_hp = self.max_hp

    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        # Player's stats
        self.max_hp = 10 + self.level * 5

        # Player's movement
        if is_key_pressed(pygame.K_LCTRL):
            self.move_speed = 6
        else:
            self.move_speed = 4

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

    def use_item(self, item):
        if item == sword:
            print("You can only use this in battle!")
            return
        elif item == potion:
            if self.current_hp == self.max_hp:
                print(f"Your HP is already full ({self.current_hp}/{self.max_hp} HP)!")
                return
            elif self.current_hp + 15 > self.max_hp:
                self.current_hp = self.max_hp
                print(f"You are fully healed ({self.current_hp}/{self.max_hp} HP).")
                return
            else:
                self.current_hp += 15
                print(f"Your HP is now {self.current_hp}/{self.max_hp}.")
                return

    def open_inventory(self):
        print("\n\n\n\n\n\n\n\n----------\nDoc's Inventory:")
        for (i, item) in enumerate(self.inventory):
            print(f"{i+1}. {item[0][0]} x{item[1]}")
        print("----------")
        try:
            selection = int(input("Select the number of the item to use: "))
        except ValueError:
            selection = int(input("Invalid option. Select the number of the item to use: "))
        while True:
            if selection < 0 or selection > len(self.inventory):
                selection = int(input("Invalid option. Select the number of the item to use: "))
                continue
            else:
                break
        self.use_item(self.inventory[selection-1][0])

    def open_stats(self):
        print("\n\n\n\n\n\n\n\n----------\nDoc's Stats:")
        print(f"Level {self.level}\n{self.current_hp}/{self.max_hp} HP")
        print("----------")