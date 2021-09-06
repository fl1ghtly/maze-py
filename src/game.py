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


