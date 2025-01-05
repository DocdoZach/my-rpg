# This file contains the set of keys that are currently being pressed on the keyboard when the game window is focused.

keys_down = set()

def is_key_pressed(key):
    return key in keys_down