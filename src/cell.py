class Cell:
    pairings = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'} 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {'N': True, 'S': True, 'W': True, 'E': True}

    def remove_wall(self, direction, other_cell):
        self.walls[direction] = False
        other_cell.walls[Cell.pairings[direction]] = False