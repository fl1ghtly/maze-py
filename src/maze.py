from collections import deque
from cell import Cell
import random

def make_empty_maze(size):
    return [[Cell(x, y) for x in range(size[0])] for y in range(size[1])]

# Prints out the maze based upon its cells
def render_maze(maze):
    for row in maze:
        for c in row:
            if c == 'W':
                print('■', end='')
            else:
                print('.', end='')
        # Print new line for next row
        print()

def convert_maze_for_render(maze, x_length, y_length):
    render = [['W' for x in range(x_length * 2 + 1)] for y in range(y_length * 2 + 1)]
    for i, row in enumerate(maze):
        for c in row:
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

# Returns a list of valid neighboring cells
def get_neighbor(cell, x_length, y_length):
    neighbor_cells = [(cell.x, cell.y - 1), # North
                        (cell.x, cell.y + 1), # South
                        (cell.x + 1, cell.y), # East
                        (cell.x - 1, cell.y)] # West

    for position in neighbor_cells:
        # Remove cell positions that are out of bounds
        if not (0 < position[0] < x_length or 0 < position[1] < y_length):
            neighbor_cells.remove(position)
            
    return neighbor_cells


def create_maze_wall(maze):
    pass

'''
Player Sprites:
    ˂ ˃˄ ˅
'''
def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))
    maze = make_empty_maze((x_length, y_length))
    create_maze_wall(maze)
    render = convert_maze_for_render(maze, x_length, y_length)
    render_maze(render)

if __name__ == "__main__":
    main()