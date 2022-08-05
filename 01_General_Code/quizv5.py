import sys
name = str(input("Please enter your name:"))
print("you are about the start a 15 question quiz,{}".format(name))
input("please press the enter key to start the quiz")
subject = input("enter your subject ")
selected_answer=[]
f = open("{}.txt".format(subject),"r")
i=0;j=5
while(i<12 and j<16):
        for line in range(i,j):
            print(f.readline())
        answer1 = input("Enter your answer here")
        answer1 = answer1.upper()
        selected_answer.append(answer1)
i+=5;j+=5
if (j == 16):
        sys.exit()
f.close()




