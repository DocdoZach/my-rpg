# This file contains a list of maps and the tiles used by them.

from entity import Entity
from physics import Body
from sprite import Sprite
from tilemap import *

def map_sprite(kind, x, y):
    if kind == "tree":
        return Entity(Sprite("media/sprites/tree.png"), Body(40, 96, 44, 64), x=x, y=y)
    if kind == "house":
        return Entity(Sprite("media/sprites/house.png"), Body(28, 92, 164, 132), x=x, y=y)
    if kind == "well":
        return Entity(Sprite("media/sprites/well.png"), Body(28, 92, 164, 132), x=x, y=y)

def switch_map(new_map):
    global worldmap
    worldmap.toggle_map(new_map)
    worldmap = new_map
    worldmap.toggle_map(new_map)

river_map_tiles = [
    None,
    TileType("grass", False, "media/sprites/tiles/grass_tile.png"),
    TileType("dirt", False, "media/sprites/tiles/dirt_tile.png"),
    TileType("water", True, "media/sprites/tiles/water_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png"),
    TileType("dark_grass", False, "media/sprites/tiles/dark_grass_tile.png"),
    TileType("black", True, "media/sprites/tiles/black_tile.png"),
    TileType("sand", False, "media/sprites/tiles/sand_tile.png")
]
house_map_tiles = [
    None,
    TileType("black", True, "media/sprites/tiles/black_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png")
]


beach_map_entities = []
beach_map = Map(river_map_tiles, 32, "maps/beach_map.json", beach_map_entities)

river_map_entities = [
map_sprite("tree", 364, 616),
map_sprite("tree", 480, 848),
map_sprite("tree", 300, 1112),
map_sprite("tree", 716, 916),
map_sprite("tree", 232, 440),
map_sprite("tree", 1180, 816),
map_sprite("tree", 636, 512),
map_sprite("tree", 892, 376),
map_sprite("tree", 24, 144),
map_sprite("tree", 1356, 1060),
map_sprite("house", 1008, 704),
map_sprite("house", 272, 288),
map_sprite("house", 464, 48),
map_sprite("house", 1328, 304),
map_sprite("well", 784, 432)
]
river_map = Map(river_map_tiles, 32, "maps/river_map.json", river_map_entities)

house_map_entities = []
house_map = Map(house_map_tiles, 32, "maps/house_map.json", house_map_entities)

maps = [beach_map, river_map, house_map]
worldmap = beach_map
for i in maps:
    i.toggle_map(beach_map)