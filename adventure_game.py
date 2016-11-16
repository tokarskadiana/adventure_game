import os
from collections import Counter
import sys
import random


class Game:

    def __init__(self):     # initialize a class variables
        self.board = []
        self.l_poss = 0
        self.w_poss = 0
        self.obstacle = ('x', '#')
        self.item = ('l', 'f', 'c', 'k', 'p')
        self.lives = ['lives'] * 5
        self.food = []
        self.clothes = []
        self.weapons = []

    def game_board(self, lenght, width):    # make a game board
        for row in range(lenght):
            self.board.append([])
            for kolumn in range(width):
                if row == 0 or row == lenght - 1 or kolumn == 0 or kolumn == width - 1:
                    self.board[row].append('x')
                else:
                    self.board[row].append('.')
        return self.board

    def random_item(self, board, item):
        for row in board:
            for i in item:
                if board[random.randrange(len(board))][random.randrange(0, len(row), 4)] in self.obstacle:
                    board[random.randrange(len(board))][random.randrange(0, len(row), 4)] = i

    def print_game_board(self, board):  # print game board
        for i in board:
            print(''.join(i))

    def define_level(self, board, x, y, ran, z=False):
        if z:
            for i in range(ran):  # lewy hak poziomy
                board[x][y] = '#'
                x += 1
        else:
            for i in range(ran):  # lewy hak poziomy
                board[x][y] = '#'
                y += 1

    def level_1(self, board):
        self.define_level(board, 10, 10, 17)

    # self.level
    #     z = 10
    #     for i in range(17):  # lewy hak poziomy
    #         board[10][z] = '#'
    #         z += 1
    #     z = 35
    #     for i in range(10):  # poziomy krzyz
    #         board[5][z] = '#'
    #         z += 1
    #     z = 66
    #     for i in range(13):  # prawy kat (poziomy)
    #         board[7][z] = '#'
    #         z += 1
    #     z = 54
    #     for i in range(9):  # poziomy krzyz
    #         board[11][z] = '#'
    #         z += 1
    #     z = 62
    #     for i in range(8):  # poziomy krzyz
    #         board[17][z] = '#'
    #         z += 1
    #     z = 36
    #     for i in range(8):  # poziomy wejscie
    #         board[13][z] = '#'
    #         z += 1
    #     z = 36
    #     for i in range(3):  # poziomy wejscie
    #         board[16][z] = '#'
    #         z += 1
    #     z = 41
    #     for i in range(3):  # poziomy wejscie
    #         board[16][z] = '#'
    #         z += 1
    #     z = 3
    #     for i in range(15):  # lewy dol
    #         board[18][z] = '#'
    #         z += 1
    #     z = 15
    #     for i in range(8):  # gorny rog
    #         board[2][z] = '#'
    #         z += 1
    #     z = 15
    #     for i in range(8):  # gorny rog
    #         board[3][z] = '#'
    #         z += 1
    #     z = 15
    #     for i in range(8):  # gorny rog
    #         board[4][z] = '#'
    #         z += 1
    #     z = 1
    #     for i in range(5):      # prawy pionowy gorny
    #         board[z][63] = '#'
    #         z += 1
    #     z = 3
    #     for i in range(5):      # krzyz gorny
    #         board[z][40] = '#'
    #         z += 1
    #     z = 5
    #     for i in range(6):      # krzyz gorny
    #         board[z][9] = '#'
    #         z += 1
    #     z = 11
    #     for i in range(7):      # krzyz gorny
    #         board[z][62] = '#'
    #         z += 1
    #     z = 14
    #     for i in range(3):      # krzyz gorny
    #         board[z][36] = '#'
    #         z += 1
    #     z = 14
    #     for i in range(3):      # krzyz gorny
    #         board[z][43] = '#'
    #         z += 1
    #     z = 16
    #     for i in range(2):      # krzyz gorny
    #         board[z][17] = '#'
    #         z += 1
    #     return board

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
            if self.lives:
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
            elif self.board[self.l_poss][self.w_poss + n] in self.obstacle:
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
            elif self.board[self.l_poss + n][self.w_poss] in self.obstacle:
                self.board[self.l_poss][self.w_poss] = '@'
            else:
                self.board[self.l_poss][self.w_poss] = '.'
                self.l_poss = self.l_poss + n
                self.board[self.l_poss][self.w_poss] = '@'

    def game_play(self):  # function of a gameplay, waiting for player input
        while True:
            os.system('clear')
            if not self.lives:
                print('You lose!!!')
                sys.exit()
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
                if not inp or inp[0] == 'y':
                    break
                if inp[0] == 'n':
                    continue
            else:
                continue

    def main(self):
        os.system('clear')
        board = self.game_board(22, 80)
        self.random_item(board, self.item)
        self.insert_player(board)
        self.game_play()
print(":)")
Game().main()
