def compu_fact(n):
    n = eval(input("please enter the number you want its factorial:"))
    number = n
    factorial = 1
    if n == 0 or n == 1:
        print("the factorial of {} is 1".format(n))
    else:
        while(n > 1):
            factorial = factorial * n
            n -= 1
        print("the factorial of {} is {}".format(number, factorial))
    return factorial
compu_fact()
