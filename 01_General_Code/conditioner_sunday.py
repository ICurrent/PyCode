
#version 1.0.1
name = input("please enter your name here:")
if name == "Esan":
    print("you entered the man with a floral shirts name")
else:
    print("you enterde either the man with a green or striped t shirt or somethingesld")

# version 1.0.1
name = input("please enter your name here:")
if name == "Esan":
    print("you entered the man with a floral shirts name")
elif name == "mayowa":
    print("you entered the man with a green shirts name")
elif name == "shina":
    print("you entered the man with a striped shirts name")
else:
    print("the name you entered is not int this class")

# version 1.0.2
name = input("please enter your name here:")
if name in ["esan","mayowa","shina"]:
    print("this student is in this class")
else:
    print("i dont know this student")
"""
"""# version 1.0.3
attendance = {"esan":"floral","mayowa":"green","shina":"stripe"}
name = input("please enter your name here for the check:")
if name in attendance:
    print("Mr {} is in this class and his wearing a {} shirt".format(name, attendance.get(name)))
else:
    print("i dont know this student")

age = eval(input("please enter your age for validation:"))
if (age >= 1) and ( age < 18):
    print(" you cant vote or drive or live alone")
elif (age >= 18) and (age < 21):
    print(" you can vote but cant drive or live alone")
elif (age >= 21) and (age < 65):
    print(" you can vote , drive or live alone")
elif( age == 66):
    print("you are special to us")
elif( age == 77 or age== 88):
    print("your age looks funny")
else:
    print("you are an elders state man")
