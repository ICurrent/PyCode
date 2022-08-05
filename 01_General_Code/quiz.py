name = str(input("Please enter your name:"))
print("Thanks for enrolling to take this quiz Mr {}".format(name))
print()
print("you are about to start a {} question quiz mr {}".format(3,name))
print("Choose the correct option for each question by entering the appropriate corresponding alphabet")
print()
print("please press \'Enter\' key Mr {} to start  this quiz".format(name))
question1 = """Who is the governor of lagos state?"""
question2 = """What year did world recorded covid-19 outbreak?"""
question3 = """The currency of transaction in the US is"""
question4 = """The currency of transaction in the Nigeria is"""
option1 = ["Mr babatunde fashola","Mr babajide sanwo-olu","Col Buba Maruwa"]
option2 = ["2017","2020","2019"]
option3 = ["Euro","Dollar","Pounds sterling"]
option4 = ["Naira","Dollar","Pounds sterling"]
questions = [question1,question2,question3,question4]
options = [option1,option2,option3,option4]
letter = ["A","B","C"]
answers = [option1[1],option2[2],option3[1],option4[0]]
score = 0
import random
import datetime

startTime = datetime.datetime.now()
f = random.sample(range(len(questions)), len(questions))
answer = [None] * len(questions)
qanswers = []
i = 0
for question in range(len(questions)):
    print("{}.{}".format(i + 1 , questions[f[i]]))
    b = 0
    g = random.sample(range(len(options[f[i]])), len(options[f[i]]))
    for option in range(len(options[f[i]])):
        print(letter[b], "." ,options[f[i]][g[b]])
        if options[f[i]][g[b]] in answers:
            qanswers.append(letter[b])
        b += 1
    answer[i] = str(input("Enter your answer:"))
    answer[i] = answer[i].upper()
    i += 1
for i in range(len(answers)):
    if answer[i] == qanswers[i]:
        score += 1

percentage = score/len(questions) * 100
endTime = datetime.datetime.now()
totalTime = endTime - startTime
if totalTime.seconds < 60:
    totalTime = str(totalTime.seconds) + "seconds"
elif 60 <= totalTime.seconds < 120:
    totalTime = str(totalTime.seconds//60) + " minute and" + str(totalTime.seconds%60) + "seconds"
else:
    totalTime = str(totalTime.seconds//60) + " minutes and " + str(totalTime.seconds%60) + "seconds"
grade = ""
if percentage < 40:
    grade = "F"
    outcome = "Mr {} ,you failed this quiz and work hard next time".format(name)
elif 40 <= percentage < 50:
    grade = "D"
    outcome = "Mr {} ,you perform poorly in this quiz and work hard next time".format(name)
elif 50 <= percentage < 60:
    grade = "C"
    outcome = "Mr {} ,you perform averagely in this quiz and work hard next time".format(name)
elif 60 <= percentage < 70:
    grade = "B"
    outcome = "Good performance Mr {}, keep it up".format(name)
elif  percentage < 70:
    grade = "A"
    outcome = "Excellent performance Mr {}, please remain a champion".format(name)
print("Dear Mr {} ".format(name))
print("here is your exam result")
print()
print("it took you total of",totalTime,"to finish the quiz")
print("your score is:",round(percentage,2),"%")
print("Mr {},your grade is {} because your score is {}".format(name,grade,percentage))
print("thanks for taking the quiz mr {}".format(name))
