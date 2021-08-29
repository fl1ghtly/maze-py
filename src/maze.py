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

# Returns a list of valid neighboring cell positions
def get_neighbor(cell, x_length, y_length):
    neighbor_cells = [(cell.x, cell.y - 1), # North
                        (cell.x, cell.y + 1), # South
                        (cell.x + 1, cell.y), # East
                        (cell.x - 1, cell.y)] # West

    cells = []
    for position in neighbor_cells:
        # Remove cell positions that are out of bounds
        if 0 <= position[0] < x_length and 0 <= position[1] < y_length:
            cells.append(position)
            
    return cells

def get_unvisited_cells(maze, cells):
    unvisited = []
    for pos in cells:
        c =  maze[pos[0]][pos[1]]
        if c.visited == False:
            unvisited.append(c)
    return unvisited            

def create_maze_wall(maze, x, y):
    stack = deque()
    start = maze[0][0]
    start.visited = True
    stack.append(start)

    while stack:
        cell = stack.pop()
        cell_neighbors = get_unvisited_cells(maze, get_neighbor(cell, x, y))
        if len(cell_neighbors) > 0:
            stack.append(cell)
            chosen = random.choice(cell_neighbors)
            cell.remove_wall(chosen)
            chosen.visited = True
            stack.append(chosen)

'''
Player Sprites:
    ˂ ˃˄ ˅
'''
def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))
    maze = make_empty_maze((x_length, y_length))
    create_maze_wall(maze, x_length, y_length)
    render = convert_maze_for_render(maze, x_length, y_length)
    render_maze(render)

if __name__ == "__main__":
    main()