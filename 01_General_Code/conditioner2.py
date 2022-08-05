#-----class work------
#Q1==Find the factorial of a number>>>>>
#Q2==Desgin a basic age detector>>>>>
#03==print multiplication table of a given number>>>>
#04==solve Quadratic equation>>>>
#05==solve AP and GP
#06==compute the mean of a number
#07==an app for a for apple

#===solution1
#===solution2

age = eval(input("please enter the age you want to verify"))
if ((age >=1) and (age < 18)):
    print("you are to young to vote and drive")
elif(age > 18 and age <= 21):
    print("you can vote but  not  drive")
elif(age >=21 and age <=65):
    print("you can vote and  drive")
#elif not age ==64:
    #print("this is a special age")
else:
    print("you are an elder state man , you should be home!!!")









