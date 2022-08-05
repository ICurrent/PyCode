customer = ("bassey", ("0813700000", "0706867756"), ("uba", 132434564, "N123456777"),32,"adewale strpe lagos")
print(type(customer))
print(customer[0])
#customer[0] = "Bassey"
#print(customer)
customer4 = ["james", ["617343546", "nycb"]]
#customer.append(customer4)
print(customer)
customer2 = ("raphel", "25/12/1960", "A12345", "125623 US Dollars")
total_customer = customer + customer2
print(total_customer)
print(type(customer2))
#31/08/2020====change the date of birth of raphel to 27/03/1972
new_customer2 = list(customer2)
print(type(new_customer2))
print(customer2)
print(new_customer2)
new_customer2[1] = "27/03/1972"
print(new_customer2)
new_customer2 = tuple(new_customer2)
customer2 = new_customer2
print(customer2)
total_customer = customer + customer2
print(total_customer)
print(customer.append("oct19"))


