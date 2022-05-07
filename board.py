class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        elif sign == -1:
            return "0"

    def add_cell(self, cell, player):
        self.board[cell] = player.symbol

    def is_win(self, player):
        s = player.symbol
        if self.board[0] == self.board[4] == self.board[8] == s:
            return True
        elif self.board[2] == self.board[4] == self.board[6] == s:
            return True

        elif self.board[0] == self.board[1] == self.board[2] == s:
            return True
        elif self.board[3] == self.board[4] == self.board[5] == s:
            return True
        elif self.board[6] == self.board[7] == self.board[8] == s:
            return True

        elif self.board[0] == self.board[3] == self.board[6] == s:
            return True
        elif self.board[1] == self.board[4] == self.board[7] == s:
            return True
        elif self.board[2] == self.board[5] == self.board[8] == s:
            return True
        return False
    
    def is_full(self):
        if 0 in self.board:
            return False
        return True

    def valid_move(self, cell):
        if self.board[cell] == 0:
            return True
        return False

    def print_board(self):
        # 0 | 0 | 0
        # 0 | 0 | 0
        # 0 | 0 | 0

        print(" " + self.sign_to_printable(self.board[0]) + " | " + self.sign_to_printable(self.board[1]) + " | " + self.sign_to_printable(self.board[2]) +
        " \n " + self.sign_to_printable(self.board[3]) + " | " + self.sign_to_printable(self.board[4]) + " | " + self.sign_to_printable(self.board[5]) + " \n "
        + self.sign_to_printable(self.board[6]) + " | " + self.sign_to_printable(self.board[7]) + " | " + self.sign_to_printable(self.board[8]) + " \n")