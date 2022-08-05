name = str(input("Please enter your name:"))
print("you are about the start a 15 question quiz,{}".format(name))
input("please press the enter key to start the quiz")
question1 = """What is python"""
question2 = """What University is rated the best in Nigeria in 2020"""
question3 = """What month is valentine usually celebrated"""
question4 = """The winner of a race occupy what place in position"""
question5 = """How many month have 28 days"""
question6 = """What is 2+2"""
question7 = """What is the capital of USA"""
question8 = """What is the capital of Nigeria"""
question9 = """How old is Nigeria"""
question10 = """In what year did Nigeria become a republic"""
question11 = """which of this country is not in Africa"""
question12 = """what is the name of the musician that sang \'shape of you\'"""
question13 = """What is the capital of Canada"""
question14= """A triangle of base 10 and height 15 has area:"""
question15 = """who is the president of Nigeria"""
option1 = ["snake", "program", "programming language", "reptile with legs"]
option2 = ["unilag", "uniben", "oau"]
option3 = ["jan", "feb", "mar"]
option4 = ["1st", "2nd", "3rd", "none"]
option5 = ["2", "1", "All of thaRe above", "depend if there is a leap year"]
option6 = ["4", "8", "22", "I don't know"]
option7 = ["oklahoma", "new york city", "mary", "washington"]
option8 = ["lagos", "ikeja", "abuja", "port harcourt"]
option9 = ["55", "60", "58", "59", "61"]
option10 = ["1960", "1961", "1962", "1963", "1965"]
option11 = ["tunisia", "seychelles", "morocco", "none of these"]
option12 = ["justin bieber", "usher", "bruno mars", "ed sheeran"]
option13 = ["toronto", "ottawa", "edmonton", "victoria"]
option14 = ["150", "75", "25", "50", "30", "300", "60"]
option15 = ["buhari", "aisha", "fashola", "ambode"]
questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9,
             question10, question11, question12, question13, question14, question15]
options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11,
           option12, option13, option14, option15]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
answers = [option1[2], option2[0], option3[1], option4[0], option5[1], option6[0], option7[3], option8[2], option9[3],
           option10[3], option11[3], option12[3], option13[1], option14[1], option15[0]]
score = 0
import random
import datetime

startTime = datetime.datetime.now()
f = random.sample(range(len(questions)), len(questions))
answer = [None]*len(questions)
i = 0
qanswers = []
for question in range(len(questions)):
    print(i+1, ".", questions[f[i]])
    b = 0
    g = random.sample(range(len(options[f[i]])), len(options[f[i]]))

    for option in range(len(options[f[i]])):
        print(letters[b], ".", options[f[i]][g[b]])
        if options[f[i]][g[b]] in answers:
            qanswers.append(letters[b])
            z = "The answer is:" + letters[b] + "." + options[f[i]][g[b]]
        b += 1
    answer[i] = str(input("enter answer:"))
    answer[i] = answer[i].upper()
    #y = options[f[i]]._len_()
    #y = letters._len_() - y
    #lettersrestrict = letters.copy()
    #s = -y
    #while s < 0:
        #lettersrestrict.pop(s)
        #s += 1
    #while answer[i] not in lettersrestrict:
        #print("Please input one of the options")
        #answer[i] = str(input("Enter answer:"))
        #answer[i] = answer[i].upper()
    #print(z)
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
    totalTime = str(totalTime.seconds//60) + "minute and" + str(totalTime.seconds%60) + "seconds"
else:
    totalTime = str(totalTime.seconds//60) + "minutes and" + str(totalTime.seconds%60) + "seconds"
grade = ""
if percentage < 40:
    grade = "F"
    outcome = "You failed this quite, so sorry!"
elif 40 <= percentage < 45:
    grade = "E"
    outcome = "Very poor performance, work hard next time"
elif 45 <= percentage < 50:
    grade = "D"
    outcome = "average performance, need for improvement next time"
elif 50 <= percentage < 60:
    grade = "C"
    outcome = "abit above average, you can do better next time"
elif 60 <= percentage < 70:
    grade = "B"
    outcome = "good poor performance, you are almost there"
elif 70 <= percentage < 90:
    grade = "A"
    outcome = "Very good performance, keep it up"
elif 90 <= percentage < 100:
    grade = "A+"
    outcome = "Excellent performance"
elif percentage == 100:
    grade = "A+++++++++"
    outcome = "you are a perfect student"
print("dear", name, ",")
print("you started this test at", startTime, "and finished at", endTime, "and spent", totalTime, "on the quiz")
print("your score is :", round(percentage, 2), "%")
print("You got", grade, ".", outcome)



