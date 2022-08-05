import random

guess = int(input("Enter the number: "))
answer = random.choice(range(10))
#print(answer)
if guess != answer:
    print("Try again")
    
    while guess != answer:
        guess = int(input("Enter the number: "))
        
        if guess == answer:
            print("You guessed right!")

        else:
            print("You guessed wrong, Try again!")
