import pygame
from camera import camera

sprites = []
loaded_images = {}

class Sprite:
    def __init__(self, x, y, image_file):
        if image_file in loaded_images:
            self.image = loaded_images[image_file]
        else:
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.image = pygame.transform.scale(self.image, [self.rect.w * 4, self.rect.h * 4])
            self.rect.center = [x, y]
            loaded_images[image_file] = self.image
        self.x = x
        self.y = y
        sprites.append(self)
    def update(self):
        self.rect.center = [self.x, self.y]
    def delete(self):
        sprites.remove(self)
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))