#===05/10/2020======
#q1....make a no converter that converters plenty kobos to naira
#q2....make a second converter that converters plenty secondss to hour and more
#q3.....try basic alarm clock
#A1
### Alhaja
time_second = eval(input("please enter the the time in seconds:"))
real_time_day = time_second //60 // 60 // 24
real_time_hour = time_second // 60 // 60 % 24
real_time_min = time_second // 60 % 60
real_time_sec = time_second % 60
print("{} is {}day {}hr {} min {} sec".format(time_second,real_time_day, real_time_hour, real_time_min, real_time_sec))
###Ib
time_second = eval(input("please enter the the time in seconds:"))
real_time_day = time_second // 60 // 60 // 60
real_time_hour = time_second // 60 // 60 % 24
real_time_min = time_second // 60 % 60
real_time_sec = time_second % 60
print("the time is {}day {}hr , {} min  and {} sec".format(real_time_day, real_time_hour, real_time_min, real_time_sec))

### Ay
time_second = eval(input("please enter the the time in seconds:"))
real_time_day = time_second // 24 % 3600
real_time_hour = time_second // 60 // 60
real_time_min = time_second // 60 % 60
real_time_sec = time_second % 60
print("the time is {}day {}hr , {} min  and {} sec".format(real_time_day, real_time_hour, real_time_min, real_time_sec))
### Ebube
time_second = eval(input("please enter the the time in seconds:"))
real_time_day = time_second // 60 // 60 // 24 % 60 % 60 % 60 % 24
real_time_hour = time_second // 60 // 60 % 60 % 60 % 24
real_time_min = time_second // 60 % 60
real_time_sec = time_second % 60
print("the value of the input seconds is {}day {}hr , {} min  and {} sec".format(real_time_day, real_time_hour, real_time_min, real_time_sec))


