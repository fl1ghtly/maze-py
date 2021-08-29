import numpy as np

def make_empty_maze(size):
    return np.full(size, True)

# Prints out the maze based upon its cells
def render_maze(maze):
    for row in maze:
        for cell in row:
            # If cell can be entered print empty character
            if cell:
                # TODO replace with better empty space character
                print(".", end='')
            # Prints wall if cell can not be entered
            else:
                print("■", end='')
        # Print new line for next row
        print()

def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))
    maze = make_empty_maze((x_length, y_length))
    render_maze(maze)

if __name__ == "__main__":
    main()