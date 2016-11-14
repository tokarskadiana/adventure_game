while True:
    def game_board():
        board = [[@]]
        for row in range(x):
            board.append([])
            for kolumn in range(y):
                if row == 0 or row == x-1 or kolumn == 0 or kolumn == y-1:
                    board[row].append('x')
                else:
                    board[row].append('.')
        return board

    def print_game_board(board):
        for i in board:
            print(''.join(i))
