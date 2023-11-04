class Game():
    def __init__(self, board, current_player):
        self.board = [[' ' for _ in range(3)]for _ in range (3)]
        #lista vazia cria o tabuleiro como uma matriz 3x3 ao longo do jogo
        self.current_player = "X"
    
    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            return True
        else:
            return False

    def make_move(self, row, col):
        if self.is_valid_move
#     def check_win(self):      #vai usar for in range p checar row e col e diagonais para o win
#     def switch_player(self):

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play(self, game):
        while True:
            try:
                row = int(input(f"{self.name}, enter row (0, 1 , 2): "))
                col = int(input(f"{self.name}, enter column (0, 1 , 2): "))
                if game.make_move(row, col):
                    break
                else:
                    print("Invalid move")
            except (ValueError, IndexError):
                    print("Invalid input")
    
    def turn(self):
        return self.symbol
    def board(self, game):
        return game.board

class Graphics: