"""main_Array_VIS_FOR_TK.py
Version of Aug. 29, 2018. Works with the formulation of
Missionaries and Cannibals that uses a State class for
representing states.
"""

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test
import random

from tkinter import font

myFont = None

WIDTH = 300
HEIGHT = 300
TITLE = 'Rising sea level'
GRID_SIZE = 3
SEA = (100, 100, 200)
LAND = (255, 180, 0)


def initialize_vis():
    initialize_tk(WIDTH, HEIGHT, TITLE)


def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).

    caption = "Current state of the puzzle. Textual version: " + str(s)
    seaLevel = int(GRID_SIZE * 1.5 * max(s.island_features['MAX_SEA_LEVEL'] - s.seaLevel, 0))

    the_color_array = [[(SEA)] * GRID_SIZE for i in range(GRID_SIZE)]
    spiral_array = generate_spiral_coordinates(seaLevel, (GRID_SIZE // 2, GRID_SIZE // 2))

    for i in range(len(spiral_array)):
        the_color_array[spiral_array[i][0]][spiral_array[i][1]] = LAND

    the_state_array = state_array(color_array=the_color_array,
                                  caption=caption,
                                  text_color='black')
    the_state_array.show()


def generate_spiral_coordinates(length, center):
    return_coordinates = [(center)]
    land_count = 0

    for num in range(1, length):
        for row in range(-num + 1, num):
            if(land_count <= length):
                return_coordinates.append((center[0] + row, center[1] + num - abs(row)))
                return_coordinates.append((center[0] + row, center[1] - num + abs(row)))
                land_count += 2
        if (land_count <= length):
            return_coordinates.append((center[0] - num, center[1]))
            return_coordinates.append((center[0] + num, center[1]))
            land_count += 2
        else:
            break

    return return_coordinates



