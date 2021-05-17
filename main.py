# Task 1
# Number guessing game
import random
# random number to guess
number = random.randint(1, 100)


# Gets number of guesses from user. If invalid entry given, gives user retry until valid entry given
while True:
    try:
        guesses = int(input('Enter number of guesses: '))
        break
    except ValueError:
        print('Not an integer, try again...')


"""Allows number of guesses stated by user. If guess incorrect, will tell user if guess too high or too low. If 
invalid entry given, gives user retry until valid entry is given """
for x in range(guesses-1, -1, -1):
    while True:
        try:
            guess = int(input('Enter guess:'))
            break
        except ValueError:
            print("Not an integer")
    if guess == number:
        print('You win! :-)')
        break
    elif x == 0:
        print('All out of guesses. The number was {}. Better luck next time :-('.format(number))
    elif guess < number:
        print('Too low. {} guesses left'.format(x))
    elif guess > number:
        print('Too high. {} guesses left'.format(x))


# Task 2
# Ten dates from today, 2 weeks apart
from datetime import datetime, timedelta

# Today's date
dt = datetime.now()

# Prints 10 dates 14 days apart
for x in range(9):
    print(x+1, "-", end='    ')
    print(dt.strftime('%Y/ %m/ %d'))
    dt = dt + timedelta(days=14)
