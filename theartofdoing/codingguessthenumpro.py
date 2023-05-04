import random

def guess_num():
    global guess
    for i in range(1,4):
        print('Guess your number')
        guess = int(input('Enter your number: '))

        if guess < secretNumber:
            print('Youe number is too low dude')

        elif guess > secretNumber:
            print('Number is too High')
        else:
            break

    return guess

def check(guess,secretNumber):
    if guess == secretNumber:
        print('Hurray you are correct')
    else:
        print('Better luck next time, the seceret number is ' + str(secretNumber))

secretNumber = random.randint(1,20)

print('Thinking about a secret numbner')

guess = guess_num()
check(guess,secretNumber)


