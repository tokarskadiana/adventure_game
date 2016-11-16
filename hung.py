import random
import os


def make_capitals():
    capitals = []
    with open("capitals.txt", "r") as capital:
        for item in capital:
            if len(item) < 7:
                capitals.append(item.replace('\n', ''))
        capital.close()
        cap_name = list(random.choice(capitals))
    return cap_name


def make_dashes(capital):
    cap_name_output = []
    for letter in capital:
        cap_name_output.append('_ ')
    return cap_name_output


def game(capital, dash):
    not_in_word = []
    while True:
        os.system("clear")
        print(capital)
        if not_in_word != []:
            print("Used letters: " + ', '.join(not_in_word))
        print('\n' + '\033[1m' + ''.join(dash) + '\033[0m' + '\n')
        if '_ ' in dash:
            inp = input('Type letter: ').upper()
            if inp not in capital and inp not in not_in_word and inp.isalpha() and len(inp) == 1:
                not_in_word.append(inp)
            for letter, i in enumerate(capital):
                if i == inp:
                    dash[letter] = inp
        else:
            break


def hang():
    capital = make_capitals()
    dash = make_dashes(capital)
    game(capital, dash)
