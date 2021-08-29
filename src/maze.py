from collections import deque

def make_empty_maze(size):
    '''
    Each cell consists of
        Position
        Occupation Type
        Visit Status
    '''
    return [[[(x, y), 1, False] for x in range(size[0])] for y in range(size[1])]

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

# Returns a list of cell positions that have not been visited by the current cell
def check_neighbor_cells(current_cell, maze):
    unvisited_cells = []
    cell_position = current_cell[0]
    to_check = [(cell_position[0], cell_position[1] - 2), # North
                (cell_position[0], cell_position[1] + 2), # South
                (cell_position[0] + 2, cell_position[1]), # East
                (cell_position[0] - 2, cell_position[1])] # West

    for new_pos in to_check:
        # Negative values make the index wrap around
        if new_pos[0] >= 0 and new_pos[1] >= 0:
            try:
                new_cell = maze[new_pos[0]][new_pos[1]]
                if new_cell[2] == False:
                    unvisited_cells.append(new_cell[0])
            except IndexError:
                continue
    
    return unvisited_cells

def create_maze_wall(maze):
    stack = deque()
    start_cell = maze[0][0]
    stack.append(start_cell)
    visited = [start_cell]

    while stack:
        cell = stack.pop()
        if cell not in visited:
            pass

'''
Cell Values:
    0 = Walkable Space
    1 = Barrier
    2 = Player

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