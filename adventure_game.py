import os
from collections import Counter


class Game:

    def __init__(self):     # initialize a class variables
        self.board = []
        self.l_poss = 0
        self.w_poss = 0
        self.item = ('l', 'f', 'c', 'k', 'p')
        self.lives = ['lives']*5
        self.food = []
        self.clothes = []
        self.weapons = []

    def game_board(self, lenght, width):    # make a game board
        for row in range(lenght):
            self.board.append([])
            for kolumn in range(width):
                if row == 0 or row == lenght-1 or kolumn == 0 or kolumn == width-1:
                    self.board[row].append('x')
                else:
                    self.board[row].append('.')
        return self.board

    def print_game_board(self, board):  # print game board
        for i in board:
            print(''.join(i))

    def insert_player(self, board):     # make a player icon and set a coordinates
        board[len(board) // 2][len(board[0]) // 2] = '@'
        n = 0
        for item in board:
            if '@' in item:
                self.l_poss = n
                self.w_poss = item.index('@')
            n += 1

    def getch(self):    # don't know what the f*king sh*t is this, but it works
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def catch_item(self, item):
        if item == 'l':
            self.lives.append('lives')
        elif item == 'f':
            self.food.append('food')
        elif item == 'c':
            self.clothes.append('clothes')
        elif item == 'k':
            self.weapons.append('weapons')
        elif item == 'p':
            del self.lives[-1]

    def print_items(self):
        a = (Counter(self.lives), Counter(self.food), Counter(self.clothes), Counter(self.weapons))
        for item in a:
            for key, value in item.items():
                print(key.capitalize(), ' - ', value)

    def motion(self, n, z=False):   # make a player icon do not do out of board
        if z:
            if self.board[self.l_poss][self.w_poss + n] in self.item:
                self.board[self.l_poss][self.w_poss] = '.'
                self.w_poss = self.w_poss + n
                item = self.board[self.l_poss][self.w_poss]
                self.catch_item(item)
                self.board[self.l_poss][self.w_poss] = '@'
            elif self.board[self.l_poss][self.w_poss + n] == 'x':
                self.board[self.l_poss][self.w_poss] = '@'
            else:
                self.board[self.l_poss][self.w_poss] = '.'
                self.w_poss = self.w_poss + n
                self.board[self.l_poss][self.w_poss] = '@'
        else:
            if self.board[self.l_poss + n][self.w_poss] in self.item:
                self.board[self.l_poss][self.w_poss] = '.'
                self.l_poss = self.l_poss + n
                item = self.board[self.l_poss][self.w_poss]
                self.catch_item(item)
                self.board[self.l_poss][self.w_poss] = '@'
            elif self.board[self.l_poss + n][self.w_poss] == 'x':
                self.board[self.l_poss][self.w_poss] = '@'
            else:
                self.board[self.l_poss][self.w_poss] = '.'
                self.l_poss = self.l_poss + n
                self.board[self.l_poss][self.w_poss] = '@'

    def game_play(self):  # function of a gameplay, waiting for player input
        while True:
            os.system('clear')
            self.print_game_board(self.board)
            print('Use A (left), S (down), D (right) and W(up) to move.\nPress E to exit.\n')
            self.print_items()
            player_input = self.getch().lower()
            if player_input == 'd':
                self.motion(1, True)
            elif player_input == 'a':
                self.motion(-1, True)
            elif player_input == 's':
                self.motion(1)
            elif player_input == 'w':
                self.motion(-1)
            elif player_input == 'e':
                inp = input('Do you really want to exit? (Y/N) ').lower()
                if inp[0] == 'y':
                    break
                if inp[0] == 'n':
                    continue
            else:
                continue

    def main(self):
        os.system('clear')
        board = self.game_board(22, 80)
        self.insert_player(board)
        self.game_play()

Game().main()
