from collections import deque
from cell import Cell
import random


def make_empty_maze(size):
    # Returns a x by y array populated with cells
    return [[Cell(x, y) for x in range(size[0])] for y in range(size[1])]


def render_svg(maze, map, filename):
    # Uses a converted maze render to generate an svg
    scale = 10
    width = len(maze[0]) * scale
    height = len(maze) * scale

    with open(filename, 'w') as f:
        print('<?xml version="1.0" encoding="utf-8"?>', file=f)
        print(f'<svg width="{width}" height="{height}"', file=f)
        print(' xmlns="http://www.w3.org/2000/svg"', file=f)
        print(' xmlns:xlink="http://www.w3.org/1999/xlink">', file=f)

        stroke = "black"
        for i, row in enumerate(maze):
            for j, c in enumerate(row):
                x, y = i * scale, j * scale
                fill = map[c]
                print(f'<rect x="{x}" y="{y}" width="{scale}" height="{scale}" \
                        fill="{fill}" stroke="{stroke}" />', file=f)

        print('</svg>', file=f)


def convert_maze_for_render(maze, x_length, y_length):
    # Converts a maze to a new array that has
    # each cell be either a wall or a path
    render = [['W' for x in range(x_length * 2 + 1)]
              for y in range(y_length * 2 + 1)]
    for i, row in enumerate(maze):
        for c in row:
            # TODO must be a better way to refactor this
            if c.start == True:
                render[2 * c.x + 1][2 * c.y + 1] = 'S'
            elif c.finish == True:
                render[2 * c.x + 1][2 * c.y + 1] = 'F'
            elif c.path == True:
                render[2 * c.x + 1][2 * c.y + 1] = 'P'
            else:
                render[2 * c.x + 1][2 * c.y + 1] = 'O'

            if c.walls['E'] == True:
                render[2 * (c.x + 1)][2 * c.y + 1] = 'W'
            else:
                render[2 * (c.x + 1)][2 * c.y + 1] = 'O'

            if c.walls['S'] == True:
                render[2 * c.x + 1][2 * (c.y + 1)] = 'W'
            else:
                render[2 * c.x + 1][2 * (c.y + 1)] = 'O'
    return render


def draw_path(maze, path):
    # Returns a maze with a solution path
    for point in path:
        maze[point[1]][point[0]] = 'P'

    return maze


def get_neighbor(cell=None, position=None):
    # Returns a list of neighboring cells
    # Must be either a cell object or a tuple
    if cell:
        neighbor_cells = [(cell.x, cell.y - 1),  # North
                          (cell.x, cell.y + 1),  # South
                          (cell.x + 1, cell.y),  # East
                          (cell.x - 1, cell.y)]  # West
    elif position:
        neighbor_cells = [(position[0], position[1] - 1),  # North
                          (position[0], position[1] + 1),  # South
                          (position[0] + 1, position[1]),  # East
                          (position[0] - 1, position[1])]  # West
    else:
        raise ValueError("Cell or position argument is required")

    return neighbor_cells


def get_adjacent(cell, x_length, y_length):
    # Returns a list of tuples defining position
    if isinstance(cell, Cell):
        neighbors = get_neighbor(cell)
    else:
        neighbors = get_neighbor(position=cell)

    adjacent = []
    for position in neighbors:
        # Remove cell positions that are out of bounds
        if 0 <= position[0] < x_length and 0 <= position[1] < y_length:
            adjacent.append(position)
    return adjacent


def get_unvisited(cell, maze, x_length, y_length):
    # Returns a list of unvisited neighbors
    adjacent = get_adjacent(cell, x_length, y_length)
    unvisited = []
    for position in adjacent:
        c = maze[position[1]][position[0]]
        # Only accept cells that are not visited
        if c.visited == False:
            unvisited.append(c)
    return unvisited


def create_maze_wall(maze, x, y):
    # Recursive backtracking algorithm
    stack = deque()
    start = maze[0][0]
    start.visited = True
    stack.append(start)
    while stack:
        cell = stack.pop()
        cell_neighbors = get_unvisited(cell, maze, x, y)
        if len(cell_neighbors) > 0:
            stack.append(cell)
            chosen = random.choice(cell_neighbors)
            cell.remove_wall(chosen)
            chosen.visited = True
            stack.append(chosen)


def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))

    # Create a maze
    maze = make_empty_maze((x_length, y_length))
    create_maze_wall(maze, x_length, y_length)

    # Set Starting and ending points
    maze[0][0].start = True
    maze[y_length - 1][x_length - 1].finish = True

    # Renders the final maze
    render = convert_maze_for_render(maze, x_length, y_length)
    svg_map = {'W': 'black', 'O': 'white', 'F': 'red',
               'S': 'green', 'P': 'orange'}
    render_svg(render, svg_map, 'maze.svg')


if __name__ == "__main__":
    main()
