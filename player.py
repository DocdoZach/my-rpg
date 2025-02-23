# This file contains the Player class. It is used as a component of an Entity object representing the player character. Movement, body and camera are set here.

import pygame
import os
import battle
from itemlist import *
from sprite import Sprite
from keyinput import is_key_pressed
from camera import camera
from entity import active_objects
from physics import Body
import maplist

class Player:
    def __init__(self, level, inventory):
        active_objects.append(self)
        self.move_speed = 4
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
            self.move_speed = 8
        else:
            self.move_speed = 4

        if is_key_pressed(pygame.K_w) or is_key_pressed(pygame.K_UP):
            if self.entity.y > -44:
                self.entity.y -= self.move_speed
                self.entity.get(Sprite).delete()
                self.entity.get(Sprite).__init__("media/sprites/player/doc_back.png")

        if is_key_pressed(pygame.K_s) or is_key_pressed(pygame.K_DOWN):
            if self.entity.y < maplist.worldmap.height * 32 - 44:
                self.entity.y += self.move_speed
                self.entity.get(Sprite).delete()
                self.entity.get(Sprite).__init__("media/sprites/player/doc.png")

        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_a) or is_key_pressed(pygame.K_LEFT):
            if self.entity.x > -12:
                self.entity.x -= self.move_speed
                self.entity.get(Sprite).delete()
                self.entity.get(Sprite).__init__("media/sprites/player/doc_left.png")

        if is_key_pressed(pygame.K_d) or is_key_pressed(pygame.K_RIGHT):
            if self.entity.x < maplist.worldmap.width * 32 - 36:
                self.entity.x += self.move_speed
                self.entity.get(Sprite).delete()
                self.entity.get(Sprite).__init__("media/sprites/player/doc_right.png")

        if not body.is_position_valid():
            self.entity.x = previous_x

        if is_key_pressed(pygame.K_w) and is_key_pressed(pygame.K_a) and is_key_pressed(pygame.K_d):
            self.entity.get(Sprite).delete()
            self.entity.get(Sprite).__init__("media/sprites/player/doc_back.png")

        if is_key_pressed(pygame.K_s) and is_key_pressed(pygame.K_a) and is_key_pressed(pygame.K_d):
            self.entity.get(Sprite).delete()
            self.entity.get(Sprite).__init__("media/sprites/player/doc.png")

        # Camera calculations

        target_camera_x = self.entity.x - camera.width / 2 + sprite.image.get_width()/2
        target_camera_y = self.entity.y - camera.height / 2 + sprite.image.get_height()/2

        if target_camera_x < 0:
            target_camera_x = 0
        elif target_camera_x > maplist.worldmap.width * maplist.worldmap.tile_size - camera.width:
            target_camera_x = maplist.worldmap.width * maplist.worldmap.tile_size - camera.width
        if target_camera_y < 0:
            target_camera_y = 0
        elif target_camera_y > maplist.worldmap.height * maplist.worldmap.tile_size - camera.height:
            target_camera_y = maplist.worldmap.height * maplist.worldmap.tile_size - camera.height

        camera.x = target_camera_x
        camera.y = target_camera_y

    def use_item(self, item):
        if item == sword:
            if not battle.in_battle:
                print("You can only use this in battle!")
                return
            else:
                battle.current_battle.use_sword()

        elif item == potion:
            if self.current_hp == self.max_hp:
                print(f"Your HP is already full ({self.current_hp}/{self.max_hp} HP)!")
                return
            elif self.current_hp + 15 > self.max_hp:
                self.current_hp = self.max_hp
                print(f"You are fully healed ({self.current_hp}/{self.max_hp} HP).")
                self.inventory.remove(item)
                return
            else:
                self.current_hp += 15
                print(f"Your HP is now {self.current_hp}/{self.max_hp}.")
                self.inventory.remove(item)
                return

        elif item == acorn:
            if self.current_hp == self.max_hp:
                print(f"Your HP is already full ({self.current_hp}/{self.max_hp} HP)! Who eats acorns anyways?")
                return
            elif self.current_hp + 5 > self.max_hp:
                self.current_hp = self.max_hp
                print(f"You are fully healed ({self.current_hp}/{self.max_hp} HP). Weirdo.")
                self.inventory.remove(item)
                return
            else:
                self.current_hp += 5
                print(f"Your HP is now {self.current_hp}/{self.max_hp}. Hope you're happy.")
                self.inventory.remove(item)
                return

    def open_inventory(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----------\nDoc's Inventory:")
        for (i, item) in enumerate(self.inventory):
            print(f"{i+1}. {item[0]}")
        print("----------")
        while True:
            try:
                selection = int(input("Select the number of the item to use: "))
                if selection <= 0 or selection > len(self.inventory):
                    print("Invalid option.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid option.")
        self.use_item(self.inventory[selection-1])

    def open_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----------\nDoc's Stats:")
        print(f"Level {self.level}\n{self.current_hp}/{self.max_hp} HP")
        print("----------")