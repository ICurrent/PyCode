#APPLICATION1-BASIC CALCULATOR
#introduction
#mathematical opreatorV1.0.0
print("{} + {} = {}".format(5, 2, 5 + 2))
print("5+2=", 5+2)
print("5-2=", 5-2)
print("5*2=", 5*2)
print("5/2=", 5/2)
print("5 raise to power 2=", 5**2)
print("5 floor 2 is", 5//2)
print("5 modulo 2 is", 5 % 2 )
#mathematical opreatorV1.0.1
x = eval(input("please  enter an integer for x :"))
y = eval(input("please  enter another integer for y :"))
print("x+y=", x+y)
print("x-y=", x-y)
print("x*y=", x*y)
print("x/y=", x/y)
print("x raise to power y =", x**y)
print("x floor y is", x//y)
print("x modulo y is", x % y )

#APPLICATION2- TIME CONVERTER FROM SECONDS TO MIN OR HOUR OR DAYS ETC
#This is an application that convert plenty seconds to min, hr,day etc...

time = eval(input("please enter your total time in seconds:"))
print(" {} minutes and {} seconds".format((time // 60),  (time % 60)))

print("your actual time is {} days,{} hours , {} minutes and {} seconds".
      format((((time // 60)//60) // 24),
                 ((time // 60)//60 % 24),
                                  (time%60), time % 60))
