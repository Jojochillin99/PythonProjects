# Guess num that is 1-20
import random

guessestaken = 0

print("Hey, what's your name?" )
username = input()

number = random.randint(1,25)
print("So, " + username + " I'm thinking of a number between 1 and 25.")

for guessestaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Try again, that was too low.")

    if guess > number:
        print("Try again, that was too high.")

    if guess == number:
        break

if guess == number:
    guessestaken = str(guessestaken + 1)
    print("Great job " + username + "! " + "It only took " + guessestaken + " guesses."
    + " That was impressive.")

if guess != number:
    number = str(number)
    print("Nah, fam. The number I was thinking of was " + number + ".")
