from collections import deque
from generator import get_adjacent
import converter
import numpy as np

def main(file):
    maze_arr = converter.svg_to_array(file)
    np_maze = np.asarray(maze_arr)
    start = find_start(np_maze)
    breadth_first_search(np_maze, start)

if __name__ == '__main__':
    main('maze.svg')