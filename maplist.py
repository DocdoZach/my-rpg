# This file contains a list of maps and the tiles used by them.

import physics
from entity import Entity
from physics import Body
from sprite import Sprite
from tilemap import *

def map_sprite(kind, x, y):
    if kind == "tree":
        return Entity(Sprite("media/sprites/tree.png", False), Body(44, 100, 40, 60), x=x, y=y)
    if kind == "house":
        return Entity(Sprite("media/sprites/house.png", False), Body(32, 96, 160, 128), x=x, y=y)
    if kind == "well":
        return Entity(Sprite("media/sprites/well.png", False), Body(32, 96, 160, 128), x=x, y=y)
    if kind == "carpet":
        return Entity(Sprite("media/sprites/carpet.png", True), Body(0, 0, 0, 0), x=x, y=y)
    if kind == "chair":
        return Entity(Sprite("media/sprites/chair.png", True), Body(0, 0, 40, 64), x=x, y=y)
    if kind == "purple npc":
        return Entity(Sprite("media/sprites/npc_purple.png", False), Body(12, 72, 24, 8), x=x, y=y)

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
    TileType("sand", False, "media/sprites/tiles/sand_tile.png"),
    TileType("planks", False, "media/sprites/tiles/planks_tile.png"),
    TileType("stone", False, "media/sprites/tiles/stone_tile.png"),
    TileType("stone_brick", True, "media/sprites/tiles/stone_brick_tile.png")
]
house_map_tiles = [
    None,
    TileType("black", True, "media/sprites/tiles/black_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png")
]

beach_map = Map(river_map_tiles, 32, "maps/beach_map.json", [])
beach_map.entities = [
    map_sprite("tree", 788, 92),
    map_sprite("tree", 200, 188)
]

river_map = Map(river_map_tiles, 32, "maps/river_map.json", [])
river_map.entities = [
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

houseSE_map = Map(river_map_tiles, 32, "maps/house_map.json", [])
houseSE_map.entities = [
    map_sprite("carpet", 288, 240),
    map_sprite("chair", 240, 240),
    map_sprite("purple npc", 424, 272)
]

houseSW_map = Map(river_map_tiles, 32, "maps/house_map.json", [])
houseSW_map.entities = [
    map_sprite("carpet", 288, 240)
]

houseNW_map = Map(river_map_tiles, 32, "maps/house_map.json", [])
houseNW_map.entities = [
    map_sprite("carpet", 288, 240)
]

houseNE_map = Map(river_map_tiles, 32, "maps/house_map.json", [])
houseNE_map.entities = [
    map_sprite("carpet", 288, 240)
]

patch_map = Map(river_map_tiles, 32, "maps/patch_map.json", [])
patch_map.entities = [
    map_sprite("tree", 32, 1092),
    map_sprite("tree", -28, 1112),
    map_sprite("tree", 112, 628),
    map_sprite("tree", 316, 1124),
    map_sprite("tree", 340, 280),
    map_sprite("tree", 948, 540),
    map_sprite("tree", 1128, 868),
]

ruins_map = Map(river_map_tiles, 32, "maps/ruins_map.json", [])
ruins_map.entities = [
    map_sprite("tree", 1336, 628),
    map_sprite("tree", 1112, 256),
    map_sprite("tree", 292, 168),
    map_sprite("tree", 180, 852)
]

west_beach_map = Map(river_map_tiles, 32, "maps/west_beach_map.json", [])
west_beach_map.entities = [
    map_sprite("tree", 1144, 48)
]

maps = [beach_map, river_map, houseSE_map, houseSW_map, houseNW_map, houseNE_map, patch_map, ruins_map, west_beach_map]
worldmap = beach_map
for i in maps:
    i.toggle_map(beach_map)
physics.bodies = []
for j in beach_map.entities:
    physics.bodies.append(j.get(Body))