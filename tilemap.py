import pygame
import json
from camera import camera

class TileType:
    def __init__(self, name, has_collision, image_file):
        self.name = name
        self.image = pygame.image.load(image_file)
        self.has_collision = has_collision

class Map:
    def __init__(self, tile_types, tile_size, map_file):
        self.tile_types = tile_types
        with open(map_file, "r") as file:
            data = json.load(file)["layers"][0]

        self.width = data["width"]
        self.height = data["height"]

        self.tiles = []
        for i, tile in enumerate(data["data"]):
            if i % self.width == 0:
                self.tiles.append([])
            self.tiles[-1].append(tile_types[tile])

        self.tile_size = tile_size
    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                screen.blit(tile.image, location)