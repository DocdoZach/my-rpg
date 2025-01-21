# This file contains the Battle class. It is used to start and control a battle between the player and an enemy.

import pygame

import physics
from player import Player
from entity import Enemy
from itemlist import *
from movelist import *
from sprite import Sprite

in_battle = False
current_battle = None

class Battle:
    def __init__(self, player, enemy, song):
        self.song = song
        if self.song is not None:
            pygame.mixer.stop()
            pygame.mixer.Sound(self.song)
        global in_battle
        in_battle = True
        print("\nAESOR appears!")
        self.player = player
        self.enemy = enemy
        self.enemy.x = self.player.x
        self.enemy.y = self.player.y - 128
        self.enemy.get(Sprite).show = True
        physics.bodies.append(self.enemy.get(physics.Body))

    def your_turn(self):
        global in_battle
        print("\n----------\n1. Fight\n2. Use item\n3. Check stats\n4. Flee battle\n----------")
        while True:
            try:
                decision = int(input("What will you do? Select a number (1-4): "))
                match decision:
                    case 0:
                        break
                    case 1:
                        self.player.get(Player).use_item(sword)
                        break
                    case 2:
                        self.player.get(Player).open_inventory()
                        break
                    case 3:
                        self.player.get(Player).open_stats()
                    case 4:
                        in_battle = False
                        self.enemy.get(Sprite).show = False
                        physics.bodies.remove(self.enemy.get(physics.Body))
                        self.enemy.get(Enemy).current_hp = self.enemy.get(Enemy).max_hp
                        print("\nYou fled the battle.")
                        pygame.mixer.stop()
                        break
                    case _:
                        print("Invalid option.")
            except ValueError:
                print("Invalid option.")

    def use_sword(self):
        self.enemy.get(Enemy).current_hp -= sword[1]
        print(f"\nDoc used Slash... AESOR took {sword[1]} damage!")

    def use_stare(self):
        self.player.get(Player).current_hp -= stare[1]
        print(f"\nAESOR used Stare.. Doc took {stare[1]} damage!")

    def check_end(self):
        if self.player.get(Player).current_hp <= 0:
            self.end(False)
        elif self.enemy.get(Enemy).current_hp <= 0:
            self.end(True)

    def end(self, player_win):
        global in_battle
        self.enemy.get(Sprite).show = False
        physics.bodies.remove(self.enemy.get(physics.Body))
        self.player.get(Player).current_hp = self.player.get(Player).max_hp
        self.enemy.get(Enemy).current_hp = self.enemy.get(Enemy).max_hp
        if player_win:
            self.player.get(Player).level += 1
            print(f"\nYou won the battle! Leveled up to level {self.player.get(Player).level}")
            in_battle = False
        else:
            print("\nYou lost the battle...")
            in_battle = False
        pygame.mixer.stop()