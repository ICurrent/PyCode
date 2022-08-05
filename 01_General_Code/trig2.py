#special tri app   version 1.0.1
four_fig_table = {"sin 30": 0.5, "cos 30": 0.866, "tan 30": 0.5771, "sin 45": 0.7071, "cos 45": 0.7071, "tan 45": 1, "sin 60": 0.866, "cos 60": 0.5, "tan 60": 1.33 }
user_question = input("please enter the value of trig that you want here:")
if user_question in four_fig_table:
    print("the value of the {} is {}".format(user_question,four_fig_table.get(user_question)))
else:
    print("so sorry bro, i cant help you becos am not design to answer this")