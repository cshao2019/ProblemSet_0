#Functions:
#Tests if the input is positive or not. 
def ifpositive(number):
	''' Checks integer positive '''
	if int(number) < 0:
		return False
	else:
		return True
		
#Function 0:
#Write a boolean function that takes in a positive integer or zero as a parameter and returns whether the number is odd or even.

def oddeven(number):
	''' Identifies if the inputted postive integer or zero is odd or even '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
	
	divison = int(number) % 2
	remainder = round(divison,1)
	
	if remainder == 0:
		return "The number is even. "
	else:
		return "The number is odd. "


#Function 1:
#Write a function that takes a non-negative integer as a parameter and returns the number of digits in it.

def numberDigits(number):
	''' Returns the number of digits in the given/inputted integer '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	return len(str(number)) 
	
		
#Function 2:
#Write a function that takes a non-negative integer as a parameter and returns the sum of its digits

def sumDigits(number):
	''' Returns sum of the digits of the input/given integer '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	newlist = list(str(number))
	intlist = map(int, newlist)
	
	#sum_of_all_digits= sum(intlist)
	#loop
	sum_of_all_digits = 0
	for eachnumber in intlist:
		sum_of_all_digits += eachnumber
			
	return sum_of_all_digits	
	
	
#Function 3:
#Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.

def sum_less_integer(number):
	''' Returns the sum of all the integers less than the given number '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	sumintegers = 0
	x = 1
	while x < int(number):
		sumintegers += x 
		x += 1
		
	return sumintegers


#Function 4:
# Write a function that takes a non-negative integer as a parameter and returns its factorial.

def factorial(number):
	''' Returns the given number's factorial '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	productintegers = 1
	x = 1
	while x <= int(number):
		productintegers *= x 
		x += 1
		
	return productintegers
	
	
#Function 5:
#Write a boolean function that takes two positive integers as parameters and figures out whether the second number is a factor the first. 
#In other words, returns true if the second number divides into the first number evenly, and false otherwise.

def factor_of_first(number1, number2):
	''' Figures out whether the second number is a factor of the first number '''
	if ifpositive(number1) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	if ifpositive(number2) == False:
		print("Input has to be positive. Program cannot continue")
		exit()	
		
	divison = int(number1) % int(number2)
	remainder = round(divison,1)
	if remainder == 0:
		return True
	else:
		return False
		

#Function 6:
#Write a boolean function that takes a positive integer as a parameter and returns whether the number is a prime.

def prime(number):
	''' Returns whether the given number is prime or not '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	intnumber = int(number)
	divisor = 1
	counter = 0
	
	while divisor < intnumber:
		divison = intnumber % divisor
		remainder = round(divison,1)
		if remainder == 0:
			counter += 1	
		divisor += 1
		
	if counter == 1:
		return True #prime
	else:
		return False #Not Prime
		
		
#Function 7:
#Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect. 
#A perfect number is a number that equals the sum of proper its proper factors. A proper factor is any factor except the number itself. 

def perfect(number):
	''' returns whther the number is perfect or not '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	intnumber = int(number)
	divisor = 1
	total = 0
	while divisor < intnumber:
		divison = intnumber % divisor
		remainder = round(divison, 1)
		if remainder == 0:
			total += divisor
		divisor += 1
	if total == intnumber:
		return True # Perfect
	else:
		return False #Not perfect 
		
		
#Function 8:
#Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number 
#divides evenly into the number, false otherwise. You MUST call the sumDigits function you wrote in question 2 to define this function.

def sumDigits_divide(number):
	''' returns true if the sum of the digits of the number divides evenly into the number '''
	if ifpositive(number) == False:
		print("Input has to be positive. Program cannot continue")
		exit()
		
	sumofDigits = sumDigits(number)
	intnumber = int(number)
	if sumofDigits == 0:
		print("Divisor cannot be zero ")
	return 
		
	divison = intnumber % sumofDigits
	remainder = round(divison, 1)
	if remainder == 0:
		return True
	else:
		return False
		