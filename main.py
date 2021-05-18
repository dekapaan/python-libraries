# # Task 1
# # Number guessing game
# import random
# # random number to guess
# number = random.randint(1, 100)
#
# # Gets number of guesses from user. If invalid entry given, gives user retry until valid entry given
# while True:
#     try:
#         guesses = int(input('Enter number of guesses: '))
#         break
#     except ValueError:
#         print('Not an integer, try again...')
#
# """Allows number of guesses stated by user. If guess incorrect, will tell user if guess too high or too low. If
# invalid entry given, gives user retry until valid entry is given """
# for x in range(guesses-1, -1, -1):
#     while True:
#         try:
#             guess = int(input('Enter guess:'))
#             break
#         except ValueError:
#             print("Not an integer")
#     if guess == number:
#         print('You win! :-)')
#         break
#     elif x == 0:
#         print('All out of guesses. The number was {}. Better luck next time :-('.format(number))
#     elif guess < number:
#         print('Too low. {} guesses left'.format(x))
#     elif guess > number:
#         print('Too high. {} guesses left'.format(x))

# # Exercise 1
# # Ten dates from today, 1 week apart
from datetime import datetime, timedelta
#
# # Today's date
# dt = datetime.now()
#
# # Prints 10 dates 14 days apart
# for x in range(10):
#     print(x+1, "-", end='    ')
#     print(dt.strftime('%Y/ %m/ %d - %H:%M'))
#     dt = dt + timedelta(days=7)

# Exercise 2
# year_born = int(input('Enter year born:'))
# month_born = int(input('Enter month born:'))
# day_born = int(input('Enter day born:'))
#
# current_year = int(datetime.today().strftime('%Y'))
# current_month = int(datetime.today().strftime('%m'))
# current_day = int(datetime.today().strftime('%d'))
#
# age = current_year - year_born - 1
#
# if month_born < current_month:
#     age += 1
# elif month_born == current_month:
#     if day_born <= current_day:
#         age += 1
#
# print('')
# print('You are {} years old'.format(age))

# tkinter class area of circle
from tkinter import *
from tkinter import messagebox
from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = (pi*(self.radius**2))
        return result


root = Tk()
label = Label(root, text='Enter radius: ')
label.grid(row=1, column=1)
entry = Entry(root)
entry.grid(row=1, column=2)
area_circle = Entry(root, state='readonly')
area_circle.grid(row=2, column=2)


def calculate():
    try:
        circle = Circle(float(entry.get()))
    except ValueError:
        messagebox.showerror(message='invalid entry')
    area_circle.config(state='normal')
    area_circle.insert(0, round(circle.area(), 1))
    area_circle.config(state='readonly')


calc = Button(root, text='calculate', command=calculate)
calc.grid(row=1,column=3)
label2 = Label(root, text='Area of circle:')
label2.grid(row=2, column=1)
root.mainloop()
