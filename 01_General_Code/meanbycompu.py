def our_mean():
    n = eval(input("the number of items you want its mean:"))
    while n <= 0:
        print("please enter a positive number becos n cant be negative or zero")
        n = eval(input("the number of items you want its mean:"))
    else:
        sum = 0
        for i in range(1, n+1):
            print(i)
            x = eval(input("Enter the item one by one:"))
            sum = sum + x
        mean = sum /n
        print("the mean of all the number item  you entered is {}".format((mean)))
    return mean