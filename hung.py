import random
import os
import time


def make_capitals(leng):
    capitals = []
    with open("capitals.txt", "r") as capital:
        for item in capital:
            if len(item) < leng:
                capitals.append(item.replace('\n', ''))
        capital.close()
        cap_name = list(random.choice(capitals))
    return cap_name


def make_dashes(capital):
    cap_name_output = []
    for letter in capital:
        if letter == ' ':
            cap_name_output.append('* ')
        else:
            cap_name_output.append('_ ')
    return cap_name_output


def introduce():
    os.system('clear')
    with open('skullface.txt', newline='') as boss:
        level = boss.read()
        print('\033[1m\033[91m{}\033[0m'.format(level))
        print(''''\n'To pass this level, you have to guess
the capital of European country
Have a try!!! Ha ha ha!''')
    time.sleep(4)
    os.system('clear')


def game(capital, dash, lives):
    not_in_word = []
    lives = sum(lives)
    while True:
        if not lives:
            return True
            break
        os.system("clear")
        with open('skullface.txt', newline='') as boss:
            level = boss.read()
            print('\033[1m\033[91m{}\033[0m'.format(level))
        print('You have {} attempts.'.format(lives))
        if not_in_word != []:
            print("Used letters: " + ', '.join(not_in_word))
        print('\n' + '\033[1m' + ''.join(dash) + '\033[0m' + '\n')
        if '_ ' in dash:
            inp = input('Type letter: ').upper()
            if inp not in capital and inp not in not_in_word and inp.isalpha() and len(inp) == 1:
                not_in_word.append(inp)
                lives -= 1
            for letter, i in enumerate(capital):
                if i == inp:
                    dash[letter] = inp
        else:
            os.system("clear")
            with open('skullface.txt', newline='') as boss:
                level = boss.read()
                print('\033[1m\033[91m{}\033[0m'.format(level))
            print('''ohhhh!! You did it!!
Next time I will win!!''')
            time.sleep(4)
            break


def hang(lives, leng):
    capital = make_capitals(leng)
    dash = make_dashes(capital)
    introduce()
    g = game(capital, dash, lives)
    if g:
        return True
