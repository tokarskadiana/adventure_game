import os
from collections import Counter
import sys
import random
from hung import hang
import time
from Hot_cold_warm import hot_cold


class Game:

    def __init__(self):     # initialize a class variables
        self.board = []
        self.l_poss = 0
        self.w_poss = 0
        self.obstacle = ('░', '🔷', '.', '/', "\\", '|', '-', '^', "'", '*')
        self.item = ('💜', '🍙', '👘', '🔰', '👿')
        self.lives = []
        self.food = []
        self.clothes = []
        self.weapons = []
        self.sum_items = [0, 0, 0]

    def game_board(self, lenght, width):    # make a game board
        for row in range(lenght):
            self.board.append([])
            for kolumn in range(width):
                if row == 0 or row == lenght - 1 or kolumn == 0 or kolumn == width - 1:
                    self.board[row].append('░')
                else:
                    self.board[row].append(' ')
        return self.board

    def random_item(self, board, item):  # set random position of items
        for z in range(10):
            for i in item:
                x = random.randint(0, (len(board) - 1))
                y = random.randint(0, (len(board[0]) - 1))
                if board[x][y] not in self.obstacle:
                    board[x][y] = i

    def item_number(self):
        f, w, c = 0, 0, 0
        for row in self.board:
            f += row.count('🍙')
            w += row.count('🔰')
            c += row.count('👘')
        return f, c, w

    def print_game_board(self, board, col):  # print game board
        for i in board:
            print('{}{}\033[0m'.format(col, ''.join(i)))

    def define_level(self, board, x, y, ran, z=False):
        if z:
            for i in range(ran):
                board[x][y] = '🔷'
                x += 1
        else:
            for i in range(ran):
                board[x][y] = '🔷'
                y += 1

    def level_1(self, board):  # set the obstacles
        self.define_level(board, 10, 10, 17)
        self.define_level(board, 5, 35, 10)
        self.define_level(board, 7, 66, 13)
        self.define_level(board, 11, 54, 9)
        self.define_level(board, 17, 62, 8)
        self.define_level(board, 13, 36, 8)
        self.define_level(board, 16, 36, 3)
        self.define_level(board, 16, 41, 3)
        self.define_level(board, 18, 3, 15)
        self.define_level(board, 2, 15, 8)
        self.define_level(board, 3, 15, 8)
        self.define_level(board, 4, 15, 8)
        self.define_level(board, 1, 63, 5, True)
        self.define_level(board, 3, 40, 5, True)
        self.define_level(board, 5, 9, 6, True)
        self.define_level(board, 11, 62, 7, True)
        self.define_level(board, 14, 36, 3, True)
        self.define_level(board, 14, 43, 3, True)
        self.define_level(board, 16, 17, 2, True)

    def level_2(self, board):  # obstacles on lvl2
        self.define_level(board, 5, 10, 69)
        self.define_level(board, 6, 10, 69)
        self.define_level(board, 11, 1, 69)
        self.define_level(board, 12, 1, 69)
        self.define_level(board, 17, 10, 69)
        self.define_level(board, 14, 11, 4, True)
        self.define_level(board, 14, 10, 4, True)
        self.define_level(board, 13, 5, 7, True)
        self.define_level(board, 13, 6, 6, True)
        self.define_level(board, 19, 60, 2, True)
        self.define_level(board, 19, 61, 2, True)
        self.define_level(board, 18, 39, 2, True)
        self.define_level(board, 18, 38, 2, True)
        self.define_level(board, 1, 39, 2, True)
        self.define_level(board, 1, 38, 2, True)
        self.define_level(board, 4, 38, 2, True)
        self.define_level(board, 4, 39, 2, True)
        self.define_level(board, 2, 10, 3, True)
        self.define_level(board, 2, 11, 3, True)
        self.define_level(board, 7, 12, 3, True)
        self.define_level(board, 7, 13, 3, True)
        self.define_level(board, 8, 22, 3, True)
        self.define_level(board, 8, 23, 3, True)
        self.define_level(board, 7, 42, 3, True)
        self.define_level(board, 7, 43, 3, True)
        self.define_level(board, 8, 73, 9, True)
        self.define_level(board, 8, 74, 9, True)

    def level_3(self, board):   # obstacles on lvl3
        self.define_level(board, 1, 19, 13, True)
        self.define_level(board, 1, 21, 13, True)
        self.define_level(board, 1, 20, 13, True)
        self.define_level(board, 16, 19, 5, True)
        self.define_level(board, 16, 21, 5, True)
        self.define_level(board, 16, 20, 5, True)
        self.define_level(board, 5, 32, 37)
        self.define_level(board, 16, 32, 45)
        self.define_level(board, 6, 32, 8, True)
        self.define_level(board, 6, 33, 8, True)
        self.define_level(board, 6, 68, 8, True)
        self.define_level(board, 6, 67, 8, True)
        self.define_level(board, 8, 52, 8, True)
        self.define_level(board, 8, 51, 8, True)

    def boss_appear(self, board):  # set position of boss on lvl3 map
        boss = [['.', '^', '-', '^', '.'],
                ['|', 'o', ',', 'o', '|'],
                ['\ ', ' ', ' ', '', '/'],
                ["'", '*', '*', '*', "'"]]
        i = 0
        x = 2
        for num in range(5):
            board[10][x] = boss[0][i]
            x += 1
            i += 1
        i = 0
        x = 2
        for num in range(5):
            board[11][x] = boss[1][i]
            x += 1
            i += 1
        i = 0
        x = 2
        for num in range(5):
            board[12][x] = boss[2][i]
            x += 1
            i += 1
        i = 0
        x = 2
        for num in range(5):
            board[13][x] = boss[3][i]
            x += 1
            i += 1

    def insert_player(self, board, level):     # make a player icon and set a coordinates
        if level == 1:
            board[len(board) // 2][len(board[0]) // 2 - 1] = '🐼'
        if level == 2:
            board[2][-7] = '🐼'
        if level == 3:
            board[10][-5] = '🐼'
        n = 0
        for item in board:
            if '🐼' in item:
                self.l_poss = n
                self.w_poss = item.index('🐼')
            n += 1

    def getch(self):    # don't know what is this, but it works
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

    def catch_item(self, item):  # adds collected items to lists
        if item == '💜':
            self.lives.append('lives 💜')
        elif item == '🍙':
            self.food.append('food 🍙')
        elif item == '👘':
            self.clothes.append('clothes 👘')
        elif item == '🔰':
            self.weapons.append('weapons 🔰')
        elif item == '👿':
            if self.lives:
                del self.lives[-1]

    def print_items(self):  # print collected items on game screen
        a = (Counter(self.lives), Counter(self.food), Counter(self.clothes), Counter(self.weapons))
        for item in a:
            for key, value in item.items():
                print(key.capitalize(), ' - ', value)

    def motion(self, n, z=False):   # make a player icon do not go out of board
        if z:
            if self.board[self.l_poss][self.w_poss + n] in self.item:
                self.board[self.l_poss][self.w_poss] = ' '
                self.w_poss = self.w_poss + n
                item = self.board[self.l_poss][self.w_poss]
                self.catch_item(item)
                self.board[self.l_poss][self.w_poss] = '🐼'
            elif self.board[self.l_poss][self.w_poss + n] in self.obstacle:
                self.board[self.l_poss][self.w_poss] = '🐼'
            else:
                self.board[self.l_poss][self.w_poss] = ' '
                self.w_poss = self.w_poss + n
                self.board[self.l_poss][self.w_poss] = '🐼'
        else:
            if self.board[self.l_poss + n][self.w_poss] in self.item:
                self.board[self.l_poss][self.w_poss] = ' '
                self.l_poss = self.l_poss + n
                item = self.board[self.l_poss][self.w_poss]
                self.catch_item(item)
                self.board[self.l_poss][self.w_poss] = '🐼'
            elif self.board[self.l_poss + n][self.w_poss] in self.obstacle:
                self.board[self.l_poss][self.w_poss] = '🐼'
            else:
                self.board[self.l_poss][self.w_poss] = ' '
                self.l_poss = self.l_poss + n
                self.board[self.l_poss][self.w_poss] = '🐼'

    def game_play(self, col):  # function of a gameplay, waiting for player input
        while True:
            bs = ('.', '/', '|', '-', '^', "'", '*')
            os.system('clear')
            if not self.lives:
                self.game_over_screen()
                break
            i_n = self.item_number()
            if sum(i_n) == 0:
                self.sum_items[0] += len(self.food)
                self.sum_items[1] += len(self.clothes)
                self.sum_items[2] += len(self.weapons)
                break
            if self.board[self.l_poss][self.w_poss - 1] in bs:
                break
            elif self.board[self.l_poss][self.w_poss + 1] in bs:
                break
            elif self.board[self.l_poss - 1][self.w_poss] in bs:
                break
            elif self.board[self.l_poss + 1][self.w_poss] in bs:
                break
            self.print_game_board(self.board, col)
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
                    os.system('clear')
                    sys.exit()
                else:
                    continue
            else:
                continue

    def welcome_screen(self):  # import background / show: menu, credits, control panel
        os.system('clear')
        with open('panda.txt', newline='') as screenfile:
            panda = screenfile.read()
            print('{}'.format(panda))
            time.sleep(6)
            screenfile.close()
            os.system('clear')
        while True:
            with open('welcomescreen.txt', newline='') as screenfile:
                welcome = screenfile.read()
                print('\033[36m\033[92m{}\033[0m'.format(welcome))
            start_input = input()
            if start_input == 'y':
                os.system('clear')
                with open('level1.txt', newline='') as level_1:
                    level = level_1.read()
                    print('\033[1m\033[95m{}\033[0m'.format(level))
                    time.sleep(3)
                    os.system('clear')
                break
            if start_input == 'e':
                sys.exit()
            if start_input == 'c':
                self.credits_screen()
                break
            else:
                os.system('clear')
                continue

    def game_over_screen(self):  # show game over screen (imported from file)
        while True:
            self.sum_items = [0, 0, 0]
            os.system('clear')
            with open('gameover.txt', newline='') as game_over:
                over = game_over.read()
                print('\033[1m\033[91m{}\033[0m'.format(over))
            end_input = input()
            if end_input == 'y':
                self.main()
                break
            if end_input == 'n':
                os.system('clear')
                sys.exit()
            else:
                continue

    def credits_screen(self):  # show credits screen (imported from file)
        while True:
            os.system('clear')
            with open('credits.txt', newline='') as credits:
                credits_page = credits.read()
                print('\033[1m\033[95m{}\033[0m'.format(credits_page))
            credits_input = input()
            if credits_input == 'b':
                self.main()
                break
            else:
                continue

    def win_screen(self):  # show win screen (imported from file)
        while True:
            os.system('clear')
            with open('victoryscreen.txt', newline='') as vin:
                vin_page = vin.read()
                print('\033[1m\033[92m{}\033[0m'.format(vin_page))
            vin_input = input()
            if vin_input == 'y':
                self.main()
            if vin_input == 'n':
                os.system('clear')
                sys.exit()
            else:
                continue

    def reset(self):  # reset the lists, variables, and dictionary to play again the game
        dic = vars(self)
        no_edit = ['obstacle', 'item', 'lives', 'sum_items']
        to_zero = ['l_poss', 'w_poss']
        for i in dic.keys():
            if i in to_zero:
                dic[i] = 0
            if i not in no_edit and i not in to_zero:
                dic[i] = []

    def level(self, level):  # set the levels, insert a player, and change colors of map
        self.reset()
        board = self.game_board(22, 80)
        self.random_item(board, self.item)
        if level == 1:
            self.level_1(board)
            self.insert_player(board, 1)
            self.game_play('\33[96m')
        if level == 2:
            self.level_2(board)
            self.insert_player(board, 2)
            self.game_play('\33[93m')
        if level == 3:
            self.level_3(board)
            self.boss_appear(self.board)
            self.insert_player(board, 3)
            self.game_play('\33[91m')

    def level_2_screen(self):  # print level info screen (import from file)
        os.system('clear')
        with open('level2.txt', newline='') as level_2:
            level = level_2.read()
            print('\033[1m\033[95m{}\033[0m'.format(level))
        time.sleep(3)
        os.system('clear')

    def level_3_screen(self):  # print level info screen (import from file)
        os.system('clear')
        with open('level3.txt', newline='') as level_3:
            level = level_3.read()
            print('\033[1m\033[95m{}\033[0m'.format(level))
        time.sleep(3)
        os.system('clear')

    def main(self):
        self.reset()
        os.system('clear')
        self.lives = ['lives 💜'] * 5
        self.welcome_screen()
        self.level(1)
        self.level_2_screen()
        self.level(2)
        t = hang(self.sum_items)
        if t:
            self.game_over_screen()
        self.level_3_screen()
        self.level(3)
        a = hot_cold(len(self.lives))
        if a:
            self.game_over_screen()
        self.win_screen()

    if __name__ == 'main':
        self.main()

Game().main()
