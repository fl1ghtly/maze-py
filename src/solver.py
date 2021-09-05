from collections import deque
import generator
import converter
import numpy as np

# Finds where the maze begins
def find_start(maze):
    for (x, y), cell in np.ndenumerate(maze):
        if cell == 'S':
            return x, y

# Returns a path from start to finish
def breadth_first_search(maze, start):
    queue = deque()
    visited = [start]
    queue.append([start])

    while queue:
        path = queue.pop()
        cell = path[-1]
        if maze[cell[0]][cell[1]] == 'F':
            return path

        neighbors = generator.get_adjacent(cell, len(maze[0]), len(maze))
        for neighbor in neighbors:
            if maze[neighbor[1]][neighbor[0]] != 'W':
                if neighbor not in visited:
                    visited.append(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        

def main(file):
    # Converts an SVG to a maze format
    maze_arr = converter.svg_to_array(file)

    np_maze = np.asarray(maze_arr)
    start = find_start(np_maze)
    path = breadth_first_search(np_maze, start)
    maze_solution = generator.draw_path(maze_arr, path)
    
    svg_map = {'W': 'black', 'O': 'white', 'F': 'red',
               'S': 'green', 'P': 'orange'}
    generator.render_svg(maze_solution, svg_map, 'solution.svg')

if __name__ == '__main__':
    main('maze.svg')