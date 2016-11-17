import random
x = []
i = 0
items = 0

def random_input():
    while len(x) < 3:
        number = random.choice(list(range(0,10)))
        if number not in x:
            x.append(number)
        else:
            pass
    random_num = str(x[0]) + str(x[1]) + str(x[2])
    random_num = str(random_num)
    print(random_num)
    return random_num

def number_guess():
    random_num = random_input() 
    guess = ''
    while guess != random_num:
        hints = []
        guess = str(input('Chose the number: ')) 
        guess = str(guess)
        print(type(guess))
        if len(guess) == 3 and guess.isdigit():
            if guess == random_num: 
                break
            i = 0
            while i < len(random_num):
                if guess[i] in random_num:
                    if guess[i] == random_num[i]:  
                        hints.append('hot')
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
    print('win!')



number_guess()
