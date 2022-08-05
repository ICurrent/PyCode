#print("functionA") version 1.0.1
'''def fivetimesr(x):
    print(x*5)

fivetimesr(10)'''

#print("functionA") version 1.0.2
def my_function(food):
    for i,d in enumerate(food):
        print(f"The number {i+1} fruit is {d}")
fruits = ["Apple","Banana","Cherry"]
my_function(fruits)
'''def fivetimers():
    name = input("please enter your name here:")
    x = eval(input("please input what you want to multiply by 5 here:"))
    print("Dear {}, the number you entered is {} and the answer is {}".format(name, x, x * 5))

fivetimers()






print("functionB")
def october():
    x = eval(input("please enter a value for x"))
    print(x*3)


october()
print("functionC")
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



print(compu_fact(5))


def solve_ap2(T1, T2, T3, n, question):
    if T2 - T1 == T3 - T2:
        print("this is surely an AP whose common difference is {}".format(T2 - T1))
        d = T2 - T1
        Tn = T1 + (n - 1) * d
        print("the {}th termof this AP is {}".format(n, Tn))
        if (question == "yes" or question == "y"):
            print("the sum of this AP with {}th term {} is {}".format(n, Tn, int((n / 2) * (T1 + Tn))))
        elif (question == "no" or question == "n"):
            print("thanks for using this App to calculate only the nth term {}".format(Tn))
        else:
            print("you are not serious at all.bye bye!!!")
    else:
        (T2 - T1 != T3 - T2)
        print("this is probably a GP or any other series")

def greetings(name):
    print("good morning, mr {}".format(name))
    print("mr {} hope you had a nice night?".format(name))
    print("have a great day mr {}".format(name))

def compudemic_enquiry(name, course, phone_number):
    print("")
def sayhello():
    print("hello world ")'''
