import numpy as np

def make_empty_maze(size):
    return [[[(x, y), 1] for x in range(size[0])] for y in range(size[1])]

# Prints out the maze based upon its cells
def render_maze(maze, character):
    for row in maze:
        for cell in row:
            # If cell can be entered print empty character
            cell_value = cell[1]
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

'''
Cell Values:
    None = Walkable Space
    False = Barrier
    True = Player

Player Sprites:
    ˂ ˃˄ ˅

'''
def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))
    maze = make_empty_maze((x_length, y_length))
    # TODO replace hardcoded character with one that changes
    # based on player's next position
    render_maze(maze, '˄')

if __name__ == "__main__":
    main()