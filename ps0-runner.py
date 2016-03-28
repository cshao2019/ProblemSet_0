#Main Program

from ps0 import ifpositive, oddeven, numberDigits, sumDigits, sum_less_integer, factorial, factor_of_first, prime, perfect, sumDigits_divide

#Function 0
print("Function 0: Test cases for function oddeven - Identifies if the inputted postive integer or zero is odd or even")
number = 3
print("Case 1: Input = " + str(number))
print(oddeven(number))

number = 10
print("Case 2: Input = " + str(number))
print(oddeven(number))

number = 0
print("Case 3: Input = " + str(number))
print(oddeven(number))


print("")


#Function 1
print("Function 1: Test cases for the function numberDigits - returns the number of digits in the given/inputted integer")
number = 654
print("Case 1: Input = " + str(number))
print(numberDigits(number))

number = 1000000
print("Case 2: Input = " + str(number))
print(numberDigits(number))

number = 0
print("Case 3: Input = " + str(number))
print(numberDigits(number))

print("")

#Function 2
print("Function 2: Test cases for the function sumDigits - Returns sum of the digits of the input/given integer")
number = 734
print("Case 1: Input = " + str(number))
print(sumDigits(number))

number = 1008
print("Case 2: Input = " + str(number))
print(sumDigits(number))

number = 0
print("Case 3: Input = " + str(number))
print(sumDigits(number))

print("")

#Function 3
print("Function 3: Test cases for the function sum_less_integer - returns the sum of all the integers that are less than the given number")
number = 654
print("Case 1: Input = " + str(number))
print(sum_less_integer(number))

number = 1003
print("Case 2: Input = " + str(number))
print(sum_less_integer(number))

number = 1
print("Case 3: Input = " + str(number))
print(sum_less_integer(number))


print("")

#Function 4
print("Function 4: Test cases for the function factorial - takes a non-negative integer as a parameter and returns its factorial")
number = 7
print("Case 1: Input = " + str(number))
print(factorial(number))

number = 21
print("Case 2: Input = " + str(number))
print(factorial(number))

number = 3
print("Case 3: Input = " + str(number))
print(factorial(number))


print("")


#Function 5
print("Function 5: Test cases for the function factor_of_first - takes two positive integers as parameters and figures out whether the second number is a factor the first. ")
number1 = 1654
number2 = 3
print("Case 1: Input = " + str(number1) + " and " + str(number2))
print(factor_of_first(number1, number2))

number1 = 100
number2 = 4
print("Case 1: Input = " + str(number1) + " and " + str(number2))
print(factor_of_first(number1, number2))

number1 = 0
number2 = 3
print("Case 1: Input = " + str(number1) + " and " + str(number2))
print(factor_of_first(number1, number2))

print("")


#Function 6
print("Function 6: Test cases for the function prime - returns whether the number is a prime")
number = 1
print("Case 1: Input = " + str(number))
print(prime(number))

number = 49
print("Case 2: Input = " + str(number))
print(prime(number))

number = 2
print("Case 3: Input = " + str(number))
print(prime(number))

print("")


#Function 7
print("Function 7: Test cases for the function perfect - returns whether the number is perfect")
number = 8
print("Case 1: Input = " + str(number))
print(perfect(number))

number = 28
print("Case 2: Input = " + str(number))
print(perfect(number))

number = 0
print("Case 3: Input = " + str(number))
print(perfect(number))

print("")


#Function 8
print("Function 8: Test cases for the function sumDigits_divide - returns true if the sum of the digits of the number divides evenly into the number, false otherwise")
number = 12
print("Case 1: Input = " + str(number))
print(sumDigits_divide(number))

number = 34
print("Case 2: Input = " + str(number))
print(sumDigits_divide(number))

number = 0
print("Case 3: Input = " + str(number))
print(sumDigits_divide(number))











