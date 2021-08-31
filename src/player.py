class Player:
    player_direction = {'N': '˄', 'S': '˅', 'E': '˃', 'W': '˂'}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.character = Player.player_direction['N']

    def change_character(self, direction):
        self.character = Player.player_direction[direction]