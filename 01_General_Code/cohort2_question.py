print("welcome to MTN nigeria")
question = input("please how can we help you?")
print("what was wrong with customer that just left here. he said that {}".format(question))
#how to format to specific decimal place....
#variable swap
name = "tope"
name = "yemi"
print(name)
name1 = "bunmi"
name2 = "thomas"
print(name1)
print(name2)
(name1, name2) = (name2, name1)
print(name1)
print(name2)
#more examples
air_time_balance = "N60.5"
customer_request = input("Do you want to check my mtn bal with *556#?yes")
print("Your account balance is {}".format(air_time_balance))
#operator
#+,-,*,/,//, %,**
value1 = eval(input("please enter the first value here:"))
value2 = eval(input("please enter the second value here:"))
print("{} + {} is {}".format(value1, value2, value1 + value2))
print("{} - {} is {}".format(value1, value2, value1 - value2))
print("{} * {} is {}".format(value1, value2, value1 * value2))
print("{} / {} is {}".format(value1, value2, value1 / value2))
print("{} // {} is {}".format(value1, value2, value1 // value2))
print("{} % {} is {}".format(value1, value2, value1 % value2))
print("{} ** {} is {}".format(value1, value2, value1 ** value2))
#===05/10/2020======
#q1....make a no converter that converters plenty kobos to naira
#q2....make a second converter that converters plenty secondss to hour and more
#q3.....try basic alarm clock
#A1
time_second = eval(input("please enter the the time in seconds:"))
real_time_min = time_second// 60
real_time_sec = time_second % 60
print("the time is {} min  and {} sec".format(real_time_min,real_time_sec))



