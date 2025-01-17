# This file contains the Battle class. It is used to start and control a battle between the player and an enemy.

import pygame
from player import Player
from entity import Enemy
from itemlist import *

in_battle = False

class Battle:
    def __init__(self, player, enemy, song):
        global in_battle
        in_battle = True
        print("\nAESOR appears!")
        self.player = player
        self.enemy = enemy
        self.song = song
        if self.song is not None:
            pygame.mixer.stop()
            pygame.mixer.Sound(self.song)

    def use_sword(self):
        self.enemy.get(Enemy).current_hp -= sword[1]
        print(f"Doc used Slash... AESOR took {sword[1]} damage!")

    def end_battle(self, player_win):
        if player_win:
            self.player.level += 1
            print(f"You won the battle! Leveled up to level {self.player.level}")
        else:
            print("You lost the battle...")