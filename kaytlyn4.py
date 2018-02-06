def numberfour():
	n = int(input("Enter a Number: "))
	sum1 = 0
	for i in range(0, n+1):
		if not i%3 or not i%5:
			sum1 = sum1+i
	print("Your sum is: ", sum1)
