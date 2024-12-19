import pygame
import json
from camera import camera
from math import ceil

map = None

class TileType:
    def __init__(self, name, has_collision, image_file):
        self.name = name
        self.image = pygame.image.load(image_file)
        self.has_collision = has_collision

class Map:
    def __init__(self, tile_types, tile_size, map_file):
        global map
        self.tile_types = tile_types
        map = self

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

    def is_point_solid(self, x, y):
        x_tile = int(x / self.tile_size)
        y_tile = int(y / self.tile_size)
        if x_tile < 0 or \
            y_tile < 0 or \
            x_tile >= len(self.tiles[y_tile]) or \
            y_tile >= len(self.tiles):
            return False
        tile = self.tiles[y_tile][x_tile]
        return self.tile_types[tile].has_collision

    def is_rect_solid(self, x, y, width, height):
        x_checks = int(ceil(width/self.tile_size))
        y_checks = int(ceil(height / self.tile_size))
        for iy in range(y_checks):
            for ix in range(x_checks):
                x = ix * self.tile_size + x
                y = iy * self.tile_size + y
                if self.is_point_solid(x, y):
                    return True
        if self.is_point_solid(x + width, y):
            return True
        if self.is_point_solid(x, y + height):
            return True
        if self.is_point_solid(x + width, y + height):
            return True
        return False

    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                screen.blit(tile.image, location)