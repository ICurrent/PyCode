name = 'Emaanoel'
print(name)

first_name= input('please Enter your name: ')
print(first_name)

age = input("Enter your age: ")
print(age)

gender = input("Enter your gender: ")
print(gender)

print(first_name +" is " + age + "years old and he is a " + gender +"child.") #concatenation of string
print(f"{first_name} is {age}years old and he is {gender} child." ) #f string
print('{} is {}years old and he is a {} child'.format(first_name, age, gender)) #format method

# String
name = 'Ayomide'
#...Methods of a string
#What is a method: A function of an object(Thet are also called function

print(name.upper()) #converts to uppercase
print(name.lower()) #converts to lowercase
print(name.count('A')) #counts the number of occurance of a character
print(name.endswith('e')) #checks if it ends with e
print(name.startswith('a')) #checks if it starts with a
print(name.split('o')) #split whenever there's an occurance of o

#Exercise:
 # Create a variable of name, surname, class and use them to make a sentence,
 # and use the following string method as well