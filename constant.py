import pandas as np


WINDOW_WIDTH = 7 * 100
WINDOW_HEIGHT = 6 * 100

TILE_SIZE = 100

Maze = np.array([
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 2, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 3, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ])