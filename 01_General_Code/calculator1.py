import math
#program for a simple calculator using multiple selection---if --elif--else
try:
    first_number = eval(input("Please enter the first number:"))
    second_number = eval(input("Please enter the second number:"))
    operator = eval(input("please enter a number from 1 to 4 as above for the operation you want to perform:"))
    if operator == 1:
        print("the sum of {} and {} is {}".format(first_number, second_number, first_number + second_number))

    elif operator == 2:
        print("the  difference between {} and {} is {}".format(first_number, second_number, first_number - second_number))

    elif operator == 3:

        print("the product of {} and {} is {}".format(first_number, second_number, first_number * second_number))

    elif operator == 4:
        print("the division of {} by {} is {}".format(first_number, second_number, first_number / second_number))

    elif operator == 5:
        print("takes squareroot of the first number enetered as {2}".format(first_number, second_number, math.sqrt(first_number)))

    else:
        print("I am designed to only handle +,-,*/.Thanks")
except NameError:
    print(" please enter only numbers!")

except SyntaxError:
    print(" Invalid input types")

except ZeroDivisionError:
    print(" please avoid dividing any number by zero by this calculator")

except ValueError:
    print(" negative number square root is not allowed")

except:
    print("Oops! something went wrong")

