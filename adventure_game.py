# while True:
def game_board(x, y):
    board = []
    for row in range(x):
        board.append([])
        for kolumn in range(y):
            if row == 0 or row == x-1 or kolumn == 0 or kolumn == y-1:
                board[row].append('x')
            else:
                board[row].append('.')
    board[len(board) // 2][len(board[0]) // 2] = '@'
    
    return board


def print_game_board(board):
    for i in board:
        print(''.join(i))

print_game_board(game_board(22, 80))
