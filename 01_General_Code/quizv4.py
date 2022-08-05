name = str(input("Please enter your name:"))
print("you are about the start a 15 question quiz,{}".format(name))
input("please press the enter key to start the quiz")
subject = input("enter your subject ")
selected_answer=[]
f = open("{}.txt".format(subject),"r")
i=0
for line in range(0,i+5):
    print(f.readline())
    print("\n")
answer1 = input("Enter your answer here")
answer1 = answer1.upper()
selected_answer.append(answer1)
for line in range(7,12):
    print(f.readline())
    print("\n")
answer2 = input("Enter your answer here")
answer2 = answer2.upper()
selected_answer.append(answer2)
for line in range(13,18):
    print(f.readline())
    print("\n")
answer3 = input("Enter your answer here")
answer3 = answer3.upper()
selected_answer.append(answer3)
f.close()


