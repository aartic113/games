print("***************")
# ask for age
age = input("How old are you: ")
# Only check for ages if not empty string
if age != "":
	age = int(age)	   
	if age >=18 and age< 21:
		# 18-21 wristband
		print("You can enter, but need a wristband")
	elif age >=21:
		# 21+ drink,normal entry
		print("You are good to enter and can drink")
	else:
		# too young, sorry
		print("Sorry, you are too young to drink :(")

else:
	print("Please enter a age")


# OR
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 21:
	    print("You are good to enter and can drink!")
	elif age >= 18:
	    print("You can enter, but need a wristband!")
	else: 
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")