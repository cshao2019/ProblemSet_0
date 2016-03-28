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
		
	return "There are " + str(len(str(number))) + " digits in " + str(number) 
	
		
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
	