num = int(input("Enter a Number: "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //=10

if num == sum:
    print(sum, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")