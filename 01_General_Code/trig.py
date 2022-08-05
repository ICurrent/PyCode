#special tri app   version 1.0.0
four_fig_table = {"sin 30": 0.5, "cos 30": 0.866, "tan 30": 0.5771, "sin 45": 0.7071, "cos 45": 0.7071, "tan 45": 1, "sin 60": 0.866, "cos 60": 0.5, "tan 60": 1.33 }
user_question = input("please enter the value of trig that you want here:")
if user_question == "sin 30":
    print("the value of {} is {}".format(user_question, 0.5))
elif user_question == "cos 30":
    print("the value of {} is {}".format(user_question, 0.866))
elif user_question == "tan 30":
    print("the value of {} is {}".format(user_question, 0.5771))
elif user_question == "sin 45":
    print("the value of {} is {}".format(user_question, 0.7071))
elif user_question == "cos 45":
    print("the value of {} is {}".format(user_question, 0.7071))
elif user_question == "tan 45":
    print("the value of {} is {}".format(user_question, 1))
elif user_question == "sin 60":
    print("the value of {} is {}".format(user_question, 0.866))
elif user_question == "cos 60":
    print("the value of {} is {}".format(user_question, 0.5))
elif user_question == "tan 60":
    print("the value of {} is {}".format(user_question, 1.33))
else:
    print("so sorry bro, i cant help you becos am not design to answer this")

