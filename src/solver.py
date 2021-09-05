from collections import deque
from generator import get_adjacent
import converter
import numpy as np

def find_start(maze):
    for (x, y), cell in np.ndenumerate(maze):
        if cell == 'S':
            return x, y

def breadth_first_search(maze, start):
    queue = deque()
    visited = [start]
    queue.append(start)

    while queue:
        cell = queue.pop()
        if maze[cell[0]][cell[1]] == 'F':
            return cell

        neighbors = get_adjacent(cell, len(maze[0]), len(maze))
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
        

def main(file):
    maze_arr = converter.svg_to_array(file)
    np_maze = np.asarray(maze_arr)
    start = find_start(np_maze)
    breadth_first_search(np_maze, start)

if __name__ == '__main__':
    main('maze.svg')