'''
My RPG summative (name is a WIP!)
Zach N
'''

import pygame

# Sprite class
class Entity(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_file):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update(self):
        self.rect.center = [self.x, self.y]

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

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.y -= 1
    if key[pygame.K_s]:
        player.y += 1
    if key[pygame.K_a]:
        player.x -= 1
    if key[pygame.K_d]:
        player.x += 1

    sprite_group.update()
    sprite_group.draw(screen)
    pygame.display.flip()

pygame.quit()