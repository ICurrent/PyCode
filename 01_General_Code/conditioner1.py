#for as a condition
for i in range(0, 5):
    print(i)
print("/n")
for i in range(0, 20, 2):
    print(i)
print("/n")
#write a python program that prints odd no btw 0 and 50 using for conditional statement

#example: time bomb v1.0.1
time_explosion = eval(input("Enter the time to blow off this bomb:"))
for i in range(time_explosion):
    print("explosion in {}".format(i))
print("gbosaaaa!!!")
print("\n")

#example: time bomb v1.0.2
time_explosion = eval(input("Enter the time to blow off this bomb:"))
while (time_explosion > 0):
    print("explosion in {} seconds".format(time_explosion))
    time_explosion -= 1
print("gbosaaaa!!!")
print("/n")
#example: data of people v1.0.1
trainees = ["bassey","victor","jacob","jide","timilehin"]
k = 1
for i in trainees:
    print("Mr {} came as number {} trainee to the center today".format(i, k ))
    k += 1
#example:
for i in (2,4,6,7):
    print(i*3)
#example:
for i in trainees:
    print("Mr {} came as number {} trainee to the center today".format(i, trainees.index(i) + 1))
    print("\n")

#example:
for i in ["bassey","victor","jacob","jide"]:
    print("Mr {} came as number {} trainee to the center today".format(i, i))


# Q1 make a multiplication table
# Q2 computes the factorial of a number

for i in range(2, 13):
    print("\n", end="")
    for j in range(1, 13):
        print("{} x {} = {}".format(i, j, i * j))

for y in range(67,100):
  if y % 2 == 0:
    continue
  print(y)
print("\n")
for y in range(89,103):
  if y % 2 == 0:
    print(y)
































