import time

from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPLayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to rep 3x3 board
        self.current_winner = None  # keeps track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 e.t.c (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())  # or you could say self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. we have to check all these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check our diagonals
        # but only if the square is not even number [0, 2, 4, 6, 8]
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these check fail
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game! or none for tie
    if print_game:
        game.print_board_nums()

    letter = 'x'  # starting letter
    # iterate while the game still has empty squares
    # (we fo not have to worry about winner because we will just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('')  # just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'o' if letter == 'x' else 'x'  # switching players
        # tiny break
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('it is a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    # x_wins = 0
    # o_wins = 0
    # ties = 0
    # times = input("please enter how many times this game should be played: ")
    # for _ in range(int(times)):
    #     t = TicTacToe()
    #     result = play(t, x_player, o_player, print_game=True)
    #     if result == 'x':
    #         x_wins += 1
    #     elif result == 'o':
    #         o_wins += 1
    #     else:
    #         ties += 1
    # print(f'after {times} games, we see x won {x_wins} times and o won {o_wins} times ,and it is a tie {ties} ')


