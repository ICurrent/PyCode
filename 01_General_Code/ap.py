#a program that compute the nth term of an AP and ask if you also want the sum of the AP
#T1=first term,T2=second term ,T3=third term and so on...till Tn is nth term
#Tn = a + (n - 1)d
T1 = eval(input("please enter the first term of the series="))
T2 = eval(input("please enter the second term of the series="))
T3 = eval(input("please enter the third term of the series="))
if T2 - T1 == T3 - T2:
    print("this is surely an AP whose common difference is {}".format(T2-T1))
    d = T2 - T1
    n = eval(input("please enter the number of the nth term you want in this series="))
    Tn = T1 + (n - 1)*d
    print("the {}th termof this AP is {}".format(n, Tn))
    question = input("Do you also want to calculate the sum of this series of n you entered earlier?")
    if (question == "yes" or question =="y"):
        print("the sum of this AP with {}th term {} is {}".format(n,Tn, int((n/2)*(T1+Tn))))
    elif(question == "no" or question =="n"):
        print("thanks for using this App to calculate only the nth term {}".format(Tn))
    else:
        print("you are not serious at all.bye bye!!!")
else:
    (T2 - T1 != T3 - T2)
    print("this is probably a GP or any other series")


#version 1.1
def solve_ap():
    T1 = eval(input("please enter the first term of the series="))
    T2 = eval(input("please enter the second term of the series="))
    T3 = eval(input("please enter the third term of the series="))
    if T2 - T1 == T3 - T2:
        print("this is surely an AP whose common difference is {}".format(T2 - T1))
        d = T2 - T1
        n = eval(input("please enter the number of the nth term you want in this series="))
        Tn = T1 + (n - 1) * d
        print("the {}th termof this AP is {}".format(n, Tn))
        question = input("Do you also want to calculate the sum of this series of n you entered earlier?")
        if (question == "yes" or question == "y"):
            print("the sum of this AP with {}th term {} is {}".format(n, Tn, int((n / 2) * (T1 + Tn))))

        elif (question == "no" or question == "n"):
            print("thanks for using this App to calculate only the nth term {}".format(Tn))
        else:
            print("you are not serious at all.bye bye!!!")
    else:
        (T2 - T1 != T3 - T2)
        print("this is probably a GP or any other series")


solve_ap()


#version 1.2
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

solve_ap2(5,10,15,20,"yes")"""






