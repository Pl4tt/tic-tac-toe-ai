from ai import AI
from player import Player
from board import Board


while True:
    board = Board()

    symbol = int(input("Do you want to be X or O? [x=1, o=-1] "))

    if symbol != 1 and symbol != -1:
        print("Input must be 1 or -1")
        exit()

    player = Player(symbol)
    ai = AI(-symbol)
    currPlayer = player if symbol == 1 else ai

    while not board.is_full():
        board.print_board()

        if currPlayer == player:
            try:
                cell = int(input("Enter your next move {}: [0-8] ".format(currPlayer.player_symbol)))
                if not 0 <= cell <= 8:
                    raise ValueError
            except ValueError:
                print("Please enter a number between 0 and 8")
                continue
        else:
            cell = ai.next_move(board.board)

        if not board.valid_move(cell):
            print("Cell is not empty")
            continue

        board.add_cell(cell, currPlayer)

        if board.is_win(currPlayer):
            print("Congrats {}! You've won :)".format(currPlayer.player_symbol))
            break

        if currPlayer == player:
            currPlayer = ai
        else:
            currPlayer = player
    else:
        print("Draw!")

    board.print_board()
    game = input("Do you want to play again? [y/n] ")
    if game != "y":
        break