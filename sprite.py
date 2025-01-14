# This file contains the Sprite class, used to give entities sprites visible in the game window.

import pygame
from camera import camera

sprites = []
loaded_images = {}

class Sprite:
    def __init__(self, image_file):
        self.show = True
        if image_file in loaded_images:
            self.image = loaded_images[image_file]
        else:
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.image = pygame.transform.scale(self.image, [self.rect.w * 4, self.rect.h * 4])
            loaded_images[image_file] = self.image
        sprites.append(self)
    def delete(self):
        sprites.remove(self)
    def draw(self, screen):
        if self.show:
            screen.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))

class AnimatedSprite:
    def __init__(self):
        pass
    def play(self):
        pass
    def stop(self):
        pass