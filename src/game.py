from player import Player
from solver import find_start
from generator import render_svg
from copy import deepcopy
import converter
import pygame


def check_possible_move(maze: list, position: tuple):
    '''
    Using the position to move to, it checks if the move 
    is possible

    maze -- array of cells
    position -- the move to be performed
    '''
    # TODO replace 'W' with enums for all scripts
    if maze[position[0]][position[1]] == 'W':
        return False
    else:
        return True


def get_new_position(current_pos: tuple, dx: int, dy: int):
    '''
    Returns the new position given a change in x and y

    current_pos -- position of the player
    dx -- change in x position
    dy -- change in y position
    '''

    return (current_pos[0] + dx, current_pos[1] + dy)


def get_move(event):
    '''
    Returns a change in position if the event is a
    valid key to move. Returns none if it is not

    event -- pygame event
    '''
    if event.key == pygame.K_UP:
        dx, dy = 0, -1
    elif event.key == pygame.K_DOWN:
        dx, dy = 0, 1
    elif event.key == pygame.K_LEFT:
        dx, dy = -1, 0
    elif event.key == pygame.K_RIGHT:
        dx, dy = 1, 0
    else:
        dx, dy = None, None

    return dx, dy


def add_player_to_maze(maze:list, p: Player):
    '''
    Returns a new deepcopy of a maze that has the 
    player added to a cell

    maze -- array of cells
    p -- player object
    '''
    player_maze = deepcopy(maze)
    player_maze[p.x][p.y] = 'C'
    return player_maze

    
def update_display(screen, maze: list, player: Player):
    '''
    Updates the game's display

    screen -- pygame screen
    maze -- array of cells
    player -- player object
    '''
    filename = 'temp.svg'
    new_maze = add_player_to_maze(maze, player)
    render_svg(new_maze, filename)
    buff = converter.convert_svg(filename)
    im = pygame.image.load(buff)
    screen.blit(im, (0, 0))
    pygame.display.update()


def main(maze_file):
    '''
    Runs the maze game
    '''
    maze_arr = converter.svg_to_array(maze_file)
    size = len(maze_arr[0]) * 10 , len(maze_arr) * 10
    start_x, start_y = find_start(maze_arr)
    player = Player(start_x, start_y)

    pygame.init()
    screen = pygame.display.set_mode(size)

    update_display(screen, maze_arr, player)
    running = True
    while running:
        for e in pygame.event.get():
            dx, dy = None, None
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                dx, dy = get_move(e)
                
            if dx is not None and dy is not None:
                new_pos = get_new_position(player.position, dx, dy)
                if check_possible_move(maze_arr, new_pos):
                    player.update_position(dx, dy)
                    update_display(screen, maze_arr, player)


if __name__ == '__main__':
    main('maze.svg')