import random

print('I am thinking of a number 0 - 20, try and guess it')
Guess_Number = random.randint(0,20)



def guessGame():
    while True:
        guess = int(input('Guess number: '))
        if guess < Guess_Number:
            print('Your guess is too low, try again')
        elif guess > Guess_Number:
            print('Your guess is too high, try again')
        else:
            print('You guessed correctly!')
            break
guessGame()
