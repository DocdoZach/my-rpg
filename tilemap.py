import pygame

class TileType:
    def __init__(self, name, has_collision, image_file):
        self.name = name
        self.image = pygame.image.load(image_file)
        self.has_collision = has_collision

class Map:
    def __init__(self, tile_types, tile_size, map_file):
        self.tile_types = tile_types
        file = open(map_file, "r")
        data = file.read()
        file.close()
        self.tiles = []

        for line in data.split("\n"):
            row = []
            for tile_number in line:
                row.append(int(tile_number))
            self.tiles.append(row)

        self.tile_size = tile_size
    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_types[tile].image
                screen.blit(image, location)