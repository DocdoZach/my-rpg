'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame

# Sprite class
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
x_pos = 400
y_pos = 300
player = Entity(x_pos, y_pos, "media/sprites/doc.png")
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
    if key[pygame.K_w]:
        y_pos -= 1
    if key[pygame.K_d]:
        y_pos += 1
    if key[pygame.K_a]:
        x_pos -= 1
    if key[pygame.K_s]:
        x_pos += 1

    pygame.display.flip()

pygame.quit()