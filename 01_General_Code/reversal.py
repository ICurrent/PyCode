#version1.0
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)



#version1.1
print()
n=int(input("Enter number: "))
rev = 0

while(n>9):

    first_digit=n%10
    second_digit=n//10
print("Reverse of the number {} is {}{}".format( n,first_digit, second_digit ))