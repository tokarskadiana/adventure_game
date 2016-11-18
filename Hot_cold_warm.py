import random
import os
import time

x = []
i = 0
items = 0


def random_input():
    while len(x) < 3:
        number = random.choice(list(range(0, 10)))
        if number not in x:
            x.append(number)
        else:
            pass
    random_num = str(x[0]) + str(x[1]) + str(x[2])
    random_num = str(random_num)
    return random_num


def introduce():
    os.system('clear')
    with open('skullface.txt', newline='') as boss:
        level = boss.read()
        print('\033[1m\033[91m{}'.format(level))
        print('\033[91m''''Welcome back!!
This time I have a new game for you...
Hot-Warm-Cold -> i think about 3-digit number
Try to guess...''')
    time.sleep(5)
    os.system('clear')


def number_guess(lives):
    random_num = random_input()
    guess = ''
    while guess != random_num:
        if not lives:
            return True
        print('You have {} lives'.format(lives))
        hints = []
        guess = str(input('Chose the number: '))
        guess = str(guess)
        if len(guess) == 3 and guess.isdigit():
            lives -= 1
            if guess == random_num:
                break
            i = 0
            while i < len(random_num):
                if guess[i] in random_num:
                    if guess[i] == random_num[i]:
                        hints.insert(0, 'hot')
                    else:
                        hints.append('warm')
                else:
                    pass
                i += 1
            if len(hints) == 0:
                print('cold')
            else:
                print(" ".join(hints))
        else:
            print('Please, type 3-digit value.')
    os.system('clear')
    with open('skullface.txt', newline='') as boss:
        level = boss.read()
        print('\033[1m\033[91m{}'.format(level))
    print('''Yes! %s is correct number!
    You WIN again!!!''' % random_num)
    time.sleep(4)


def hot_cold(lives):
    introduce()
    a = number_guess(lives)
    if a:
        return True
