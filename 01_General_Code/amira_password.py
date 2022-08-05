'''#version 1.0.0
nkechi_password = "december"
attempt = input("Please enter your password:")
if attempt == "december":
    print("welcome to my phone")
else:
    print("you dont know the password")


#version 1.0.1
chiagozie_password = "november"
trial = 0
attempt = input("Please enter your password:")
if attempt == "november":
    print("welcome to my phone")
else:
    while( attempt != chiagozie_password and trial < 3):
        print("incorrect password")
        trial += 1
        attempt = input("Please enter your password:")
    print("you have exhausted your access number")


#version 1.0.2
chiagozie_password = "november"
trial = 0
warner = 3
attempt = input("Please enter your password:")
if attempt == "november":
    print("welcome to my phone")
else:
    while( attempt != chiagozie_password and trial < 3):
        print("incorrect password")
        trial += 1
        warner -= 1
        print("you have {} attempt(s) left".format(warner))
        attempt = input("Please enter your password:")
    print("you have exhausted your access number")'''

#version 1.0.3
chiagozie_password = "november"
trial = 0
warner = 3
attempt = input("Please enter your password:")
if attempt == "november":
    print("welcome to my phone")
else:
    while( attempt != chiagozie_password and trial < 3):
        print("incorrect password")
        trial += 1
        warner -= 1
        if warner > 0:
            print("you have {} attempt(s) left".format(warner))
        else:
            print("this is your last trial before your phone is blocked")
        attempt = input("Please enter your password:")
    print("you have exhausted your access number and your has been blocked")