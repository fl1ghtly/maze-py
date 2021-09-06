class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.position = (x, y)

    def update_position(self, dx, dy):
        self.x += dx
        self.y += dy
        self.position = (self.x, self.y)