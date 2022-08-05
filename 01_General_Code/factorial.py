#version1 of factorial

n = eval(input("please  bukola enter the number you want its factorial:"))
number = n
factorial = 1
if n == 0 or n == 1:
    print("the factorial of {} is 1".format(n))
else:
    while(n > 1):
        factorial = factorial * n
        n -= 1
    print("the factorial of {} is {}".format(number, factorial))

#version1.1 of factorial>>>>>>captures negative number and re ask the user for a positive no




#version 2 of factorial
import math
n = eval(input("please enter the number you want its factorial:"))
print("the factorial of {} is {}".format(number, math.factorial(n)))

