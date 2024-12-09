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
        self.image = pygame.transform.scale(self.image, [self.rect.w*4, self.rect.h*4])
        self.rect.center = [pos_x, pos_y]
    def update(self):
        self.rect.center = [self.x, self.y]
#class Player(Entity):

# Game window
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))

# Repeating tile background (wip)
for i in range(0, screen_x, 16):
    for j in range(0, screen_y, 16):
        pygame.image.load("media/sprites/grass_tile.png")

# Player
player = Entity(400, 300, "media/sprites/doc.png")
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