from collections import deque
from cell import Cell
import random

# Returns a x by y array populated with cells
def make_empty_maze(size):
    return [[Cell(x, y) for x in range(size[0])] for y in range(size[1])]

# Uses a converted maze render to generate an svg
def render_svg(maze, map):
    scale = 10
    width = len(maze[0]) * scale
    height = len(maze) * scale
    
    filename = 'maze.svg'
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

# Prints out the maze based upon its cells
def render_text(maze):
    for row in maze:
        for c in row:
            if c == 'W':
                print('■', end='')
            elif c == 'O':
                print('.', end='')
            else:
                print('#', end='')

        # Print new line for next row
        print()

# Converts a maze to a new array that has 
# each cell be either a wall or a path
def convert_maze_for_render(maze, x_length, y_length):
    render = [['W' for x in range(x_length * 2 + 1)] for y in range(y_length * 2 + 1)]
    for i, row in enumerate(maze):
        for c in row:
            if c.start == True or c.finish == True:
                render[2 * c.x + 1][2 * c.y + 1] = 'F'
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

# Returns a list of uunvisited neighboring cells
def get_neighbor(cell, maze, x_length, y_length):
    neighbor_cells = [(cell.x, cell.y - 1), # North
                        (cell.x, cell.y + 1), # South
                        (cell.x + 1, cell.y), # East
                        (cell.x - 1, cell.y)] # West

    unvisited = []
    for position in neighbor_cells:
        # Remove cell positions that are out of bounds
        if 0 <= position[0] < x_length and 0 <= position[1] < y_length:
            c =  maze[position[1]][position[0]]
            # Only accept cells that are not visited
            if c.visited == False:
                unvisited.append(c)
    return unvisited         

# Recursive backtracking algorithm
def create_maze_wall(maze, x, y):
    stack = deque()
    start = maze[0][0]
    start.visited = True
    stack.append(start)
    while stack:
        cell = stack.pop()
        cell_neighbors = get_neighbor(cell, maze, x, y)
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
    svg_map = {'W': 'black', 'O': 'white', 'F': 'red'}
    render_svg(render, svg_map)

if __name__ == "__main__":
    main()