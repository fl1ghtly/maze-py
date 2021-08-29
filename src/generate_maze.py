import numpy as np

def make_empty_maze(size):
    return np.full(size, True)

def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))
    maze = make_empty_maze((x_length, y_length))

if __name__ == "__main__":
    main()