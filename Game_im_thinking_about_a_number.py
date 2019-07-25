# This is a game about guessing the right number

import random

guessesTaken = 0

print('Hello! What is your name?')
myname = input()
number = random.randint(1,20)

print('Okay, my friend'+ myname+'，I\'m thinking about a number between 0 and 20')

while guessesTaken < 6:
    print('Why not take a guess?')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken +1

    if guess < number:
        print('Ohh, it\'s a little bit small!')
    if guess > number:
        print('You may want try a smaller one')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Wow，'+myname+'，Congratulations! You only took'+guessesTaken+'guesses!')
    input()
if guess != number:
    number = str(number)
    print('I\'m sorry… The number I was thinking about was'+number+'! See you next time!')
    input()
