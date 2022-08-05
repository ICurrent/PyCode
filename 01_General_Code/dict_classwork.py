'''customers = {"name":"raphel", "DOB":"25/12/1960", "passport_number":"A12345", "amount":"125623 USD", "age":67,"height" : 6.12 }
print(type(customers))
print(customers.values())
print(customers.keys())
print(customers.items())
#q1---change the name of the customer to james----
customers["name"] = "james"
print(customers)
#q2----delete the age part of the data====
del customers["age"]
print(customers)
#q3--- add phone no to the data=====
customers["phone_no"]="08054959268"
print(customers)
#q4----add sex immediately after name===
new_customers = list(customers)
new_customers_values = list(customers.values())
print(new_customers_values.insert(2,"male"))
print(new_customers_values)
print(type(new_customers))
print(customers)
print(new_customers)
new_customers.insert(2,'sex')

print(dict(zip("ade","boy")))
print(dict(zip(new_customers, new_customers_values)))
customers = zip(new_customers, new_customers_values)
print(customers)
#apply all the properties of the list earlier create'''
personal_info={
    Bio:"name":"louis","age":"25","marital_status":"single","religion":}



