from random import randrange

num = randrange(20)
prompt = 'Guess a number between 1 and 20'
guess = input(prompt)


def init_game():
    num = randrange(20)
    prompt = 'Guess a number between 1 and 20'
    guess = input(prompt)
    handle_guess(guess=guess)


def handle_guess(guess=guess, num=num, prompt=prompt):
    if (int(guess) == num):
        print('Wow you got it')
        exit()

    elif int(guess) > num:
        print('Too high')
        handle_guess(guess=input(prompt))

    elif int(guess) < num:
        print('Too low')
        handle_guess(guess=input(prompt))


init_game()
