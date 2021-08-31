class Cell:
    pairings = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'} 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.start = False
        self.finish = False
        self.player_occupied = False
        self.walls = {'N': True, 'S': True, 'W': True, 'E': True}
        
    # Removes the wall between two cells
    def remove_wall(self, other):
        delta = (other.x - self.x, other.y - self.y)
        if delta == (0, -1):
            direction = 'N'
        elif delta == (0, 1):
            direction = 'S'
        elif delta == (-1, 0):
            direction = 'W'
        else:
            direction = 'E'
            
        self.walls[direction] = False
        other.walls[Cell.pairings[direction]] = False