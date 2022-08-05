def main():
   name = eval(input("please enter your name"))
    try:
        print("welcome {}".format(name))
    except SyntaxError:
        print("Opps!, something went wrong")

    except NameError:
        print("Opps!, something else went wrong")

main()















'''
name = "yemi"
print(name[1])
print(name.index("e"))
print("the  second alphabeth in {} is {} and its at position{}".format(name, name[1], (name.index("e") + 1)))
help(print)
import math
print(dir(math))
import time
print(dir(time))
print()
import compu_factorial
print(dir(compu_factorial))'''