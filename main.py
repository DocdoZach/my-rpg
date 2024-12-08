'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# Game window
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))

# Player
pos_x = 400
pos_y = 300
player = Entity(pos_x, pos_y, "media/sprites/doc.png")
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    sprite_group.draw(screen)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        pos_x += 1

    pygame.display.flip()

pygame.quit()