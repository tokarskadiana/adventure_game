import os
import sys


class Game:

    def __init__(self):     # initialize a class variables
        self.board = []
        self.l_poss = 0
        self.w_poss = 0

    def game_board(self, lenght, width):    # make a game board
        for row in range(lenght):
            self.board.append([])
            for kolumn in range(width):
                if row == 0 or row == lenght - 1 or kolumn == 0 or kolumn == width - 1:
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

    def motion(self, n, z=False):   # make a player icon do not go out of board
        if z:
            if self.board[self.l_poss][self.w_poss + n] != 'x':
                self.board[self.l_poss][self.w_poss] = '.'
                self.w_poss = self.w_poss + n
                self.board[self.l_poss][self.w_poss] = '@'
            else:
                self.board[self.l_poss][self.w_poss] = '@'
        else:
            if self.board[self.l_poss + n][self.w_poss] != 'x':
                self.board[self.l_poss][self.w_poss] = '.'
                self.l_poss = self.l_poss + n
                self.board[self.l_poss][self.w_poss] = '@'
            else:
                self.board[self.l_poss][self.w_poss] = '@'

    def game_play(self):  # function of a gameplay, waiting for player input
        while True:
            os.system('clear')
            self.print_game_board(self.board)
            print('Use A (left), S (down), D (right) and W(up) to move.\nPress E to exit.')
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
                inp = input('\nDo you really want to exit? (Y/N) ').lower()
                if inp[0] == 'y':
                    break
                if inp[0] == 'n':
                    continue
            else:
                continue

    def welcome_screen(self):
        # import background / show: menu, credits, control panel
        while True:
            with open('welcomescreen.txt', newline='') as screenfile:
                welcome = screenfile.read()
                print('\033[36m\033[92m', welcome)
            start_input = input()
            if start_input == 'y':
                break
            if start_input == 'e':
                sys.exit()
            if start_input == 'c':
                self.credits_screen()
            else:
                continue

    def game_over_screen(self):
        # import background, and ask if u want to play again
        while True:
            os.system('clear')
            with open('gameover.txt', newline='') as game_over:
                over = game_over.read()
                print('\033[1m\033[91m', over)
            end_input = input()
            if end_input == 'y':
                Game().main()
            if end_input == 'n':
                os.system('clear')
                sys.exit()
            else:
                continue

    def credits_screen(self):
        # import background - with credits info
        while True:
            os.system('clear')
            with open('credits.txt', newline='') as credits:
                credits_page = credits.read()
                print('\033[1m\033[95m', credits_page)
            credits_input = input()
            if credits_input == 'b':
                Game().main()
            else:
                continue

    def win_screen(self):
        # import background - congratulations!
        while True:
            os.system('clear')
            with open('victoryscreen.txt', newline='') as vin:
                vin_page = vin.read()
                print('\033[1m\033[92m', vin_page)
            vin_input = input()
            if vin_input == 'y':
                Game().main()
            if vin_input == 'n':
                os.system('clear')
                sys.exit()
            else:
                continue

    def main(self):
        os.system('clear')
        self.welcome_screen()
        self.win_screen()
        # self.game_over_screen()  # trzeba ustawić kiedy ma się pojawić GAME OVER
        board = self.game_board(22, 80)
        self.insert_player(board)
        self.game_play()

Game().main()
