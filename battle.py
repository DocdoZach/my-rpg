# This file contains the Battle class. It is used to start and control a battle between the player and an enemy.

import pygame

class Battle:
    def __init__(self, player, enemy, song):
        self.player = player
        self.enemy = enemy
        self.song = song
        if self.song is not None:
            pygame.mixer.stop()
            pygame.mixer.Sound(self.song)
        #self.player.entity.x =