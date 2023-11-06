class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play(self, game):
        while True:
            try:
                row, col = map(int, input(f'{self.name}, enter row and column (e.g., 0 1): ').split())
                if game.make_move(row, col):
                    break
                else:
                    print('Invalid move. Try again.')
            except (ValueError, IndexError):
                print('Invalid input. Try again.')

    def turn(self):
        return self.symbol

    def board(self, game):
        return game.board


class Graphics:
    @staticmethod
    def display_board(board):
        for row in board:
            print(' | '.join(row))
            print('---------')

def main():
    game = Game()
    player1 = Player("Player 1", 'X')
    player2 = Player("Player 2", 'O')

    while True:
        Graphics.display_board(game.board)
        current_player = player1 if game.current_player == 'X' else player2
        current_player.play(game)

        if game.check_win():
            Graphics.display_board(game.board)
            print(f'{current_player.name} wins!')
            break
        if all(' ' not in row for row in game.board):
            Graphics.display_board(game.board)
            print("It's a draw!")
            break

        game.switch_player()

if __name__ == "__main__":
    main()
