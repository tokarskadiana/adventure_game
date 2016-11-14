# while True:
# player = '@'
board = []
player = []
icon = '@'
def game_board(x, y):
    for row in range(x):
        board.append([])
        for kolumn in range(y):
            if row == 0 or row == x-1 or kolumn == 0 or kolumn == y-1:
                board[row].append('x')
            else:
                board[row].append('.')
    board[len(board) // 2][len(board[0]) // 2] = icon
    a = board[len(board) // 2][len(board[0]) // 2]
    x = 0
    for item in board:
        if a in item:
            player.append(item.index(icon))
            player.append(x)
        x+=1

    return board
def print_game_board(board):
    for i in board:
        print(''.join(i))

def motion():
    player_input = 's' #input('press the key to move: _')
    if player_input == 's':
        player[1] += 1
        a = board[player[0]][player[1]]
    return a


print_game_board(game_board(22,80))
# motion()
