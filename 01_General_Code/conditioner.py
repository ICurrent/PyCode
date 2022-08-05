
#version 1.0.1
name = input("please enter trainee name here:")
name = name.capitalize() 
if name == "Lateef" or name == "Jide":
    print("you entered the man on native")
else:
    print("you entered any other person in the class not wearing native")

# version 1.0.1
name = input("please enter your name here:")
name = name.capitalize()
if name == "peter":
    print("you entered the man with an orange shirts ")
elif name == "tomiwa":
    print("you entered the lady with a brown shirts ")
elif name == "shina":
    print("you entered the man with a native attire")
else:
    print(" you entered either toba or nkechi or hassan or any other person the class")

# version 1.0.2
name = input("please enter your name here:")
if name in ["esan","mayowa","shina"]:
    print("this student is in this class")
else:
    print("i dont know this student")

# version 1.0.3
attendance = {"peter":"orange","tomiwa":"brown","shina":"native"}
name = (input("please enter your name here for the check:"))
if name in attendance:
    #print("Mr {} is in this class and his wearing a  shirt".format(attendance.values(), attendance.key()))
    print("Mr/mrs {} is in this class and his wearing an {} shirt".format(name, attendance.get(name)))
else:
    print("i dont know this student")

# version 1.0.3.a
#if, for, if else, if elif else, while, for else,while else....etc.........diiferent types of conditioner
x = eval(input("please enter the value of x here:"))
if x == 2:
    print("say the value of x is two ")
if x == 3:
    print("say the value of x is three ")
if x == 4:
    print("say the value of x is four")
else:
    print("what you entered for x is neither two, three nor four")

print("/n")
# version 1.0.3.b
x = eval(input("please enter the value of x here:"))
if x == 2:
    print("say the value of x is two ")
    if x == 3:
        print("say the value of x is three ")
        if x == 4:
            print("say the value of x is four")
else:
    print("what you entered for x is neither two, three nor four")

print("/n")
# version 1.0.3.c
x = eval(input("please enter the value of x here:"))
if x == 2:
    print("say the value of x is two ")
    if x == 3:
        print("say the value of x is three ")
        if x == 4:
            print("say the value of x is four")
        else:
            print("what you entered for x is neither two, three nor four")

print("/n")
# version 1.0.3.d
x = eval(input("please enter the value of x here:"))
if x == 2:
    print("say the value of x is two ")
elif x == 3:
    print("say the value of x is three ")
elif x == 4:
    print("say the value of x is four")
else:
    print("what you entered for x is neither two, three nor four")

print("/n")
# version 1.0.4
x = eval(input("please enter the value of x here:"))
if (x == 2 or x ==3 or x == 4):
    print("say the value of x is two ")
    print("say the value of x is three ")
    print("say the value of x is four")
else:
    print("what you entered for x is neither two, three nor four")

