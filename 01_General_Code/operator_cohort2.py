#+*-///%operator usage
name_of_user = input("what is your name:")
current_age = eval(input("please enter your current age:"))
years_later = eval(input("number of years later:"))
current_age += years_later
future_age = current_age# this to give the new current age to the future age after the addition
print("Dear {}, you will be {} years old in {} years time".format(name_of_user,future_age, years_later))

#Q1:DESIGN AN APP TO CALCULATE YOUR EXPENSES ON FEEDING, TRANSPORTION AND CALL CARDS STARTING FROM WHAT YOU (HAD TO LEFT)
#Q2:DESIGN AN APP TO CALCULATE NUMBER OF CHICKEN HATCHED EVERY MONTH IF THE INCREMENT IS IN GEOMETRIC OF 2 OVER 6 MONTHS
#Q3:DESIGN AN APP TO CALCULATE ANY NUMBER ENTERED AND ITS POWER TO WHICH IT IS RAISED

amount_now = eval(input("please input what you have now:"))
amount_on_feeding = eval(input("enter feeding amount:"))
amount_on_transportation = eval(input("enter transportation amount:"))
amount_on_call_card = eval(input("enter call card amount:"))
amount_now -= amount_on_feeding
amount_now -= amount_on_transportation
amount_now -= amount_on_call_card
final_amount = amount_now
print("the amount left on me is {} because I spent {} on feeding, {} on transportation and {} on call card".format(
    final_amount, amount_on_feeding, amount_on_transportation, amount_on_call_card
))

last_month_count = eval(input("what was your count last month"))
current_month = last_month_count * 2
