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
