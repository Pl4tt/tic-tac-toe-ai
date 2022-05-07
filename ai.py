from player import Player


class AI(Player):
    def winner(self, board):
        if board[0] == board[4] == board[8] and board[0] != 0:
            return board[0]
        elif board[2] == board[4] == board[6] and board[2] != 0:
            return board[2]

        elif board[0] == board[1] == board[2] and board[0] != 0:
            return board[0]
        elif board[3] == board[4] == board[5] and board[3] != 0:
            return board[3]
        elif board[6] == board[7] == board[8] and board[6] != 0:
            return board[6]

        elif board[0] == board[3] == board[6] and board[0] != 0:
            return board[0]
        elif board[1] == board[4] == board[7] and board[1] != 0:
            return board[1]
        elif board[2] == board[5] == board[8] and board[2] != 0:
            return board[2]

        return 0

    def valid_cells(self, board):
        cells = set()

        for cell in range(len(board)):
            if board[cell] == 0:
                cells.add(cell)

        return cells

    def set_cell(self, board, position, symbol):
        board[position] = symbol
        return board
    
    def max_value(self, board):
        cells = self.valid_cells(board)

        if not cells or self.winner(board) != 0:
            return self.winner(board)
        
        val = -float("inf")

        for cell in cells:
            val = max(val, self.min_value(self.set_cell(board, cell, 1)))
            self.set_cell(board, cell, 0)
        
        return val
    
    def min_value(self, board):
        cells = self.valid_cells(board)

        if not cells or self.winner(board) != 0:
            return self.winner(board)
        
        val = float("inf")

        for cell in cells:
            val = min(val, self.max_value(self.set_cell(board, cell, -1)))
            self.set_cell(board, cell, 0)
        
        return val

    def next_move(self, board):
        board = board[:]

        cells = self.valid_cells(board)

        if not cells:
            return None

        val = -self.symbol*float("inf")
        a = None

        for cell in cells:
            if self.symbol == 1:
                v = self.min_value(self.set_cell(board, cell, self.symbol))
            elif self.symbol == -1:
                v = self.max_value(self.set_cell(board, cell, self.symbol))
            
            self.set_cell(board, cell, 0)
            
            if v > val and self.symbol == 1 or v < val and self.symbol == -1:
                val = v
                a = cell
        
        return a