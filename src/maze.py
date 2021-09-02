from collections import deque
from svglib.svglib import svg2rlg
from player import Player
from cell import Cell
import random
import pygame
import io

def make_empty_maze(size):
    return [[Cell(x, y) for x in range(size[0])] for y in range(size[1])]

def load_svg(svg):
    drawing = svg2rlg(svg)
    byte = io.BytesIO(drawing.asString('png'))
    return pygame.image.load(byte)

def render_svg(maze):
    scale = 10
    width = len(maze[0]) * scale
    height = len(maze) * scale
    filename = 'maze.svg'
    with open(filename, 'w') as f:
        print('<?xml version="1.0" encoding="utf-8"?>', file=f)
        print(f'<svg width="{width}" height="{height}"', file=f)
        print(' xmlns="http://www.w3.org/2000/svg"', file=f)
        print(' xmlns:xlink="http://www.w3.org/1999/xlink">', file=f)
        
        for i, row in enumerate(maze):
            for j, c in enumerate(row):
                x, y = i * scale, j * scale
                stroke = "black"
                if c == 'W':
                    fill = "black"
                elif c == 'O':
                    fill = "white"
                elif c == 'P':
                    fill = 'yellow'
                else:
                    fill = "red"
                    
                print(f'<rect x="{x}" y="{y}" width="{scale}" height="{scale}" \
                        fill="{fill}" stroke="{stroke}" />', file=f)

        print('</svg>', file=f)
    return filename

# Prints out the maze based upon its cells
def render_text(maze, player):
    for row in maze:
        for c in row:
            if c == 'W':
                print('■', end='')
            elif c == 'O':
                print('.', end='')
            elif c == 'P':
                print(player.character, end='')
            else:
                print('#', end='')

        # Print new line for next row
        print()

# TODO possible optimization by only
# changing the player pos, not generating entire maze
def convert_maze_for_render(maze, x_length, y_length):
    render = [['W' for x in range(x_length * 2 + 1)] for y in range(y_length * 2 + 1)]
    for i, row in enumerate(maze):
        for c in row:
            if c.player_occupied == True:
                render[2 * c.x + 1][2 * c.y + 1] = 'P'
            elif c.start == True or c.finish == True:
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

def check_possible_move(player, direction, maze):
    pos_x = player.x
    pos_y = player.y
    if direction == 'N':
        pos_y = player.y - 1
    elif direction == 'S':
        pos_y = player.y + 1
    elif direction == 'W':
        pos_x = player.x - 1
    elif direction == 'E':
        pos_x = player.x + 1
    else:
        return False

    if maze[pos_y][pos_x].walls[direction] == False:
        return True
    else:
        return False

# Assumes the move is possible
def update_player_position(player, maze, command):
    maze[player.x][player.y].player_occupied = False
    if command == 'N':
        player.y -= 1
    elif command == 'S':
        player.y += 1
    elif command == 'W':
        player.x -= 1
    elif command == 'E':
        player.x += 1
        
    player.change_character(command)
    maze[player.y][player.x].player_occupied = True

def display_svg(screen, maze, x_length, y_length):
    render = convert_maze_for_render(maze, x_length, y_length)
    svg = render_svg(render)
    im = load_svg(svg)
    screen.blit(im, (0, 0))
    pygame.display.update()

# TODO make function that gets player input and outputs direction
def main():
    x_length = int(input("How wide should the maze be: "))
    y_length = int(input("How tall should the maze be: "))

    maze = make_empty_maze((x_length, y_length))
    maze[0][0].start = True
    maze[0][0].player_occupied = True
    maze[y_length - 1][x_length - 1].finish = True

    player = Player(0, 0)
    create_maze_wall(maze, x_length, y_length)
    '''
    render = convert_maze_for_render(maze, x_length, y_length)
    render_svg(render)
    '''
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    display_svg(screen, maze, x_length, y_length)
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    dir = 'N'
                elif e.key == pygame.K_DOWN:
                    dir = 'S'
                elif e.key == pygame.K_LEFT:
                    dir = 'W'
                elif e.key == pygame.K_RIGHT:
                    dir = 'E'
                else:
                    dir = None

                if check_possible_move(player, dir, maze):
                    update_player_position(player, maze, dir)
                    display_svg(screen, maze, x_length, y_length)
                    '''
                    render = convert_maze_for_render(maze, x_length, y_length)
                    svg = render_svg(render)
                    im = load_svg(svg)
                    pygame.Surface.blit(im)
                    '''
                
if __name__ == "__main__":
    main()