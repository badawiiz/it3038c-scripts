import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

choice = random.choice(list)

print('Hello! Please guess a number between 1 and 10')

guess = int(input())

if guess < choice:
    print ('Oh oh.. guess a bigger number')

elif guess > choice:
    print ('Oh oh.. guess a smaller number')

elif guess == choice:
    print ('YOu got it!! Nice work')
