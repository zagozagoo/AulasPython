class Game:
    def __init__(self, board, current_player):
        self.board = [[' ' for _ in range (3)]for _ in range (3)]
        self.current_player = "X"

    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board == ' ':
            return True
        else:
            return False

    def make_move(self, row, col):
        if self.is_valid_move(row,col):
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def check_win(self):
        for i in range (3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                return True
            else:
                return False
    
    def switch_player(self):
        self.current_player = "0" if self.current_player == "X" else "X"

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def play(self, game):
        while True:
            try:
                row = int(input(f"{self.name} enter row (0, 1, 2): "))

                if game.make_move(row, col):
                    break
