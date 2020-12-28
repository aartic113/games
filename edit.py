# ROCK PAPER SCISSORS -- Basic Formats
from random import randint
print("...RoCk...")
print("...PaPeR...")
print("...ScIsSoRs...")

player = input("Make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer:{computer}")

# player = rock
if player == computer:
	print("Its a tie")
elif player == "rock":
	if computer == "scissors":
		print("Player wins!")
	else:
		print("Computer wins!")
elif player == "paper":
	if computer == "rock":
		print("Player wins")
	else:
		print("Computer wins")
elif player == "scissors":
	if computer == "paper":
		print("Player wins")
	else:
		print("Computer wins!")
else:
	print("Something went wrong. Please try again")
	print(":("*10)