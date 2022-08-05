customer = ["bassey", ["0813700000", "0706867756"], ["uba", 132434564, "N123456777"], ["Gtb", "133554344", "N3445456777"],
             32,"adewale strpe lagos",
            ["mike", ["0913700000", "0706867756"],["Gtb", "133554344", "N3445456777"],
            86, "ojo str ogun"],
            ["tope", "08175475000", ["ubn", 3546535464, "N34632224777"],
            ["Gtb", "34543544", "N3445456777"], 132, "abuja str abia"]]

print(customer)

#print(type(customer))
#print(customer)
#class work
#Q1===submit the phone numbers of the intended loan applicants from the customers
#Q2===submit the account details of mr bassey, address of mr tope and account number of mr mike respectively
#Q3===write a code that allows the manager to input the customers name and get there details
#Q4===Add yourself as a customer


print("mr {}'s phone nmubers are {} and {}".format(customer[0], customer[1][0], customer[1][1]))
print("mr {}'s phone nmubers are {} and {}".format(customer[6][0], customer[6][1][0],customer[6][1][1]))
print("mr {}'s phone nmubers is {}".format(customer[7][0], customer[7][1]))
print("\n"*5)
print('''mr {}'s phone nmubers are {} and {} while that of mr {}'s phone nmubers are {} and {} and that of mr {}'s phone nmubers is 
{}'''.format(customer[0],customer[1][0], customer[1][1], customer[6][0], customer[6][1][0], customer[6][1][1], customer[7][0], customer[7][1]))


print("the details of mr {} details are phone {} and {},bank details are {} and {} lives at {}, {}"
      .format(customer[0], customer[1][0], customer[1][1], customer[2], customer[3], customer[4], customer[5]))
customer[4] = "32b"

print("the details of mr {} details are phone {} and {},bank details are {} and {} lives at {}, {}"
      .format(customer[0], customer[1][0], customer[1][1], customer[2], customer[3], customer[4], customer[5]))
print("\n")



print("the details of mr {} details are phone {} and {},bank details is {} and  lives at {}, {}"
      .format(customer[6][0], customer[6][1][0], customer[6][1][1], customer[6][2], customer[6][3], customer[6][4]))

print("\n"*2)
customer[0] = customer[0].capitalize()
customer[6][0] = customer[6][0].capitalize()
customer[7][0] = customer[7][0].capitalize()
customer_name = input("Please enter the customer whose details you want? ")

print("the details of mr {} details are phone {} and {},bank details are {} and {} lives at {}, {}"
      .format(customer_name, customer[1][0], customer[1][1], customer[2], customer[3], customer[4], customer[5]))

vowel_letters = ["a","e","i","o","u"]
print(vowel_letters[1:4])
vowel_letters.reverse()
print(vowel_letters)
print(vowel_letters[1:4])
print(customer[0].capitalize())
print(customer[6][0].capitalize())
print(customer[7][0].capitalize())
customer[0] = customer[0].capitalize()
customer[6][0] = customer[6][0].capitalize()
customer[7][0] = customer[7][0].capitalize()
print("the details of mr {} details are phone {} and {},bank details are {} and {} lives at {}, {}"
      .format(customer[0].capitalize(), customer[1][0], customer[1][1], customer[2], customer[3], customer[4], customer[5]))
print(customer)
customer4 = ["james", ["617343546", "nycb"]]
customer.append(customer4)
print(customer)

