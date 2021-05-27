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
# # """Allows number of guesses stated by user. If guess incorrect, will tell user if guess too high or too low. If
# # invalid entry given, gives user retry until valid entry is given """
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
#
# Exercise 1
# Ten dates from today, 1 week apart
# from datetime import datetime, timedelta
#
# # Today's date
# dt = datetime.now()
#
# # Prints 10 dates 14 days apart
# for x in range(10):
#     print(x+1, "-", end='    ')
#     print(dt.strftime('%Y/ %m/ %d - %H:%M'))
#     dt = dt + timedelta(days=14)
#
# class studentMark:
#     def __init__(self, name, surname, grade_percent1, grade_percent2, grade_percent3):
#         self.name = name
#         self.surname = surname
#         self.grade_percent1 = grade_percent1
#         self.grade_percent2 = grade_percent2
#         self.grade_percent3 = grade_percent3
#
#     def average(self):
#         return (self.grade_percent1+self.grade_percent2+self.grade_percent3)/3
#
#     def pass_fail(self):
#         result = self.average()
#         if result < 50:
#             return False
#         if result >= 50:
#             return True
#
#
# stud_name = input("Enter name: ")
# stud_surname = input("Enter surname: ")
# while True:
#     try:
#         x = int(input('Enter first mark(0-100): '))
#         if x < 0 or x > 100:
#             raise ValueError
#         break
#     except ValueError:
#         print('Must be integer between 0-100')
#
# while True:
#     try:
#         y = int(input('Enter second mark(0-100): '))
#         if y < 0 or y > 100:
#             raise ValueError
#         break
#     except ValueError:
#         print('Must be integer between 0-100')
#
# while True:
#     try:
#         z = int(input('Enter third mark(0-100): '))
#         if z < 0 or z > 100:
#             raise ValueError
#         break
#     except ValueError:
#         print('Must be integer between 0-100')
#
# grade_sys = studentMark(stud_name, stud_surname, x, y, z)
# print("")
# print(grade_sys.name + ' ' + grade_sys.surname)
# print('Average percentage: ' + str(round(grade_sys.average(), 2)) + '%')
# if not grade_sys.pass_fail():
#     print('You failed :-(')
# elif grade_sys.pass_fail():
#     print('You Passed :-D')
# # Exercise 2
# # Calculate date of birth
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
#
#
# # tkinter class area of circle
# from tkinter import *
# from tkinter import messagebox
# from math import pi
#
#
# class Circle:
#     def __init__(self, master):
#         self.label = Label(master, text='Enter radius: ')
#         self.label.grid(row=1, column=1)
#         self.entry = Entry(master)
#         self.entry.grid(row=1, column=2)
#         self.area_circle = Entry(master, state='readonly')
#         self.area_circle.grid(row=2, column=2)
#         self.calc = Button(root, text='calculate', command=self.area)
#         self.calc.grid(row=1, column=3)
#         self.label2 = Label(root, text='Area of circle:')
#         self.label2.grid(row=2, column=1)
#
#     def area(self):
#         result = (pi*(int(self.entry.get())**2))
#         self.area_circle.config(state='normal')
#         self.area_circle.insert(0, round(result))
#         self.area_circle.config(state='readonly')
#
#
# root = Tk()
# root.title('Circle Area Calculator')
# Circle(root)
# root.mainloop()
#
#
#
