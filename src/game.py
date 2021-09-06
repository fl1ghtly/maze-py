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

