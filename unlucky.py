# Loop through numbers 1-20
# for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"


for x in range(1,20):
	if x == 4 or x == 13:
		print("x is unlucky")
	elif x %2 == 0:
		print("x is even")
	else:
		print("x is odd")