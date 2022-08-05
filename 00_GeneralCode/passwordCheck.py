import getpass
database = {"Emmanuel" : "5998", "Current" : "2341"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break
print("Verified")