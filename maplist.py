from tilemap import *

river_map_tiles = [
    None,
    TileType("grass", False, "media/sprites/tiles/grass_tile.png"),
    TileType("dirt", False, "media/sprites/tiles/dirt_tile.png"),
    TileType("water", True, "media/sprites/tiles/water_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png"),
    TileType("dark_grass", False, "media/sprites/tiles/dark_grass_tile.png")
]
house_map_tiles = [
    None,
    TileType("black", True, "media/sprites/tiles/black_tile.png"),
    TileType("wood", False, "media/sprites/tiles/wood_tile.png"),
    TileType("brick", True, "media/sprites/tiles/brick_tile.png")
]

river_map = Map(river_map_tiles, 32, "maps/river_map.json")
house_map = Map(house_map_tiles, 32, "maps/house_map.json")

worldmap = river_map