import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

choice = random.choice(list)

print('Hello! Please guess a number between 1 and 10')

guess = int(input())

if guess > 10:
	print('You must pick a number between 1 and 10')
	guess = int(input())
elif guess < 1:
	print('You must pick a number between 1 and 10')
	guess = int(input())	

if guess == choice:
	print ('You got it!! Nice work. The random number was'  + str(int(choice)))

else:
	for g in range(0,choice):
		if guess < choice:
			print ('Oh oh.. guess a bigger number')	
			guess = int(input())
			continue
		elif guess > choice:
			print ('Oh oh.. guess a smaller number')
			guess = int(input())
			continue
print ('You got it!! Nice work. The random number was ' + str(int(choice)))