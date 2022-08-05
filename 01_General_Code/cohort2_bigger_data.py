#list, tuple, dictionary
#LIST
customer1 = ["ola",17, 5.6, "no, 23, adetunde str", "lagos", "Nig"]
print(customer1)
name_of_customer1 = customer1[0]
print(name_of_customer1)
#Q1===print the state and address of customer1
#Q2===Create another customer2 and give it different respective dataset then print any 3 individual data from customer2
#Q3===Create a cojoin variable customer 1 and 2 with other external data not previously stored.
#A1
name_of_customer1 = customer1[4]
name_of_customer1 = customer1[3]
#A2
customer2 = ["james","Rodrigo",37, 94.6, "house, 23, mexica ave", "mexicali", "mexico","462574687"]
phone_no_of_customer2 = customer2[-1]#same as phone_no_of_customer2 = customer2[7]
print(phone_no_of_customer2)
#surname_and_weight_of_customer2
surname_of_customer2 = customer2[1]
weight_of_customer2 = customer2[3]
print('the weight and surname  of customer2 are {} and {} respectively'.format(weight_of_customer2, surname_of_customer2))
#A3
print("the two customers we have in this example are {} and {} {}".format(customer1[0], customer2[0], customer2[1]))
###will give same answer
print(customer1[0] + "is my friend")
print(customer1[0], "is my friend")
print("{} {} ".format(customer1[0] , "is my friend"))
print(customer1)
customer1.append(1245)
customer1.append("male")
print(customer1)
customer1.insert(2, "Nigerian")
print(customer1)
print(customer1[2:4])
print(customer1[-4:-2])

