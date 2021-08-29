from collections import deque
from cell import Cell
import random

def make_empty_maze(size):
    return [[Cell(x, y) for x in range(size[0])] for y in range(size[1])]

# Prints out the maze based upon its cells
def render_maze(maze, character):
    for row in maze:
        for cell in row:
            cell_value = cell[1]
            # If cell can be entered print empty character
            if cell_value == 0:
                # TODO replace with better empty space character
                print(".", end='')
            # Prints wall if cell can not be entered
            elif cell_value == 1:
                print("■", end='')
            # Prints the player character
            else:
                print(character, end='')
        # Print new line for next row
        print()

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
    # TODO replace hardcoded character with one that changes
    # based on player's next position
    create_maze_wall(maze)
    render_maze(maze, '˄')

if __name__ == "__main__":
    main()