# User guesses a number the computer selected


from random import randint
number = randint(1,15)
value = number
answer = int(input("Guess a number between 1 and 15: "))
while answer != value:
	if answer > value:
		print("Too high, try again!")
		answer = int(input("Guess a number between 1 and 15: "))
	else:
		print("Too low, try again!")
		answer = int(input("Guess a number between 1 and 15: "))
print("You guessed it! You won!")

reply = str(input("Do you want to keep playing? (y/n)"))
while reply != "n":
	answer = int(input("Guess a number between 1 and 15: "))
	number1 = randint(1,15)
	value1 = number1
	while answer != value1:
		if answer > value1:
			print("Too high, try again!")
			answer = int(input("Guess a number between 1 and 15: "))
		else:
			print("Too low, try again!")
			answer = int(input("Guess a number between 1 and 15: "))
	print("You guessed it! You won!")
	reply = str(input("Do you want to keep playing? (y/n)"))
print("Thanks for playing. Bye :)")
